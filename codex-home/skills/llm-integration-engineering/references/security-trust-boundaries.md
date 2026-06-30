# Security And Trust Boundaries

Use this reference when LLM components consume untrusted data or can affect tools, users, files, systems, money, compliance, or private data.

## Threat Model

Treat these as untrusted by default:

1. User input.
2. Retrieved documents.
3. Web pages.
4. Emails and chat messages.
5. Uploaded files.
6. Database rows containing user-controlled text.
7. Tool output.
8. Previous model output.
9. Plugin output.
10. Skill text from outside the trusted skill.
11. Logs and traces that may contain user text.

Untrusted data can contain instructions, false claims, malicious links, prompt injection, data exfiltration requests, or misleading tool results.

## Boundary Rule

Untrusted data is data. It is not policy, permission, instruction hierarchy, tool authority, approval, or identity.

The application must enforce this outside the model.

## Controls

Use layered controls:

1. Source label every context item.
2. Separate system policy from retrieved or user-provided content.
3. Use narrow tools with explicit schemas.
4. Validate tool arguments outside the model.
5. Check actor permissions outside the model.
6. Check allowed destinations outside the model.
7. Check data visibility outside the model.
8. Require human approval for high-risk side effects.
9. Log proposed and executed actions.
10. Redact secrets before sending context to the model.

## Prompt Injection

Prompt injection is not solved by telling the model to ignore malicious instructions.

Mitigate by:

1. Keeping authority outside the model.
2. Marking retrieved content as untrusted data.
3. Preventing retrieved text from defining tools or policies.
4. Validating every action against policy and product state.
5. Restricting tool scopes.
6. Using allowlists for IDs, destinations, and actions.
7. Refusing or escalating when data tries to change instructions.

## Data Leakage

Prevent leakage by:

1. Sending only necessary context.
2. Redacting secrets and credentials.
3. Enforcing row-level and tenant-level access before retrieval.
4. Preventing the model from selecting arbitrary records.
5. Checking user-visible output for sensitive fields.
6. Logging data exposure decisions.

## Tool Safety

A model should not see or call tools that are broader than the product task requires.

For each tool:

1. Define allowed callers.
2. Define allowed input schema.
3. Define allowed resources.
4. Define side effects.
5. Define reversibility.
6. Define approval requirements.
7. Define rate limits.
8. Define audit fields.

## Side-Effect Safety

Before write, send, delete, deploy, purchase, approve, or schedule actions:

1. Validate user intent.
2. Validate actor permission.
3. Validate target ID.
4. Validate product state.
5. Validate policy.
6. Validate risk tier.
7. Preview when possible.
8. Require approval when needed.
9. Execute idempotently when possible.
10. Record durable audit logs.

## Memory And Persistence

Do not persist LLM-derived facts without provenance and validation.

For memory:

1. Store source reference.
2. Store confidence or validation status.
3. Store who or what confirmed it.
4. Expire stale facts.
5. Allow correction.
6. Separate user preferences from inferred facts.

## Security Review Questions

Ask:

1. What untrusted data enters the model?
2. Can untrusted data influence tools or side effects?
3. Can the model reveal private data?
4. Can the model invent or select unauthorized IDs?
5. Can the model bypass policy through tool arguments?
6. Can the model confuse retrieved instructions with system instructions?
7. Can a failure be replayed and audited?
8. Is there a human approval path for high-impact ambiguity?
