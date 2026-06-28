---
name: convallaria
description: "Agentic design suite for routing professional design work across brand concepting, design-system extraction, logo and icon production, image optimization, token handoff, visual QA, and asset packaging. Use when a user asks Codex to create, refine, inspect, formalize, export, or QA visual identity systems, design systems, logos, images, UI styling, or design handoff assets. Also use as the coordinating parent skill for the bundled refine subskill."
---

# Convallaria

Convallaria is a routing and production skill for design work. Treat it as the design director for a modular suite: classify the task, load only the relevant subskill, use deterministic scripts for fragile asset operations, and produce polished deliverables that another agent or designer can continue.

Convallaria project files, templates, references, examples, and durable deliverables are authored in English. If a consuming project explicitly requires localization, keep the Convallaria source of truth in English and treat localized copies as secondary exports.

## Routing First

Start by identifying the task family:

- **Design-system extraction**: route to `subskills/refine/`.
- **Brand concepting**: read `subskills/concept/SKILL.md`.
- **Logo and icon production**: read `subskills/logo/SKILL.md`.
- **Image optimization**: read `subskills/images/SKILL.md`.
- **Token handoff**: read `subskills/tokens/SKILL.md`.
- **UI visual QA**: read `subskills/audit/SKILL.md`.
- **Complete brand pack**: read `subskills/pack/SKILL.md` for brand concept, logo, tokens, asset packaging, and handoff as one workflow.
- **Asset packaging or multi-step delivery**: read `subskills/export/SKILL.md`.
- **Unclear or mixed request**: read `routing.md`, then select a workflow.

For quick classification, run:

```bash
python3 scripts/route_task.py "user request here"
```

Use the script as an advisor, not as the final authority. Prefer the user's explicit intent over keyword matches.

## Core Workflows

### Extract a Design System

Use the `refine` subskill when the user provides screenshots, a website, a codebase, a Figma export, a brand guide, or a mood description and asks for a formal design system.

1. Read `subskills/refine/SKILL.md`.
2. Follow its workflow exactly.
3. Produce `DESIGN.md` and the HTML report it specifies.

### Create a Brand Direction

Read `subskills/concept/SKILL.md` when the task starts from strategy, naming, personality, audience, positioning, visual territories, or early identity exploration. Use `subskills/concept/templates/BRAND.md` as the output structure when the user wants a durable artifact.

### Build a Complete Brand Pack

Read `subskills/pack/SKILL.md` when the user wants the full path from early brand intent to deliverable assets. Produce a coherent package that includes `BRAND.md`, `LOGO_SPEC.md`, token files, logo assets, `asset-manifest.json`, and handoff notes when they are relevant.

### Produce Logo and Platform Assets

Read `subskills/logo/SKILL.md` when the user asks for logo concepts, SVG cleanup, favicon sets, app icons, social avatars, or platform-specific logo exports. Use `subskills/logo/scripts/rasterize_svg.py` for SVG-to-PNG export when a source SVG exists.

### Optimize Images

Read `subskills/images/SKILL.md` when the user asks for compression, conversion, responsive variants, image manifests, metadata stripping, or delivery optimization. Use `subskills/images/scripts/optimize_images.py` when bitmap assets are present.

### Package a Handoff

Read `subskills/export/SKILL.md` when a task spans multiple outputs or needs a final brand pack. Use `subskills/export/templates/asset-manifest.json` to record source files, outputs, roles, and producer steps.

## Output Conventions

Use a project-local output folder unless the user names a destination:

```text
convallaria-output/
├── BRAND.md
├── DESIGN.md
├── LOGO_SPEC.md
├── DESIGN_QA.md
├── asset-manifest.json
├── tokens/
├── logo/
├── images/
├── screenshots/
└── handoff/
```

For every multi-file deliverable, create or update `asset-manifest.json` with:

- project name and slug
- input files and their roles
- generated outputs and their producer skill
- token paths
- logo and image asset paths
- notes about assumptions, unresolved decisions, and next actions

## Quality Bar

- Preserve source material unless the user requests transformation.
- Prefer scripts for repetitive image, logo, token, and packaging work.
- Keep strategic writing specific enough for production decisions.
- Verify generated files exist before reporting completion.
- For frontend or UI QA tasks, use screenshots when possible and report concrete visual deviations.
- For brand and design outputs, name rationale, constraints, and anti-patterns so future agents can maintain the system.
- Avoid generic AI collage output: every aesthetic choice should map to a strategic reason, an implementation token, a logo rule, an asset file, or an explicit open decision.
