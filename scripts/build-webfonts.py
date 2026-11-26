#!/usr/bin/env python3
"""生成站点网页字体（woff2），并逐字形校验无损。

为什么要这一步：fonts/ 里的原始字体是 TTF，未压缩；中文的方正新书宋简体单个
就 2.7 MB，中文博客页每次都要整份下载，走跨境线路要好几秒。

做两件事：
1. 西文字体（CMU Serif 四个字重、Fira Code 两个字重）整份转成 woff2。
   woff2 只是 TTF 的压缩封装（Brotli + 可逆的 glyf 变换），字形、度量、hinting
   原样保留，体积约为 TTF 的一半。
2. 中文字体按字频切成多个 woff2 分片，每片在 CSS 里用 unicode-range 声明。
   浏览器只下载当前页面实际用到的字所在的分片。分片覆盖字体里的每一个字，
   所以对任何页面都不缺字；顺序按站内正文的字频排，常用字集中在前几片，
   一篇文章通常只命中少数几片。

生成物：fonts/web/*.woff2、fonts/web/cjk/*.woff2，以及 assets/css/custom.css 里
「BEGIN/END generated CJK font slices」之间的 @font-face 声明（脚本会整段重写）。
原始 TTF 不动：简历的 XeLaTeX 仍从 fonts/ 读 TTF。

依赖：pip install fonttools brotli
用法：python scripts/build-webfonts.py
新增大量文章后可重跑一次，让分片顺序跟上新的字频（不重跑也不会缺字）。
"""

from __future__ import annotations

import collections
import io
import pathlib
import re
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = ROOT / "fonts"
OUT = FONTS / "web"
CSS = ROOT / "assets" / "css" / "custom.css"

LATIN = [
    ("cmu-serif/cmunrm.ttf", "cmunrm.woff2"),
    ("cmu-serif/cmunti.ttf", "cmunti.woff2"),
    ("cmu-serif/cmunbx.ttf", "cmunbx.woff2"),
    ("cmu-serif/cmunbi.ttf", "cmunbi.woff2"),
    ("Fira_Code/static/FiraCode-Regular.ttf", "FiraCode-Regular.woff2"),
    ("Fira_Code/static/FiraCode-Bold.ttf", "FiraCode-Bold.woff2"),
]
CJK_SRC = FONTS / "方正新书宋简体" / "方正新书宋简体.ttf"
CJK_FAMILY = "SiteTextCJK"
CJK_PREFIX = "fzxss"

# 站内用到的字按字频分片；越靠前的分片越常被命中，所以前面切小、后面切大。
USED_SLICE_SIZES = [150, 200, 250, 300, 400]  # 之后的「站内字」每片 500
USED_SLICE_DEFAULT = 500
REST_SLICE = 800  # 站内没用到的字（按码位顺序），只在新文章用到生僻字时才会下载

BEGIN = "/* BEGIN generated CJK font slices (scripts/build-webfonts.py) */"
END = "/* END generated CJK font slices */"


def glyph_signature(font: TTFont, gname: str):
    """字形的完整几何描述：轮廓点、端点、flags、组件、进宽。用来做无损比对。"""
    glyf = font["glyf"]
    g = glyf[gname]
    if g.isComposite():
        comps = tuple(
            (c.glyphName, c.x, c.y, c.flags, tuple(getattr(c, "transform", ()) or ()))
            for c in g.components
        )
        outline = ("composite", comps)
    elif g.numberOfContours == 0:
        outline = ("empty",)
    else:
        coords, ends, flags = g.getCoordinates(glyf)
        outline = ("simple", tuple(coords), tuple(ends), tuple(f & 1 for f in flags))
    adv = font["hmtx"][gname]
    vadv = font["vmtx"][gname] if "vmtx" in font else None
    return outline, adv, vadv


def latin_woff2() -> list[tuple[str, int, int]]:
    rows = []
    for src_rel, dst_name in LATIN:
        src = FONTS / src_rel
        dst = OUT / dst_name
        f = TTFont(src)
        f.flavor = "woff2"
        f.save(dst)
        # 无损校验：解回来逐字形比对
        a, b = TTFont(src), TTFont(dst)
        assert a.getGlyphOrder() == b.getGlyphOrder(), dst_name
        assert a.getBestCmap() == b.getBestCmap(), dst_name
        for g in a.getGlyphOrder():
            assert glyph_signature(a, g) == glyph_signature(b, g), (dst_name, g)
        rows.append((dst_name, src.stat().st_size, dst.stat().st_size))
    return rows


def site_char_frequency(cjk_cmap: dict, latin_cmap: dict) -> collections.Counter:
    """站内正文里、需要用中文字体显示的字（西文字体没有的）的出现次数。"""
    cnt: collections.Counter = collections.Counter()
    for p in (ROOT / "content").rglob("*"):
        if p.is_file() and p.suffix in (".md", ".html"):
            for ch in p.read_text(encoding="utf-8", errors="ignore"):
                o = ord(ch)
                if o in cjk_cmap and o not in latin_cmap:
                    cnt[o] += 1
    for p in (ROOT / "data").rglob("*.yaml"):
        for ch in p.read_text(encoding="utf-8", errors="ignore"):
            o = ord(ch)
            if o in cjk_cmap and o not in latin_cmap:
                cnt[o] += 1
    return cnt


def plan_slices(cjk_cmap: dict, latin_cmap: dict) -> list[list[int]]:
    freq = site_char_frequency(cjk_cmap, latin_cmap)
    used = sorted(freq, key=lambda c: (-freq[c], c))
    rest = sorted(c for c in cjk_cmap if c not in freq)
    slices: list[list[int]] = []
    i = 0
    k = 0
    while i < len(used):
        size = USED_SLICE_SIZES[k] if k < len(USED_SLICE_SIZES) else USED_SLICE_DEFAULT
        slices.append(used[i : i + size])
        i += size
        k += 1
    for j in range(0, len(rest), REST_SLICE):
        slices.append(rest[j : j + REST_SLICE])
    covered = [c for s in slices for c in s]
    assert sorted(covered) == sorted(cjk_cmap), "分片必须恰好覆盖字体的全部码位"
    return slices


def subset_options() -> subset.Options:
    o = subset.Options()
    o.flavor = "woff2"
    o.layout_features = ["*"]  # 保留全部 OpenType 特性（含竖排 vert 等）
    o.name_IDs = ["*"]
    o.name_languages = ["*"]
    o.glyph_names = True
    o.notdef_outline = True
    o.hinting = True
    o.legacy_kern = True
    o.recalc_bounds = False
    o.recalc_timestamp = False
    return o


def unicode_range(cps: list[int]) -> str:
    cps = sorted(cps)
    parts = []
    start = prev = cps[0]
    for c in cps[1:]:
        if c == prev + 1:
            prev = c
            continue
        parts.append(f"U+{start:X}" if start == prev else f"U+{start:X}-{prev:X}")
        start = prev = c
    parts.append(f"U+{start:X}" if start == prev else f"U+{start:X}-{prev:X}")
    return ", ".join(parts)


def cjk_slices(latin_cmap: dict) -> tuple[list[tuple[str, list[int], int]], int]:
    src_font = TTFont(CJK_SRC)
    cjk_cmap = src_font.getBestCmap()
    slices = plan_slices(cjk_cmap, latin_cmap)
    out_dir = OUT / "cjk"
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob(f"{CJK_PREFIX}-*.woff2"):
        old.unlink()
    rows = []
    for idx, cps in enumerate(slices):
        name = f"{CJK_PREFIX}-{idx:03d}.woff2"
        font = TTFont(CJK_SRC)
        sub = subset.Subsetter(options=subset_options())
        sub.populate(unicodes=cps)
        sub.subset(font)
        buf = io.BytesIO()
        font.flavor = "woff2"
        font.save(buf)
        (out_dir / name).write_bytes(buf.getvalue())
        # 无损校验：分片里每个字的字形与原字体完全一致
        chk = TTFont(out_dir / name)
        chk_cmap = chk.getBestCmap()
        for c in cps:
            assert chk_cmap.get(c) is not None, (name, hex(c))
            assert glyph_signature(chk, chk_cmap[c]) == glyph_signature(src_font, cjk_cmap[c]), (name, hex(c))
        rows.append((name, cps, len(buf.getvalue())))
    return rows, CJK_SRC.stat().st_size


def write_css(rows) -> None:
    lines = [BEGIN, "/* 方正新书宋简体按字频切片：浏览器只下载页面实际用到的字所在的分片 */"]
    for name, cps, _ in rows:
        lines += [
            "@font-face {",
            f'  font-family: "{CJK_FAMILY}";',
            f'  src: url("/fonts/web/cjk/{name}") format("woff2");',
            "  font-weight: 400;",
            "  font-style: normal;",
            "  font-display: swap;",
            f"  unicode-range: {unicode_range(cps)};",
            "}",
        ]
    lines.append(END)
    raw = CSS.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8").replace("\r\n", "\n")
    block = "\n".join(lines)
    if BEGIN in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        sys.exit(f"custom.css 里找不到标记 {BEGIN!r}，请先放好占位标记")
    CSS.write_bytes(text.replace("\n", nl).encode("utf-8"))


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    latin = latin_woff2()
    latin_cmap = TTFont(FONTS / "cmu-serif" / "cmunrm.ttf").getBestCmap()
    rows, cjk_ttf = cjk_slices(latin_cmap)
    write_css(rows)
    print("西文 woff2（逐字形校验一致）：")
    for name, a, b in latin:
        print(f"  {name:26s} {a/1024:7.0f} KB -> {b/1024:6.0f} KB")
    total = sum(r[2] for r in rows)
    print(f"中文分片（逐字形校验一致）：{len(rows)} 片，覆盖 {sum(len(r[1]) for r in rows)} 字，"
          f"合计 {total/1024:.0f} KB（原 TTF {cjk_ttf/1024:.0f} KB）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
