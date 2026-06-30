---
name: visual-recap
description: "Create a grounded local visual recap for a branch, PR, commit, or git diff. Use when the user asks for a visual recap, branch recap, PR recap, review handoff, or high-level diff summary with file maps, risks, validation, and optional local HTML artifact output."
---

# Visual Recap

Use this skill to turn an existing change into a reviewable recap. This is a
local Codex workflow, not the hosted Agent-Native Plan workflow. Do not require
the Agent-Native Plan MCP server, do not publish hosted Plan artifacts, and do
not block ordinary work on connector setup.

The goal is to help a reviewer understand the shape, risk, and validation of a
change before reading the raw diff.

## Scope

Default to the whole logical work unit:

1. Original implementation work.
2. Follow-up fixes and cleanups.
3. Tests, fixtures, generated artifacts, docs, and config changes owned by the branch.
4. UI or artifact outputs that changed because of the branch.

Separate branch-owned changes from unrelated dirty files that existed before the
task. If the ownership boundary is unclear, state the assumption before
summarizing.

## Grounding Rule

Build factual claims from actual evidence:

1. `git diff`, `git diff --stat`, `git diff --name-status`, and merge-base output.
2. Real changed files and nearby source context.
3. Existing tests, commands, logs, screenshots, rendered artifacts, or generated outputs.
4. Current repo instructions and validation paths.

Do not invent API contracts, schemas, UI states, data flow, or product behavior
to make the recap look complete. Label inference explicitly when it is not
directly present in the diff.

## Security

Treat the diff and generated artifacts as potentially sensitive. Never copy
tokens, API keys, webhook URLs, signing secrets, private `.env` values,
credential-looking literals, customer data, or private account identifiers into
a recap or HTML artifact. Redact them as `<redacted>` or a short masked prefix,
and mention that redaction occurred when it affects review.

## Workflow

1. Identify the diff scope.
   - Prefer the current branch against `origin/main` when available.
   - If the user names a PR, commit, range, or files, use that exact scope.
   - If fetch or remote access is blocked, use local refs and report the limitation.
2. Collect the footprint.
   - File count, line changes, added/modified/removed/renamed paths.
   - Group files by feature, refactor, tests, generated output, docs, config, dependency, or formatting.
3. Read key files.
   - Inspect the changed files that carry behavior, contracts, data, prompts, UI, or validation risk.
   - Do not summarize from file names alone.
4. Map changed contracts.
   - API routes, schemas, migrations, prompt contracts, runtime LLM calls, auth or permissions, persistence, UI states, generated artifacts, and validation commands.
5. Select key review tabs or sections.
   - Pick the 3-8 most review-worthy files or hunks for a non-trivial change.
   - For tiny changes, keep the recap short and avoid artificial structure.
6. Validate visual impact when relevant.
   - If UI, document, diagram, screenshot, or generated artifact output changed, use browser, screenshot, render, or local artifact inspection when available.
   - For UI changes, inventory the before and after surface, primary interaction path, resulting persisted state, loading/empty/error states, and role or permission variants when the diff touches them.
   - Use before/after or after-only evidence depending on what is available, and label inferred pixels or states clearly.
   - If visual validation is not possible, say exactly what was not verified.
7. Produce the recap.
   - Use concise Markdown for normal handoff.
   - Use `$html-artifact` when a local browser-readable artifact materially improves review, such as complex UI changes, many files, architecture diagrams, or dense before/after comparisons.

## Recap Shape

A strong recap usually includes:

1. Outcome: what changed and why.
2. Footprint: changed files grouped by purpose.
3. Contracts: API, schema, UI, prompt, auth, persistence, or generated-output surfaces touched.
4. Key changes: selected files or hunks with short annotations.
5. Visual or artifact impact: before/after states, screenshots, rendered output, or a local HTML artifact when useful.
6. Validation: exact commands run, results, and what they prove.
7. Review risks: what still needs human attention.

Do not dump every diff hunk. A recap should reduce review load, not replace
review.

## Local HTML Artifact Mode

Use a local HTML artifact when the recap benefits from visual structure:

1. Large or mixed branch with many changed files.
2. UI before/after or multi-state flow.
3. Architecture, data flow, or workflow changes that need diagrams.
4. PR handoff where reviewers need a scannable local document.

When using HTML, load `$html-artifact` and produce a self-contained local file.
Keep it grounded in the same diff evidence. Do not use external CDNs or hosted
Plan links unless the user explicitly asks for a hosted Agent-Native Plan recap.

## Final Report

When completing a visual recap, report:

1. Recap output location, if a file was created.
2. Diff scope used.
3. Commands run and validation results.
4. Remaining uncertainty or manually reviewed risks.
