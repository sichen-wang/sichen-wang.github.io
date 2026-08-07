#!/usr/bin/env python3
"""把 LaTeXML 生成的 HTML 整理成可直接嵌入本站页面的 HTML 片段。

为什么不转 Markdown
-------------------
本站的数学是客户端 KaTeX（assets/js/katex-config.js 调 `renderMathInElement
(document.body, ...)`），扫描的是整个 body，所以 HTML 里的 `$...$` 一样会被渲染。
LaTeXML 已经把嵌套结构、交叉引用、表格、定理环境都处理好了，再拆成 Markdown 让
Hugo 转回 HTML 只会丢结构。因此这里只做最小必要的改动：

1. 取出正文（丢掉 LaTeXML 的 head / 页眉 / 自带样式引用）
2. 标题、作者、摘要、关键词删掉 —— 它们已在 front matter 里
3. `<span class="ltx_Math">TEX</span>` → `$TEX$`，交给 KaTeX
4. 图片：LaTeXML 没装 ImageMagick 时转不出图且会丢掉文件名（src 为空），
   故从中间产物 main.xml 的 `graphic=` 按 `xml:id` 取回，指向预先转好的 SVG
5. 其余 `ltx_*` 结构原样保留，样式由 assets/css/custom.css 的 .paper-body 规则接管

仅依赖 Python 标准库，方便在 macOS / Windows 上开箱即用。
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# 数学：还原成 KaTeX 能认的 $...$
# --------------------------------------------------------------------------

RE_MATH = re.compile(r'<span([^>]*)class="ltx_Math[^"]*"([^>]*)>(.*?)</span>', re.S)


def find_block_end(text: str, start: int, tag: str) -> int:
    """返回 text[start] 处 <tag> 的配对结束标签之后的位置（支持嵌套）。"""
    open_re = re.compile(rf"<{tag}\b", re.I)
    close_re = re.compile(rf"</{tag}\s*>", re.I)
    depth = 0
    pos = start
    while pos < len(text):
        mo = open_re.search(text, pos)
        mc = close_re.search(text, pos)
        if not mc:
            return len(text)
        if mo and mo.start() < mc.start():
            depth += 1
            pos = mo.end()
        else:
            depth -= 1
            pos = mc.end()
            if depth <= 0:
                return pos
    return len(text)


def replace_blocks(text: str, open_pattern: re.Pattern, tag: str, handler) -> str:
    out = []
    pos = 0
    while True:
        m = open_pattern.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        end = find_block_end(text, m.start(), tag)
        out.append(text[pos : m.start()])
        out.append(handler(text[m.start() : end], m))
        pos = end
    return "".join(out)


RE_EQGROUP_OPEN = re.compile(r'<table[^>]*class="[^"]*ltx_equationgroup[^"]*"[^>]*>')
RE_TR = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S)
RE_TD = re.compile(r"<td\b([^>]*)>(.*?)</td>", re.S)

# LaTeXML 给每个片段都加了 \displaystyle 之类的样式前缀，判别续行前要先剥掉
RE_STYLE_PREFIX = re.compile(
    r"^(?:\s*\\(?:displaystyle|textstyle|scriptstyle|scriptscriptstyle)\b)+\s*"
)

# 以关系符/运算符开头 ⇒ 这一行没有自己的左侧表达式，是上一行的延续
RE_CONTINUATION = re.compile(
    r"^\s*(?:=|\\le(?:q)?\b|\\ge(?:q)?\b|\\l(?:eqslant)?\b|\\g(?:eqslant)?\b"
    r"|\\approx\b|\\equiv\b|\\sim\b|\\simeq\b|\\cong\b|\\propto\b"
    r"|\\subseteq\b|\\supseteq\b|\\subset\b|\\supset\b|\\in\b"
    r"|\\to\b|\\rightarrow\b|\\Rightarrow\b|\\implies\b|\\mapsto\b"
    r"|\\pm\b|\\times\b|\\cdot\b|<|>|\+|-)"
)


def merge_continuation_rows(rows: list[str]) -> list[str]:
    """把为适配双栏而断开的续行接回上一行。

    论文原本是 ICML 双栏，栏宽只有 ~234pt，长公式不得不用 `\\\\` 断行；转成单栏
    网页后版心宽裕，这些断行反而显得莫名其妙。

    判别依据：整行去掉对齐符 `&` 后若以关系符开头（`\\le ...`、`= ...`），说明它
    没有独立的左侧表达式，只是上一行的延续，应当合并；而 `\\delta_\\mu &= ...`、
    `\\kappa_t &:= ...` 这类每行自带左侧的，是语义上并列的多个式子，必须保留分行。
    """
    out: list[str] = []
    for row in rows:
        bare = row.replace("&", " ").strip()
        # LaTeXML 会在每个片段前插 \displaystyle，挡住后面的关系符，判别前先剥掉
        probe = RE_STYLE_PREFIX.sub("", bare)
        if out and RE_CONTINUATION.match(probe):
            # 合并后对齐符失去意义，一并去掉
            out[-1] = f"{out[-1].replace('&', ' ').strip()} {bare}"
        else:
            out.append(row)
    return out


def convert_equation_groups(html: str) -> str:
    """align 组必须整组交给 KaTeX 的 aligned 环境，不能逐片段渲染。

    LaTeXML 把 align 拆成表格：每个 `&` 片段是一个 <td> 里独立的
    <span class="ltx_Math">。若逐个替换成 $...$，每个片段会被 KaTeX 当成一条
    独立公式来排版 —— 跨行对齐关系丢失，片段之间还会各自断行，表现为
    "= m_t +" 单独占一行、下一行才是 "m_{t+1} ..." 这种错位。

    这里把整组还原成 `\\begin{aligned} ... \\\\ ... \\end{aligned}`：
    同一行的各片段用 `&` 连接，行间用 `\\\\`。公式编号不塞进 LaTeX
    （KaTeX 的 aligned 内不支持 \\tag），改由右侧的 HTML 单元格承载。
    """

    def handle(block: str, _m: re.Match) -> str:
        rows: list[str] = []
        nums: list[str] = []
        # 正文里的「见式 (27)」指向的是每一行公式自带的 id。整组替换成
        # paper-eqgroup 时若不把这些 id 带过来，那些交叉引用就会指向不存在的
        # 锚点，点了没有任何反应。
        anchor_ids: list[str] = []
        gm = re.search(r'\bid="([^"]+)"', _m.group(0))
        if gm:
            anchor_ids.append(gm.group(1))
        # 组里每个带编号的公式各占一个 <tbody>，编号 id 就挂在 tbody 上
        # （不是 table，也不是 tr），漏掉它交叉引用就会指向空锚点
        for tbm in re.finditer(r'<tbody\b[^>]*\bid="([^"]+)"', block):
            anchor_ids.append(tbm.group(1))
        for tr in RE_TR.finditer(block):
            tm = re.search(r'\bid="([^"]+)"', tr.group(0)[: tr.group(0).find(">") + 1])
            if tm:
                anchor_ids.append(tm.group(1))
            parts: list[str] = []
            for td in RE_TD.finditer(tr.group(1)):
                attrs, inner = td.group(1), td.group(2)
                if "ltx_eqn_eqno" in attrs:
                    num = strip_tags(inner)
                    if num:
                        nums.append(num)
                    continue
                texs = [clean_tex(mm.group(3)) for mm in RE_MATH.finditer(inner)]
                seg = " ".join(t for t in texs if t)
                if seg:
                    parts.append(seg)
            if parts:
                rows.append(" & ".join(parts))
        if not rows:
            return ""
        rows = merge_continuation_rows(rows)
        if len(rows) == 1:
            # 合并后只剩一行，就不必再套 aligned（否则残留的 & 会把左侧留空）
            tex = rows[0].replace("&", " ").strip()
        else:
            body = " \\\\\n".join(rows)
            tex = f"\\begin{{aligned}}\n{body}\n\\end{{aligned}}"
        nums_html = "<br>".join(html_mod.escape(n) for n in nums)
        anchors = "".join(
            f'<span class="paper-eq-anchor" id="{html_mod.escape(i, quote=True)}"></span>'
            for i in dict.fromkeys(anchor_ids)
        )
        return (
            '\n<div class="paper-eqgroup">'
            f"{anchors}"
            f'<div class="paper-eqgroup-body">$${tex_to_html(tex)}$$</div>'
            f'<div class="paper-eqgroup-no">{nums_html}</div>'
            "</div>\n"
        )

    return replace_blocks(html, RE_EQGROUP_OPEN, "table", handle)


# LaTeXML 会把 `\bigl(` 写成 `\bigl{(}`。LaTeX 容忍这种花括号，KaTeX 不容忍
# （报 "Invalid delimiter type 'ordgroup'"），需要把定界符外的花括号去掉。
# 内容可能是转义花括号 `\{` / `\}`（本身含花括号），需单列一支
RE_BIG_DELIM = re.compile(r"(\\[bB]igg?[lrm]?)\{(\\[{}]|\\?[^{}]{1,8})\}")


def strip_tags(fragment: str) -> str:
    return html_mod.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def clean_tex(tex: str) -> str:
    tex = re.sub(r"<[^>]+>", "", tex)
    tex = html_mod.unescape(tex)
    # LaTeX 行尾 `%`+换行是续行注释，KaTeX 不认
    tex = re.sub(r"%\s*\n\s*", "", tex)
    tex = re.sub(r"\s*\n\s*", " ", tex)
    tex = tex.replace("~{}", " ")
    tex = RE_BIG_DELIM.sub(r"\1\2", tex)
    return tex.strip()


def tex_to_html(tex: str) -> str:
    """把整理好的 LaTeX 放回 HTML 文本节点。

    clean_tex 为了处理 `&amp;`、`&lt;` 之类做了 unescape，拿到的是真实 LaTeX；
    直接写回 HTML 会出事 —— `$\\{\\widehat z_m : m<n\\}$` 里的 `<n` 会被浏览器
    当作标签开头，连同后面的正文一起吞掉（表现为段落中间莫名少一大段字）。
    这里重新转义 & < >，浏览器解析后 KaTeX 拿到的仍是原始字符。
    """
    return html_mod.escape(tex, quote=False)


def convert_math(html: str, display_ids: set[str]) -> str:
    """行内数学 → $tex$；位于公式表格中的 → $$tex$$。"""

    def repl(m: re.Match) -> str:
        attrs = m.group(1) + m.group(2)
        tex = clean_tex(m.group(3))
        if not tex:
            return ""
        id_m = re.search(r'id="([^"]+)"', attrs)
        mid = id_m.group(1) if id_m else ""
        # 公式表格里的数学用 display 模式
        if any(mid.startswith(p) for p in display_ids):
            return f"$${tex_to_html(tex)}$$"
        return f"${tex_to_html(tex)}$"

    return RE_MATH.sub(repl, html)


def collect_display_ids(html: str) -> set[str]:
    """收集所有行间公式表格的 id 前缀（其中的 Math 用 display 模式）。"""
    ids = set()
    for m in re.finditer(r'<table[^>]*\bid="([^"]+)"[^>]*class="ltx_equation[^"]*"', html):
        ids.add(m.group(1) + ".")
    for m in re.finditer(r'<table[^>]*class="ltx_equation[^"]*"[^>]*\bid="([^"]+)"', html):
        ids.add(m.group(1) + ".")
    for m in re.finditer(r'<table[^>]*\bid="([^"]+)"[^>]*class="ltx_equationgroup[^"]*"', html):
        ids.add(m.group(1) + ".")
    for m in re.finditer(r'<table[^>]*class="ltx_equationgroup[^"]*"[^>]*\bid="([^"]+)"', html):
        ids.add(m.group(1) + ".")
    return ids


# --------------------------------------------------------------------------
# 图片：从中间 XML 取回原始文件名
# --------------------------------------------------------------------------

RE_GRAPHIC_A = re.compile(r'<graphics[^>]*\bgraphic="([^"]+)"[^>]*\bxml:id="([^"]+)"')
RE_GRAPHIC_B = re.compile(r'<graphics[^>]*\bxml:id="([^"]+)"[^>]*\bgraphic="([^"]+)"')


RE_GRAPHIC_TAG = re.compile(r"<graphics\b[^>]*/?>")
RE_ATTR_ID = re.compile(r'\bxml:id="([^"]+)"')
RE_ATTR_GRAPHIC = re.compile(r'\bgraphic="([^"]+)"')
RE_OPT_WIDTH = re.compile(r"width=([0-9.]+)pt")


def build_image_map(xml_path: Path) -> dict[str, str]:
    if not xml_path or not xml_path.exists():
        return {}
    xml = xml_path.read_text(encoding="utf-8", errors="replace")
    mapping: dict[str, str] = {}
    for graphic, xid in RE_GRAPHIC_A.findall(xml):
        mapping[xid] = graphic
    for xid, graphic in RE_GRAPHIC_B.findall(xml):
        mapping.setdefault(xid, graphic)
    return mapping


def build_width_map(xml_path: Path) -> dict[str, float]:
    """取回每张图在论文里的目标宽度，换算成相对版心的百分比。

    论文用 `\\includegraphics[width=...]` 决定每张图多大：跨栏大图用 \\textwidth，
    单栏小图只有它的一半。转换后这层信息就没了，若一刀切等宽，本来小的图会被
    放大到和主结果图一样，版面失衡。这里以文中出现的最大宽度为 100%，其余按比例缩。
    """
    if not xml_path or not xml_path.exists():
        return {}
    xml = xml_path.read_text(encoding="utf-8", errors="replace")
    raw: dict[str, float] = {}
    for tag in RE_GRAPHIC_TAG.findall(xml):
        mid = RE_ATTR_ID.search(tag)
        mw = RE_OPT_WIDTH.search(tag)
        if mid and mw:
            raw[mid.group(1)] = float(mw.group(1))
    if not raw:
        return {}
    widest = max(raw.values())
    return {k: v / widest for k, v in raw.items()}


RE_IMG = re.compile(r"<img\b[^>]*>")
RE_SVG_VIEWBOX = re.compile(r'viewBox="[\d.eE+-]+\s+[\d.eE+-]+\s+([\d.eE+-]+)\s+([\d.eE+-]+)"')


def svg_size(path: Path) -> tuple[int, int] | None:
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return None
    m = RE_SVG_VIEWBOX.search(head)
    if not m:
        return None
    try:
        w, h = float(m.group(1)), float(m.group(2))
    except ValueError:
        return None
    if w <= 0 or h <= 0:
        return None
    return round(w), round(h)


def png_size(path: Path) -> tuple[int, int] | None:
    """PNG 的 IHDR 块固定在文件头，宽高各 4 字节大端。"""
    try:
        data = path.read_bytes()[:33]
    except OSError:
        return None
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        return None
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def webp_size(path: Path) -> tuple[int, int] | None:
    """WebP 有三种码流（VP8 有损 / VP8L 无损 / VP8X 扩展），宽高位置各不相同。"""
    try:
        d = path.read_bytes()[:40]
    except OSError:
        return None
    if d[:4] != b"RIFF" or d[8:12] != b"WEBP":
        return None
    fmt = d[12:16]
    try:
        if fmt == b"VP8 ":
            return int.from_bytes(d[26:28], "little") & 0x3FFF, int.from_bytes(d[28:30], "little") & 0x3FFF
        if fmt == b"VP8L":
            n = int.from_bytes(d[21:25], "little")
            return (n & 0x3FFF) + 1, ((n >> 14) & 0x3FFF) + 1
        if fmt == b"VP8X":
            return int.from_bytes(d[24:27], "little") + 1, int.from_bytes(d[27:30], "little") + 1
    except (IndexError, ValueError):
        return None
    return None


def image_size(path: Path) -> tuple[int, int] | None:
    """给 <img> 补 width/height。

    懒加载的图在加载完成前高度为 0，若不预留尺寸，滚动时整页会不断跳动。
    浏览器可以从 width/height 属性推出宽高比，配合 CSS 的 height:auto 预留空间。
    """
    suffix = path.suffix.lower()
    if suffix == ".svg":
        return svg_size(path)
    if suffix == ".png":
        return png_size(path)
    if suffix == ".webp":
        return webp_size(path)
    return None


def fix_images(
    html: str,
    id_to_file: dict[str, str],
    image_files: dict[str, Path],
    width_ratio: dict[str, float] | None = None,
) -> tuple[str, int]:
    missing = 0
    width_ratio = width_ratio or {}

    def repl(m: re.Match) -> str:
        nonlocal missing
        tag = m.group(0)
        id_m = re.search(r'\bid="([^"]+)"', tag)
        if not id_m:
            return tag
        src = id_to_file.get(id_m.group(1))
        stem = Path(src).stem if src else None
        target = image_files.get(stem) if stem else None
        if target is None:
            missing += 1
            return f'<span class="paper-figure-missing">[figure not converted: {stem or id_m.group(1)}]</span>'
        tag = re.sub(r'\bsrc="[^"]*"', f'src="{target.name}"', tag)
        if 'src="' not in tag:
            tag = tag.replace("<img", f'<img src="{target.name}"', 1)
        # 去掉 LaTeXML 的缺图标记类
        tag = tag.replace("ltx_missing_image", "").replace("ltx_missing", "")
        if "loading=" not in tag:
            tag = tag.replace("<img", '<img loading="lazy"', 1)
        # 预留宽高比，避免懒加载造成滚动跳动
        if "width=" not in tag:
            size = image_size(target)
            if size:
                tag = tag.replace("<img", f'<img width="{size[0]}" height="{size[1]}"', 1)
        # 按论文里的相对宽度显示，保住原有的大图/小图层次
        ratio = width_ratio.get(id_m.group(1))
        if ratio:
            pct = max(30, min(100, round(ratio * 100)))
            tag = tag.replace("<img", f'<img style="width:{pct}%"', 1)
        return tag

    return RE_IMG.sub(repl, html), missing


# --------------------------------------------------------------------------
# 正文提取
# --------------------------------------------------------------------------

RE_PAGE_OPEN = re.compile(r'<div[^>]*class="ltx_page_content"[^>]*>')
RE_DIV_OPEN = re.compile(r"<div\b", re.I)
RE_DIV_CLOSE = re.compile(r"</div\s*>", re.I)
DROP_CLASSES = ("ltx_title_document", "ltx_authors", "ltx_abstract", "ltx_keywords")


def extract_page_content(html: str) -> str:
    """取出 ltx_page_content 的内容，用配对计数而非贪婪正则。

    贪婪的 `(.*)</div>` 会一路匹配到文档最后一个 </div>，把 page_content 自己的
    闭合标签也吞进来，导致产物多出一个 </div>。这个多余的闭合标签会提前关闭页面
    模板里的 <article>/<main>，把后续的页脚等元素挤到外层容器 —— 表现为页脚宽度
    溢出、脱离正文版心。
    """
    m = RE_PAGE_OPEN.search(html)
    if not m:
        return html
    start = m.end()
    depth = 1
    pos = start
    while pos < len(html):
        mo = RE_DIV_OPEN.search(html, pos)
        mc = RE_DIV_CLOSE.search(html, pos)
        if not mc:
            break
        if mo and mo.start() < mc.start():
            depth += 1
            pos = mo.end()
        else:
            depth -= 1
            if depth == 0:
                return html[start : mc.start()]
            pos = mc.end()
    return html[start:]


def check_balanced(fragment: str) -> list[str]:
    """自检标签配对，不平衡会破坏页面 DOM 结构。"""
    problems = []
    for tag in ("div", "section", "figure", "table", "span", "p", "li", "ul", "ol"):
        o = len(re.findall(rf"<{tag}\b", fragment, re.I))
        c = len(re.findall(rf"</{tag}\s*>", fragment, re.I))
        if o != c:
            problems.append(f"<{tag}>: {o} open / {c} close")
    return problems


def extract_body(html: str, include_appendix: bool) -> str:
    body = extract_page_content(html)

    for cls in DROP_CLASSES:
        body = re.sub(
            rf'<(div|h1)[^>]*class="[^"]*{cls}[^"]*"[^>]*>.*?</\1>', "", body, flags=re.S
        )

    # LaTeXML 的页脚（生成时间等）
    body = re.sub(r'<footer[^>]*class="ltx_page_footer".*?</footer>', "", body, flags=re.S)
    body = re.sub(r'<div[^>]*class="ltx_page_logo".*?</div>', "", body, flags=re.S)

    if not include_appendix:
        idx = body.find('class="ltx_appendix"')
        if idx != -1:
            start = body.rfind("<section", 0, idx)
            if start != -1:
                head = body[:start]
                # 参考文献的位置随模板而变：ICML 模板把它排在附录之前，此时
                # head 里已经有了，再补一次就会出现两个 References 章节。
                # 只有当它排在附录之后（head 里没有）时才需要补回。
                if "ltx_bibliography" not in head:
                    bib = re.search(
                        r'<section[^>]*class="ltx_bibliography".*?</section>', body, re.S
                    )
                    if bib:
                        head += bib.group(0)
                body = head

    return body.strip()


# --------------------------------------------------------------------------
# 标题：补 id，供目录锚点使用
# --------------------------------------------------------------------------

RE_HEADING = re.compile(r"<h([2-4])\b([^>]*)>(.*?)</h\1>", re.S)
RE_TAG_SPAN = re.compile(r'<span[^>]*class="ltx_tag[^"]*"[^>]*>.*?</span>', re.S)


def slugify(title: str) -> str:
    s = re.sub(r"<[^>]+>", "", title)
    s = html_mod.unescape(s).strip().lower()
    s = re.sub(r"[^\w\s一-鿿-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    return s.strip("-") or "section"


def add_heading_ids(html: str) -> str:
    """给正文标题补上稳定 id。

    目录（layouts/_partials/components/toc.html）直接读取这里写入的 id，
    而不是用 Hugo 的 anchorize 重新推导 —— 两套规则不一致会导致锚点失效。
    """
    seen: dict[str, int] = {}

    def repl(m: re.Match) -> str:
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        if 'id="' in attrs:
            return m.group(0)
        text = RE_TAG_SPAN.sub("", inner)
        slug = slugify(text)
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        if n:
            slug = f"{slug}-{n}"
        return f'<h{level}{attrs} id="{slug}">{inner}</h{level}>'

    return RE_HEADING.sub(repl, html)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html", type=Path, help="latexmlpost 生成的 HTML")
    ap.add_argument("-o", "--output", type=Path, required=True, help="输出 HTML 片段")
    ap.add_argument("--xml", type=Path, default=None, help="latexml 中间 XML（取回图片路径）")
    ap.add_argument("--figures", type=Path, default=None, help="已转好的图片目录（webp / svg / png）")
    ap.add_argument("--appendix", action="store_true", help="包含附录（默认只要正文）")
    args = ap.parse_args()

    html = args.html.read_text(encoding="utf-8")
    xml_path = args.xml or args.html.with_suffix(".xml")
    id_to_file = build_image_map(xml_path)
    width_ratio = build_width_map(xml_path)
    image_files: dict[str, Path] = {}
    if args.figures and args.figures.is_dir():
        # 同名多格式时按此优先级取用；矢量优先（插图的细线与小字位图会失真）
        for ext in (".svg", ".webp", ".png", ".jpg", ".jpeg"):
            for p in sorted(args.figures.glob(f"*{ext}")):
                image_files.setdefault(p.stem, p)

    display_ids = collect_display_ids(html)
    body = extract_body(html, args.appendix)
    # align 组要先整组合并，否则下一步会把各片段拆成独立公式
    body = convert_equation_groups(body)
    body = convert_math(body, display_ids)
    body, missing = fix_images(body, id_to_file, image_files, width_ratio)
    body = add_heading_ids(body)

    args.output.write_text(body, encoding="utf-8")

    print(f"wrote {args.output} ({len(body):,} bytes)")
    print(f"display-math tables: {len(display_ids)}, images mapped: {len(id_to_file)}, images available: {len(image_files)}")
    if missing:
        print(f"WARNING: {missing} image(s) could not be resolved", file=sys.stderr)

    problems = check_balanced(body)
    if problems:
        print("ERROR: 标签不平衡，会破坏页面 DOM 结构：", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1
    print("tag balance: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
