#!/usr/bin/env python3
"""一条命令把论文 LaTeX 源转成站内论文全文页。

用法::

    python3 scripts/paper-html/convert.py \
        --src ~/Desktop/ICML/paper \
        --slug depth-over-fidelity

流程：

0. 把论文源目录复制到工作目录（latexml / bibtex 的日志与中间文件都落在副本里，
   源目录保持原样），在副本上做必要的改写（见下）
1. ``latexml``      main.tex  → main.xml   （解析 LaTeX）
2. ``latexmlpost``  main.xml  → main.html  （出 HTML，数学保留原始 LaTeX）
3. ``pdftocairo``   figures/*.pdf → *.svg  （LaTeXML 自身转不了 PDF 图）
4. ``postprocess.py``                      （整理成站内 HTML 片段）
5. 产物写入 ``content/publications/<slug>/``（或 ``--dest``），并替换 index.md 的正文
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
sys.path.insert(0, str(HERE))
import postprocess as pp  # noqa: E402  （同目录模块：TeX 源码解析与 .bbl 解析）

# LaTeX.pool.ltxml 里 $BIBSTYLES 认识的样式；其余样式（alphaurl 等）LaTeXML 只能
# 忽略，用自己的格式排 .bib，标签与顺序都和 PDF 对不上。
LATEXML_BIBSTYLES = {"plain", "unsrt", "alpha", "abbrv", "plainnat", "unsrtnat", "alphanat", "abbrvnat"}


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


def patch_aliascnt(tex_text: str) -> tuple[str, dict[str, str]]:
    """LaTeXML 没有 aliascnt 的绑定。

    用了它的稿件里，\\newtheorem{lemma}[lemma]{Lemma} 的计数器指向一个未定义的别名，
    结果引理/命题/推论全部渲染成没有编号的「Lemma」「Proposition」，正文里的 \\cref
    交叉引用随之失效（定理本身不受影响，因为它用的是自己的计数器）。这里把 aliascnt
    的写法改写成等价的共享计数器语法 —— \\newtheorem{X}[Y]{Label} 本来就是「与 Y 共用
    计数器」。
    """
    if "\\newaliascnt" not in tex_text:
        return tex_text, {}
    alias = dict(re.findall(r"\\newaliascnt\{(\w+)\}\{(\w+)\}", tex_text))  # 别名 -> 真实计数器
    patched = tex_text
    for name, target in alias.items():
        patched = patched.replace(rf"\newtheorem{{{name}}}[{name}]{{", rf"\newtheorem{{{name}}}[{target}]{{")
    patched = re.sub(r"\\newaliascnt\{\w+\}\{\w+\}\s*", "", patched)
    patched = re.sub(r"\\aliascntresetthe\{\w+\}\s*", "", patched)
    patched = re.sub(r"\\usepackage\{aliascnt\}\s*", "", patched)
    return patched, alias


def find_bib(src: Path, name: str) -> Path | None:
    for cand in (src / name, src / f"{name}.bib"):
        if cand.is_file() and cand.suffix == ".bib":
            return cand
    return None


def make_bbl(work_src: Path, jobname: str, style: str, bibfiles: list[str], tex: pp.TexSource) -> Path | None:
    """源目录没有 .bbl 时用 BibTeX 生成一份（PDF 的参考文献就是它排的）。

    有 main.aux 就直接用；没有就按源码里的引用顺序合成一个只含 \\citation /
    \\bibstyle / \\bibdata 的 aux —— BibTeX 只读这三样，不必先跑一遍 pdflatex
    （也就不受缺宏包、缺字体的影响）。
    """
    bibtex = shutil.which("bibtex")
    if not bibtex:
        print("      （未找到 bibtex，跳过生成 .bbl）")
        return None
    aux = work_src / f"{jobname}.aux"
    if not aux.exists():
        keys: list[str] = []
        for m in re.finditer(
            r"\\(?!citetext)(?:[cC]ite[a-zA-Z]*|nocite)\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}", tex.body
        ):
            for k in m.group(1).split(","):
                if k.strip() and k.strip() not in keys:
                    keys.append(k.strip())
        aux.write_text(
            "\\relax\n"
            + "".join(f"\\citation{{{k}}}\n" for k in keys)
            + f"\\bibstyle{{{style}}}\n\\bibdata{{{','.join(bibfiles)}}}\n",
            encoding="utf-8",
        )
    proc = subprocess.run([bibtex, jobname], cwd=work_src, capture_output=True, text=True)
    bbl = work_src / f"{jobname}.bbl"
    if proc.returncode > 1 or not bbl.exists() or "\\bibitem" not in bbl.read_text(encoding="utf-8", errors="replace"):
        tail = (proc.stdout or proc.stderr or "").strip().splitlines()[-5:]
        print("      bibtex 未能生成 .bbl：\n        " + "\n        ".join(tail))
        return None
    return bbl


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=Path, required=True, help="论文源目录（含 main.tex 与 figures/）")
    ap.add_argument("--slug", required=True, help="content/publications/ 下的文件夹名")
    ap.add_argument("--tex", default="main.tex", help="主 tex 文件名（默认 main.tex）")
    ap.add_argument("--appendix", action="store_true", help="连附录一起转换（默认只转正文）")
    ap.add_argument("--work", type=Path, default=None, help="中间产物目录（默认在系统临时目录，不污染论文源目录）")
    ap.add_argument(
        "--dest",
        type=Path,
        default=None,
        help="写入的 page bundle 目录（默认 content/publications/<slug>；对比或预览时可指向别处，须已有 index.md）",
    )
    args = ap.parse_args()

    src: Path = args.src.expanduser().resolve()
    tex_path = src / args.tex
    if not tex_path.exists():
        sys.exit(f"找不到 {tex_path}")

    dest = (args.dest.expanduser().resolve() if args.dest else REPO / "content" / "publications" / args.slug)
    if not dest.is_dir():
        sys.exit(f"目标不存在：{dest}\n  请先创建该论文条目（至少要有 index.md）")
    index_md = dest / "index.md"
    if not index_md.exists():
        sys.exit(f"找不到 {index_md}")

    latexml = need("latexml", "LaTeXML 未安装（arXiv 官方 HTML 用的就是它）")
    latexmlpost = need("latexmlpost", "LaTeXML 未安装或不完整")
    pdftocairo = need("pdftocairo", "poppler 未安装（用于渲染 PDF 插图）")

    work = (args.work or (Path(tempfile.gettempdir()) / f"paper-html-{args.slug}")).resolve()
    if work == src or src in work.parents:
        sys.exit(f"--work 不能放在论文源目录里：{work}")
    work.mkdir(parents=True, exist_ok=True)
    xml = work / "main.xml"
    html = work / "main.html"
    img_dir = work / "figures-svg"
    if img_dir.exists():
        shutil.rmtree(img_dir)
    img_dir.mkdir()

    # ---- 0. 源码副本 -------------------------------------------------------
    # latexml 把 main.latexml.log、latexmlpost 把 main.latexmlpost.log 写进当前目录，
    # bibtex 还会写 .aux/.bbl/.blg；全部在副本里运行，论文源目录不留任何痕迹。
    work_src = work / "src"
    if work_src.exists():
        shutil.rmtree(work_src)
    shutil.copytree(src, work_src)
    main_tex = work_src / tex_path.name
    tex_text = main_tex.read_text(encoding="utf-8")

    tex_text, alias = patch_aliascnt(tex_text)
    if alias:
        print(f"      已改写 aliascnt（{', '.join(alias)} → 共用 {set(alias.values())} 计数器）")

    # natbib 的预定义样式钩子（plainnat → 方括号、逗号分隔）由 \bibliographystyle 经
    # .aux 在 \begin{document} 时生效；LaTeXML 读到 \bibliographystyle 时正文引用早已
    # 排完，于是 citep / citet 一律退回默认的圆括号与分号。在导言区末尾补一次
    # \bibstyle：natbib 带 round/square/numbers 等选项时它本来就被禁用（\@gobble），
    # 与 LaTeX 的行为一致；未加载 natbib 时不做任何事。
    tex = pp.TexSource(main_tex)
    style, bibnames = tex.bibliography()
    # 第一个不在注释里的 \begin{document}：本行去掉注释后它仍在
    doc = next(
        (
            m
            for m in re.finditer(r"\\begin\{document\}", tex_text)
            if pp.strip_tex_comments(tex_text[tex_text.rfind("\n", 0, m.start()) + 1 : m.end()]).endswith(m.group(0))
        ),
        None,
    )
    if style and doc:
        hook = f"\\makeatletter\\@ifpackageloaded{{natbib}}{{\\bibstyle{{{style}}}}}{{}}\\makeatother\n"
        tex_text = tex_text[: doc.start()] + hook + tex_text[doc.start() :]
    main_tex.write_text(tex_text, encoding="utf-8")

    # ---- 参考文献：.bib 还是 .bbl -----------------------------------------
    bbl: Path | None = None
    bib_files = [p for p in (find_bib(work_src, n) for n in bibnames) if p]
    if bibnames:
        bbl = work_src / f"{main_tex.stem}.bbl"
        if bbl.exists():
            print(f"      参考文献：源目录自带 {bbl.name}")
        elif style and bib_files:
            bbl = make_bbl(work_src, main_tex.stem, style, bibnames, pp.TexSource(main_tex))
            if bbl:
                print(f"      参考文献：已用 bibtex（{style}）生成 {bbl.name}")
        else:
            bbl = None
    if bbl and bib_files:
        entries = pp.parse_bbl(bbl.read_text(encoding="utf-8", errors="replace"))
        alpha = bool(entries) and sum(pp.is_alpha_label(lab) for _, lab in entries) >= 0.8 * len(entries)
        natbib = tex.package_options("natbib") is not None
        reason = None
        if style and style not in LATEXML_BIBSTYLES:
            reason = f"样式 {style} 不在 LaTeXML 内置列表"
        elif natbib and alpha:
            reason = "natbib 配 alpha 标签（LaTeXML 会把 AA88 拆成「AA [88]」）"
        if reason:
            # LaTeXML 只在找不到 .bib 时才读 .bbl（LaTeX.pool 的 \lx@ifusebbl）
            hidden = work / "hidden-bib"
            if hidden.exists():
                shutil.rmtree(hidden)
            hidden.mkdir()
            moved = []
            for p in bib_files:
                target = hidden / p.name
                shutil.move(str(p), str(target))
                moved.append(target)
            bib_files = moved
            print(f"      参考文献：{reason}，改读 {bbl.name}（.bib 已移出工作副本）")
    elif bibnames and not bbl:
        print("      参考文献：没有 .bbl，文献顺序无法与 PDF 核对")

    print("[1/5] latexml：解析 LaTeX")
    run([latexml, f"--dest={xml}", main_tex.name], cwd=work_src)

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
        cwd=work_src,
    )

    print("[3/5] 插图：PDF → SVG（矢量，无损）")
    # 曾试过位图（PNG→WebP，统一像素宽度），但论文插图里的细线、小号刻度文字
    # 在任何质量下都能看出与 PDF 的差别，故改回矢量。显示尺寸由 CSS 统一控制，
    # 与图源的固有尺寸无关。
    figures = work_src / "figures"
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
        "--tex",
        str(main_tex),
    ]
    if bbl:
        cmd += ["--bbl", str(bbl)]
    # .bib 用来给引用链接补标题（读 .bbl 时 LaTeXML 拿不到），以及按标题把条目对回 key
    for p in bib_files:
        cmd += ["--bib", str(p)]
    if args.appendix:
        cmd.append("--appendix")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    print("  $ " + " ".join(cmd))
    for line in (proc.stdout + proc.stderr).strip().splitlines():
        print(f"      {line}")
    if proc.returncode != 0:
        sys.exit(f"postprocess 失败（退出码 {proc.returncode}）")

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

    shown = dest.relative_to(REPO) if REPO in dest.parents else dest
    print(f"      图片 {used} 张 → {shown}")
    print(f"      正文 {len(body):,} 字节 → {index_md.relative_to(REPO) if REPO in index_md.parents else index_md}")
    print("\n完成。front matter 未被改动；本地预览：hugo server")
    return 0


if __name__ == "__main__":
    sys.exit(main())
