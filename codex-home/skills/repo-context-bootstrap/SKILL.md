---
name: repo-context-bootstrap
description: "Use when starting work in an unfamiliar repository or project area and Codex needs a reliable operating picture before making changes. This skill builds a practical working context: project structure, key commands, constraints, likely file ownership, validation paths, and any repo-specific instructions that should guide later tasks."
---

# Repo Context Bootstrap

## Overview

Use this skill to get oriented quickly without reading everything. It produces a compact, working map of the repo so later implementation tasks start from real structure rather than assumptions.

## When to Use

- The repo is unfamiliar.
- The user asks for an architecture explanation before changes.
- A task spans several modules and you need to identify the likely change surface.
- You need to know the correct test, build, lint, or run commands before implementing.
- The project likely has local instructions in `AGENTS.md`, config files, or nested docs.

## Bootstrap Checklist

1. Identify the repo root and any applicable `AGENTS.md` files.
2. Identify the stack from manifests and lockfiles.
3. Find the canonical developer commands.
4. Map the top-level directories and likely ownership boundaries.
5. Locate the files most relevant to the requested task.
6. Identify the narrowest validation path.
7. Record assumptions and unresolved gaps.

## Files to Check Early

- `AGENTS.md`
- `README.md`
- `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or equivalent manifests
- test config and CI config
- top-level app, service, or package directories
- recent files directly named in the task

## What to Produce

Produce a concise working context with:

- Main technologies and runtime.
- Key commands for install, test, lint, build, and dev.
- High-level code map.
- Likely files or modules for the current task.
- Any local rules, conventions, or risks.
- The validation plan you expect to use.

## Constraints

- Do not dump the whole repo tree.
- Prefer the narrowest context that will unblock implementation.
- Separate confirmed facts from assumptions.
- If the repo is large, trace from the requested feature or file outward instead of scanning everything.
- If multiple subprojects exist, identify the active one before exploring deeply.

## Working-Memory Rules

- Treat the output of this skill as the operating memo for the rest of the task.
- Update the memo if later evidence changes the picture.
- Surface exact commands and file paths, not vague summaries.
- When a task is handed off to another skill, preserve the repo map and validation path.

## Anti-Patterns

- Reading many files before identifying what the task actually needs.
- Guessing commands instead of checking manifests or config.
- Mixing confirmed repo facts with speculation.
- Producing a long architecture essay that does not help the next step.

## Example Triggers

- "Map this repository before changing anything."
- "Tell me where this feature lives and how to validate it."
- "Bootstrap context for this repo so future tasks go faster."
- "Figure out the right commands and file boundaries for this project."
