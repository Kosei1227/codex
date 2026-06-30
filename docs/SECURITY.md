# Security Notes

This export is designed for private backup and transfer, not public sharing.

## Never Commit

- `auth.json`
- `.sandbox`, `.sandbox-secrets`, `.tmp`, `tmp`
- `sessions`, `log`, `history.jsonl`, `session_index.jsonl`
- `*.sqlite`, `*.sqlite-wal`, `*.sqlite-shm`
- `plugins/cache`, runtime caches, browser state, computer-use state, Node REPL state
- Raw memories, rollout summaries, transcripts, screenshots, generated evidence bundles
- Personal access tokens, OAuth credentials, API keys, SSH keys, cloud credentials

## Why Raw Memories Are Excluded

Codex memories can contain old project names, repository paths, debugging evidence, snippets, and conclusions from prior work. That is useful context on the old laptop, but it is not automatically safe to import into a new work laptop. If memory transfer is needed, create a separate reviewed and sanitized memory seed.

## Required Before Push

Run:

```powershell
.\scripts\audit-export.ps1
```

Also verify that the target GitHub repo is private before pushing. The export was blocked from upload when the GitHub API reported `Kosei1227/codex` as public.
