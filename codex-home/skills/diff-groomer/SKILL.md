---
name: diff-groomer
description: Use when a branch has become large, redundant, hard to review, or mixed across feature, refactor, tests, formatting, generated output, dependency changes, and cleanup.
---

# Diff Groomer

Use this skill to make a current Git branch easier to review without changing behavior.

The goal is not to improve the whole codebase. The goal is to control branch entropy.

## Operating Rule

Start read-only unless the user has already approved a specific cleanup scope.

Default base branch:

- Use `origin/main` when available.
- If `origin/main` is unavailable, inspect remotes and local branches to infer the most likely base.
- If the base is still unclear, state the uncertainty and use the safest read-only summary path.

## First Step

In a Git repo, inspect the branch:

```bash
git fetch origin
git merge-base HEAD origin/main
git diff --stat $(git merge-base HEAD origin/main)..HEAD
git diff --name-status $(git merge-base HEAD origin/main)..HEAD
```

If fetching is blocked or inappropriate, continue with local refs and report that limitation.

Then inspect changed files directly before recommending edits.

## Required Pre-Edit Output

Before modifying files, produce:

- Branch summary.
- Changed files grouped by purpose.
- Mixed concerns.
- Redundancy candidates inside touched files.
- Risky files and review hotspots.
- Whole work-unit recap that includes the original implementation, follow-up fixes, generated artifacts, tests, and later cleanup owned by the branch.
- Grounded file map with change type, purpose, and review relevance for each meaningful changed file.
- Key changed files whose diffs carry the main implementation risk.
- Recommended PR or commit split.
- Minimal cleanup plan.
- Validation plan.

If the branch touches more than about 10 files, changes more than about 500 lines, or mixes feature, refactor, formatting, tests, dependencies, generated artifacts, or unrelated modules, recommend splitting before continuing.

## Edit Scope

Only edit files already changed on the branch unless the user explicitly approves a broader scope.

Allowed edits:

- Remove duplicated helper logic introduced or touched on the branch.
- Extract small local helper functions from repeated branch-local code.
- Consolidate repeated literals introduced or touched on the branch.
- Simplify nested conditionals when equivalence is clear.
- Remove dead code introduced by the branch.
- Move branch-local tests to the appropriate existing test file when the destination is clear.
- Update small nearby tests when needed to preserve current behavior.

Not allowed without explicit approval:

- Broad architecture rewrites.
- Public API changes.
- Cross-module renames.
- Dependency additions.
- Formatting-only churn across whole files.
- Cleanup in unrelated modules.
- Rewriting generated files unless required by the build process.
- Silent behavior changes.

## Validation

Run the smallest meaningful validation first:

- Existing targeted tests for touched behavior.
- Typecheck or lint when relevant and affordable.
- Build only when it is the closest meaningful proof or the change affects build output.
- Browser, screenshot, rendered artifact, or local HTML-artifact verification when the diff changes visible UI, generated documents, diagrams, screenshots, or other visual review surfaces.

If validation is blocked, report the exact command, error, and residual risk.

## Final Report

Return:

- Files changed.
- Whole work-unit recap grounded in the actual diff, not only the last edit.
- Key changed files and why they matter.
- Behavior-preserving refactors made.
- Any behavior changes, or explicitly say none intended.
- Commands run and results.
- Suggested commit or PR split.
- Remaining review risks.

## Recap Discipline

When the user asks for a recap, PR summary, branch summary, or review handoff,
summarize the whole logical work unit rather than the most recent prompt or
last hunk. Separate branch-owned changes from unrelated dirty work that existed
before the task. Build claims mechanically from real diffs, files, tests,
schemas, and rendered outputs. Label any inference that is not directly present
in the diff.

A useful recap includes:

- Outcome: what changed and why.
- Footprint: changed files grouped by feature, refactor, tests, generated output, dependency, config, or formatting.
- Contracts: API, schema, prompt, runtime, auth, permission, persistence, or UI contracts changed by the diff.
- Key changes: the 3-8 most review-worthy files or hunks, with short annotations.
- UI or artifact impact: screenshots, browser checks, rendered documents, or an HTML artifact when prose cannot prove the visual result.
- Validation: exact commands and what they prove.
- Residual risk: what a reviewer should inspect manually.
