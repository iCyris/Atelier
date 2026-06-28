---
name: pack
description: "End-to-end brand pack workflow that coordinates concept, logo, tokens, export, manifests, and handoff. Use when the user wants a complete identity path from loose intent to production-ready brand assets."
---

# End-to-End Brand Pack Workflow

Use this reference when the user wants a complete identity path from loose intent to production-ready brand assets. This workflow coordinates brand concepting, logo production, design tokens, asset packaging, and handoff without treating those outputs as disconnected AI-generated material.

## Observable Outcomes

A successful run produces a package that can be inspected without reading the conversation:

- `BRAND.md` explains the brand promise, audience, visual territories, recommended direction, anti-patterns, and production plan.
- `LOGO_SPEC.md` defines source files, variants, clear space, minimum sizes, color versions, misuse rules, and platform exports.
- `logo/source/` contains editable SVG sources with clear naming.
- `logo/png/` contains raster exports when a renderer is available.
- `tokens/` contains implementation-ready values such as `tokens.json`, `tokens.css`, or framework theme files.
- `asset-manifest.json` lists inputs, outputs, producer steps, quality checks, assumptions, open questions, and next actions.
- `handoff/` contains practical notes for designers, engineers, or follow-up agents.
- The manifest validates with `python3 subskills/export/scripts/validate_outputs.py <path-to-manifest>` from the parent `skills/convallaria/` directory.

## Process

1. Define the project promise, audience, category, constraints, and delivery context.
2. Generate 3 to 5 visual territories using `concept`; each territory must include concrete visual language, not just mood words.
3. Select or recommend one direction and state the tradeoffs.
4. Create logo concept seeds tied to the selected direction.
5. Produce or refine editable SVG logo sources using `logo`.
6. Export required PNG sizes with `subskills/logo/scripts/rasterize_svg.py` from the parent skill directory when SVG sources exist.
7. Convert brand decisions into implementation tokens using `tokens`.
8. Package outputs with `export`, including `asset-manifest.json` and handoff notes.
9. Run validation and record the result in `qualityChecks`.

## Craft Gate

Before final delivery, check that the work is coherent and ownable:

- The logo idea is tied to a brand concept, not a decorative prompt artifact.
- Color roles are named by use and can survive UI implementation.
- Typography direction includes fallbacks and production constraints.
- The brand voice has examples, forbidden habits, and vocabulary.
- Every major aesthetic decision has a strategic reason or a delivery reason.
- Generated assets are traceable from source to export through the manifest.
- The package names unresolved decisions instead of hiding them behind confident prose.

## Failure Modes

Avoid these patterns:

- Moodboard language without implementation consequences.
- Logo exports with no source SVG or no usage rules.
- Tokens that only rename raw colors without semantic roles.
- Handoff notes that repeat the brand story but omit how to use files.
- Visual variety that breaks the selected direction.
- Generated images or copy included only because they look impressive.

## Recommended Package Shape

```text
convallaria-output/
├── BRAND.md
├── LOGO_SPEC.md
├── asset-manifest.json
├── tokens/
│   ├── tokens.json
│   └── tokens.css
├── logo/
│   ├── source/
│   └── png/
└── handoff/
    ├── developer-handoff.md
    └── ai-agent-prompt.md
```
