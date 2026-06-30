# Runtime LLM Component Contract

Component name:

Product behavior:

Owner module:

Trigger:

Non-goals:

Inputs:

- Schema:
- Source:
- Trust level:
- Required fields:
- Size limits:

Context assembly:

- Retrieved evidence:
- Product state:
- Prior model outputs:
- Tool outputs:
- Untrusted data isolation:

Output contract:

- Schema version:
- Allowed enums:
- Allowed IDs:
- Required evidence refs:
- Confidence field:
- Ambiguous, abstain, or block states:
- Prohibited fields:

Authority boundary:

- May interpret:
- May propose:
- Must not decide:
- Must not mutate:
- Human approval required for:

Deterministic validators:

- Schema:
- ID membership:
- Evidence refs:
- Permissions:
- Product state:
- Policy:
- Side effects:

Failure policy:

- Malformed output:
- Unknown ID:
- Missing evidence:
- Low confidence:
- Ambiguous result:
- Timeout or rate limit:
- Policy or permission violation:

Retry and repair policy:

Trace fields:

- Component:
- Prompt version:
- Schema version:
- Model:
- Reasoning effort:
- Input digest:
- Evidence IDs:
- Raw output:
- Parsed output:
- Validation result:
- Failure category:
- Retry or fallback decision:

Eval cases:

- Happy path:
- Known regression:
- Ambiguous or low-confidence case:
- Malformed or adversarial input:
- Permission or policy boundary:

Release gate:

Residual risk:
