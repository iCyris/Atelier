---
name: export
description: "Asset export and handoff workflow for packaging multi-file design deliverables, validating manifests, documenting source-of-truth files, and preparing designer, engineer, or agent handoff."
---

# Asset Export Workflow

Use this reference when packaging multi-file design deliverables for another designer, engineer, or agent.

## Package Shape

```text
brand-pack/
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
    ├── developer-handoff.md
    └── ai-agent-prompt.md
```

Only include files that exist and are relevant to the task.

## Manifest

Use `templates/asset-manifest.json` as the base. The manifest should record:

- project metadata
- source inputs and their role
- generated outputs
- producer subskill or script
- assumptions
- unresolved decisions
- recommended next actions

Validate a manifest with:

```bash
python3 subskills/export/scripts/validate_outputs.py asset-manifest.json
```

## Handoff Writing

A good handoff explains:

- what was produced
- what is the source of truth
- how to use the assets
- what should not be changed casually
- what remains open
- which files another agent should read first

Keep handoff writing practical and production-facing.
