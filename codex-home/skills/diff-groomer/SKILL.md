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

If validation is blocked, report the exact command, error, and residual risk.

## Final Report

Return:

- Files changed.
- Behavior-preserving refactors made.
- Any behavior changes, or explicitly say none intended.
- Commands run and results.
- Suggested commit or PR split.
- Remaining review risks.
