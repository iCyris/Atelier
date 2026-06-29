#!/usr/bin/env python3
"""Validate a Convallaria asset manifest and referenced outputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_KEYS = {"schema", "project", "inputs", "outputs"}


def validate_manifest(path: Path) -> list[str]:
    errors = []
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Cannot read JSON: {exc}"]

    missing = REQUIRED_KEYS - set(manifest)
    if missing:
        errors.append(f"Missing required keys: {', '.join(sorted(missing))}")

    base = path.parent
    outputs = manifest.get("outputs", [])
    if not isinstance(outputs, list):
        errors.append("`outputs` must be a list.")
        return errors

    for index, output in enumerate(outputs):
        if not isinstance(output, dict):
            errors.append(f"outputs[{index}] must be an object.")
            continue
        output_path = output.get("path")
        if not output_path:
            errors.append(f"outputs[{index}] is missing `path`.")
            continue
        candidate = (base / output_path).resolve()
        if not candidate.exists():
            errors.append(f"Missing output file: {output_path}")
            continue
        if not candidate.is_file():
            continue
        if candidate.stat().st_size == 0:
            errors.append(f"Output file is empty: {output_path}")
            continue
        if candidate.suffix.lower() == ".json":
            try:
                json.loads(candidate.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"Output JSON is invalid: {output_path}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    errors = validate_manifest(args.manifest)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"ok: {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
