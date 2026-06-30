# Cleanup Policy

Cleanup after long-horizon work must preserve reproduction and recovery.

## Keep

- accepted artifacts
- inputs that generated accepted artifacts
- final acceptance summaries
- final live execution logs
- final plancheck or dry-run logs when relevant
- reproduction scripts or commands
- commit hashes, patches, or manifest files
- packaged reproduction archives

## Cleanup Candidates

- failed trial logs
- intermediate generated artifacts
- obsolete stdout and stderr logs
- duplicate screenshots
- temporary bundles not used for acceptance
- old candidate outputs superseded by accepted artifacts

## Required Procedure

1. List exact paths.
2. Explain why each group is safe to remove from the working tree.
3. Preserve or package accepted artifacts first.
4. Ask for confirmation when artifacts are important or ambiguous.
5. Use Recycle Bin, archive, or quarantine by default.
6. Do not permanently delete unless the user explicitly requests permanent deletion and names the target.

For graph, browser, evidence, screenshot, or generated-output workflows, be extra conservative. These files often become the only proof of what happened.
