# Security Threat Audit Checklist

Use this checklist for security-sensitive production audits. Keep findings evidence-backed and avoid speculative noise.

## Application Security

- Auth and authorization: missing middleware, default-allow checks, IDOR, role escalation, token expiration, and session misuse.
- Input validation: request body, query params, file uploads, webhook signatures, path inputs, and type checks.
- Injection: SQL, command, template, LDAP, header, prompt injection, and unsafe deserialization.
- XSS and content injection: raw HTML, `dangerouslySetInnerHTML`, `v-html`, `innerHTML`, template safe filters, and markdown rendering.
- SSRF and external fetches: user-controlled URLs, internal IP access, redirects, metadata services, and allowlists.
- Secrets and PII: committed credentials, logs, error responses, URLs, plaintext storage, and overbroad telemetry.

## Infrastructure And Supply Chain

- CI/CD: workflow permissions, third-party actions pinned by SHA, secret exposure, artifact upload, release idempotency, and protected branch assumptions.
- Dependencies: lockfile drift, install scripts, abandoned packages, native binaries, and license or distribution constraints.
- Containers and deploy: root users, exposed ports, health checks, rollback path, migration ordering, and environment parity.
- Agent and skill supply chain: imported hooks, MCP servers, shell scripts, auto-updaters, telemetry, generated code, and prompt injection surfaces.

## Runtime LLM And Agent Systems

- Strict structured outputs and schema validation.
- Allowed IDs or enums for side effects.
- Evidence references for semantic decisions.
- Ambiguous, abstain, or block states.
- Deterministic validation before persistence or external actions.
- Traceability of prompt version, model, input digest, raw output, parsed output, accepted output, and validation result.

## Finding Bar

Classify only issues supported by code, config, logs, traces, or documented platform behavior.

- `Blocker`: should not ship.
- `High`: likely incident, user harm, or data exposure.
- `Medium`: meaningful exploitable or operational risk.
- `Low`: hardening, clarity, or monitoring gap.
