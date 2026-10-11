# Pull the top N videos from every channel in research-channels.txt.
#   .\tools\fetch_research.ps1              (top 15 each)
#   .\tools\fetch_research.ps1 -Top 25
#   .\tools\fetch_research.ps1 -Top 15 -Browser firefox
param(
    [int]$Top = 15,
    [string]$Browser = ""
)
$ErrorActionPreference = "Continue"
Set-Location (Split-Path $PSScriptRoot -Parent)

$channels = Get-Content research-channels.txt | Where-Object { $_ -notmatch '^\s*(#|$)' } | ForEach-Object { $_.Trim() }
if (-not $channels) { Write-Host "No channels in research-channels.txt yet."; exit 1 }

foreach ($ch in $channels) {
    Write-Host "=== $ch ===" -ForegroundColor Cyan
    $pyArgs = @("tools\fetch_channel.py", $ch, "--out", "data\research", "--top", $Top)
    if ($Browser) { $pyArgs += @("--cookies-from-browser", $Browser) }
    & py @pyArgs
    if ($LASTEXITCODE -ne 0) { Write-Host "!! $ch failed, continuing" -ForegroundColor Yellow }
}
