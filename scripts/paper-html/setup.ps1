<#
.SYNOPSIS
    安装论文 HTML 转换所需的工具链（Windows）。

.DESCRIPTION
    需要两样：
      latexml   —— LaTeX → HTML，arXiv 官方 HTML 用的就是它
      pdftocairo（poppler）—— 把论文里的 PDF 插图转成 SVG

    Windows 上原生安装 LaTeXML 比 macOS 麻烦：它是 Perl 应用，要靠
    Strawberry Perl 现场编译 XS 模块，Chocolatey 包与新版 Strawberry Perl
    之间存在已知的版本不匹配问题（LaTeXML issue #1714 / #2298）。

    因此本脚本默认推荐 WSL 路线（最省事），并提供原生安装作为备选。

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File scripts\paper-html\setup.ps1
#>

[CmdletBinding()]
param(
    # 跳过 WSL 建议，直接尝试在 Windows 原生安装
    [switch]$Native
)

function Info($msg) { Write-Host "==> $msg" -ForegroundColor Cyan }
function Ok($msg)   { Write-Host "  ok $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "  !! $msg" -ForegroundColor Yellow }

function Test-Tool($name) {
    $cmd = Get-Command $name -ErrorAction SilentlyContinue
    if ($cmd) { Ok "$name 已就绪 ($($cmd.Source))"; return $true }
    Warn "$name 缺失"
    return $false
}

Info "检查现有工具"
$haveLatexml = Test-Tool latexml
$havePost    = Test-Tool latexmlpost
$havePoppler = Test-Tool pdftocairo

if ($haveLatexml -and $havePost -and $havePoppler) {
    Info "工具链完整，无需安装"
    exit 0
}

if (-not $Native) {
    Info "推荐路线：WSL"
    Write-Host @"
  在 Windows 上装 LaTeXML，最稳的方式是走 WSL（Ubuntu）：

      wsl --install -d Ubuntu          # 若尚未安装 WSL
      wsl sudo apt-get update
      wsl sudo apt-get install -y latexml poppler-utils

  之后在 WSL 里进入本仓库目录运行 convert.py 即可（仓库在 /mnt/c/... 下可直接访问）。

  原因：LaTeXML 是 Perl 应用，Windows 原生安装需要 Strawberry Perl 现场编译
  XS 模块，Chocolatey 包与较新的 Strawberry Perl 存在已知版本冲突
  （LaTeXML issue #1714 / #2298），失败率明显更高。

  若仍要在 Windows 原生安装，重跑本脚本并加 -Native 参数。
"@
    exit 0
}

Info "尝试 Windows 原生安装"

if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Warn "未找到 Chocolatey，请先安装：https://chocolatey.org/install"
    exit 1
}

if (-not $haveLatexml) {
    Info "choco install latexml（若因 Strawberry Perl 版本报错，请改走 WSL）"
    choco install latexml -y
}
if (-not $havePoppler) {
    Info "choco install poppler"
    choco install poppler -y
}

Info "复检（可能需要重开终端以刷新 PATH）"
$ok = (Test-Tool latexml) -and (Test-Tool latexmlpost) -and (Test-Tool pdftocairo)
if (-not $ok) {
    Warn "仍有工具缺失。建议改走 WSL：wsl sudo apt-get install -y latexml poppler-utils"
    exit 1
}

Info "完成。用法：python scripts\paper-html\convert.py --src <论文源目录> --slug <条目文件夹名>"
