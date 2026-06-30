# OpenPrism Reference Notes

Use this file only when the user asks to compare this Codex-backed workflow with OpenPrism or asks whether to reuse OpenPrism implementation ideas.

## Current Local Reference

The local reference clone is:

```text
C:\Users\fruit\OneDrive\Documents\Playground\_external\OpenPrism
```

The useful design ideas observed locally are:

1. Keep LaTeX compilation as an explicit loop with logs.
2. Support common engines such as `pdflatex`, `xelatex`, `lualatex`, `latexmk`, and `tectonic`.
3. Provide arXiv search and BibTeX helpers.
4. Let the agent inspect files and propose bounded edits.
5. Treat compile logs as first-class input for repair.
6. Keep template transfer separate from ordinary manuscript drafting.

## Boundary For This Skill

Do not copy OpenPrism source code into this skill. The local clone's README references an MIT license, but no `LICENSE` file was present when inspected locally. Until licensing is clarified, treat OpenPrism as a design reference only.

This skill does not start an OpenPrism frontend or backend. It implements the efficient Codex-native subset through local artifacts and deterministic scripts.
