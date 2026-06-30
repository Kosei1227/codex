param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$forbiddenPathRegexes = @(
    '(^|[\\/])auth\.json$',
    '(^|[\\/])\.sandbox([\\/]|$)',
    '(^|[\\/])\.sandbox-secrets([\\/]|$)',
    '(^|[\\/])sessions([\\/]|$)',
    '(^|[\\/])log([\\/]|$)',
    '(^|[\\/])cache([\\/]|$)',
    '(^|[\\/])plugins[\\/]cache([\\/]|$)',
    '(^|[\\/])browser([\\/]|$)',
    '(^|[\\/])computer-use([\\/]|$)',
    '(^|[\\/])node_repl([\\/]|$)',
    '(^|[\\/])history\.jsonl$',
    '\.sqlite(-shm|-wal)?$',
    '\.db(-shm|-wal)?$'
)

$secretRegexes = @(
    '(?i)(api[_-]?key|secret|password|authorization|bearer|oauth|refresh[_-]?token|access[_-]?token|client[_-]?secret)\s*[:=]\s*["'']?[A-Za-z0-9_./+=-]{16,}',
    'sk-[A-Za-z0-9_-]{20,}',
    'gh[pousr]_[A-Za-z0-9_]{20,}',
    'github_pat_[A-Za-z0-9_]{20,}',
    'xox[baprs]-[A-Za-z0-9-]{20,}',
    'AIza[0-9A-Za-z\-_]{20,}'
)

$issues = New-Object System.Collections.Generic.List[string]
$root = (Resolve-Path $RepoRoot).Path
$rootPrefix = $root.TrimEnd('\') + '\'

Get-ChildItem -LiteralPath $root -Recurse -File -Force |
    Where-Object { $_.FullName -notmatch '[\\/]\\.git[\\/]' } |
    ForEach-Object {
        if ($_.FullName.StartsWith($rootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
            $relative = $_.FullName.Substring($rootPrefix.Length)
        } else {
            $relative = $_.FullName
        }

        foreach ($pattern in $forbiddenPathRegexes) {
            if ($relative -match $pattern) {
                $issues.Add("Forbidden path: $relative")
                break
            }
        }

        if ($_.Length -gt 2MB) {
            $issues.Add("Large file needs review: $relative ($($_.Length) bytes)")
            return
        }

        $extension = $_.Extension.ToLowerInvariant()
        $textLike = @('.md', '.txt', '.toml', '.ps1', '.json', '.yaml', '.yml', '.py', '.js', '.ts', '.tsx', '.css', '.html', '.svg', '.rules')
        if ($textLike -notcontains $extension -and $_.Name -notmatch '^(AGENTS|README|LICENSE)$') {
            return
        }

        $content = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
        foreach ($pattern in $secretRegexes) {
            if ($content -match $pattern) {
                $issues.Add("Secret-like content: $relative")
                break
            }
        }
    }

if ($issues.Count -gt 0) {
    Write-Host "Audit failed:"
    $issues | Sort-Object -Unique | ForEach-Object { Write-Host "  $_" }
    exit 1
}

Write-Host "Audit passed: no forbidden state files or secret-shaped values found."
