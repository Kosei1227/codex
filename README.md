# Codex Private Profile Export

This repository is a portable Codex profile export for restoring my local Codex operating setup on a new laptop.

It is intentionally not a raw copy of `C:\Users\fruit\.codex`. The raw directory contains auth state, session transcripts, caches, SQLite databases, logs, browser state, and machine-specific runtime paths. Those are not safe to publish, even to a private repository.

## Included

- `codex-home/AGENTS.md`: global operating instructions.
- `codex-home/agents/`: custom multi-agent profiles.
- `codex-home/skills/`: reusable local skills, excluding system-generated bundled skills.
- `codex-home/rules/`: local rules.
- `codex-home/templates/`: reusable local templates.
- `config/config.portable.toml`: curated Codex config that removes local runtime paths and project trust entries.
- `scripts/import-codex-profile.ps1`: restore script for a new Windows laptop.
- `scripts/audit-export.ps1`: local scan for accidentally included secrets or non-portable state.

## Excluded

- `auth.json`, sandbox secrets, OAuth tokens, API keys, and account auth state.
- `sessions/`, `log/`, `history.jsonl`, SQLite databases, and generated state.
- Browser, computer-use, Node REPL, plugin cache, runtime cache, and temporary files.
- Raw memories and rollout summaries. These can include old project details and should not be imported into a new work laptop without explicit review.
- Project trust paths from the old laptop.

## Restore On A New Laptop

1. Install Codex Desktop or Codex CLI on the new machine and open it once so it can create its local runtime structure.
2. Clone this repository from the private GitHub repo.
3. From the repository root, run:

```powershell
.\scripts\audit-export.ps1
.\scripts\import-codex-profile.ps1
```

4. Sign in again through Codex and any connectors that you want to use. Auth is intentionally not included here.
5. Run a basic config check:

```powershell
codex --strict-config --version
codex doctor --json
```

If `codex doctor --json` reports machine-specific plugin or runtime issues, open Codex Desktop once more and let it regenerate local runtime paths.

## Privacy Rule

Do not push this repository while it is public. At the time this export was created, the GitHub API reported `Kosei1227/codex` as `public`, so publication must wait until the repository visibility is changed to private.
