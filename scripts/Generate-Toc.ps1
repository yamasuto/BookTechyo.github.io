# PowerShell で Markdown のファイルを読み込み、見出し (#, ##, ### …) から Table of Contents (TOC) を自動生成するスクリプト
# .\Generate-Toc.ps1 -Path .\sample.md

param(
    [Parameter(Mandatory=$true)]
    [string]$Path
)

# Markdownファイルの内容を取得
$lines = Get-Content $Path

$toc = @()

foreach ($line in $lines) {
    if ($line -match "^(#+)\s+(.*)") {
        $level = $matches[1].Length
        $title = $matches[2].Trim()

        # アンカーリンクを生成（GitHub形式）
        $anchor = $title.ToLower() -replace '[^a-z0-9\s-]', '' -replace '\s+', '-'

        # インデント付きでMarkdownリンクを作成
        $indent = '  ' * ($level - 1)
        $toc += "$indent- [$title](#$anchor)"
    }
}

# 出力
$toc -join "`n"
