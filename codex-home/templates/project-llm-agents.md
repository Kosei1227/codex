# Project LLM Agent Operating Contract

Use this as repo-local `AGENTS.md` content for projects where runtime LLM behavior is part of the product.

## Runtime LLM Product Work

- Treat each runtime LLM call as a product component with a bounded purpose, authority boundary, schema, validators, traces, eval cases, and failure policy.
- Do not replace semantic uncertainty with keyword, substring, selector, label, alias, or string-based heuristics.
- Deterministic code owns permissions, allowed IDs, schema validation, evidence reference validation, provenance, persistence, idempotency, side effects, and fail-closed policy.
- LLM components may interpret, classify, extract, rank, retrieve, summarize, judge, plan, or propose. They must not silently acquire authority.
- Missing semantic contracts, low confidence, missing evidence refs, schema violations, ambiguous decisions, or unknown IDs become validation blockers, graph gaps, or human-escalation points.

## Work Loop

- Before implementation, identify the short-term goal, medium-term product goal, acceptance criteria, unacceptable shortcuts, likely validation, and files that should not be touched.
- Keep changes scoped to the component or module that owns the behavior.
- Do not hide defects behind broad fallbacks, retries, tolerant parsing, selector guesses, sleeps, Playwright workarounds, or catch-all exception paths.
- Browser automation can reproduce, observe, and verify UI effects. It is not a semantic decision layer.
- A task is complete only when validation proves the intended product effect, not merely that an action ran.

## Review Gate

- Review new fallbacks, heuristic logic, retry loops, and browser workarounds as product-risk changes.
- Require evidence for one happy path, one known regression, one ambiguous or low-confidence case, and one malformed or adversarial case when the component risk warrants it.
- If validation is blocked, report the blocker, command or artifact path, and residual risk.
