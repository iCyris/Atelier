# Convallaria Routing Guide

Use this guide when the user's request is mixed, ambiguous, or spans more than one design operation.

## Task Families

| Family | Use when the user asks for | Primary resource | Common outputs |
| --- | --- | --- | --- |
| Refine | extracting style, reverse-engineering visuals, formalizing existing UI, creating tokens from screenshots or code | `subskills/refine/SKILL.md` | `DESIGN.md`, `report.html` |
| Concept | naming, positioning, personality, brand voice, creative direction, visual territories | `subskills/concept/SKILL.md` | `BRAND.md` |
| Logo | logo concepts, SVG cleanup, favicon/app icon export, lockups, clear space | `subskills/logo/SKILL.md` | `LOGO_SPEC.md`, `logo/` |
| Images | compression, conversion, responsive variants, metadata removal | `subskills/images/SKILL.md` | `images/`, `image-manifest.json` |
| Tokens | CSS variables, Tailwind config, Style Dictionary, theme files | `subskills/tokens/SKILL.md` | `tokens/` |
| Audit | screenshot review, design-system compliance, responsive visual checks | `subskills/audit/SKILL.md` | `DESIGN_QA.md`, screenshots |
| Pack | full brand creation from intent to logo, tokens, exports, handoff, and manifest | `subskills/pack/SKILL.md` | `BRAND.md`, `LOGO_SPEC.md`, `tokens/`, `logo/`, `asset-manifest.json`, `handoff/` |
| Export | final packaging, handoff, manifest, cross-tool delivery | `subskills/export/SKILL.md` | brand pack, handoff docs |

## Composition Patterns

### From a vague product idea to a usable identity

1. `pack`
2. `concept`
3. `logo`
4. `tokens`
5. `export`

### From screenshots to an implementation-ready design system

1. `refine`
2. `tokens`
3. `audit` if there is an implementation to inspect
4. `export`

### From an SVG logo to platform assets

1. `logo`
2. `images`
3. `export`

### From an existing app to a design audit

1. `refine` if no design system exists
2. `audit`
3. `tokens` if token drift needs repair

## Routing Rules

- Route to the narrowest resource that can complete the task.
- Use `pack` when the user wants a complete identity system, not just isolated concept copy or isolated logo exports.
- Load `refine` only for extraction or formalization tasks; it is intentionally large.
- Use scripts for image transforms, SVG rasterization, and manifest validation.
- When multiple subskills are needed, create an `asset-manifest.json` early so each step can append outputs.
- Ask a concise clarifying question only when the target deliverable or source asset is impossible to infer.
