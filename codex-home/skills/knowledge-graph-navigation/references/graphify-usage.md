# Graphify Usage

Use this reference when operating Graphify through the `knowledge-graph-navigation` skill.

## What Graphify Is For

Graphify builds or queries a project knowledge graph. Use it for:

1. Architecture orientation.
2. Cross-module relationship discovery.
3. Design-rationale discovery.
4. Central concept and god-node inspection.
5. Community structure.
6. Questions like "what connects X to Y?"
7. Existing `graphify-out/GRAPH_REPORT.md` and `graphify-out/graph.json` navigation.

Do not use it as an authority source. Graphify output is a candidate map.

## Command Quick Reference

Use existing graphs:

```powershell
graphify query "what connects auth to the database?"
graphify query "what connects graph generation to validation?" --budget 1500
graphify path "SourceNode" "TargetNode"
graphify explain "NodeName"
```

Use explicit graph paths when outside the graph root:

```powershell
graphify query "show the auth flow" --graph "C:\path\to\graphify-out\graph.json"
graphify path "UserService" "DatabasePool" --graph "C:\path\to\graphify-out\graph.json"
graphify explain "RateLimiter" --graph "C:\path\to\graphify-out\graph.json"
```

Update an existing graph after code changes:

```powershell
graphify update .
graphify cluster-only . --no-viz
```

Read-only checks:

```powershell
graphify hook status
graphify benchmark graphify-out\graph.json
```

## Build Policy

Do not create a graph unless the user asked for Graphify, graph navigation, architecture mapping, onboarding, or a pilot.

Before building:

1. Check `.graphifyignore`.
2. Prefer a scoped path such as `docs`, `.agents`, `core`, or a feature directory.
3. Avoid broad private or generated folders.
4. Confirm whether non-code files may be semantically processed.
5. Use `--no-viz` when the user only needs report and JSON.

Headless semantic extraction can require provider credentials and may send non-code content to a model provider. Do not run it on private docs, PDFs, images, audio, logs, receipts, or evidence bundles without explicit approval.

## Trust Labels

Interpret graph edges conservatively:

1. `EXTRACTED`
   Strong candidate. The relationship was found directly in source, but still verify the file before acting.

2. `INFERRED`
   Useful lead. Verify in source and treat as uncertain until confirmed.

3. `AMBIGUOUS`
   Review-only lead. Do not base implementation or conclusions on it without manual verification.

Score or confidence is retrieval priority, not truth.

## Source Verification

After using Graphify:

1. Open the source files named by the graph.
2. Use `rg` to confirm exact symbols, call sites, tests, and config keys.
3. Check current code state, not only graph state.
4. Mention graph staleness if the graph predates relevant edits.
5. Use tests, builds, or runtime checks for behavior claims.

## Ignore Policy

Exclude by default:

1. `.git`, dependency folders, virtualenvs, build outputs, caches.
2. `.env`, credentials, auth files, session state.
3. SQLite and database files.
4. Logs and temporary files.
5. Screenshots and generated artifacts unless the user asks to analyze them.
6. User evidence bundles or graph artifacts unless the task is specifically about them.

Prefer allowlists for sensitive projects.

## Installer Policy

Do not run Graphify's assistant installers by default:

```powershell
graphify install
graphify codex install
graphify hook install
graphify cursor install
graphify claude install
```

These can write assistant instructions, skills, hooks, or project files. Use this custom Codex skill as the control layer unless the user explicitly chooses the vendor integration.
