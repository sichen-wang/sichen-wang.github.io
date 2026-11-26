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
- `--work`：中间产物目录（默认系统临时目录下的 `paper-html-<slug>`）
- `--dest`：写到别的 page bundle 目录（须已有 `index.md`），用于对比或试转，
  不碰仓库里的论文正文

脚本**只替换 `index.md` 的正文，front matter 原样保留**，所以标题、作者、日期、
按钮链接这些不会被覆盖。论文源目录会先整份复制到 `<work>/src`，LaTeXML、BibTeX
的日志与中间文件都落在副本里，源目录保持原样。

新增 publications 要与现有论文详情保持一致时，需要加入可读的 HTML 正文，
不能只添加摘要与 PDF。完整论文使用 `--appendix`，并核对参考文献与补充材料。

### 转换器已自动处理的项

以下是 LaTeXML 与 PDF 不一致、过去要逐篇手工补的地方，现在由 `convert.py` /
`postprocess.py` 处理，运行时会逐项打印处理了多少处（`WARNING` 开头的是没能
自动对齐、需要人工看的）：

- **参考文献**：源目录有 `main.bbl` 就用它，没有就用 BibTeX 生成（按源码的引用
  合成 aux，不需要先跑 pdflatex）。样式不在 LaTeXML 内置列表（如 `alphaurl`），
  或 natbib 配 alpha 标签时，工作副本里的 `.bib` 会被移走，让 LaTeXML 改读 `.bbl`；
  条目标签与正文引用按 `.bbl` 的 `\bibitem[标签]` 改正（修掉「AA [88]」与退化成
  序号的引用，et al. 的「+」为上标）；条目顺序以 `.bbl` 为准；读 `.bbl` 时空着的
  引用悬停标题从 `.bib` 补上。natbib 的样式钩子（plainnat → 方括号、逗号分隔）、
  cite 宏包的 `\citepunct` 按源码生效；文献备注里的 URL 变成链接；落进 `<span>`
  的分页 div 删掉。
- **align 组**：整格文字的列（`\text{splitter:}\qquad &`）还原为 `\text{…}`，
  文字后的间距按源码补回；以 `&` 开头的行补回空的右对齐列；`\hskip` 还原为 `\hspace`。
- **算法**：`\REQUIRE` / `\Require` / `\ENSURE` 行不编号，加上标签（读源码里的
  `\renewcommand{\algorithmicrequire}`），后续行号与引用行号的链接顺延。
- **cleveref**：公式引用补括号（「Equation (3.9)」）；同一 `\cref` 里类型不同的目标
  按类型分组（「Theorem 1.1 and Corollary 1.3」）；同类型内排序，三个以上连号压缩
  成「Equations (2.1) to (2.3)」——与 cleveref 默认的 sort&compress 一致。
- **其他**：行间公式里的 `\qedhere` 补回右端的 ∎；enumitem 的 `font=`
  （如 `description[font=\normalfont\itshape]`）作用到列表标签；行内公式以
  `\times`、`+` 等二元运算符结尾时先加花括号，再并入后面的标点；
  `\hfill$\square$` 右浮动。

### 仍需人工核对的项

转换成功不代表内容已完全保真。验收时还需对照源稿与 PDF 检查：

- 运行输出里的 `WARNING`：源码与 HTML 的算法 / 列表数目对不上、文献条目找不到
  `.bbl` key 时，相应修正会跳过。
- `thm-restate` 的星号重述可能被 LaTeXML 简化为 `See N`，需恢复完整定理，
  给副本使用不同的 ID，并保留原落点与交叉引用。
- `algorithmic` 的 `\Statex` 输入/初始化说明应不带行号；PDF 的固定栏宽需
  改为网页自适应布局。正文以 HTML 直接渲染，避免算法缩进被当成 Markdown 代码。
- 数学中的 `\eqref` 需按原稿 `.aux` 的实际编号展开；不支持的字体命令也需
  等价处理。TikZ 可从原稿编译为 SVG，核对文字、箭头和图注。
- 公式编号需逐项对照原 PDF；例如带 `\qedhere` 的公式可能被 LaTeXML 额外编号，
  进而使后续编号和引用整体偏移。不能仅检查引用目标是否存在。带编号公式
  （`equation` + `split`）里的 `\qedhere` 仍会丢掉 ∎。
- align 的 `\\[4pt]` 额外行距、`\cellcolor` 等表格底色（暗色模式下宜改半透明）、
  个别表格的不换行或竖线，需对照 PDF 手工调整。
- 检查各章节、定理/证明、公式编号、表格、算法行号和参考文献是否完整，
  所有内部锚点、图片是否有效，再运行公式检查、构建与浏览器验收。

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
  紧随行内公式的标点会并入末尾的 `\text{...}`，防止逗号或句点独占下一行。
- **align 组必须整组渲染**：LaTeXML 把 `align` 拆成表格，每个 `&` 片段是独立的
  `<span class="ltx_Math">`。若逐个替换成 `$...$`，每段会被 KaTeX 当成独立公式，
  跨行对齐丢失、片段各自断行（表现为 `= m_t +` 单独一行）。`convert_equation_groups`
  会保留原稿的每一行和空对齐单元格，多列还原成 `aligned`，单列还原成居中的
  `gathered`。以关系符开头的续行也保留换行，不因网页版心较宽而自动合并；
  表格的居中填充单元格不作为公式列。编号不进 LaTeX（KaTeX 的 aligned 内不支持
  `\tag`），改由右侧独立 HTML 编号按组高排列，原公式锚点继续保留。
  原稿的 `\\[4pt]` 等额外行距可能已被上游 HTML 丢弃，需对照 TeX 恢复。
- **对照源码**：LaTeXML 丢掉的信息（文字后的间距、`\algorithmicrequire`、
  enumitem 的 `font=`、`\citepunct`、cleveref 的名称与选项、正文字号）由
  `postprocess.py` 的 `TexSource` 从源码读取：展开 `\input`/`\include`、去掉注释，
  同目录的 `.sty` 也一并扫描（会议模板常在里面加载 natbib）。需要按出现顺序对齐的
  修正（算法、列表）只在源码与 HTML 的数目一致时才做。
- **natbib 的样式钩子**：`\bibliographystyle{plainnat}` 在 LaTeX 里经 `.aux` 于
  `\begin{document}` 生效，LaTeXML 读到它时正文引用已经排完。`convert.py` 在工作
  副本的导言区末尾补一句 `\@ifpackageloaded{natbib}{\bibstyle{…}}{}`；natbib 带
  round/square/numbers 等选项时 `\bibstyle` 本来就被禁用，行为与 LaTeX 一致。
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
| `convert.py` | 一条命令跑完整流程（跨平台）：源码副本、`.bbl` 选择与生成、LaTeXML、插图 |
| `postprocess.py` | LaTeXML HTML → 站内 HTML 片段（纯标准库），含对照源码 / `.bbl` 的各项修正 |
| `setup.sh` / `setup.ps1` | 安装工具链 |
