# Plugin Restore Notes

The portable config enables the plugins that were enabled locally:

- `hugging-face@openai-curated`
- `gmail@openai-curated`
- `documents@openai-primary-runtime`
- `spreadsheets@openai-primary-runtime`
- `presentations@openai-primary-runtime`
- `google-calendar@openai-curated`
- `github@openai-curated`
- `chrome@openai-bundled`
- `computer-use@openai-bundled`
- `browser@openai-bundled`
- `pdf@openai-primary-runtime`
- `template-creator@openai-primary-runtime`

Plugin caches are intentionally not copied. On a new laptop, install Codex Desktop, open it once, sign in, and let the app install or refresh plugin runtimes. Connector accounts such as GitHub, Gmail, Google Calendar, and Hugging Face must be authenticated again on the new machine.
