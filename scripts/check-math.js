#!/usr/bin/env node
/**
 * 用 KaTeX 本身离线校验站内全部公式，列出会渲染失败的那些。
 *
 *   node scripts/check-math.js            # 默认扫 content/
 *   node scripts/check-math.js content/blog
 *
 * 为什么需要它：站点的 KaTeX 配置是 throwOnError:false（assets/js/katex-config.js），
 * 公式写错不会报错，只会在页面上显示成一段红色源码 —— 除非逐篇肉眼翻，否则很难发现。
 * 这个脚本用同一个 KaTeX 引擎把所有公式跑一遍，几秒钟给出完整清单。
 *
 * 退出码：有失败公式时为 1，便于挂到 CI 或 pre-commit。
 */
const fs = require("fs");
const os = require("os");
const path = require("path");

// 站点 assets/js/katex-config.js 里配置的分隔符
const DELIMS = [
  { left: "$$", right: "$$", display: true },
  { left: "\\[", right: "\\]", display: true },
  { left: "\\(", right: "\\)", display: false },
  { left: "$", right: "$", display: false },
];

function findKatex() {
  if (process.env.KATEX_JS) return process.env.KATEX_JS;
  const roots = [
    path.join(os.homedir(), "Library/Caches/hugo_cache/modules/filecache/modules/pkg/mod/github.com"),
    path.join(os.homedir(), ".cache/hugo_cache/modules/filecache/modules/pkg/mod/github.com"),
  ];
  for (const root of roots) {
    if (!fs.existsSync(root)) continue;
    const stack = [root];
    while (stack.length) {
      const dir = stack.pop();
      let entries;
      try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { continue; }
      for (const e of entries) {
        const p = path.join(dir, e.name);
        if (e.isDirectory()) stack.push(p);
        else if (e.name === "katex.min.js") return p;
      }
    }
  }
  return null;
}

function loadKatex(src) {
  // Hugo 模块缓存的路径里含 `!`（如 !hugo!blox），require 无法直接解析，
  // 先复制到临时目录再加载
  const tmp = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "katex-")), "katex.min.js");
  fs.copyFileSync(src, tmp);
  return require(tmp);
}

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith(".md")) out.push(p);
  }
  return out;
}

// 代码块里的 $ 不是公式；换成等长空白以保住偏移量，便于报行号
function maskCode(src) {
  return src
    .replace(/```[\s\S]*?```/g, (m) => m.replace(/[^\n]/g, " "))
    .replace(/`[^`\n]*`/g, (m) => " ".repeat(m.length));
}

function extract(src) {
  const found = [];
  let i = 0;
  while (i < src.length) {
    if (src[i] === "\\" && (src[i + 1] === "$" || src[i + 1] === "\\")) { i += 2; continue; }
    let matched = false;
    for (const d of DELIMS) {
      if (src.startsWith(d.left, i)) {
        const end = src.indexOf(d.right, i + d.left.length);
        if (end === -1) continue;
        found.push({ tex: src.slice(i + d.left.length, end), display: d.display, index: i });
        i = end + d.right.length;
        matched = true;
        break;
      }
    }
    if (!matched) i++;
  }
  return found;
}

const katexPath = findKatex();
if (!katexPath) {
  console.error("找不到 katex.min.js。先跑一次 hugo 让模块缓存就位，或用 KATEX_JS=/path/to/katex.min.js 指定。");
  process.exit(2);
}
const katex = loadKatex(katexPath);

const root = process.argv[2] || "content";
if (!fs.existsSync(root)) {
  console.error(`目录不存在：${root}`);
  process.exit(2);
}

const files = walk(root);
let total = 0;
const problems = [];

for (const f of files) {
  const masked = maskCode(fs.readFileSync(f, "utf8"));
  for (const m of extract(masked)) {
    if (!m.tex.trim()) continue;
    total++;
    // 论文全文页的正文是 HTML 片段，< > & 已按 HTML 规则转义；
    // 浏览器解析后 KaTeX 收到的是原字符，校验前先解码，否则全是误报
    const tex = m.tex
      .replace(/&lt;/g, "<").replace(/&gt;/g, ">")
      .replace(/&amp;/g, "&").replace(/&quot;/g, '"');
    try {
      katex.renderToString(tex, { displayMode: m.display, throwOnError: true, strict: false });
    } catch (err) {
      problems.push({
        file: path.relative(process.cwd(), f),
        line: masked.slice(0, m.index).split("\n").length,
        tex: m.tex.replace(/\s+/g, " ").trim().slice(0, 120),
        msg: String(err.message).replace(/^KaTeX parse error: /, "").slice(0, 110),
      });
    }
  }
}

console.log(`扫描 ${files.length} 篇，公式 ${total} 条，失败 ${problems.length} 条`);
if (problems.length) {
  const byFile = {};
  for (const p of problems) (byFile[p.file] = byFile[p.file] || []).push(p);
  for (const [f, list] of Object.entries(byFile)) {
    console.log(`\n── ${f}  (${list.length})`);
    for (const p of list) {
      console.log(`   L${p.line}  ${p.msg}`);
      console.log(`         ${p.tex}`);
    }
  }
  process.exit(1);
}
