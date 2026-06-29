# Convallaria

<p align="center">
  <img src="assets/brand/convallaria-mark.png" alt="Convallaria logo" width="180">
</p>

<h1 align="center">Convallaria</h1>

<p align="center">
  <strong>Quiet brand craft from first feeling to final assets.</strong>
</p>

<p align="center">
  <img alt="doctor passing" src="https://img.shields.io/badge/doctor-passing-2ea043">
  <img alt="version 0.1.0" src="https://img.shields.io/badge/version-0.1.0-0969da">
  <img alt="license MIT" src="https://img.shields.io/badge/license-MIT-0969da">
  <img alt="local plugin" src="https://img.shields.io/badge/distribution-local_plugin-6f42c1">
</p>

Convallaria helps agents turn rough brand or UI material into useful design handoff files. It keeps the path quiet: one routed entry, focused design workflows, deterministic asset scripts, and durable outputs another designer, engineer, or agent can continue.

## Start With `/conva`

Use `/conva` as the front door. Describe the design task in plain language and let Convallaria route the work.

```text
/conva I need a brand direction for this app idea.
/conva Turn these screenshots into a design system.
/conva Export this logo for favicon and app icon use.
/conva QA this UI against the attached brand system.
```

## What Can I Give It?

- a product idea, audience, name, tone, or mood
- screenshots, a website, a codebase, or a visual reference
- an existing logo, SVG, icon, or bitmap image
- brand notes, design decisions, token files, or UI source files
- a local app or screenshots that need visual QA

## What Will I Get?

- `BRAND.md` for positioning, voice, visual direction, and production decisions
- `DESIGN.md` and `report.html` for extracted design systems
- `LOGO_SPEC.md` and logo export guidance or assets
- `tokens/` with CSS, JSON, Tailwind, and TypeScript theme files
- optimized images and image manifests when bitmap assets are provided
- `asset-manifest.json` for traceable multi-file handoff

## Skills

Each design operation lives as a focused subskill. Most users should start with `/conva`; advanced users can jump directly to a specific command when the task is already clear.

| Subskill | When | What it does |
| --- | --- | --- |
| `concept` | Starting from a product idea, audience, name, tone, or mood | Creates positioning, voice, visual territories, brand strategy, anti-patterns, and a production direction. |
| `refine` | Existing visuals need to become a design system | Extracts color, type, spacing, component rules, tokens, and an HTML report from screenshots, sites, code, docs, or mood references. |
| `logo` | Marks, wordmarks, favicons, app icons, or platform exports are needed | Produces logo system guidance, SVG source rules, clear-space rules, variants, and raster export plans. |
| `images` | Bitmap assets need delivery preparation | Compresses, converts, resizes, strips metadata, and records responsive image variants. |
| `tokens` | Brand or design decisions need implementation files | Converts decisions into CSS variables, JSON tokens, Tailwind extensions, and TypeScript theme files. |
| `audit` | A UI needs visual QA against a brand or design system | Reviews screenshots, implementations, tokens, responsive states, and design drift. |

Complete identity work is coordinated by the parent `convallaria` skill using the focused subskills above. Multi-file delivery uses the shared manifest and handoff protocol in `skills/convallaria/shared/`.

Typical outputs include:

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

## Install

Convallaria is maintained as a local plugin project. It is not published to a public Codex or Claude marketplace from this repository.

Run the local installer from this checkout:

```bash
python3 scripts/conva.py install
```

This command:

- syncs project Claude Code guide and slash-command adapters into `.claude/`
- installs managed user-level Claude Code commands into `~/.claude/commands/`
- creates `~/plugins/convallaria` as a symlink to this checkout for the default personal Codex marketplace
- creates or updates `~/.agents/plugins/marketplace.json` with a local `convallaria` plugin entry
- runs the smoke test by default
- prints the local Codex reinstall command, usually `codex plugin add convallaria@personal`

For Claude Code, start with:

```text
/conva
```

Advanced users can also jump directly to focused commands:

```text
/conva-concept
/conva-logo
/conva-refine
/conva-images
/conva-tokens
/conva-audit
```

Compatibility aliases remain available:

```text
/conva-brand -> /conva-concept
/conva-optimize -> /conva-images
```

If a Claude Code command shows as unknown, run `python3 scripts/conva.py install` from this checkout and restart Claude Code if the command list is already loaded.

For Codex, run the command printed by the installer:

```bash
codex plugin add convallaria@personal
```

Then start a new Codex thread so the refreshed plugin metadata and `skills/` directory are loaded. The plugin manifest exposes `skills/`, and the main skill is `skills/convallaria/SKILL.md`.

For other AI coding tools, point the agent at:

```text
AGENTS.md
skills/convallaria/SKILL.md
```

Then ask it to route to the relevant subskill under `skills/convallaria/subskills/`.

## Use

Start with `/conva` and a plain-language brief:

```text
/conva Create a complete brand identity for this product idea.
/conva Turn these screenshots into a design system.
/conva Produce logo exports and a handoff manifest.
/conva QA this UI against the attached brand system.
```

Route a request manually:

```bash
cd skills/convallaria
python3 scripts/route_task.py "create a complete brand identity from positioning to logo, tokens, and handoff assets"
```

Common deterministic asset commands:

```bash
cd skills/convallaria
python3 subskills/logo/scripts/rasterize_svg.py logo/source/logo.svg --out logo/png --sizes 16 32 64 128 256 512 1024
python3 subskills/images/scripts/optimize_images.py input.png --out images --formats webp jpeg --max-width 1600 --quality 82
python3 shared/scripts/validate_outputs.py asset-manifest.json
```

The SVG rasterizer uses CairoSVG when available, then falls back to `rsvg-convert`, Inkscape, or macOS QuickLook when available.

## Chaining Skills

Convallaria subskills can be chained, but each transition should be intentional. A good run names the next source of truth before moving on.

Common workflows:

```text
brand idea -> concept -> logo -> tokens -> shared manifest and handoff
```

```text
screenshots -> refine -> DESIGN.md -> tokens -> audit
```

```text
source SVG -> logo -> raster export -> images -> shared manifest and handoff
```

For multi-file work, create or update `asset-manifest.json` early. It should record inputs, generated outputs, producer steps, quality checks, assumptions, open questions, and next actions.

## Maintain

Run the health check:

```bash
python3 scripts/conva.py doctor
```

Use `--skip-raster` only when an SVG brand asset needs rasterization and the machine lacks CairoSVG, `rsvg-convert`, Inkscape, or macOS QuickLook:

```bash
python3 scripts/conva.py doctor --skip-raster
```

Refresh local integrations after editing the skill:

```bash
python3 scripts/conva.py update
```

When iterating on a local Codex plugin and you need to force Codex to notice refreshed metadata, use an explicit cachebuster:

```bash
python3 scripts/conva.py update --codex-cachebuster
codex plugin add convallaria@personal
```

Skip the smoke test only when you are intentionally doing a metadata-only sync:

```bash
python3 scripts/conva.py update --no-smoke
```

## Uninstall

Remove generated Convallaria adapters:

```bash
python3 scripts/conva.py uninstall
```

The uninstall command removes project `.claude/` files that still match their tracked sources, managed user-level Claude Code commands containing the Convallaria marker, the generated personal Codex marketplace entry, and the `~/plugins/convallaria` symlink when it points at this checkout. It does not delete `.claude/settings.local.json` or unmanaged user files.

## Project Layout

```text
Convallaria/
├── .codex-plugin/
│   └── plugin.json
├── assets/
│   └── brand/
│       └── convallaria-mark.png
├── AGENTS.md
├── CLAUDE.md
├── claude/
│   └── commands/
├── scripts/
│   ├── conva.py
│   ├── smoke_test.py
│   └── update_convallaria.py
└── skills/
    └── convallaria/
        ├── SKILL.md
        ├── routing.md
        ├── agents/
        ├── shared/
        ├── scripts/
        │   └── route_task.py
        └── subskills/
            ├── audit/
            ├── concept/
            ├── images/
            ├── logo/
            ├── refine/
            └── tokens/
```

`.claude/` is a generated local Claude Code adapter directory created by `scripts/conva.py sync`; it is intentionally ignored by git. The Claude Code guide lives at root `CLAUDE.md`, and command adapter sources live under `claude/commands/`.

## Language Policy

Convallaria project files, templates, references, examples, and durable deliverables are authored in English. If a consuming project explicitly requires localization, keep the Convallaria source of truth in English and treat localized copies as secondary exports.

## Design Philosophy

Convallaria treats design as both atmosphere and system.

Good agentic design work should be able to hold feeling, constraints, source files, tokens, exports, manifests, and handoff in one continuous thread. The goal is not to replace a designer's judgment. The goal is to give AI-assisted design work a better studio: one where taste is observable, assets are traceable, and delivery is not an afterthought.

## License

MIT License. See [LICENSE](LICENSE) for the full text.
