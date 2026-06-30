param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$CodexHome = (Join-Path $env:USERPROFILE '.codex'),
    [switch]$SkipConfig
)

$ErrorActionPreference = 'Stop'

function Copy-WithBackup {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$Destination,
        [Parameter(Mandatory = $true)][string]$BackupRoot
    )

    if (Test-Path -LiteralPath $Destination) {
        $relative = Split-Path -Leaf $Destination
        $backupPath = Join-Path $BackupRoot $relative
        Copy-Item -LiteralPath $Destination -Destination $backupPath -Recurse -Force
    }

    $parent = Split-Path -Parent $Destination
    if (-not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent | Out-Null
    }

    Copy-Item -LiteralPath $Source -Destination $Destination -Recurse -Force
}

$sourceHome = Join-Path $RepoRoot 'codex-home'
$portableConfig = Join-Path $RepoRoot 'config\config.portable.toml'

if (-not (Test-Path -LiteralPath $sourceHome)) {
    throw "Missing source directory: $sourceHome"
}

if (-not (Test-Path -LiteralPath $CodexHome)) {
    New-Item -ItemType Directory -Path $CodexHome | Out-Null
}

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupRoot = Join-Path $CodexHome "backups\portable-import-$timestamp"
New-Item -ItemType Directory -Path $backupRoot | Out-Null

if (-not $SkipConfig) {
    Copy-WithBackup -Source $portableConfig -Destination (Join-Path $CodexHome 'config.toml') -BackupRoot $backupRoot
}

Copy-WithBackup -Source (Join-Path $sourceHome 'AGENTS.md') -Destination (Join-Path $CodexHome 'AGENTS.md') -BackupRoot $backupRoot

foreach ($folderName in @('agents', 'rules', 'templates')) {
    $sourceFolder = Join-Path $sourceHome $folderName
    if (Test-Path -LiteralPath $sourceFolder) {
        Copy-WithBackup -Source $sourceFolder -Destination (Join-Path $CodexHome $folderName) -BackupRoot $backupRoot
    }
}

$sourceSkills = Join-Path $sourceHome 'skills'
if (Test-Path -LiteralPath $sourceSkills) {
    $targetSkills = Join-Path $CodexHome 'skills'
    if (-not (Test-Path -LiteralPath $targetSkills)) {
        New-Item -ItemType Directory -Path $targetSkills | Out-Null
    }

    Get-ChildItem -LiteralPath $sourceSkills -Directory | ForEach-Object {
        Copy-WithBackup -Source $_.FullName -Destination (Join-Path $targetSkills $_.Name) -BackupRoot $backupRoot
    }
}

Write-Host "Imported Codex profile into: $CodexHome"
Write-Host "Backed up overwritten files under: $backupRoot"
Write-Host "Auth, sessions, logs, caches, browser state, and raw memories were not imported."
Write-Host "After import, sign in to Codex and connectors again on this machine."
