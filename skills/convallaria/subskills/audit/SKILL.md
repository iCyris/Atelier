---
name: audit
description: "UI visual QA workflow for reviewing implementations against brand systems, design systems, screenshots, token files, responsive states, and style drift."
---

# UI Visual QA Workflow

Use when: a user needs UI visual QA against a brand system, design system, screenshots, tokens, or responsive states.
Needs: the expected source of truth and either screenshots, a local app URL, or implementation files to inspect.
Produces: `DESIGN_QA.md` with concrete findings, severity, expected behavior, and fixes when editing is in scope.
Done when: defects and optional polish are separated, evidence is concrete, and no design rule is invented without a source.

Use this reference when reviewing a UI implementation against a design system, screenshot, brand direction, or token set.

## Inputs

- local app URL
- screenshots
- `DESIGN.md`
- token files
- component source files
- visual references

## Process

1. Identify the expected design source of truth.
2. Capture or inspect desktop and mobile states when possible.
3. Compare:
   - color roles
   - typography hierarchy
   - spacing rhythm
   - border radius
   - shadows and depth
   - icon style
   - responsive behavior
   - interaction states
4. Record findings in `DESIGN_QA.md`.
5. If editing code is in scope, fix the highest-impact deviations and re-check.

## Finding Format

Use concise findings:

```text
Severity: High
Surface: Pricing card heading
Issue: Uses body font at 20 px instead of display font at 24 px.
Expected: Follow DESIGN.md typography rule for section headings.
Fix: Update heading class to use the heading token and line-height token.
```

## Quality Criteria

- Prefer concrete values over subjective comments.
- Include screenshots when visual inspection matters.
- Separate defects from optional polish.
- Do not invent design-system rules when a source of truth is present.
