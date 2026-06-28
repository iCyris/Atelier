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

Convallaria is an agentic design suite for turning loose product or brand intent into a coherent identity system: brand direction, logo guidance, implementation tokens, visual QA, optimized assets, manifests, and handoff notes.

It behaves less like a prompt collection and more like a small design studio for agents. The parent skill routes the brief, loads the focused subskill, uses deterministic scripts for fragile asset work, and leaves behind files another designer, engineer, or agent can continue.

## Skills

Each design operation lives as a focused subskill. Use the parent `convallaria` skill to route mixed requests, or jump directly to the relevant subskill when the task is clear.

| Subskill | When | What it does |
| --- | --- | --- |
| `concept` | Starting from a product idea, audience, name, tone, or mood | Creates positioning, voice, visual territories, brand strategy, anti-patterns, and a production direction. |
| `pack` | A complete brand system is needed | Coordinates concept, logo, tokens, exports, manifest, and handoff into one coherent brand package. |
| `refine` | Existing visuals need to become a design system | Extracts color, type, spacing, component rules, tokens, and an HTML report from screenshots, sites, code, docs, or mood references. |
| `logo` | Marks, wordmarks, favicons, app icons, or platform exports are needed | Produces logo system guidance, SVG source rules, clear-space rules, variants, and raster export plans. |
| `images` | Bitmap assets need delivery preparation | Compresses, converts, resizes, strips metadata, and records responsive image variants. |
| `tokens` | Brand or design decisions need implementation files | Converts decisions into CSS variables, JSON tokens, Tailwind extensions, and TypeScript theme files. |
| `audit` | A UI needs visual QA against a brand or design system | Reviews screenshots, implementations, tokens, responsive states, and design drift. |
| `export` | Files need packaging for another designer, engineer, or agent | Builds manifests, handoff notes, source-of-truth maps, and final package structure. |

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

- syncs Claude Code guide and slash-command adapters into `.claude/`
- refreshes Codex plugin metadata in `.codex-plugin/plugin.json`
- runs the smoke test by default
- prints the next local Codex plugin command when it can infer one

For Claude Code, use the synced slash commands:

```text
/conva
/conva-brand
/conva-logo
/conva-refine
/conva-optimize
```

For Codex, use the local plugin entry that points at this checkout. The plugin manifest exposes `skills/`, and the main skill is `skills/convallaria/SKILL.md`.

For other AI coding tools, point the agent at:

```text
AGENTS.md
skills/convallaria/SKILL.md
```

Then ask it to route to the relevant subskill under `skills/convallaria/subskills/`.

## Use

Starter prompts:

```text
Use Convallaria to create a complete brand pack for this product idea.
Use Convallaria to turn these screenshots into a design system.
Use Convallaria to produce logo exports and a handoff manifest.
Use Convallaria to QA this UI against the attached brand system.
```

Route a request manually:

```bash
cd skills/convallaria
python3 scripts/route_task.py "create a complete brand pack from positioning to logo, tokens, and handoff assets"
```

Common deterministic asset commands:

```bash
cd skills/convallaria
python3 subskills/logo/scripts/rasterize_svg.py logo/source/logo.svg --out logo/png --sizes 16 32 64 128 256 512 1024
python3 subskills/images/scripts/optimize_images.py input.png --out images --formats webp jpeg --max-width 1600 --quality 82
python3 subskills/export/scripts/validate_outputs.py asset-manifest.json
```

The SVG rasterizer uses CairoSVG when available, then falls back to `rsvg-convert`, Inkscape, or macOS QuickLook when available.

## Chaining Skills

Convallaria subskills can be chained, but each transition should be intentional. A good run names the next source of truth before moving on.

Common workflows:

```text
brand idea -> pack -> concept -> logo -> tokens -> export
```

```text
screenshots -> refine -> DESIGN.md -> tokens -> audit
```

```text
source SVG -> logo -> raster export -> images -> export
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

Skip the smoke test only when you are intentionally doing a metadata-only sync:

```bash
python3 scripts/conva.py update --no-smoke
```

## Uninstall

Remove generated local Claude Code adapters:

```bash
python3 scripts/conva.py uninstall
```

The uninstall command only removes generated Claude Code files that still match their tracked source files. It does not delete `.claude/settings.local.json` or other local user settings.

Remove the Codex plugin entry separately from the local marketplace or plugin manager that points at this checkout.

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
        ├── scripts/
        │   └── route_task.py
        └── subskills/
            ├── audit/
            ├── concept/
            ├── export/
            ├── images/
            ├── logo/
            ├── pack/
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
