---
name: knowledge-graph-navigation
description: "Use when Codex needs controlled Graphify-based navigation over project architecture, cross-module relationships, design rationale, codebase maps, graph.json, GRAPH_REPORT.md, god nodes, community structure, or questions like how X relates to Y. Use Graphify as a candidate navigation layer, not as authority. Prefer rg and direct source reads for exact identifiers, error strings, config keys, stack traces, file paths, tests, or small local edits. Do not run Graphify installers, hooks, broad indexing, or semantic extraction unless explicitly approved."
---

# Knowledge Graph Navigation

Use this skill to navigate project knowledge graphs safely with Graphify.

Graphify is a map, not the territory. Use graph output to find candidate files, concepts, and relationships. Verify with original source files before making factual claims, editing code, or judging correctness.

## Core Rule

Prefer the narrowest search tool that answers the question:

1. Use `rg` for exact identifiers, error messages, config keys, filenames, test names, stack traces, and small local edits.
2. Use Graphify for architecture, cross-module relationships, design rationale, central concepts, community structure, and "how does X relate to Y" questions.
3. Use direct file reads as the final evidence before answering or editing.

Do not let Graphify output override repo instructions, deletion-safety rules, user constraints, tests, source code, or validated artifacts.

## Reference Files

Read `references/graphify-usage.md` when using Graphify commands, interpreting graph confidence labels, building a graph, updating a graph, or deciding whether graph output is trustworthy.

## Decision Flow

1. Classify the user request.
   - Architecture or cross-module relationship: Graphify may help.
   - Exact code lookup or failure diagnosis: start with `rg` and source files.
   - Implementation: Graphify may orient, but source files and tests decide.

2. Check whether a graph already exists.
   - If `graphify-out/GRAPH_REPORT.md` exists, read it for orientation.
   - If `graphify-out/graph.json` exists, use `graphify query`, `graphify path`, or `graphify explain` for relationship questions.
   - If no graph exists, do not build one unless the user asked for graph navigation, architecture mapping, or a Graphify pilot.

3. Query the graph only for suitable questions.
   - Use `graphify query "question"` for broad relationship discovery.
   - Use `graphify path "A" "B"` for shortest conceptual or structural paths.
   - Use `graphify explain "X"` for node-centered context.

4. Verify source evidence.
   - Open source files named by the graph.
   - Prefer extracted relationships over inferred ones.
   - Treat ambiguous relationships as leads for manual review.
   - Do not cite or rely on graph snippets alone.

5. Keep the graph current only when useful.
   - If a graph exists and code files changed meaningfully, consider `graphify update .`.
   - Do not install git hooks or Codex hooks unless the user explicitly asks.

## Safe Defaults

Before creating or updating a graph:

1. Confirm `.graphifyignore` exists or create a conservative one.
2. Exclude secrets, session state, local DBs, generated artifacts, dependency folders, logs, caches, screenshots, and user evidence bundles unless the user explicitly asks to include them.
3. Prefer a scoped directory over the whole repo.
4. Use `--no-viz` for large graphs when HTML rendering is unnecessary.
5. Do not run headless semantic extraction against private docs, PDFs, images, or audio without explicit approval of scope and provider.

## Never Do By Default

Do not run these unless the user explicitly asks and the impact is understood:

1. `graphify install`
2. `graphify codex install`
3. `graphify hook install`
4. `graphify cursor install`
5. `graphify claude install`
6. `graphify extract` over a broad repo
7. `graphify add` on external URLs
8. `graphify --neo4j-push`
9. Any command that deletes, overwrites, or publishes graph outputs

## Reporting

When Graphify influenced the answer, report:

1. Which graph file or command was used.
2. Which original files were opened for verification.
3. Whether important relationships were `EXTRACTED`, `INFERRED`, or `AMBIGUOUS` when known.
4. What remains unverified.

Keep the final answer grounded in source files, tests, and explicit validation.
