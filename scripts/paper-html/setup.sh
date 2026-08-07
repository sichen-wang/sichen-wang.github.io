#!/usr/bin/env bash
# 安装论文 HTML 转换所需的工具链（macOS / Linux）。
#
# 装两样：
#   latexml   —— LaTeX → HTML，arXiv 官方 HTML 用的就是它
#   poppler   —— 提供 pdftocairo，把论文里的 PDF 插图转成 SVG
#
# Windows 请改用同目录的 setup.ps1。
set -euo pipefail

info() { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
ok()   { printf '\033[1;32m  ok\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m  !!\033[0m %s\n' "$*"; }

missing=0
check() {
  if command -v "$1" >/dev/null 2>&1; then
    ok "$1 已就绪 ($(command -v "$1"))"
  else
    warn "$1 缺失"
    missing=1
  fi
}

info "检查现有工具"
check latexml
check latexmlpost
check pdftocairo

if [ "$missing" -eq 0 ]; then
  info "工具链完整，无需安装"
  exit 0
fi

case "$(uname -s)" in
  Darwin)
    if ! command -v brew >/dev/null 2>&1; then
      warn "未找到 Homebrew，请先安装：https://brew.sh"
      exit 1
    fi
    info "通过 Homebrew 安装（LaTeXML 依赖较多，可能要几分钟）"
    command -v latexml    >/dev/null 2>&1 || brew install latexml
    command -v pdftocairo >/dev/null 2>&1 || brew install poppler

    ;;
  Linux)
    if command -v apt-get >/dev/null 2>&1; then
      info "通过 apt 安装"
      sudo apt-get update
      sudo apt-get install -y latexml poppler-utils
    elif command -v dnf >/dev/null 2>&1; then
      info "通过 dnf 安装"
      sudo dnf install -y perl-LaTeXML poppler-utils
    else
      warn "未识别的包管理器，请手动安装 latexml 与 poppler-utils"
      exit 1
    fi
    ;;
  *)
    warn "未支持的系统：$(uname -s)"
    exit 1
    ;;
esac

info "复检"
missing=0
check latexml
check latexmlpost
check pdftocairo

[ "$missing" -eq 0 ] || { warn "仍有工具缺失"; exit 1; }

info "完成。用法：python3 scripts/paper-html/convert.py --src <论文源目录> --slug <条目文件夹名>"
