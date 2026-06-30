# Long Horizon Prompt Template

Use this template when asking Codex to work for a long time, complete a phase, or continue until acceptance.

```text
Goal:
State the final outcome. Make it artifact-verifiable.

Acceptance:
List what must be true before the work is complete. Include required commands, live checks, generated artifacts, logs, or manual inspection criteria.

Allowed:
List directories, files, commands, browser flows, and artifacts Codex may use.

Forbidden:
No permanent delete.
No push, deploy, release, purchase, or external post.
No credential display or secret extraction.
No artifact overwrite unless explicitly allowed.
No platform-specific hardcode unless the task is explicitly adapter-specific.
No weakening acceptance criteria to claim success.

Start state:
Read git status.
Separate existing user changes from Codex changes.
Read relevant AGENTS.md and named docs.
Identify current best artifacts and known blockers.

Work loop:
Use one hypothesis per loop.
Make scoped changes.
Run validation.
Inspect actual output.
Record proven, unproven, and blocked claims.
Create checkpoints around long commands and major decisions.

Validation:
Use tests for debugging and regression protection.
Use real artifacts, logs, browser runs, or live execution when required for acceptance.
Do not claim stronger validation than was actually performed.

Stop when:
The same validation fails twice.
Root cause remains unclear after two speculative branches.
The next step requires deletion, credentials, push, deploy, external service changes, irreversible migration, or acceptance weakening.

Final report:
Changed files.
Commands run.
Artifacts created or preserved.
Acceptance checks passed.
Unverified claims.
Residual risks.
Next human decision.
```
