# Overnight Automation Prompt Template

Use `$overnight-engineer`.

Work only on the approved task below. Use an isolated worktree or dedicated branch when available. Do not overwrite dirty user changes.

Task:

Repository:

Allowed scope:

Forbidden actions:

Validation commands:

Expected output:

Constraints:

1. Do not deploy, merge, push to protected branches, modify secrets, alter billing, or change external services.
2. Do not permanently delete user files, generated artifacts, screenshots, logs, evidence bundles, graph artifacts, configs, or project files.
3. Implement the smallest correct change that satisfies the task.
4. Run the listed validation commands. If validation fails, diagnose once, fix if the cause is clear, then rerun.
5. If validation still fails, stop and report the exact blocker.
6. End with a reviewable branch, draft PR, patch, or morning report.

Morning report must include changed files, commands run, pass or fail results, residual risks, blockers, and recommended human review focus.
