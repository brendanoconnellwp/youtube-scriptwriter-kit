# Package the skill for Claude (app/web) and install it for Claude Code.
#   .\tools\package_skill.ps1
$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)
$skill = "skill\youtube-scriptwriter"

$placeholders = Get-ChildItem "$skill\*.md" | Where-Object { (Get-Content $_ -TotalCount 1) -match '^STATUS: NOT GENERATED' }
if ($placeholders) {
    Write-Host "Heads up: these reference files are still placeholders:" -ForegroundColor Yellow
    $placeholders | ForEach-Object { Write-Host "  $($_.Name)" }
    if ((Read-Host "Package anyway? [y/N]") -ne "y") { exit 1 }
}

New-Item -ItemType Directory -Force dist | Out-Null
$zip = "dist\youtube-scriptwriter.zip"
if (Test-Path $zip) { Remove-Item $zip }
Compress-Archive -Path $skill -DestinationPath $zip
Write-Host "Built $zip  -> upload this in Claude's Skills settings" -ForegroundColor Green

$dest = Join-Path $env:USERPROFILE ".claude\skills\youtube-scriptwriter"
New-Item -ItemType Directory -Force (Split-Path $dest -Parent) | Out-Null
if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
Copy-Item $skill $dest -Recurse
Write-Host "Installed to $dest  -> available in Claude Code everywhere" -ForegroundColor Green
