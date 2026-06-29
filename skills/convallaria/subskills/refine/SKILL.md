---
name: refine
description: "Extract design elements from any user input source (images, documents, projects, websites) and distill them into a complete, structured design system. Outputs a DESIGN.md with Design Tokens (CSS custom properties and Tailwind mappings) plus AI-friendly style descriptions, and a polished single-file HTML report with full-page snap-scroll sections showcasing the extracted color palette, typography, component library, and composite patterns — all rendered in the source's own visual language. Use when a user wants to reverse-engineer, document, or formalize a design system from existing materials."
---

# Refine — Extract & Formalize Design Systems

Use when: existing visual material needs to become a structured design system.
Needs: screenshots, images, documents, websites, code, Figma exports, brand guidelines, or a mood description to analyze.
Produces: `DESIGN.md` and a polished single-file HTML report from `templates/report.html`.
Done when: design decisions are explicit, inferred gaps are named, and the output can guide humans and AI agents.

## Core Mission

You are a senior design systems architect. Your job is to analyze any input source the user provides — screenshots, images, documents, live websites, codebases, Figma exports, brand guidelines, or even a vague mood description — and extract every meaningful design decision into a **complete, production-ready design system**.

You produce two deliverables:

1. **DESIGN.md** — A structured design specification with Design Tokens (CSS custom properties + Tailwind config mappings) and AI-friendly style descriptions
2. **An HTML report** — A polished, single-file visual presentation of the design system, built from the template in `templates/report.html`

## Output Language

Write generated `DESIGN.md` and HTML report content in English by default, matching the Convallaria project language policy. If the consuming project explicitly requires localization, keep the English source of truth and treat localized files as secondary exports.

---

## Phase 1: Source Analysis

### Accepting Any Input

The user may provide:

- **Images/Screenshots**: Analyze visual elements — colors, typography, spacing, component patterns, illustration style, photography treatment
- **Documents**: Extract brand guidelines, style references, tone descriptions
- **Projects/Codebases**: Scan CSS/SCSS/Tailwind configs, component libraries, theme files, design token files
- **Websites/URLs**: Analyze the live visual presentation — fetch and inspect if possible
- **Verbal descriptions**: The user describes an aesthetic ("minimal, warm, Japanese-inspired") — you interpret and formalize it
- **Mixed inputs**: Combine multiple sources into a unified system

### Extraction Checklist

For every source, systematically extract:

1. **Color Palette** — Every distinct color, organized by role (primary, secondary, accent, surface, text, border, semantic states)
2. **Typography** — Font families, size scale, weight scale, line-height scale, letter-spacing scale, hierarchy rules
3. **Spacing & Layout** — Base unit, full spacing scale (from 0 to largest observed), grid system, container widths, section rhythm
4. **Border Radius** — Radius scale from sharp to fully rounded, with usage contexts
5. **Border Width** — Border thickness scale (thin, medium, thick) with usage contexts
6. **Depth & Elevation** — Shadow styles, border treatments, layering strategy, z-index scale
7. **Opacity System** — Opacity values for disabled states, hover overlays, text hierarchy, backdrop overlays
8. **Motion & Transitions** — Duration scale (fast, normal, slow), easing curves, animation timing, hover/focus transitions
9. **Component Patterns** — Buttons, cards, inputs, navigation, badges, tags, and any domain-specific components
10. **Visual Personality** — The emotional character: warm vs. cool, organic vs. geometric, editorial vs. functional, playful vs. serious
11. **Iconography & Illustration Style** — Line weight, fill style, color treatment, geometric vs. organic, icon sizing scale
12. **Focus & Accessibility** — Focus ring styles (width, offset, color), minimum touch target sizes, contrast requirements
13. **Gradients** — Gradient definitions (directions, color stops) or explicit statement if gradient-free
14. **Sizing Tokens** — Icon sizes, touch targets, avatar sizes, and other reusable dimension values
15. **Aspect Ratios** — Standard aspect ratios for images, videos, cards, and media containers
16. **Responsive Strategy** — Breakpoints, container widths per breakpoint, collapsing behavior, scaling approach
17. **Dark Mode / Theming** — Whether a dark mode exists, and if so, how token values map between themes (or note if single-theme only)

### When Information is Missing

If the source doesn't provide enough information for certain categories (e.g., a single screenshot can't reveal responsive behavior), you must:

- **Infer reasonable defaults** based on the visual personality you've identified
- **State your inference explicitly** in the DESIGN.md: "Inferred from visual style — not directly observed in source"
- **Never leave a section empty** — a complete design system always has a position on every dimension

---

## Phase 2: Produce DESIGN.md

The DESIGN.md must follow this exact structure. Each section serves a specific purpose — the file is designed to be consumed by both humans and AI agents.

### Required Sections

```
# {Design System Name}

## 1. Visual Theme & Atmosphere
## 2. Color Palette & Roles
## 3. Typography Rules
## 4. Component Stylings
## 5. Layout Principles
## 6. Depth & Elevation
## 7. Do's and Don'ts
## 8. Responsive Behavior
## 9. Design Tokens
## 10. Agent Prompt Guide
```

### Section Specifications

#### Section 1: Visual Theme & Atmosphere

**Purpose**: Give any reader (human or AI) an instant, visceral understanding of what this design _feels like_.

Write 2-3 paragraphs in a descriptive, almost literary style that captures:

- The emotional character and personality of the design
- What makes it visually distinctive compared to conventional approaches
- The key design philosophy and principles at work
- Specific sensory metaphors (e.g., "feels like reading a well-set book" or "the crispness of a Swiss railway timetable")

End with a **Key Characteristics** bullet list (6-10 items) summarizing the signature visual moves with specific color/size values in parentheses.

#### Section 2: Color Palette & Roles

**Purpose**: Define every color in the system with its semantic role, not just its hex value.

Organize colors into these groups:

- **Primary** — Brand colors and primary actions
- **Secondary & Accent** — Supporting chromatic colors
- **Surface & Background** — Page, card, and container backgrounds
- **Neutrals & Text** — Text hierarchy colors from darkest to lightest
- **Semantic & Accent** — Borders, rings, shadows, success/error/warning states
- **Gradient System** — Gradient definitions, or explicit statement if gradient-free

For each color entry:

```
- **{Semantic Name}** (`{hex}`): {One sentence describing exactly when and why to use this color.}
```

Always include RGB/HSL values for each color. The semantic name should be evocative and memorable — "Parchment" not "Light Background 1".

#### Section 3: Typography Rules

**Purpose**: Define the complete type system so any implementation produces identical results.

Include:

- **Font Family**: Primary, secondary, monospace — with specific fallback stacks
- **Hierarchy Table**: A markdown table with columns: Role | Font | Size | Weight | Line Height | Letter Spacing | Notes
- **Principles**: 3-5 typographic principles explaining _why_ the choices were made (e.g., "Serif for authority, sans for utility")

#### Section 4: Component Stylings

**Purpose**: Define the visual treatment for every reusable component.

For each component, specify:

- Background color (by semantic name + hex)
- Text color (by semantic name + hex)
- Padding (exact spacing scale values)
- Border radius (exact value + scale name)
- Border (width from border-width scale + color)
- Shadow (exact CSS value from shadow scale)
- Opacity (disabled state, hover overlay — from opacity scale)
- Transitions (duration + easing from motion tokens)
- Hover/Active/Focus states (including focus ring style)
- Any variants (primary, secondary, ghost, etc.)

Required components:

- Buttons (all variants)
- Cards & Containers
- Inputs & Forms
- Navigation
- Badges & Tags
- Image Treatment
- Any domain-specific components observed in the source

#### Section 5: Layout Principles

**Purpose**: Define the spatial system.

Include:

- **Spacing System**: Base unit and full scale (from 0 to largest value, with named steps)
- **Grid & Container**: Max widths per breakpoint (from container tokens), column system, alignment
- **Whitespace Philosophy**: The reasoning behind spacing decisions
- **Border Radius Scale**: Named scale (e.g., none 0 → full 9999px) with usage contexts
- **Border Width Scale**: Thickness levels (thin/medium/thick) and when each is used
- **Sizing Tokens**: Icon sizes, touch target minimums, avatar sizes
- **Aspect Ratios**: Standard ratios for images, videos, cards, media containers

#### Section 6: Depth & Elevation

**Purpose**: Define how depth is communicated.

Include:

- **Shadow Scale Table**: Level | CSS Value | Use
- **Z-Index Scale Table**: Name | Value | Use (e.g., dropdown, modal, tooltip layers)
- **Opacity System Table**: Name | Value | Use (e.g., disabled states, hover overlays, text de-emphasis)
- **Shadow Philosophy**: A paragraph explaining the approach to depth
- **Layering Strategy**: How z-index values are assigned to prevent conflicts

#### Section 7: Do's and Don'ts

**Purpose**: Guard rails for maintaining design consistency.

- **Do**: 8-12 specific, actionable rules with exact values
- **Don't**: 8-12 specific anti-patterns with explanations of _why_ they break the system

These must be specific enough that an AI agent can programmatically verify compliance. Not "use warm colors" but "use Parchment (#f5f4ed) as the primary light background — never pure white (#ffffff)".

#### Section 8: Responsive Behavior

**Purpose**: Define how the system adapts across screen sizes.

Include:

- **Breakpoints table**: Name | Width (from container tokens) | Key Changes
- **Touch Targets**: Minimum sizes (referencing `--size-touch-target` token)
- **Collapsing Strategy**: How each component type responds
- **Image Behavior**: Scaling, art direction rules, and aspect ratio usage
- **Motion Adaptation**: Whether animations are reduced for `prefers-reduced-motion`
- **Dark Mode**: Whether the system supports `prefers-color-scheme: dark`, and how token values remap between themes (or explicitly note single-theme only)

#### Section 9: Design Tokens

**Purpose**: Machine-readable tokens for direct integration with Tailwind CSS and CSS custom properties.

This section is critical for engineering adoption. Provide:

**CSS Custom Properties:**

```css
:root {
  /* ── Colors ── */
  --color-primary: #XXXXXX;
  --color-primary-rgb: R, G, B;
  --color-secondary: #XXXXXX;
  /* ... every color from Section 2 ... */

  /* ── Typography — Font Families ── */
  --font-family-heading: 'Font Name', fallback;
  --font-family-body: 'Font Name', fallback;
  --font-family-mono: 'Font Name', fallback;

  /* ── Typography — Font Sizes ── */
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  /* ... full scale ... */

  /* ── Typography — Font Weights ── */
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;

  /* ── Typography — Line Heights ── */
  --leading-none: 1;
  --leading-tight: 1.1;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;

  /* ── Typography — Letter Spacing ── */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0em;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;

  /* ── Spacing (full scale) ── */
  --spacing-0: 0;
  --spacing-px: 1px;
  --spacing-0-5: 0.125rem;
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-5: 1.25rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-10: 2.5rem;
  --spacing-12: 3rem;
  --spacing-16: 4rem;
  --spacing-20: 5rem;
  --spacing-24: 6rem;
  /* ... extend as needed ... */

  /* ── Border Radius ── */
  --radius-none: 0;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-full: 9999px;

  /* ── Border Width ── */
  --border-width-none: 0;
  --border-width-thin: 1px;
  --border-width-medium: 2px;
  --border-width-thick: 4px;

  /* ── Shadows ── */
  --shadow-ring: 0px 0px 0px 1px var(--color-border);
  --shadow-sm: ...;
  --shadow-md: ...;
  --shadow-lg: ...;
  --shadow-xl: ...;
  /* ... all shadow levels ... */

  /* ── Opacity ── */
  --opacity-0: 0;
  --opacity-hover: 0.04;
  --opacity-disabled: 0.38;
  --opacity-overlay-light: 0.5;
  --opacity-overlay-medium: 0.6;
  --opacity-secondary: 0.7;
  --opacity-overlay-heavy: 0.8;
  --opacity-full: 1;

  /* ── Z-Index ── */
  --z-deep: -1;
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-popover: 500;
  --z-tooltip: 600;
  --z-toast: 700;
  --z-max: 9999;

  /* ── Motion / Transitions ── */
  --duration-instant: 0ms;
  --duration-fast: 100ms;
  --duration-normal: 200ms;
  --duration-moderate: 300ms;
  --duration-slow: 500ms;
  --duration-slower: 700ms;
  --easing-default: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-in: cubic-bezier(0.4, 0, 1, 1);
  --easing-out: cubic-bezier(0, 0, 0.2, 1);
  --easing-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* ── Focus Ring ── */
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-color: var(--color-primary);
  --focus-ring-style: solid;

  /* ── Container / Breakpoint Widths ── */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1280px;
  --container-2xl: 1536px;

  /* ── Sizing ── */
  --size-icon-xs: 12px;
  --size-icon-sm: 16px;
  --size-icon-md: 20px;
  --size-icon-lg: 24px;
  --size-icon-xl: 32px;
  --size-touch-target: 44px;
  --size-avatar-sm: 32px;
  --size-avatar-md: 40px;
  --size-avatar-lg: 56px;

  /* ── Gradients ── */
  --gradient-primary: linear-gradient(135deg, var(--color-primary), var(--color-accent));
  --gradient-surface: linear-gradient(180deg, var(--color-bg), var(--color-bg-alt));
  /* ... or state "gradient-free" if not applicable ... */

  /* ── Aspect Ratios ── */
  --aspect-square: 1 / 1;
  --aspect-video: 16 / 9;
  --aspect-photo: 4 / 3;
  --aspect-portrait: 3 / 4;
  --aspect-wide: 21 / 9;

  /* ── Scrollbar ── */
  --scrollbar-width: 4px;
  --scrollbar-track: transparent;
  --scrollbar-thumb: var(--color-border-strong);
  --scrollbar-radius: 2px;

  /* ── Text Decoration ── */
  --decoration-thickness: 1px;
  --decoration-offset: 2px;
  --decoration-color: currentColor;
}
```

**Tailwind CSS Config Extension:**

```js
// tailwind.config.js extend
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#XXXXXX',
        // ... all colors with semantic names
      },
      fontFamily: {
        heading: ['Font Name', 'fallback'],
        body: ['Font Name', 'fallback'],
        mono: ['Font Name', 'fallback'],
      },
      fontSize: { /* xs through 4xl — full scale */ },
      fontWeight: {
        light: '300',
        regular: '400',
        medium: '500',
        semibold: '600',
        bold: '700',
        extrabold: '800',
      },
      lineHeight: {
        none: '1',
        tight: '1.1',
        snug: '1.25',
        normal: '1.5',
        relaxed: '1.625',
        loose: '2',
      },
      letterSpacing: {
        tighter: '-0.05em',
        tight: '-0.025em',
        normal: '0em',
        wide: '0.025em',
        wider: '0.05em',
        widest: '0.1em',
      },
      spacing: { /* 0 through 24 — full scale */ },
      borderRadius: { /* none through full — full scale */ },
      borderWidth: {
        none: '0',
        thin: '1px',
        medium: '2px',
        thick: '4px',
      },
      boxShadow: { /* ring, sm, md, lg, xl — all shadows */ },
      opacity: {
        hover: '0.04',
        disabled: '0.38',
        'overlay-light': '0.5',
        secondary: '0.7',
        'overlay-heavy': '0.8',
      },
      zIndex: {
        deep: '-1',
        dropdown: '100',
        sticky: '200',
        overlay: '300',
        modal: '400',
        popover: '500',
        tooltip: '600',
        toast: '700',
        max: '9999',
      },
      transitionDuration: {
        instant: '0ms',
        fast: '100ms',
        normal: '200ms',
        moderate: '300ms',
        slow: '500ms',
        slower: '700ms',
      },
      transitionTimingFunction: {
        default: 'cubic-bezier(0.4, 0, 0.2, 1)',
        in: 'cubic-bezier(0.4, 0, 1, 1)',
        out: 'cubic-bezier(0, 0, 0.2, 1)',
        'in-out': 'cubic-bezier(0.4, 0, 0.2, 1)',
        bounce: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
      ringWidth: { focus: '2px' },
      ringOffsetWidth: { focus: '2px' },
      containers: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1536px',
      },
      width: {
        'icon-xs': '12px',
        'icon-sm': '16px',
        'icon-md': '20px',
        'icon-lg': '24px',
        'icon-xl': '32px',
        'touch-target': '44px',
      },
      aspectRatio: {
        square: '1 / 1',
        video: '16 / 9',
        photo: '4 / 3',
        portrait: '3 / 4',
        wide: '21 / 9',
      },
      backgroundImage: {
        'gradient-primary': 'linear-gradient(135deg, var(--color-primary), var(--color-accent))',
        'gradient-surface': 'linear-gradient(180deg, var(--color-bg), var(--color-bg-alt))',
      },
    }
  }
}
```

Every token must trace back to a specific color/value defined in earlier sections. Use consistent naming conventions across CSS vars and Tailwind config.

#### Section 10: Agent Prompt Guide

**Purpose**: Help AI agents (like Claude, GPT, etc.) use this design system correctly when generating code or UI.

Include:

- **Quick Color Reference**: A compact lookup table for the most commonly used colors
- **Example Component Prompts**: 4-6 copy-paste-ready prompts that demonstrate how to reference the design system when asking an AI to generate components
- **Iteration Guide**: 5-7 rules for working with this design system in AI-assisted workflows

---

## Phase 3: Produce HTML Report

### Overview

Generate a polished, single-file HTML report that visually showcases the extracted design system. The report must be a compelling presentation — think "brand book as a web experience."

### Template System

Read the HTML template from `templates/report.html` in this skill's directory. The template provides:

- Full-page snap-scroll sections with smooth damping
- CSS reset and base layout
- JavaScript for scroll behavior and interactions
- Placeholder slots for AI-generated content

Your job is to populate the template's content slots with the extracted design data, using the source's own color palette to style the presentation.

### Report Sections (one full-page section each)

The HTML report must contain these sections, each occupying a full viewport height and scrollable with snap behavior:

**Section 1 — Cover**

- Design system name as a large hero title
- Source description / tagline
- Date of extraction
- Visual personality keywords as subtle tags

**Section 2 — Color Palette**

- Large color swatches for each primary/secondary/accent color
- Each swatch shows: color name, hex, RGB values
- Background/surface colors shown as layered cards
- The section itself uses the extracted palette for its own styling

**Section 3 — Typography**

- Font family specimens showing all weights
- Size scale demonstration with actual rendered text at each size
- Hierarchy demonstration (heading → body → caption → label)

**Section 4 — Design Tokens**

- A well-formatted reference table of all CSS custom properties
- Organized by category (colors, typography, spacing, radius, shadows)
- Each token shows: variable name, value, and a visual preview (color swatch, size indicator, etc.)

**Section 5 — Atomic Components**

- Button variants rendered as live examples
- Card variants
- Input/form elements
- Badge/tag variants
- Each component rendered using the actual design tokens

**Section 6 — Composite Patterns**

- A hero section composition using the design system
- A feature card grid
- A navigation bar
- A form layout
- A content section with typography hierarchy
- These demonstrate how atomic components combine into real UI patterns

**Section 7 — Guidelines**

- Do's and Don'ts presented as a visual comparison grid
- Each rule with a ✅ or ❌ icon and a brief explanation

### HTML Generation Rules

1. **Self-contained**: The entire report must be a single `.html` file. All CSS and JS inline. No external dependencies except Google Fonts (if the design uses web fonts).
2. **Use extracted colors**: The report's own color scheme must use the colors extracted from the source. The background, text, accents — everything should feel like it belongs to the source's design system.
3. **Template compliance**: Read `templates/report.html` and inject your content into the designated placeholder areas. Do not modify the template's structural HTML, scroll behavior JS, or base CSS. Only populate content slots.
4. **Responsive**: The report itself should be responsive and look good on both desktop and mobile.
5. **Print-friendly**: Include a `@media print` stylesheet that produces clean output.
6. **Dark design system — unified dark report**: When the extracted design system uses a dark palette (dark backgrounds like `#0a0a0a`–`#1a1a1a`, light text like `#ffffff`), the **entire report must use a unified dark theme**. Set `data-system-theme="dark"` on the `<html>` element. The template will automatically remap all section themes to use dark backgrounds with light text, creating visual rhythm through different shades of dark (bg → bg-alt → surface) instead of light/dark alternation. Do NOT add any "dark theme overrides" CSS block — the template handles everything automatically via the `data-system-theme` attribute.
7. **No hardcoded color overrides**: Never add CSS blocks that hardcode element colors (e.g., `.ds-token-table td { color: #ffffff; }`). The template uses `color: inherit` and `currentColor` throughout, so all child elements automatically adapt to their section's color scheme. Hardcoded overrides will cause contrast failures.

---

## Execution Workflow

When the user triggers this skill:

### Step 1: Identify and Ingest Sources

- Determine what the user has provided (images, files, URLs, descriptions, project paths)
- For images: analyze visual elements directly
- For codebases: scan for CSS/SCSS/Tailwind configs, theme files, component files
- For URLs: fetch and analyze the page
- For descriptions: interpret the aesthetic intent

### Step 2: Extract Design Elements

- Follow the Extraction Checklist systematically
- For each element, record the specific value (hex code, pixel size, font name)
- Note where you're observing vs. inferring

### Step 3: Read the HTML Template

- Read `templates/report.html` from this skill's directory (use the skill's installation path)
- Understand the placeholder structure

### Step 4: Generate DESIGN.md

- Follow the Required Sections structure exactly
- Include all Design Tokens with CSS custom properties and Tailwind config
- Write in the user's language

### Step 5: Generate HTML Report

- Populate the template with extracted data
- Style the report using the extracted color palette
- Render live component examples
- Write all content in the user's language

### Step 6: Save Outputs

- Save `DESIGN.md` to the user's working directory (or a path they specify)
- Save the HTML report (e.g., `design-system-report.html`) to the same location
- Tell the user where the files are and offer to open the HTML report

---

## Quality Standards

### DESIGN.md Quality

- Every color must have a semantic name AND a hex value
- Every component must have exact pixel/rem values — no vague descriptions
- Design Tokens must be valid CSS and valid Tailwind config
- The Agent Prompt Guide must contain copy-paste-ready examples
- Do's and Don'ts must reference specific values, not general principles

### HTML Report Quality

- All color swatches must display the actual color (not a placeholder)
- Typography specimens must use the actual fonts (with web font loading or fallbacks)
- Component examples must be rendered with the actual design tokens (inline styles or scoped CSS using the token values)
- Smooth scroll snapping must work without jank
- The report must be visually impressive — this is a showcase piece

### Completeness Check

Before delivering, verify:

- [ ] All 10 DESIGN.md sections are present and non-empty
- [ ] CSS custom properties cover every color, font size, spacing, radius, and shadow
- [ ] Tailwind config extension is syntactically valid
- [ ] HTML report has all 7 sections
- [ ] HTML report uses the extracted color palette for its own styling
- [ ] All content is in the user's language
- [ ] Component examples actually render (not just described)
