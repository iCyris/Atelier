---
name: tokens
description: "Design token workflow for converting brand or design-system decisions into CSS variables, Tailwind theme extensions, JSON tokens, TypeScript themes, and implementation handoff."
---

# Design Tokens Workflow

Use this reference when converting brand or design-system decisions into implementation-ready tokens.

## Supported Outputs

- CSS custom properties
- Tailwind `theme.extend`
- JSON tokens
- TypeScript theme objects
- Style Dictionary compatible JSON

## Process

1. Read the source of truth: usually `DESIGN.md`, `BRAND.md`, existing CSS variables, Tailwind config, or theme files.
2. Preserve semantic naming. Prefer `color.surface.night` over `blue900` when the design system has named roles.
3. Separate primitives from semantic roles:
   - primitives: raw values such as `#0b0d1f`
   - semantic roles: usage such as `background.canvas`
4. Include typography, spacing, radius, shadow, opacity, z-index, motion, breakpoint, and sizing tokens when available.
5. Add comments or notes for inferred values.

## Output Convention

```text
tokens/
├── tokens.json
├── tokens.css
├── tailwind.extend.js
├── theme.ts
└── tokens.report.md
```

## Quality Criteria

- Every token must have a clear role or usage.
- Avoid duplicate names for the same role.
- Keep values consistent across CSS, JSON, and Tailwind outputs.
- Note gaps when the source does not define a category.
