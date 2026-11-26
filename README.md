# Sichen Wang's Academic Website & Digital Garden

基于 [Hugo Blox](https://hugoblox.com) 的 academic-cv 模板，部署到 GitHub Pages
（`hugoblox.yaml` 里 `deploy.host: github-pages`，push 到 `main` 触发 `.github/workflows/deploy.yml`）。

## 常用命令

| 命令 | 作用 |
|---|---|
| `npm run dev` | 本地预览（含 Pagefind 搜索索引） |
| `npm run build` | 生产构建 |
| `npm run check:math` | 用 KaTeX 离线校验全站公式 |

`check:math` 值得每次发文前跑一次：站点的 KaTeX 配的是 `throwOnError: false`，
公式写错不会报错，只会在页面上显示成一段红色源码，肉眼翻不出来。

## 本地脚本

- `scripts/check-math.js` — 站内公式自检，列出文件/行号/错误原因，有问题时退出码为 1
- `scripts/paper-html/` — 把论文 LaTeX 源转成站内全文页（LaTeXML），详见该目录的 README
- `scripts/build-webfonts.py` — 从 `fonts/` 的 TTF 生成网页字体并逐字形校验无损：西文转 woff2，
  方正新书宋按站内字频切成 `unicode-range` 分片（中文页只下载用到的分片，约 200 KB，原 TTF 2.7 MB），
  同时重写 `custom.css` 里的分片声明。需要 `pip install fonttools brotli`。生成物入库，CI 不需要这套依赖；
  不重跑也不会缺字，新增大量中文文章后重跑一次能让常用字集中到前几片。

## 字体与部署体积

`fonts/` 挂载到站点的 `/fonts/`，但 `config/_default/module.yaml` 只发布网页实际引用的文件
（`fonts/web/` 的 woff2 和西文 TTF 后备）。其余字体（Sarasa 等约 250 MB）只供简历等本地排版用，
不进部署产物。CSS 新引用 `fonts/` 下的其他文件时，要同步把它加进挂载的 `files` 列表。

## 论文条目

每篇一个目录 `content/publications/<slug>/`：`index.md`（front matter + 全文 HTML）、
`cite.bib`、`paper.pdf`。列表页由 `layouts/publications/section.html` 渲染：

- 按 `publication_types` 分两组：含 `manuscript` 的进 Preprints，其余进 Accepted Papers；
  录用后改掉 `manuscript`、把 `publication_short` 改成会议名，条目自动换组。
- 卡片上的一句话摘要取 `tldr` 字段（已录用的取 OpenReview 的 TL;DR），留空不显示；
  标签页里的论文卡片同样只显示 `tldr`，不再回落到整段 abstract。
- 新论文的全文用 `scripts/paper-html/` 转换，不能只放摘要和 PDF。

## 覆盖了主题的这些文件

`upgrade.yml` 升级 Hugo Blox 后若行为异常，先看这几处本地覆盖是否与上游脱节
（每个文件头部都写了改动原因）：

```
layouts/single.html
layouts/_partials/site_footer.html
layouts/_partials/components/toc.html
layouts/_partials/jsonld/webpage.html
layouts/_partials/views/card.html
layouts/_partials/views/card--start.html
layouts/_partials/views/article-grid--start.html
layouts/_partials/hbx/blocks/resume-biography-3/block.html
assets/js/hb-citation.js
```

## 简历

`static/uploads/CV_zh.tex`（中文）/ `CV_en.tex`（英文），XeLaTeX。
**必须在 `static/uploads/` 目录下编译**（字体与图片走相对路径）：

```bash
cd static/uploads && latexmk -xelatex CV_zh.tex && latexmk -xelatex CV_en.tex
```

顶栏用 tikz overlay 定位，**必须连编两遍**（`latexmk` 会自动跑足）。只编一遍顶栏会静默
消失——编译照样报成功、照样单页。改完用 `pdffonts CV_en.pdf | grep -ic fontawesome`
确认顶栏还在（应 ≥1），再渲染首屏肉眼看一眼。

## 几个已知问题

- 改 `assets/` 下的 JS/CSS 后产物没更新 → `rm -rf resources/_gen`（Hugo 会复用打包缓存）
- 新用的 Tailwind 动态 class 首次不生效、页面塌掉 → 重启 `hugo server`
  （Hugo 要先把 class 写进 `hugo_stats.json`，Tailwind 才能编出 CSS）
- `hugo server` 偶发 panic（`Shift: unknown type … for "/authors"`）——Hugo 0.157 的问题，
  CI 用的是 0.156，**生产构建不受影响**，重启即可
