#!/usr/bin/env python3
"""一条命令把论文 LaTeX 源转成站内论文全文页。

用法::

    python3 scripts/paper-html/convert.py \
        --src ~/Desktop/ICML/paper \
        --slug depth-over-fidelity

流程：

1. ``latexml``      main.tex  → main.xml   （解析 LaTeX）
2. ``latexmlpost``  main.xml  → main.html  （出 HTML，数学保留原始 LaTeX）
3. ``pdftocairo``   figures/*.pdf → *.svg  （LaTeXML 自身转不了 PDF 图）
4. ``postprocess.py``                      （整理成站内 HTML 片段）
5. 产物写入 ``content/publications/<slug>/``，并替换 index.md 的正文
   （front matter 原样保留）

跨平台：macOS / Windows 都可用，前提是 latexml 与 pdftocairo 在 PATH 中。
安装见同目录 setup.sh（macOS/Linux）或 setup.ps1（Windows）。
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def need(tool: str, hint: str) -> str:
    path = shutil.which(tool)
    if not path:
        sys.exit(
            f"找不到 {tool}。\n  {hint}\n"
            f"  安装脚本：{'scripts/paper-html/setup.ps1' if sys.platform == 'win32' else 'scripts/paper-html/setup.sh'}"
        )
    return path


def run(cmd: list[str], cwd: Path | None = None) -> None:
    printable = " ".join(str(c) for c in cmd)
    print(f"  $ {printable}")
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-15:]
        print("\n".join(tail), file=sys.stderr)
        sys.exit(f"命令失败（退出码 {proc.returncode}）：{printable}")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, required=True, help="论文源目录（含 main.tex 与 figures/）")
    ap.add_argument("--slug", required=True, help="content/publications/ 下的文件夹名")
    ap.add_argument("--tex", default="main.tex", help="主 tex 文件名（默认 main.tex）")
    ap.add_argument("--appendix", action="store_true", help="连附录一起转换（默认只转正文）")
    ap.add_argument("--work", type=Path, default=None, help="中间产物目录（默认在系统临时目录，不污染论文源目录）")
    args = ap.parse_args()

    src: Path = args.src.expanduser().resolve()
    tex = src / args.tex
    if not tex.exists():
        sys.exit(f"找不到 {tex}")

    dest = REPO / "content" / "publications" / args.slug
    if not dest.is_dir():
        sys.exit(f"目标不存在：{dest}\n  请先创建该论文条目（至少要有 index.md）")
    index_md = dest / "index.md"
    if not index_md.exists():
        sys.exit(f"找不到 {index_md}")

    latexml = need("latexml", "LaTeXML 未安装（arXiv 官方 HTML 用的就是它）")
    latexmlpost = need("latexmlpost", "LaTeXML 未安装或不完整")
    pdftocairo = need("pdftocairo", "poppler 未安装（用于渲染 PDF 插图）")

    work = (args.work or (Path(tempfile.gettempdir()) / f"paper-html-{args.slug}")).resolve()
    work.mkdir(parents=True, exist_ok=True)
    xml = work / "main.xml"
    html = work / "main.html"
    img_dir = work / "figures-svg"
    img_dir.mkdir(exist_ok=True)

    # LaTeXML 没有 aliascnt 的绑定。用了它的稿件里，\newtheorem{lemma}[lemma]{Lemma}
    # 的计数器指向一个未定义的别名，结果引理/命题/推论全部渲染成没有编号的
    # 「Lemma」「Proposition」，正文里的 \cref 交叉引用随之失效（定理本身不受影响，
    # 因为它用的是自己的计数器）。这里把 aliascnt 的写法改写成等价的共享计数器
    # 语法再交给 LaTeXML —— \newtheorem{X}[Y]{Label} 本来就是「与 Y 共用计数器」。
    # 改写发生在工作目录的副本上，论文源目录不受影响。
    src_for_latexml = src
    tex_text = tex.read_text(encoding="utf-8")
    if "\\newaliascnt" in tex_text:
        alias = dict(
            re.findall(r"\\newaliascnt\{(\w+)\}\{(\w+)\}", tex_text)
        )  # 别名 -> 真实计数器
        patched = tex_text
        for name, target in alias.items():
            patched = patched.replace(
                rf"\newtheorem{{{name}}}[{name}]{{", rf"\newtheorem{{{name}}}[{target}]{{"
            )
        patched = re.sub(r"\\newaliascnt\{\w+\}\{\w+\}\s*", "", patched)
        patched = re.sub(r"\\aliascntresetthe\{\w+\}\s*", "", patched)
        patched = re.sub(r"\\usepackage\{aliascnt\}\s*", "", patched)

        src_for_latexml = work / "src"
        if src_for_latexml.exists():
            shutil.rmtree(src_for_latexml)
        shutil.copytree(src, src_for_latexml)
        (src_for_latexml / tex.name).write_text(patched, encoding="utf-8")
        print(f"      已改写 aliascnt（{', '.join(alias)} → 共用 {set(alias.values())} 计数器）")

    print("[1/5] latexml：解析 LaTeX")
    run([latexml, f"--dest={xml}", tex.name], cwd=src_for_latexml)

    print("[2/5] latexmlpost：生成 HTML（数学保留 LaTeX 源）")
    run(
        [
            latexmlpost,
            f"--dest={html}",
            "--format=html5",
            "--mathtex",          # 数学输出原始 LaTeX，交给站点的 KaTeX
            "--nodefaultresources",  # 不要 LaTeXML 自带的 CSS/JS
            "--novalidate",
            str(xml),
        ],
        cwd=src,
    )

    print("[3/5] 插图：PDF → SVG（矢量，无损）")
    # 曾试过位图（PNG→WebP，统一像素宽度），但论文插图里的细线、小号刻度文字
    # 在任何质量下都能看出与 PDF 的差别，故改回矢量。显示尺寸由 CSS 统一控制，
    # 与图源的固有尺寸无关。
    figures = src / "figures"
    count = 0
    if figures.is_dir():
        for pdf in sorted(figures.rglob("*.pdf")):
            run([pdftocairo, "-svg", str(pdf), str(img_dir / (pdf.stem + ".svg"))])
            count += 1
    print(f"      转换 {count} 张")

    print("[4/5] postprocess：整理为站内 HTML 片段")
    fragment = work / "body.html"
    cmd = [
        sys.executable,
        str(HERE / "postprocess.py"),
        str(html),
        "-o",
        str(fragment),
        "--xml",
        str(xml),
        "--figures",
        str(img_dir),
    ]
    if args.appendix:
        cmd.append("--appendix")
    run(cmd)

    print("[5/5] 写入站点")
    body = fragment.read_text(encoding="utf-8")

    # 清掉上一轮遗留的插图（可能是别的格式或已不再引用的图），
    # 但保留 featured.*（列表页封面，由人工挑选，不属于本流程产物）
    stems = {p.stem for p in img_dir.iterdir()}
    for old in dest.iterdir():
        if old.is_file() and old.stem in stems and not old.stem.startswith("featured"):
            old.unlink()

    # 只有正文引用到的图才拷进 page bundle，避免未引用的图白白进仓库
    used = 0
    for img in sorted(img_dir.iterdir()):
        if f'src="{img.name}"' in body:
            shutil.copy2(img, dest / img.name)
            used += 1

    raw = index_md.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        sys.exit(f"{index_md} 缺少 front matter，已中止（不覆盖）")
    parts = raw.split("---", 2)
    front = "---" + parts[1] + "---\n"
    index_md.write_text(front + "\n" + body + "\n", encoding="utf-8")

    print(f"      图片 {used} 张 → {dest.relative_to(REPO)}")
    print(f"      正文 {len(body):,} 字节 → {index_md.relative_to(REPO)}")
    print("\n完成。front matter 未被改动；本地预览：hugo server")
    return 0


if __name__ == "__main__":
    sys.exit(main())
