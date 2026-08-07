# 论文全文 HTML

把论文的 LaTeX 源转成站内可读的全文页面，排版沿用本站自己的字体与配色
（CMU Serif / 方正新书宋简体 + KaTeX），而不是 LaTeXML 或 arXiv 自带的那套样式。

## 为什么工具不入库

LaTeXML 是 Perl 应用，底下依赖 `libxml2` / `libxslt` 等 C 库，装出来的是平台相关的
编译产物，塞进 git 只会得到一堆在别的机器上跑不起来的二进制。

所以这里的做法是：

- **转换产物入库** —— 生成的 HTML 正文与 SVG 插图都是纯文本，随仓库走。
  换任何一台电脑克隆下来，`hugo server` 照常跑、论文页照常在、部署照常成功，
  **日常完全不需要这套工具链**。
- **安装脚本入库** —— 只有在"转换一篇新论文"时才需要装工具，跑一次 setup 即可。

## 安装（只在需要转换新论文时）

macOS / Linux：

```bash
bash scripts/paper-html/setup.sh
```

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File scripts\paper-html\setup.ps1
```

Windows 上脚本默认推荐走 WSL。原因是 LaTeXML 需要 Strawberry Perl 现场编译 XS 模块，
Chocolatey 包与较新的 Strawberry Perl 有已知版本冲突（LaTeXML issue
[#1714](https://github.com/brucemiller/LaTeXML/issues/1714) /
[#2298](https://github.com/brucemiller/LaTeXML/issues/2298)），失败率偏高。
WSL 里一行 `apt-get install latexml poppler-utils` 就装好了。要强行原生安装就加 `-Native`。

装的是两样东西：

| 工具 | 用途 |
|---|---|
| `latexml` / `latexmlpost` | LaTeX → HTML，arXiv 官方 HTML 版用的就是它 |
| `pdftocairo`（poppler） | 论文插图 PDF → SVG（LaTeXML 自己转不了 PDF 图） |

## 使用

```bash
python3 scripts/paper-html/convert.py --src ~/Desktop/ICML/paper --slug depth-over-fidelity
```

- `--src`：论文源目录，需含 `main.tex` 与 `figures/`
- `--slug`：`content/publications/` 下的条目文件夹名（须已存在且有 `index.md`）
- `--appendix`：连附录一起转（默认只转正文）
- `--tex`：主文件名不是 `main.tex` 时指定

脚本**只替换 `index.md` 的正文，front matter 原样保留**，所以标题、作者、日期、
按钮链接这些不会被覆盖。

## 实现要点

- **不转 Markdown。** 本站数学是客户端 KaTeX（`assets/js/katex-config.js` 调
  `renderMathInElement(document.body, ...)`），扫描整个 body，所以 HTML 里的
  `$...$` 一样会被渲染。LaTeXML 已经处理好了嵌套结构、交叉引用、表格和定理环境，
  再拆成 Markdown 让 Hugo 转回 HTML 只会丢结构。
- **目录**：`layouts/_partials/components/toc.html` 原本只认 Markdown 标题，
  已加一条分支读取 HTML 标题上的 `id`；那些 `id` 由 `postprocess.py` 写入，
  两边用同一套规则，不依赖 Hugo 的 `anchorize`（规则不一致会让锚点失效）。
- **图片**：LaTeXML 没装 ImageMagick 时转不出 PDF 图，而且会把文件名一并丢掉
  （`<img src="">`）。所以图片路径改从中间产物 `main.xml` 的 `graphic=` 属性
  按 `xml:id` 取回，再指向预先用 `pdftocairo` 转好的 SVG。
- **KaTeX 兼容**：LaTeXML 会把 `\bigl(` 写成 `\bigl{(}`，LaTeX 容忍，KaTeX 报
  `Invalid delimiter type 'ordgroup'`；`postprocess.py` 会把这类花括号去掉。
  行尾续行注释 `%\n` 同理需要清除。
- **align 组必须整组渲染**：LaTeXML 把 `align` 拆成表格，每个 `&` 片段是独立的
  `<span class="ltx_Math">`。若逐个替换成 `$...$`，每段会被 KaTeX 当成独立公式，
  跨行对齐丢失、片段各自断行（表现为 `= m_t +` 单独一行）。`convert_equation_groups`
  会把整组还原成 `\begin{aligned}...\end{aligned}`；编号不进 LaTeX（KaTeX 的
  aligned 内不支持 `\tag`），改由右侧 HTML 单元格承载。
- **标签平衡自检**：提取正文若用贪婪的 `(.*)</div>`，会把 `ltx_page_content` 自己的
  闭合标签也吞进来，多出的 `</div>` 会提前关闭页面模板的 `<article>`，把页脚挤到
  外层容器（表现为页脚溢出版心）。现在改用配对计数提取，并在转换结束时检查各类
  标签是否配对，不平衡直接报错退出。
- **插图用矢量**：曾试过位图（PNG→WebP），但插图里的细线与小号刻度文字在任何
  质量下都看得出与 PDF 的差别，故改回 SVG。论文里各图靠 `\includegraphics` 的
  `width=` 缩放，转换后那层信息就没了，因此显示尺寸由 CSS 统一约束
  （宽度上限 + 高度上限），而不依赖图源的固有尺寸。
- **样式**：`assets/css/custom.css` 末尾的 `.paper-body` 一节接管所有
  `ltx_*` 结构（定理、证明、公式编号、三线表、参考文献悬挂缩进等）。

## 文件

| 文件 | 作用 |
|---|---|
| `convert.py` | 一条命令跑完整流程（跨平台） |
| `postprocess.py` | LaTeXML HTML → 站内 HTML 片段（纯标准库） |
| `setup.sh` / `setup.ps1` | 安装工具链 |
