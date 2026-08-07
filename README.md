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

`static/uploads/CV.tex`（中文）/ `CV_en.tex`（英文），XeLaTeX。
**必须在 `static/uploads/` 目录下编译**（字体与图片走相对路径）：

```bash
cd static/uploads && latexmk -xelatex CV.tex
```

顶栏用 tikz overlay 定位，**必须连编两遍**（`latexmk` 会自动跑足）。只编一遍顶栏会静默
消失——编译照样报成功、照样单页。改完用 `pdffonts CV.pdf | grep -ic fontawesome`
确认顶栏还在（应 ≥1），再渲染首屏肉眼看一眼。

## 几个已知问题

- 改 `assets/` 下的 JS/CSS 后产物没更新 → `rm -rf resources/_gen`（Hugo 会复用打包缓存）
- 新用的 Tailwind 动态 class 首次不生效、页面塌掉 → 重启 `hugo server`
  （Hugo 要先把 class 写进 `hugo_stats.json`，Tailwind 才能编出 CSS）
- `hugo server` 偶发 panic（`Shift: unknown type … for "/authors"`）——Hugo 0.157 的问题，
  CI 用的是 0.156，**生产构建不受影响**，重启即可
