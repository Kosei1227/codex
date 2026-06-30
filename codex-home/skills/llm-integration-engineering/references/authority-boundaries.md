# Authority Boundaries

Use this reference to decide how much authority a runtime LLM component should have.

## Core Rule

An LLM can propose. Product code authorizes.

The higher the authority, the stronger the required contract, validation, logging, and human review path.

## Authority Levels

1. `inform`
   Produces user-facing text without changing system state.
   Controls: content policy, grounding checks when factual, user feedback, trace logging.

2. `classify`
   Chooses from a closed set of labels.
   Controls: allowed enum, confidence or ambiguity state, deterministic routing guard, regression evals.

3. `extract`
   Converts messy input into structured fields.
   Controls: schema validation, source evidence, field-level uncertainty, provenance, human review for high-impact fields.

4. `rank`
   Orders known candidates.
   Controls: closed candidate set, candidate IDs from code, reason and evidence fields, deterministic tie handling.

5. `retrieve`
   Generates search queries, selects context, or reranks context.
   Controls: source attribution, freshness checks, retrieval metrics, grounding evals, injection handling.

6. `judge`
   Evaluates another output.
   Controls: judge rubric, judge version, calibration against human labels, disagreement sampling, evaluator drift checks.

7. `plan`
   Proposes steps for a workflow.
   Controls: allowed action set, state-machine constraints, plan validation, step budget, human approval for high-impact plans.

8. `tool_args`
   Proposes arguments for a tool or API.
   Controls: strict schema, allowed IDs, permission checks, dry-run support, reversible execution when possible.

9. `side_effect_request`
   Requests a write, send, delete, purchase, deploy, schedule, or state change.
   Controls: policy engine, risk tier, audit log, confirmation or pre-authorization, compensation plan.

10. `autonomous_action`
   Directly performs side effects through narrow pre-authorized tools.
   Controls: avoid by default. Require narrow scope, deterministic policy, durable audit, rate limits, rollback or compensation, monitoring, and explicit product acceptance.

## Tool Risk Tiers

Classify each tool independently:

1. `read_only`
   Reads internal or external data. Still needs privacy and prompt-injection controls.

2. `reversible_write`
   Creates drafts, temporary records, or changes that can be undone.

3. `external_communication`
   Sends email, chat, ticket comments, forms, or notifications.

4. `financial_or_legal`
   Affects money, contracts, claims, compliance, identity, access, or obligations.

5. `destructive_or_irreversible`
   Deletes data, overwrites artifacts, cancels orders, changes permissions, deploys production, or triggers irreversible actions.

High-risk tools require human approval, pre-authorized narrow scopes, or deterministic policy checks before execution.

## Boundary Design

Use narrow product APIs instead of exposing raw tools.

Prefer:

1. `create_draft_invoice` over unrestricted database writes.
2. `send_preapproved_template_email` over arbitrary email sending.
3. `lookup_customer_by_id` over free-form SQL.
4. `attach_existing_file_by_id` over arbitrary file path access.
5. `schedule_review_request` over direct approval.

## Required Checks Before Side Effects

Before a model-proposed side effect:

1. Validate schema.
2. Validate allowed IDs.
3. Validate actor permissions.
4. Validate product state.
5. Validate policy constraints.
6. Validate evidence references.
7. Validate reversibility or approval.
8. Log decision and execution result.

## Anti-Patterns

Avoid:

1. Giving an LLM a broad shell, filesystem, browser, SQL, or admin API unless the product explicitly requires it and has external controls.
2. Letting the LLM choose arbitrary endpoints, selectors, file paths, table names, or recipients.
3. Treating a prompt instruction as a permission boundary.
4. Hiding policy enforcement inside the same agent context that sees untrusted data.
5. Executing multi-step side effects without durable state and idempotency.
