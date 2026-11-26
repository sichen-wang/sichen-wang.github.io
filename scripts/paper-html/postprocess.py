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

LaTeXML 在若干地方会丢信息或与 PDF 不一致（参考文献标签与顺序、align 的文字列、
algorithmic 的 Require 行、\\qedhere、cleveref 的公式括号与混合类型、enumitem 的
font=、\\citepunct ……）。这些修正需要对照论文源码（`--tex`）、BibTeX 产物
（`--bbl`）与 `.bib`（`--bib`），各自在对应函数的文档里说明。

仅依赖 Python 标准库，方便在 macOS / Windows 上开箱即用。
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------
# 论文源码：读取 HTML 里已经丢失、但决定 PDF 外观的排版信息
# --------------------------------------------------------------------------

RE_TEX_COMMENT = re.compile(r"(?<!\\)((?:\\\\)*)%.*")


def strip_tex_comments(text: str) -> str:
    return "\n".join(RE_TEX_COMMENT.sub(r"\1", line) for line in text.split("\n"))


def read_group(text: str, i: int, open_ch: str = "{") -> tuple[str | None, int]:
    """text[i] 为 `{` 或 `[` 时返回 (组内文字, 组后位置)；不配对时返回 (None, i)。

    方括号组只在花括号外计数，`[label={[a]}]` 这类写法不会提前结束。
    """
    if i >= len(text) or text[i] != open_ch:
        return None, i
    depth = brace = 0
    j = i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if open_ch == "{":
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return text[i + 1 : j], j + 1
        else:
            if c == "{":
                brace += 1
            elif c == "}":
                brace -= 1
            elif brace == 0 and c == "[":
                depth += 1
            elif brace == 0 and c == "]":
                depth -= 1
                if depth == 0:
                    return text[i + 1 : j], j + 1
        j += 1
    return None, i


TEX_ACCENTS = {
    "'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308", "~": "\u0303",
    "=": "\u0304", ".": "\u0307", "u": "\u0306", "v": "\u030c", "H": "\u030b",
    "c": "\u0327", "k": "\u0328", "r": "\u030a",
}
TEX_LETTERS = {
    "ss": "ß", "o": "ø", "O": "Ø", "ae": "æ", "AE": "Æ", "aa": "å", "AA": "Å",
    "l": "ł", "L": "Ł", "i": "ı", "j": "ȷ", "oe": "œ", "OE": "Œ",
}


def tex_to_plain(s: str) -> str:
    """BibTeX 字段 / 文献标签里的 TeX → 纯文本（重音合成，命令与花括号去掉）。"""

    def accent(m: re.Match) -> str:
        base = {"\\i": "i", "\\j": "j"}.get(m.group(2), m.group(2))
        return unicodedata.normalize("NFC", base + TEX_ACCENTS[m.group(1)])

    s = re.sub(r"\\([`'^\"~=.])\s*\{?(\\[ij](?![a-zA-Z])|[A-Za-z])\}?", accent, s)
    s = re.sub(r"\\([uvHckr])(?:\s+|\s*\{)(\\[ij](?![a-zA-Z])|[A-Za-z])\}?", accent, s)
    s = re.sub(
        r"\\(ss|ae|AE|aa|AA|oe|OE|o|O|l|L|i|j)(?![a-zA-Z])\s*",
        lambda m: TEX_LETTERS[m.group(1)],
        s,
    )
    s = s.replace("---", "—").replace("--", "–").replace("~", " ")
    s = re.sub(r"\\[a-zA-Z]+\*?\s*", "", s)
    s = re.sub(r"\\(.)", r"\1", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


# algorithmic / algpseudocode 中开启新一行的命令：Require 行之后遇到它们即结束
ALG_LINE_COMMANDS = {
    "STATE", "IF", "ELSIF", "ELSE", "ENDIF", "FOR", "FORALL", "ENDFOR", "WHILE",
    "ENDWHILE", "REPEAT", "UNTIL", "LOOP", "ENDLOOP", "RETURN", "PRINT",
    "State", "Statex", "If", "ElsIf", "Else", "EndIf", "For", "ForAll", "EndFor",
    "While", "EndWhile", "Repeat", "Until", "Loop", "EndLoop", "Function",
    "EndFunction", "Procedure", "EndProcedure",
}


class TexSource:
    """论文源码的扁平视图：展开 \\input / \\include、去掉注释，分出导言区与正文。"""

    def __init__(self, main: Path):
        self.main = main
        self.root = main.parent
        self.flat = self._flatten(main, 0)
        k = self.flat.find("\\begin{document}")
        self.preamble = self.flat[:k] if k >= 0 else self.flat
        self.body = self.flat[k:] if k >= 0 else ""
        # 同目录的 .sty（会议模板等）也会加载宏包，比如 neurips_*.sty 自带 natbib
        self.local_styles = ""
        for m in re.finditer(r"\\(?:usepackage|RequirePackage)\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}", self.preamble):
            for name in m.group(1).split(","):
                sty = self.root / f"{name.strip()}.sty"
                if name.strip() and sty.is_file():
                    self.local_styles += "\n" + strip_tex_comments(sty.read_text(encoding="utf-8", errors="replace"))

    def _flatten(self, path: Path, depth: int) -> str:
        try:
            text = strip_tex_comments(path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            return ""
        if depth > 20:
            return text

        def repl(m: re.Match) -> str:
            name = (m.group(1) or m.group(2) or "").strip()
            for cand in (self.root / name, self.root / f"{name}.tex"):
                if name and cand.is_file():
                    return self._flatten(cand, depth + 1)
            return m.group(0)

        return re.sub(r"\\(?:input|include)(?![a-zA-Z])\s*(?:\{([^}]*)\}|([^\s{}\\]+))", repl, text)

    # ---- 宏包与选项 ------------------------------------------------------

    def package_options(self, name: str) -> list[str] | None:
        """宏包的选项列表；未加载时返回 None（本地 .sty 里加载的也算）。"""
        opts: list[str] | None = None
        text = self.preamble + "\n" + self.local_styles
        for m in re.finditer(r"\\(?:usepackage|RequirePackage)\s*(\[[^\]]*\])?\s*\{([^}]*)\}", text):
            if name in [n.strip() for n in m.group(2).split(",")]:
                more = [o.strip() for o in (m.group(1) or "[]")[1:-1].split(",") if o.strip()]
                opts = (opts or []) + more
        if opts is not None:
            for m in re.finditer(r"\\PassOptionsToPackage\s*\{([^}]*)\}\s*\{([^}]*)\}", text):
                if name in [n.strip() for n in m.group(2).split(",")]:
                    opts += [o.strip() for o in m.group(1).split(",") if o.strip()]
        return opts

    def base_size_pt(self) -> float:
        m = re.search(r"\\documentclass\s*\[([^\]]*)\]", self.preamble)
        if m:
            sm = re.search(r"(\d+(?:\.\d+)?)pt", m.group(1))
            if sm:
                return float(sm.group(1))
        return 10.0

    def bibliography(self) -> tuple[str | None, list[str]]:
        """(\\bibliographystyle, \\bibliography 的文件列表)。"""
        styles = re.findall(r"\\bibliographystyle\s*\{([^}]*)\}", self.flat)
        files = re.findall(r"\\bibliography\s*\{([^}]*)\}", self.flat)
        names = [f.strip() for f in files[-1].split(",") if f.strip()] if files else []
        return (styles[-1].strip() if styles else None), names

    def macro_body(self, name: str) -> str | None:
        """\\(re)newcommand / \\def / \\algrenewcommand 定义的最后一个宏体。"""
        pat = re.compile(
            r"\\(?:(?:re|provide)?newcommand|alg(?:re)?newcommand|algrenewtext)\*?\s*"
            r"(?:\{\s*\\" + re.escape(name) + r"\s*\}|\\" + re.escape(name) + r"(?![a-zA-Z]))"
            r"\s*(?:\[\d\])?\s*"
            r"|\\[gex]?def\s*\\" + re.escape(name) + r"(?![a-zA-Z])\s*"
        )
        body = None
        for m in pat.finditer(self.flat):
            content, _ = read_group(self.flat, m.end())
            if content is not None:
                body = content
        return body

    def crefnames(self) -> dict[str, tuple[str, str]]:
        """{类型: (单数, 复数)}；\\Crefname 存成 'Type' 键（首字母大写形式）。"""
        out: dict[str, tuple[str, str]] = {}
        for m in re.finditer(r"\\(c|C)refname\s*\{([^}]*)\}\s*\{([^}]*)\}\s*\{([^}]*)\}", self.preamble):
            key = m.group(2).strip() if m.group(1) == "c" else "^" + m.group(2).strip()
            out[key] = (m.group(3).strip(), m.group(4).strip())
        return out

    def text_spacing(self) -> dict[str, str]:
        """`\\text{标签:}\\qquad` 这类文字后的间距：LaTeXML 转 align 时会丢掉。

        键是去掉数学与空白后的文字；同一文字在全文只对应一种间距时才采用。
        """
        found: dict[str, set[str]] = {}
        for m in re.finditer(r"\\(?:text|textrm|textnormal|textup|mbox)\s*(?=\{)", self.body):
            content, end = read_group(self.body, m.end())
            if content is None:
                continue
            sm = re.match(
                r"\s*(\\q?quad(?![a-zA-Z])|\\[,;:>!](?![a-zA-Z])|\\enspace(?![a-zA-Z])"
                r"|\\hspace\*?\s*\{[^}]*\})",
                self.body[end:],
            )
            found.setdefault(text_key(content), set()).add(sm.group(1) if sm else "")
        return {k: next(iter(v)) for k, v in found.items() if len(v) == 1 and "" not in v}

    def algorithmic_leads(self) -> list[list[str]]:
        """每个 algorithmic 环境开头连续的 Require / Ensure 行（按文中顺序）。"""
        leads = []
        for m in re.finditer(r"\\begin\{algorithmic\}", self.body):
            end = self.body.find("\\end{algorithmic}", m.end())
            seg = self.body[m.end() : end if end >= 0 else len(self.body)]
            lead: list[str] = []
            for c in re.finditer(r"\\([A-Za-z]+)", seg):
                if c.group(1).lower() in ("require", "ensure"):
                    lead.append(c.group(1).lower())
                elif c.group(1) in ALG_LINE_COMMANDS:
                    break
            leads.append(lead)
        return leads

    def list_fonts(self) -> list[tuple[str, str | None]]:
        """[(环境名, enumitem 的 font= 值)]，按文中顺序；含 \\setlist 的全局设置。"""
        defaults: dict[str, str] = {}
        for m in re.finditer(r"\\setlist\s*(\[[^\]]*\])?\s*(?=\{)", self.preamble):
            opts, _ = read_group(self.preamble, m.end())
            font = enumitem_font(opts or "")
            if font is None:
                continue
            known = ("description", "enumerate", "itemize")
            if m.group(1):
                envs = [e.strip() for e in m.group(1)[1:-1].split(",") if e.strip() in known]
            else:
                envs = list(known)
            for env in envs:
                defaults[env] = font
        out = []
        for m in re.finditer(r"\\begin\{(description|enumerate|itemize)\}\s*", self.body):
            env = m.group(1)
            opts, _ = read_group(self.body, m.end(), "[")
            font = enumitem_font(opts) if opts is not None else None
            out.append((env, font if font is not None else defaults.get(env)))
        return out

    def has_hfill_square(self) -> bool:
        return bool(re.search(r"\\hfill\s*(?:\$|\\\()\s*\\(?:square|blacksquare|Box)\b", self.body))


def text_key(s: str) -> str:
    """比较 `\\text{...}` 内容用的键：去掉数学、命令名与空白。"""
    s = re.sub(r"\$[^$]*\$|\\\(.*?\\\)", "", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    return re.sub(r"[\s{}]", "", s)


def enumitem_font(opts: str) -> str | None:
    m = re.search(r"(?:^|,)\s*font\s*=\s*", opts)
    if not m:
        return None
    rest = opts[m.end() :]
    if rest.startswith("{"):
        val, _ = read_group(rest, 0)
        return val or ""
    return rest.split(",")[0].strip()

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


def convert_equation_groups(html: str, spacing: dict[str, str] | None = None) -> str:
    """整组还原 align/gather 的行列结构，不能逐片段渲染或合并续行。

    LaTeXML 把 align 拆成表格：每个 `&` 片段是一个 <td> 里独立的
    <span class="ltx_Math">。若逐个替换成 $...$，每个片段会被 KaTeX 当成一条
    独立公式来排版 —— 跨行对齐关系丢失，片段之间还会各自断行，表现为
    "= m_t +" 单独占一行、下一行才是 "m_{t+1} ..." 这种错位。

    多列还原成 aligned，单列还原成 gathered，保留原稿的居中方式。
    同一行的各片段（含空左侧单元格）用 `&` 连接，行间用 `\\\\`。
    以关系符开头的续行也是原稿的显式换行，不能擅自拼回上一行。
    公式编号不塞进 LaTeX
    （KaTeX 的 aligned 内不支持 \\tag），改由右侧的 HTML 单元格承载。

    LaTeXML 还会在这里丢两样东西，需要补回：

    - 整格是文字的列（`\\text{splitter:}\\qquad &`）输出成
      `<span class="ltx_text ltx_markedasmath">`，不是 ltx_Math；文字里的行内数学
      另成 span。这里拆开拼成 `\\text{refinement }j\\text{:}`，文字后的间距
      LaTeXML 已丢弃，按源码（spacing）补回。
    - 以 `&` 开头的行（左侧空着的右对齐列）会被吞掉首个空单元格，
      首格变成 ltx_align_left；此时先补一个空列，否则各列整体左移一格。
    """
    spacing = spacing or {}

    def handle(block: str, _m: re.Match) -> str:
        rows: list[list[str]] = []
        nums: list[str] = []
        qed_rows: list[int] = []
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
            first_classes: list[str] | None = None
            row_qed = False
            for td in RE_TD.finditer(tr.group(1)):
                attrs, inner = td.group(1), td.group(2)
                cm = re.search(r'\bclass="([^"]*)"', attrs)
                classes = cm.group(1).split() if cm else []
                if "ltx_eqn_eqno" in classes:
                    num = strip_tags(inner)
                    if num:
                        nums.append(num)
                    continue
                # 居中填充和编号不是 TeX 的对齐列。真正的空公式单元格则
                # 必须保留，否则 `&= ...` 会变成下一行的左侧表达式。
                if any("padleft" in c or "padright" in c for c in classes):
                    continue
                # \qedhere 在 LaTeXML 里展开成公式末尾的 \qed，见 restore_qedhere
                if RE_QED_END.search(inner):
                    row_qed = True
                    inner = RE_QED_END.sub("", inner)
                seg = cell_tex(inner, spacing)
                if seg or "ltx_eqn_cell" in classes:
                    if first_classes is None:
                        first_classes = classes
                    parts.append(seg)
            if any(parts):
                if first_classes and "ltx_align_left" in first_classes and len(parts) > 1:
                    parts.insert(0, "")
                if row_qed:
                    qed_rows.append(len(rows))
                rows.append(parts)
        if not rows:
            return ""
        environment = "gathered" if all(len(row) == 1 for row in rows) else "aligned"
        body = " \\\\\n".join(" & ".join(row) for row in rows)
        tex = f"\\begin{{{environment}}}\n{body}\n\\end{{{environment}}}"
        nums_html = "".join(
            f'<span class="paper-eqgroup-number">{html_mod.escape(n)}</span>'
            for n in nums
        )
        if qed_rows and not nums:
            # 证毕符号跟着最后一行，靠右下对齐
            nums_html = '<span class="paper-eqgroup-number" style="opacity:1">∎</span>'
            nums = ["∎"]
            nums_class = "paper-eqgroup-no"
            return (
                '\n<div class="paper-eqgroup">'
                + "".join(
                    f'<span class="paper-eq-anchor" id="{html_mod.escape(i, quote=True)}"></span>'
                    for i in dict.fromkeys(anchor_ids)
                )
                + f'<div class="paper-eqgroup-body">$${tex_to_html(tex)}$$</div>'
                + f'<div class="{nums_class}" style="align-self:flex-end">{nums_html}</div>'
                + "</div>\n"
            )
        nums_class = "paper-eqgroup-no paper-eqgroup-no-rows" if nums else "paper-eqgroup-no"
        anchors = "".join(
            f'<span class="paper-eq-anchor" id="{html_mod.escape(i, quote=True)}"></span>'
            for i in dict.fromkeys(anchor_ids)
        )
        return (
            '\n<div class="paper-eqgroup">'
            f"{anchors}"
            f'<div class="paper-eqgroup-body">$${tex_to_html(tex)}$$</div>'
            f'<div class="{nums_class}">{nums_html}</div>'
            "</div>\n"
        )

    return replace_blocks(html, RE_EQGROUP_OPEN, "table", handle)


RE_QED_END = re.compile(r"\\qed(?![a-zA-Z])\s*(?=</span>\s*$)")
TEXT_SPECIALS = {
    "\\": "\\textbackslash{}", "{": "\\{", "}": "\\}", "$": "\\$", "&": "\\&",
    "#": "\\#", "%": "\\%", "_": "\\_", "^": "\\^{}", "~": "\\~{}",
}


def cell_tex(inner: str, spacing: dict[str, str]) -> str:
    """align 单元格 → TeX。数学片段原样；数学之外的文字（文字列）转成 \\text{…}。"""
    pieces: list[tuple[str, str]] = []
    pos = 0
    for mm in RE_MATH.finditer(inner):
        pieces.append(("text", inner[pos : mm.start()]))
        pieces.append(("math", clean_tex(mm.group(3))))
        pos = mm.end()
    pieces.append(("text", inner[pos:]))
    texts = [html_mod.unescape(re.sub(r"<[^>]+>", "", v)) for k, v in pieces if k == "text"]
    if not any(t.strip() for t in texts):
        return " ".join(v for k, v in pieces if k == "math" and v)
    # 首尾空白来自 HTML 排版，中间的空白（"refinement j"）属于原文
    out: list[str] = []
    started = False
    for kind, val in pieces:
        if kind == "math":
            if val:
                out.append(val)
                started = True
            continue
        t = re.sub(r"\s+", " ", html_mod.unescape(re.sub(r"<[^>]+>", "", val)))
        if not started:
            t = t.lstrip()
        if not t:
            continue
        out.append("\\text{" + "".join(TEXT_SPECIALS.get(c, c) for c in t) + "}")
        started = True
    # 末尾文字的尾随空白去掉
    if out and out[-1].startswith("\\text{"):
        out[-1] = re.sub(r"\s+\}$", "}", out[-1])
    tex = "".join(out)
    if pieces[-1][0] == "text" and texts[-1].strip():
        tex += spacing.get(text_key("".join(texts)), "")
    return tex


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
    # amsthm 的证毕符号。写在行末的 `\qed` 会被 LaTeXML 一并收进公式源码，
    # 而 KaTeX 没有这个宏，整条公式会渲染成红色报错。它是排版记号不是数学，
    # 直接丢掉（章节末尾的 ∎ 由 LaTeXML 另行输出，不受影响）。
    tex = re.sub(r"\\qed(?![a-zA-Z])\s*", "", tex)
    # LaTeXML 把 \hspace{1em} 记成 \hskip 10.00002pt（还可能带 plus/minus 伸缩量），
    # 还原成 \hspace。能整除成 1/4 em 的按正文字号换回 em，否则保留 pt。
    tex = RE_HSKIP.sub(hskip_to_hspace, tex)
    # 末尾的 TeX 控制空格不能被 strip 截成孤立反斜杠。
    tex = re.sub(r"(?<!\\)((?:\\\\)*)\\[ \t]+$", r"\1\\space{}", tex)
    return tex.strip()


# 正文字号（pt），main() 按 \documentclass 的选项设置
BASE_PT = 10.0
RE_HSKIP = re.compile(
    r"\\hskip\s*(-?\d*\.?\d+)\s*pt"
    r"(?:\s*plus\s*-?\d*\.?\d+\s*(?:pt|fil+|em))?(?:\s*minus\s*-?\d*\.?\d+\s*(?:pt|fil+|em))?"
)


def hskip_to_hspace(m: re.Match) -> str:
    pt = float(m.group(1))
    em = pt / BASE_PT
    if abs(em * 4 - round(em * 4)) < 1e-3:
        return f"\\hspace{{{round(em * 4) / 4:g}em}}"
    return f"\\hspace{{{pt:.2f}".rstrip("0").rstrip(".") + "pt}"


def tex_to_html(tex: str) -> str:
    """把整理好的 LaTeX 放回 HTML 文本节点。

    clean_tex 为了处理 `&amp;`、`&lt;` 之类做了 unescape，拿到的是真实 LaTeX；
    直接写回 HTML 会出事 —— `$\\{\\widehat z_m : m<n\\}$` 里的 `<n` 会被浏览器
    当作标签开头，连同后面的正文一起吞掉（表现为段落中间莫名少一大段字）。
    这里重新转义 & < >，浏览器解析后 KaTeX 拿到的仍是原始字符。
    """
    return html_mod.escape(tex, quote=False)


def attach_inline_punctuation(body: str) -> str:
    """让紧随行内公式的标点留在最后一个数学片段上，避免孤立到下一行。

    只移动紧邻单美元分隔符的标点；正文文字、展示公式和数学内容不变。
    使用 text 保留正文标点的字形，不把冒号解释为数学关系符。

    公式以二元运算符结尾时（`$60\\times$.`），TeX 把末尾的二元运算符当普通符号，
    不加间距；标点挪进公式后它不再位于末尾，KaTeX 会按二元运算符两侧留白，
    显示成「60 × .」。先给运算符加花括号，保持普通符号的间距。
    """
    pattern = re.compile(r"(?<!\\)(\$\$|\$)(.*?)(?<!\\)\1([,.;:]*)", re.S)

    def repl(m: re.Match) -> str:
        delimiter, tex, punctuation = m.groups()
        if delimiter == "$" and punctuation:
            tex = RE_TRAILING_BINOP.sub(r"{\1}", tex)
            return f"${tex}\\text{{{punctuation}}}$"
        return m.group(0)

    return pattern.sub(repl, body)


RE_TRAILING_BINOP = re.compile(
    r"(?<![\\{^_])(\\(?:times|pm|mp|cdot|ast|star|circ|bullet|oplus|ominus|otimes|odot|"
    r"cup|cap|sqcup|sqcap|vee|wedge|setminus|div|uplus|amalg)(?![a-zA-Z])|(?<!\\)[+\-*])\s*$"
)


def restore_qedhere(html: str) -> str:
    """\\qedhere 落在行间公式里时补回右侧的 ∎。

    amsthm 的 LaTeXML 绑定把 \\qedhere 展开成公式末尾的 \\qed（证明结尾不再输出 ∎），
    而 clean_tex 必须丢掉 \\qed（KaTeX 没有这个宏）。这里先把它从公式里拿出来，
    放进编号单元格的位置——PDF 里 ∎ 正是在这一行的右端。
    """

    def handle(block: str, _m: re.Match) -> str:
        if not RE_QED_IN_MATH.search(block):
            return block
        block = RE_QED_IN_MATH.sub("", block)
        if "ltx_eqn_eqno" in block:
            return block
        pad = '<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>'
        k = block.rfind(pad)
        if k < 0:
            return block
        k += len(pad)
        return block[:k] + "\n" + QED_CELL + block[k:]

    return replace_blocks(html, RE_EQ_TABLE_OPEN, "table", handle)


RE_EQ_TABLE_OPEN = re.compile(r'<table\b[^>]*class="ltx_equation ltx_eqn_table"[^>]*>')
RE_QED_IN_MATH = re.compile(r"\\qed(?![a-zA-Z])\s*(?=</span>)")
QED_CELL = (
    '<td class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right" '
    'style="opacity:1">∎</td>'
)


def float_hfill_squares(body: str, tex: TexSource | None) -> str:
    """源码里的 `\\hfill$\\square$`（手写的证毕符号）在 PDF 中靠右，网页上同样右浮动。

    LaTeXML 把 \\hfill 变成普通空格，□ 紧跟在段末文字后面。
    """
    if not tex or not tex.has_hfill_square():
        return body
    return re.sub(
        r"\s+(\$\\(?:square|blacksquare|Box)\$)(?=\s*</p>)",
        r' <span style="float:right">\1</span>',
        body,
    )


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
# 参考文献：标签、顺序、引用文字以 BibTeX 产物 main.bbl 为准
# --------------------------------------------------------------------------


def parse_bbl(text: str) -> list[tuple[str, str | None]]:
    """[(key, 可选标签)]，按 .bbl 里的顺序（即 PDF 参考文献的顺序）。"""
    entries = []
    for m in re.finditer(r"\\bibitem(?![a-zA-Z])\s*", text):
        pos = m.end()
        label = None
        if text.startswith("[", pos):
            label, pos = read_group(text, pos, "[")
        while pos < len(text) and text[pos].isspace():
            pos += 1
        key, _ = read_group(text, pos)
        if key is not None:
            entries.append((key.strip(), label))
    return entries


def is_alpha_label(label: str | None) -> bool:
    """alpha 系样式的标签（AA88、CFG{\\etalchar{+}}02）。natbib 作者-年份标签带括号年份，不算。"""
    return bool(label) and "(" not in label and bool(re.search(r"[A-Za-z]", label)) and len(label) < 40


def bbl_label_html(label: str) -> str:
    parts = re.split(r"\{?\\etalchar\s*\{([^}]*)\}\}?", label)
    return "".join(
        f'<sup class="ltx_sup">{html_mod.escape(p)}</sup>' if i % 2 else html_mod.escape(tex_to_plain(p))
        for i, p in enumerate(parts)
    )


def bbl_label_plain(label: str) -> str:
    return tex_to_plain(re.sub(r"\{?\\etalchar\s*\{([^}]*)\}\}?", r"\1", label))


def bib_titles(paths: list[Path]) -> dict[str, str]:
    """{key: 标题纯文本}，供引用链接的悬停提示使用（LaTeXML 读 .bbl 时拿不到标题）。"""
    out: dict[str, str] = {}
    for path in paths:
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in re.finditer(r"@\s*(\w+)\s*\{\s*([^,\s]+)\s*,", src):
            if m.group(1).lower() in ("string", "preamble", "comment"):
                continue
            nxt = re.search(r"\n\s*@", src[m.end() :])
            entry = src[m.end() : m.end() + nxt.start() if nxt else len(src)]
            tm = re.search(r"(?<![a-z])title\s*=\s*", entry, re.I)
            if not tm:
                continue
            rest = entry[tm.end() :]
            if rest.startswith("{"):
                title, _ = read_group(rest, 0)
            elif rest.startswith('"'):
                end = rest.find('"', 1)
                title = rest[1:end] if end > 0 else None
            else:
                title = None
            if title:
                out[m.group(2)] = tex_to_plain(title)
    return out


def bibitem_keys(xml: str, html: str, titles: dict[str, str] | None = None) -> dict[str, str]:
    """{参考文献条目 id: BibTeX key}。

    LaTeXML 读 .bbl 时，main.xml 里有 <bibitem key=... xml:id=...>，直接取。
    读 .bib 时条目要到 latexmlpost 才生成，main.xml 里只有正文的 <bibref>；
    这时按文中顺序把 XML 的每处引用与 HTML 的每个 <cite> 对齐，逐个配对；
    对不齐的（两边 <cite> 数目不同等）再用条目标题与 .bib 的 title 匹配。
    """
    out = bibitem_keys_by_citation(xml, html)
    if titles:
        import difflib

        norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())  # noqa: E731
        cands = {k: norm(t) for k, t in titles.items()}
        used = set(out.values())
        for m in RE_BIBITEM_OPEN.finditer(html):
            if m.group(1) in out:
                continue
            tm = re.compile(r'<span class="ltx_text ltx_bib_title">').search(html, m.end(), m.end() + 3000)
            if not tm:
                continue
            # 标题里的公式两边写法不同（.bib 的 $\widehat{R}$ 与 HTML 的数学 span），去掉后模糊比较
            title = html[tm.start() : find_block_end(html, tm.start(), "span")]
            title = norm(strip_tags(RE_MATH.sub("", title)))
            scored = sorted(
                ((difflib.SequenceMatcher(None, title, c).ratio(), k) for k, c in cands.items() if k not in used),
                reverse=True,
            )
            if scored and scored[0][0] >= 0.9 and (len(scored) == 1 or scored[1][0] < scored[0][0] - 0.05):
                out[m.group(1)] = scored[0][1]
                used.add(scored[0][1])
    return out


def bibitem_keys_by_citation(xml: str, html: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for tag in re.findall(r"<bibitem\b[^>]*>", xml):
        k = re.search(r'\bkey="([^"]+)"', tag)
        i = re.search(r'\bxml:id="([^"]+)"', tag)
        if k and i:
            out[i.group(1)] = html_mod.unescape(k.group(1))
    if out:
        return out
    xml_cites = []
    for c in re.findall(r"<cite\b[^>]*>(.*?)</cite>", xml, re.S):
        keys: list[str] = []
        for b in re.findall(r"<bibref\b[^>]*>", c):
            m = re.search(r'\bbibrefs="([^"]+)"', b)
            if m:
                keys += [k.strip() for k in html_mod.unescape(m.group(1)).split(",") if k.strip()]
        xml_cites.append(keys)
    html_cites = [
        re.findall(r'<a href="#(bib\.[^"]+)"', c)
        for c in re.findall(r"<cite\b[^>]*>(.*?)</cite>", html, re.S)
    ]
    if len(xml_cites) != len(html_cites):
        return {}
    conflict = set()
    for keys, ids in zip(xml_cites, html_cites):
        if len(keys) != len(ids):
            continue
        for k, i in zip(keys, ids):
            if out.setdefault(i, k) != k:
                conflict.add(i)
    for i in conflict:
        out.pop(i, None)
    return out


RE_BIBLIST_OPEN = re.compile(r'<ul\b[^>]*class="ltx_biblist"[^>]*>')
RE_BIBITEM_OPEN = re.compile(r'<li\b[^>]*\bid="([^"]+)"[^>]*class="ltx_bibitem\b[^"]*"[^>]*>')
RE_BIBTAG_OPEN = re.compile(r'<span class="ltx_tag\b[^"]*ltx_tag_bibitem[^"]*">')
RE_CITE_BLOCK = re.compile(r"<cite\b[^>]*>.*?</cite>", re.S)


def fix_bibliography(
    html: str,
    xml: str,
    bbl: list[tuple[str, str | None]],
    titles: dict[str, str],
    citepunct: str | None,
    report: list[str],
) -> str:
    """参考文献列表与正文引用对齐 PDF。

    1. 标签：alpha 系样式（alpha / alphaurl，或 natbib 配 alpha）下，LaTeXML 的
       natbib 解析器会把 `\\bibitem[AA88]` 拆成「AA [88]」，正文引用退化成序号。
       按 key 对回 .bbl 的标签，条目标签与引用文字一起改正。
    2. 顺序：LaTeXML 自己排序 .bib 的规则与 BibTeX 样式不同，按 .bbl 重排；
       数字标签随之重新编号。
    3. 读 .bbl 时引用链接的 title 为空，从 .bib 补上论文标题。
    4. cite 宏包的 \\citepunct：LaTeXML 写死成 ", "，按源码的定义替换。
    5. 文献备注里的 URL 只是文字，改成链接；\\pagebreak 之类留下的分页 div
       落进第一条文献的 <span> 里（非法嵌套），删掉。
    """
    id2key = bibitem_keys(xml, html, titles) if (bbl or titles) else {}
    key2label = {k: lab for k, lab in bbl}
    order = {k: n for n, (k, _) in enumerate(bbl)}
    alpha = bool(bbl) and sum(is_alpha_label(lab) for _, lab in bbl) >= 0.8 * len(bbl)
    relabeled: dict[str, tuple[str, str]] = {}  # 条目 id -> (新标签 HTML, 旧标签纯文本)

    def handle_list(block: str, m: re.Match) -> str:
        items = []
        pos = m.end() - m.start()  # m 的位置相对整篇 HTML，换算到 block 内
        while True:
            im = RE_BIBITEM_OPEN.search(block, pos)
            if not im:
                break
            end = find_block_end(block, im.start(), "li")
            items.append([im.group(1), im.start(), end])
            pos = end
        if not items:
            return block
        texts = [block[s:e] for _, s, e in items]
        seps = [block[items[i][2] : items[i + 1][1]] for i in range(len(items) - 1)]
        prefix, suffix = block[: items[0][1]], block[items[-1][2] :]

        # 1. 标签
        if alpha:
            for n, (bid, _, _) in enumerate(items):
                label = key2label.get(id2key.get(bid, ""))
                if not label:
                    continue
                t = texts[n]
                tm = RE_BIBTAG_OPEN.search(t)
                if not tm:
                    continue
                tend = find_block_end(t, tm.start(), "span")
                inner = t[tm.end() : tend - len("</span>")]
                shown = strip_tags(inner)
                # 文字对上且 et al. 的「+」已是上标（或本来就没有）才算标签正确
                if shown == f"[{bbl_label_plain(label)}]" and ("etalchar" not in label or "<sup" in inner):
                    continue
                relabeled[bid] = (bbl_label_html(label), re.sub(r"[\s\[\]]", "", shown))
                texts[n] = t[: tm.end()] + f"[{relabeled[bid][0]}]" + t[tend - len("</span>") :]
            if relabeled:
                report.append(f"bib labels from .bbl: {len(relabeled)}")

        # 2. 顺序
        if order:
            known = [id2key.get(bid) in order for bid, _, _ in items]
            if all(known):
                perm = sorted(range(len(items)), key=lambda n: order[id2key[items[n][0]]])
                if perm != list(range(len(items))):
                    moved = sum(1 for a, b in zip(perm, range(len(items))) if a != b)
                    texts = [texts[n] for n in perm]
                    items = [items[n] for n in perm]
                    renumber_numeric_tags(texts, items, relabeled)
                    report.append(f"bib entries reordered to .bbl order: {moved} moved")
            else:
                report.append(
                    f"WARNING: bib order not checked ({known.count(False)} entries without a .bbl key)"
                )

        out = [prefix]
        for n, t in enumerate(texts):
            out.append(t)
            if n < len(seps):
                out.append(seps[n])
        out.append(suffix)
        return "".join(out)

    html = replace_blocks(html, RE_BIBLIST_OPEN, "ul", handle_list)

    # 1b. 正文引用文字（只动 <cite> 里指向被改标签条目的链接）
    if relabeled:
        def fix_cite(cm: re.Match) -> str:
            def fix_a(am: re.Match) -> str:
                if am.group(2) not in relabeled:
                    return am.group(0)
                new, old = relabeled[am.group(2)]
                shown = re.sub(r"\s", "", strip_tags(am.group(3)))
                if re.fullmatch(r"\d+", shown) or shown in (old, strip_tags(new)):
                    return am.group(1) + new + "</a>"
                return am.group(0)

            return re.sub(r'(<a href="#([^"]+)"[^>]*>)(.*?)</a>', fix_a, cm.group(0), flags=re.S)

        html = RE_CITE_BLOCK.sub(fix_cite, html)

    # 3. 引用链接的悬停标题
    if titles and id2key:
        filled = 0

        def fill_title(am: re.Match) -> str:
            nonlocal filled
            t = titles.get(id2key.get(am.group(1), ""))
            if not t:
                return am.group(0)
            filled += 1
            return am.group(0).replace('title=""', f'title="{html_mod.escape(t, quote=True)}"')

        html = re.sub(r'<a href="#(bib\.[^"]+)" title=""', fill_title, html)
        if filled:
            report.append(f"citation hover titles from .bib: {filled}")

    # 4. \citepunct
    if citepunct and citepunct != ", ":
        sep = html_mod.escape(citepunct, quote=False)

        def fix_punct(cm: re.Match) -> str:
            return re.sub(r'</a>, (?=<a href="#bib\.)', f"</a>{sep}", cm.group(0))

        new = RE_CITE_BLOCK.sub(fix_punct, html)
        if new != html:
            report.append(f"multi-key citation separator: {citepunct!r}")
        html = new

    # 5. 文献区的 URL 文字与分页 div
    bm = re.search(r'<section\b[^>]*class="ltx_bibliography"[^>]*>', html)
    if bm:
        end = find_block_end(html, bm.start(), "section")
        sect = html[bm.start() : end]
        sect = re.sub(
            r'<span class="ltx_ref ltx_nolink ltx_url ltx_font_typewriter ltx_ref_self">(https?://[^<\s"]+)</span>',
            r'<a href="\1" class="ltx_ref ltx_url ltx_font_typewriter">\1</a>',
            sect,
        )
        sect = re.sub(r'\n?<div class="ltx_pagination[^"]*"></div>\n?', "\n", sect)
        html = html[: bm.start()] + sect + html[end:]
    return html


def renumber_numeric_tags(texts: list[str], items: list, relabeled: dict[str, tuple[str, str]]) -> None:
    """数字标签 [n] 的文献重排后按新位置重新编号（正文引用由 fix_bibliography 的调用方处理）。"""
    nums = []
    for t in texts:
        tm = RE_BIBTAG_OPEN.search(t)
        shown = strip_tags(t[tm.end() : find_block_end(t, tm.start(), "span")]) if tm else ""
        nm = re.fullmatch(r"\[?(\d+)\]?", shown)
        if not nm:
            return
        nums.append(nm.group(1))
    for n, t in enumerate(texts):
        tm = RE_BIBTAG_OPEN.search(t)
        tend = find_block_end(t, tm.start(), "span")
        inner = t[tm.end() : tend - len("</span>")]
        texts[n] = t[: tm.end()] + inner.replace(nums[n], str(n + 1), 1) + t[tend - len("</span>") :]
        if nums[n] != str(n + 1):
            relabeled[items[n][0]] = (str(n + 1), nums[n])


def drop_nested_pagination(html: str) -> str:
    """\\newpage / \\pagebreak 的分页 div 落在 <span> 或 <p> 里时是非法嵌套，删掉。"""
    out = []
    depth = 0
    pos = 0
    for m in re.finditer(r'<(/?)(span|p)\b[^>]*>|<div class="ltx_pagination[^"]*"></div>', html):
        if m.group(2):
            depth += -1 if m.group(1) else 1
            continue
        if depth > 0:
            out.append(html[pos : m.start()])
            pos = m.end()
    out.append(html[pos:])
    return "".join(out)


# --------------------------------------------------------------------------
# 交叉引用：cleveref 的公式括号与混合类型
# --------------------------------------------------------------------------

RE_REF_ANCHOR = re.compile(
    r'<a href="#(?P<id>[^"]+)"(?P<attrs>[^>]*)>'
    r'(?P<inner>(?:<span class="ltx_text ltx_ref_tag">[^<]*</span>[ \xa0]?)+)</a>'
)
RE_REF_TAG = re.compile(r'<span class="ltx_text ltx_ref_tag">([^<]*)</span>([ \xa0]?)')
CREF_CONJUNCTIONS = (", and ", " and ", ", ", " to ")  # 比较前 NBSP 已换成空格


def pluralize(word: str) -> str:
    if re.search(r"[^aeiou]y$", word):
        return word[:-1] + "ies"
    if re.search(r"(s|x|ch|sh)$", word):
        return word + "es"
    return word + "s"


def ref_targets(html: str) -> dict[str, tuple[str, str]]:
    """{锚点 id: (类型, 显示名)}。类型取 equation 或定理环境名（ltx_theorem_<env>）。"""
    out: dict[str, tuple[str, str]] = {}
    for m in re.finditer(r'<table\b[^>]*>', html):
        tag = m.group(0)
        cm = re.search(r'class="([^"]*)"', tag)
        cls = cm.group(1) if cm else ""
        im = re.search(r'\bid="([^"]+)"', tag)
        if "ltx_equationgroup" in cls:
            block = html[m.start() : find_block_end(html, m.start(), "table")]
            for i in re.findall(r'<(?:tbody|tr)\b[^>]*\bid="([^"]+)"', block):
                out[i] = ("equation", "")
            if im:
                out[im.group(1)] = ("equation", "")
        elif re.search(r"\bltx_equation\b", cls) and im:
            out[im.group(1)] = ("equation", "")
    for m in re.finditer(r'<div id="([^"]+)" class="ltx_theorem ltx_theorem_(\w+)"', html):
        word = ""
        tm = re.compile(r'<span class="ltx_tag ltx_tag_theorem">').search(html, m.end(), m.end() + 2000)
        if tm:
            text = strip_tags(html[tm.start() : find_block_end(html, tm.start(), "span")])
            wm = re.match(r"(.*?)\s*[\w.]*\d[\w.]*\.?$", text)
            word = (wm.group(1) if wm else text).strip()
        out[m.group(1)] = (m.group(2), word)
    return out


def fix_cleveref(html: str, tex: TexSource | None, report: list[str]) -> str:
    """按 cleveref 的规则重排 LaTeXML 输出的 \\cref 列表。

    LaTeXML 的 cleveref 绑定与 cleveref 本身有三处不同：

    - 公式编号：cleveref 默认 `\\creflabelformat{equation}{#2(#1)#3}`，PDF 是
      「Equation (3.9)」；LaTeXML 输出「Equation 3.9」。
    - 混合类型：一个 \\Cref 里有定理又有推论（共用计数器）时，cleveref 按类型分组，
      「Theorem 1.1 and Corollary 1.3」；LaTeXML 沿用第一个的类型并改成复数，
      「Theorems 1.1 and 1.3」。按每个目标的实际类型重新分组。
    - 排序与压缩：cleveref 默认 sort&compress，同类型内按编号排序，三个以上连号
      写成「Equations (2.1) to (2.3)」；LaTeXML 原样逐个列出。

    只处理「带类型词的链接 + cleveref 连接词 + 纯编号链接」这样的序列，
    作者手写的「Theorem~\\ref{a}」不受影响。
    """
    if tex is None:
        return html
    options = tex.package_options("cleveref")
    if options is None:
        return html
    explicit = {"sort", "compress", "sort&compress", "nosort"} & set(options)
    do_sort = not explicit or bool({"sort", "sort&compress"} & explicit)
    do_compress = not explicit or bool({"compress", "sort&compress"} & explicit)
    fmt = re.search(r"\\creflabelformat\s*\{equation\}\s*\{([^}]*)\}", tex.preamble)
    eq_parens = not fmt or "(" in fmt.group(1)
    targets = ref_targets(html)
    names = tex.crefnames()
    counts = {"parens": 0, "mixed": 0, "compressed": 0}
    tag_open = '<span class="ltx_text ltx_ref_tag">'

    def tags(m: re.Match) -> list[tuple[str, str]]:
        return RE_REF_TAG.findall(m.group("inner"))

    def type_names(env: str, word: str, capital: bool) -> tuple[str, str]:
        key = ("^" + env) if capital and ("^" + env) in names else env
        s, p = names[key] if key in names else (word, pluralize(word))
        if capital:
            return s[:1].upper() + s[1:], p[:1].upper() + p[1:]
        return s[:1].lower() + s[1:], p[:1].lower() + p[1:]

    def number(m: re.Match, kind: str) -> str:
        num = tags(m)[-1][0]
        if kind == "equation" and eq_parens and not num.startswith("("):
            return f"({num})"
        return num

    def anchor(m: re.Match, word: str | None, sep: str, kind: str) -> str:
        inner = (f"{tag_open}{word}</span>{sep}" if word else "") + f"{tag_open}{number(m, kind)}</span>"
        return f'<a href="#{m.group("id")}"{m.group("attrs")}>{inner}</a>'

    def join(parts: list[str], pair: str, mid: str, last: str) -> str:
        if len(parts) <= 2:
            return pair.join(parts)
        return mid.join(parts[:-1]) + last + parts[-1]

    def num_key(m: re.Match):
        num = tags(m)[-1][0]
        if not re.fullmatch(r"[\w.]*\d", num):
            return None
        return tuple((0, int(p)) if p.isdigit() else (1, p) for p in num.split("."))

    def consecutive(a, b) -> bool:
        return bool(a and b and a[:-1] == b[:-1] and a[-1][0] == b[-1][0] == 0 and b[-1][1] == a[-1][1] + 1)

    def render_group(members: list[re.Match], singular: str, plural: str, sep: str, kind: str) -> str:
        keys = [num_key(a) for a in members]
        if do_sort and all(keys):
            order = sorted(range(len(members)), key=lambda n: keys[n])
            members, keys = [members[n] for n in order], [keys[n] for n in order]
        runs: list[list[int]] = []
        for n, k in enumerate(keys):
            if do_compress and runs and consecutive(keys[runs[-1][-1]], k):
                runs[-1].append(n)
            else:
                runs.append([n])
        word = plural if len(members) > 1 else singular
        rendered = []
        for run in runs:
            label = word if not rendered else None
            if len(run) >= 3:
                counts["compressed"] += 1
                rendered.append(
                    anchor(members[run[0]], label, sep, kind) + " to\xa0" + anchor(members[run[-1]], None, sep, kind)
                )
            else:
                for n in run:
                    rendered.append(anchor(members[n], word if not rendered else None, sep, kind))
        return join(rendered, " and\xa0", ", ", " and\xa0")

    out = []
    pos = 0
    anchors = list(RE_REF_ANCHOR.finditer(html))
    i = 0
    while i < len(anchors):
        head = anchors[i]
        ht = tags(head)
        if len(ht) != 2 or not re.search(r"[A-Za-z]", ht[0][0]):
            i += 1
            continue
        seq, conj = [head], []
        j = i + 1
        while j < len(anchors):
            between = html[seq[-1].end() : anchors[j].start()].replace("\xa0", " ")
            if between in CREF_CONJUNCTIONS and len(tags(anchors[j])) == 1:
                seq.append(anchors[j])
                conj.append(between)
                j += 1
            else:
                break
        word, sep = ht[0]
        capital = word[:1].isupper()
        kinds = [targets.get(a.group("id"), ("", ""))[0] for a in seq]
        original = html[head.start() : seq[-1].end()]
        if " to " in conj:
            # \crefrange：结构本身就是区间，只补公式括号
            replacement = anchor(head, word, sep, kinds[0])
            for n in range(1, len(seq)):
                replacement += html[seq[n - 1].end() : seq[n].start()] + anchor(seq[n], None, sep, kinds[n])
        elif len(set(kinds)) > 1 and all(kinds):
            groups: dict[str, list[re.Match]] = {}
            for a, k in zip(seq, kinds):
                groups.setdefault(k, []).append(a)
            texts = []
            for k, members in groups.items():
                if k == "equation":
                    s, p = type_names("equation", "Equation", capital)
                else:
                    s, p = type_names(k, targets[members[0].group("id")][1] or word, capital)
                texts.append(render_group(members, s, p, sep, k))
            replacement = join(texts, " and\xa0", ", ", ", and\xa0")
            counts["mixed"] += 1
        else:
            # 同一类型（或类型未知）：LaTeXML 的类型词已正确，只做排序、压缩与公式括号
            kind = kinds[0] if all(k == kinds[0] for k in kinds) else ""
            replacement = render_group(seq, word, word, sep, kind)
        if replacement.replace("\xa0", " ") != original.replace("\xa0", " "):
            counts["parens"] += replacement.count(f"{tag_open}(") - original.count(f"{tag_open}(")
            out.append(html[pos : head.start()])
            out.append(replacement)
            pos = seq[-1].end()
        i = j
    out.append(html[pos:])
    if counts["parens"]:
        report.append(f"cleveref equation numbers parenthesized: {counts['parens']}")
    if counts["mixed"]:
        report.append(f"mixed-type \\cref lists regrouped: {counts['mixed']}")
    if counts["compressed"]:
        report.append(f"\\cref ranges compressed: {counts['compressed']}")
    return "".join(out)


# --------------------------------------------------------------------------
# 算法：algorithmic / algpseudocode 的 Require / Ensure 行
# --------------------------------------------------------------------------


def tex_label_html(tex: str) -> str:
    """`\\textbf{Parameters:}` → 加粗 span；其余命令去掉。"""
    m = re.fullmatch(r"\s*\\(textbf|textit|emph|textsc)\s*\{(.*)\}\s*", tex, re.S)
    if m:
        cls = {"textbf": "ltx_font_bold", "textit": "ltx_font_italic", "emph": "ltx_font_italic",
               "textsc": "ltx_font_smallcaps"}[m.group(1)]
        return f'<span class="ltx_text {cls}">{html_mod.escape(tex_to_plain(m.group(2)))}</span>'
    m = re.fullmatch(r"\s*\{?\s*\\bfseries\s*(.*?)\}?\s*", tex, re.S)
    if m:
        return f'<span class="ltx_text ltx_font_bold">{html_mod.escape(tex_to_plain(m.group(1)))}</span>'
    return html_mod.escape(tex_to_plain(tex))


RE_LISTING_OPEN = re.compile(r'<div\b[^>]*class="ltx_listing\b[^"]*"[^>]*>')


def fix_algorithms(html: str, tex: TexSource | None, report: list[str]) -> str:
    """Require / Ensure 行补回标签、去掉行号，后续行号顺延。

    PDF 里 `\\REQUIRE` / `\\Require` 是 `\\item[\\algorithmicrequire]`：不编号，
    行首是「Require:」（或 `\\renewcommand{\\algorithmicrequire}` 改成的文字）。
    LaTeXML 两样都丢：algorithmic 给这行编号 0，algpseudocode 编号 1 并让后面整体
    多 1。按源码里每个 algorithmic 开头的 Require / Ensure 行数处理，引用行号的
    链接（`Line~\\ref{ln:x}`）一起改。
    """
    if tex is None:
        return html
    leads = tex.algorithmic_leads()
    if not any(leads):
        return html
    labels = {
        "require": tex_label_html(tex.macro_body("algorithmicrequire") or r"\textbf{Require:}"),
        "ensure": tex_label_html(tex.macro_body("algorithmicensure") or r"\textbf{Ensure:}"),
    }
    blocks = []
    for m in RE_LISTING_OPEN.finditer(html):
        end = find_block_end(html, m.start(), "div")
        if re.search(r'<div id="[^"]+\.l\d+" class="ltx_listingline">', html[m.start() : end]):
            blocks.append((m.start(), end))
    # 嵌套的 listing（listing 里再套 listing）只算最外层
    blocks = [b for b in blocks if not any(o[0] < b[0] and b[1] <= o[1] for o in blocks)]
    if len(blocks) != len(leads):
        report.append(
            f"WARNING: algorithm Require lines not fixed ({len(leads)} algorithmic environments "
            f"in source, {len(blocks)} listings in HTML)"
        )
        return html
    renum: dict[str, str] = {}
    out = []
    pos = 0
    fixed = 0
    for (start, end), lead in zip(blocks, leads):
        block = html[start:end]
        if lead:
            lines = list(re.finditer(r'<div id="([^"]+)" class="ltx_listingline">', block))
            shift = 0
            pieces = []
            bpos = 0
            for n, lm in enumerate(lines):
                lend = find_block_end(block, lm.start(), "div")
                line = block[lm.start() : lend]
                tm = re.search(r'<span class="ltx_tag ltx_tag_listingline">(.*?)</span>(</span>)?', line, re.S)
                if not tm:
                    continue
                num_txt = strip_tags(tm.group(1) + (tm.group(2) or ""))
                nm = re.fullmatch(r"(\d+):?", num_txt)
                if n < len(lead):
                    if nm and int(nm.group(1)) >= 1:
                        shift += 1
                    rest = line[tm.end() :]
                    ws = re.match(r"[ \t\r\n]*", rest).group(0)  # \s 会吃掉 NBSP
                    rest = rest[len(ws) :]
                    rest = re.sub(r"^(?:\xa0|&nbsp;)+", "", rest)
                    line = (
                        line[: tm.start()] + '<span class="ltx_tag ltx_tag_listingline"></span>'
                        + ws + labels[lead[n]] + " " + rest
                    )
                    fixed += 1
                elif shift and nm:
                    new = int(nm.group(1)) - shift
                    renum[lm.group(1)] = str(new)
                    line = line[: tm.start()] + tm.group(0).replace(f"{nm.group(1)}:", f"{new}:", 1) + line[tm.end() :]
                pieces.append(block[bpos : lm.start()])
                pieces.append(line)
                bpos = lend
            pieces.append(block[bpos:])
            block = "".join(pieces)
        out.append(html[pos:start])
        out.append(block)
        pos = end
    out.append(html[pos:])
    html = "".join(out)
    if renum:
        html = re.sub(
            r'(<a href="#([^"]+)"[^>]*><span class="ltx_text ltx_ref_tag">)\d+(</span></a>)',
            lambda m: m.group(1) + renum[m.group(2)] + m.group(3) if m.group(2) in renum else m.group(0),
            html,
        )
    if fixed:
        report.append(f"algorithm Require/Ensure lines: {fixed} (later lines renumbered: {len(renum)})")
    return html


# --------------------------------------------------------------------------
# 列表：enumitem 的 font= 选项
# --------------------------------------------------------------------------

FONT_COMMANDS = {
    "itshape": ("+", "italic"), "textit": ("+", "italic"), "em": ("+", "italic"),
    "emph": ("+", "italic"), "slshape": ("+", "italic"), "upshape": ("-", "italic"),
    "bfseries": ("+", "bold"), "textbf": ("+", "bold"), "mdseries": ("-", "bold"),
    "scshape": ("+", "smallcaps"), "ttfamily": ("+", "typewriter"), "sffamily": ("+", "sansserif"),
}


def fix_list_fonts(html: str, tex: TexSource | None, report: list[str]) -> str:
    """enumitem 的 `font=`（如 `description[font=\\normalfont\\itshape]`）LaTeXML 不理会，
    描述列表标签一律加粗。按源码中同类列表的出现顺序对上 HTML 的列表，改标签字体。
    """
    if tex is None:
        return html
    specs = tex.list_fonts()
    if not any(f is not None for _, f in specs):
        return html
    kinds = {"description": r'<dl id="([^"]+)" class="ltx_description', "enumerate": r'<ol id="([^"]+)" class="ltx_enumerate',
             "itemize": r'<ul id="([^"]+)" class="ltx_itemize'}
    changed = 0
    for env, pat in kinds.items():
        src = [f for e, f in specs if e == env]
        if not any(f is not None for f in src):
            continue
        ids = re.findall(pat, html)
        if len(ids) != len(src):
            report.append(f"WARNING: {env} font= not applied ({len(src)} in source, {len(ids)} in HTML)")
            continue
        for lid, font in zip(ids, src):
            if font is None:
                continue
            classes = {"bold"} if env == "description" else set()
            for cmd in re.findall(r"\\([a-zA-Z]+)", font):
                if cmd == "normalfont":
                    classes.clear()
                elif cmd in FONT_COMMANDS:
                    op, c = FONT_COMMANDS[cmd]
                    (classes.add if op == "+" else classes.discard)(c)
            cls = " ".join(f"ltx_font_{c}" for c in sorted(classes))
            item_re = re.compile(
                r'(<(?:dt|li) id="' + re.escape(lid) + r'\.ix?\d+" class="ltx_item[^"]*">'
                r'<span class="ltx_tag ltx_tag_item">)(<span class="ltx_text ([^"]*)">(.*?)</span>|[^<]*)(</span>)',
                re.S,
            )

            def repl(m: re.Match) -> str:
                content = m.group(4) if m.group(3) is not None else m.group(2)
                kept = " ".join(c for c in (m.group(3) or "").split() if not c.startswith("ltx_font_"))
                all_cls = " ".join(c for c in (kept, cls) if c)
                inner = f'<span class="ltx_text {all_cls}">{content}</span>' if all_cls else content
                return m.group(1) + inner + m.group(5)

            html, n = item_re.subn(repl, html)
            changed += n
    if changed:
        report.append(f"enumitem font= applied to {changed} list labels")
    return html


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

    # 用配对计数删整块，不能用 `.*?</div>`：非贪婪会停在**第一个**闭合标签，
    # 遇到内部有嵌套的块（摘要里带 itemize、作者块用 tabular 排版）就会在中途
    # 截断——开标签被吃掉、内层的 </div></ul></li> 留在原地，产物随即失衡。
    for cls in DROP_CLASSES:
        for tag in ("div", "h1"):
            pattern = re.compile(rf'<{tag}[^>]*class="[^"]*{cls}[^"]*"[^>]*>')
            body = replace_blocks(body, pattern, tag, lambda block, m: "")

    # 标题块的脚注（\thanks、\footnotetext[1]{Corresponding author.} 之类）。
    # LaTeXML 把它们搬到文档开头一个独立的 <p> 里，而作者块已被上面的 DROP_CLASSES
    # 删掉 —— 两者不在同一个容器，于是正文顶部会孤零零留下一行
    # 「1footnotetext: Corresponding author.」，指向一个页面上根本不存在的作者列表。
    # 只清理第一个 <section> 之前的范围：正文里的脚注是内容，必须留着。
    first_section = body.find("<section")
    if first_section > 0:
        head, rest = body[:first_section], body[first_section:]
        head = replace_blocks(
            head,
            re.compile(r'<span[^>]*class="[^"]*ltx_role_footnotetext[^"]*"[^>]*>'),
            "span",
            lambda block, m: "",
        )
        head = re.sub(r"<p>\s*</p>", "", head)
        body = head + rest

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
    ap.add_argument("--tex", type=Path, default=None, help="论文主 tex 文件（读取 HTML 丢失的排版信息）")
    ap.add_argument("--bbl", type=Path, default=None, help="BibTeX 生成的 .bbl（参考文献标签与顺序以它为准）")
    ap.add_argument("--bib", type=Path, action="append", default=[], help=".bib 文件（补引用链接的标题），可重复")
    args = ap.parse_args()

    html = args.html.read_text(encoding="utf-8")
    xml_path = args.xml or args.html.with_suffix(".xml")
    xml_text = xml_path.read_text(encoding="utf-8", errors="replace") if xml_path.exists() else ""
    id_to_file = build_image_map(xml_path)
    width_ratio = build_width_map(xml_path)
    tex = TexSource(args.tex) if args.tex and args.tex.exists() else None
    global BASE_PT
    if tex:
        BASE_PT = tex.base_size_pt()
    bbl = parse_bbl(args.bbl.read_text(encoding="utf-8", errors="replace")) if args.bbl and args.bbl.exists() else []
    citepunct = None
    if tex and tex.package_options("cite") is not None:
        body_def = tex.macro_body("citepunct")
        if body_def is not None:
            s = re.sub(r"\\penalty\s*(?:\\[a-zA-Z@]+|-?\d+)\s*", "", body_def)
            s = re.sub(r"\\(?: |space(?![a-zA-Z]))", " ", s).replace("~", "\xa0")
            citepunct = re.sub(r"\\[a-zA-Z@]+\s*", "", s).replace("{", "").replace("}", "")
    report: list[str] = []
    image_files: dict[str, Path] = {}
    if args.figures and args.figures.is_dir():
        # 同名多格式时按此优先级取用；矢量优先（插图的细线与小字位图会失真）
        for ext in (".svg", ".webp", ".png", ".jpg", ".jpeg"):
            for p in sorted(args.figures.glob(f"*{ext}")):
                image_files.setdefault(p.stem, p)

    # 需要整篇（含附录、摘要）才能与源码 / XML 对齐的修正，先在完整 HTML 上做
    html = fix_bibliography(html, xml_text, bbl, bib_titles(args.bib), citepunct, report)
    html = fix_cleveref(html, tex, report)
    html = fix_algorithms(html, tex, report)
    html = fix_list_fonts(html, tex, report)

    display_ids = collect_display_ids(html)
    body = extract_body(html, args.appendix)
    body = drop_nested_pagination(body)
    body = restore_qedhere(body)
    # align 组要先整组合并，否则下一步会把各片段拆成独立公式
    body = convert_equation_groups(body, tex.text_spacing() if tex else {})
    body = convert_math(body, display_ids)
    body = attach_inline_punctuation(body)
    body = float_hfill_squares(body, tex)
    body, missing = fix_images(body, id_to_file, image_files, width_ratio)
    body = add_heading_ids(body)

    args.output.write_text(body, encoding="utf-8")

    print(f"wrote {args.output} ({len(body):,} bytes)")
    for line in report:
        print(("  " if not line.startswith("WARNING") else "") + line, file=sys.stderr if line.startswith("WARNING") else sys.stdout)
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
