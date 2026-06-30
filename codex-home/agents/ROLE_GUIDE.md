# Codex Agent Roles And Profiles

Use this guide to keep role selection stable across sessions.

Profiles:

- Default: normal day-to-day work. Uses `gpt-5.5`, xhigh reasoning, workspace-write sandboxing, and `auto_review` for approval requests.
- `balanced`: normal day-to-day work. Uses `gpt-5.5`, high reasoning, bounded tool output, workspace-write sandboxing, and `auto_review` for approval requests.
- `architect`: architecture and planning work. Uses `gpt-5.5`, xhigh reasoning, medium verbosity, workspace-write sandboxing, and `auto_review` for approval requests.
- `overnight`: supervised long-running execution. Uses `gpt-5.5`, high reasoning, bounded tool output, compaction, workspace-write sandboxing, and `auto_review` for approval requests.
- `overnight_unattended`: unattended off-hours engineering. Uses `gpt-5.5`, high reasoning, larger bounded tool output, workspace-write sandboxing, and no approval prompts. Use only with explicit task scope, validation commands, stop conditions, and PR-only or report-only output.
- `full_autonomy`: explicit high-autonomy escape hatch. Uses `gpt-5.5`, high reasoning, danger-full-access sandboxing, and no approval prompts. Use only when the user intentionally chooses broad local machine access.

Custom agents:

- `architect`: defines short-term goal, medium-term product goal, tradeoffs, unacceptable shortcuts, acceptance criteria, and validation design. It should not edit files.
- `executor`: performs scoped implementation after the goal, write scope, and validation path are clear.
- `reviewer`: reviews implementation risk, regressions, heuristic debt, runtime LLM contract gaps, and validation evidence.
- `explorer`: gathers read-only source evidence, traces execution paths, and reports file or symbol findings before fixes are proposed.
- `docs-researcher`: verifies APIs, framework behavior, release notes, and current documentation claims against primary sources.

Operating loop:

- For non-trivial LLM-product, architecture, or long-horizon work, use the mental loop `architect -> executor -> reviewer`.
- Spawn custom agents only when the user explicitly asks for subagents, delegation, or parallel agent work.
- Keep global `AGENTS.md` short. Put task-specific details in skills, custom agent files, or repo-local `AGENTS.md`.
- Use `explorer` and `docs-researcher` for bounded read-only evidence gathering when that avoids mixing research with implementation. These agents use high reasoning unless their agent files are intentionally changed.
