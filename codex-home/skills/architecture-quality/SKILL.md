---
name: architecture-quality
description: Use when designing, implementing, refactoring, or reviewing non-trivial code structure so produced code follows proportional Atomic Design, SOLID, Hexagonal Architecture, Clean Architecture, Layered Architecture, dependency inversion, separation of responsibilities, testability, and change-resistant design. Trigger for feature work, shared modules, UI component systems, service boundaries, domain logic, adapters, repositories, controllers, use cases, architecture reviews, 依存性逆転, 責務分離, テストしやすい設計, and 変更に強い設計.
---

# Architecture Quality

Use this skill to make code easier to change, test, and reason about without forcing unnecessary layers into small tasks.

## Design Stance

Optimize for maintainability under real product change. Use architecture patterns as tools, not as ceremony.

- Prefer the repo's existing architecture when it is coherent.
- Improve boundaries when the current code mixes domain logic, infrastructure, UI, persistence, side effects, or orchestration.
- Keep simple changes simple. Do not create ports, adapters, factories, services, or abstractions unless they reduce real coupling or protect a likely change.
- Preserve behavior unless the user explicitly asked for behavior change.
- Validate the design with tests, type checks, or executable examples where feasible.

## Pattern Selection

Choose the smallest pattern set that fits the change.

- Atomic Design: use for reusable UI systems. Keep atoms stateless when practical, compose molecules and organisms from smaller pieces, and keep page or route components responsible for wiring data and layout rather than low-level UI logic.
- SOLID: use for classes, services, and modules with meaningful behavior. Prefer single responsibility, clear interfaces, substitutable implementations, and extension through composition rather than modification.
- Hexagonal Architecture: use when domain behavior should be independent of frameworks, databases, APIs, queues, or UI. Put business rules in the core and isolate external systems behind ports and adapters.
- Clean Architecture: use when use cases, entities, controllers, gateways, and presenters are naturally distinct. Dependencies should point inward toward policy and domain rules.
- Layered Architecture: use when the repo already has layers such as presentation, application, domain, infrastructure, and persistence. Keep layer direction explicit and avoid upward imports.
- Dependency inversion: depend on interfaces or protocols at boundaries where implementation details vary, such as storage, HTTP clients, email, payments, file systems, and LLM providers.
- Responsibility separation: keep validation, authorization, orchestration, domain rules, persistence, formatting, and transport concerns separate unless the code is intentionally small and local.

## Boundary Rules

Apply these rules when adding or changing production code:

1. Domain or business rules must not depend on UI frameworks, web controllers, database clients, HTTP clients, browser APIs, shell commands, or cloud SDKs.
2. Controllers, routes, handlers, and UI pages should translate inputs and outputs, not own core business decisions.
3. Infrastructure code should implement ports or interfaces defined by the application or domain layer, not define the policy.
4. Shared utilities should stay pure or near-pure when possible. If a helper needs I/O, time, randomness, network, or environment access, make that dependency explicit.
5. New abstractions must have a real consumer or a credible near-term variation. Avoid speculative generic layers.
6. Public APIs, exported types, and persistence schemas are higher-cost boundaries. Change them deliberately and add regression tests when risk warrants it.

## Testability Checklist

Before finishing implementation, check:

- Can domain logic be tested without a database, browser, network, or real filesystem?
- Can side effects be replaced with fakes, mocks, in-memory adapters, or test doubles?
- Are inputs and outputs explicit enough to test without inspecting private state?
- Are error paths and edge cases testable without sleeps, broad retries, or timing luck?
- Are LLM, payment, auth, storage, and external API boundaries validated with contracts or schema checks?
- Does the nearest meaningful test prove the intended behavior rather than only line coverage?

## Change-Resistance Checklist

Review the change against likely future edits:

- New UI variant.
- New persistence backend.
- New API provider.
- New business rule.
- New validation policy.
- New workflow step.
- New locale, tenant, permission level, or data shape.

If one likely change would require editing many unrelated files, improve the boundary before shipping.

## Review Output

When using this skill for design or review, report:

- Existing architecture pattern observed.
- Boundary or responsibility problem, if any.
- Proposed structure with file or module ownership.
- Why the abstraction is necessary, or why no new abstraction is needed.
- Tests or validation that prove the boundary.
- Residual risk or overengineering risk.
