#!/usr/bin/env python3
"""Generate implementation token files from a structured Convallaria token spec."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


TOKEN_REF_RE = re.compile(r"^\{([^{}]+)\}$")


def load_spec(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError("Token spec must be a JSON object.")
    tokens = data.get("tokens")
    if not isinstance(tokens, dict) or not tokens:
        raise RuntimeError("Token spec must include a non-empty `tokens` object.")
    return data


def flatten_tokens(value: Any, prefix: tuple[str, ...] = ()) -> dict[tuple[str, ...], Any]:
    if isinstance(value, dict):
        flattened: dict[tuple[str, ...], Any] = {}
        for key, child in value.items():
            if not isinstance(key, str) or not key:
                raise RuntimeError("Token keys must be non-empty strings.")
            flattened.update(flatten_tokens(child, prefix + (key,)))
        return flattened
    if isinstance(value, (str, int, float)) or isinstance(value, bool):
        return {prefix: value}
    raise RuntimeError(f"Unsupported token value at {'.'.join(prefix)}: {value!r}")


def css_name(path: tuple[str, ...]) -> str:
    return "--" + "-".join(part.replace("_", "-") for part in path)


def css_value(value: Any) -> str:
    if isinstance(value, str):
        match = TOKEN_REF_RE.match(value)
        if match:
            return f"var({css_name(tuple(match.group(1).split('.')))})"
        return value
    return str(value).lower() if isinstance(value, bool) else str(value)


def nested_set(root: dict[str, Any], path: tuple[str, ...], value: Any) -> None:
    cursor = root
    for part in path[:-1]:
        cursor = cursor.setdefault(part, {})
    cursor[path[-1]] = value


def tailwind_group(tokens: dict[tuple[str, ...], Any], category: str) -> dict[str, Any]:
    grouped: dict[str, Any] = {}
    for path, value in sorted(tokens.items()):
        if not path or path[0] != category:
            continue
        nested_set(grouped, path[1:], css_value(value))
    return grouped


def write_tokens_json(path: Path, spec: dict[str, Any], tokens: dict[tuple[str, ...], Any]) -> None:
    output = {
        "schema": "convallaria.tokens.v1",
        "project": spec.get("project", {}),
        "tokens": {".".join(key): value for key, value in sorted(tokens.items())},
        "notes": spec.get("notes", []),
    }
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


def write_css(path: Path, tokens: dict[tuple[str, ...], Any]) -> None:
    lines = [":root {"]
    for key, value in sorted(tokens.items()):
        lines.append(f"  {css_name(key)}: {css_value(value)};")
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_tailwind(path: Path, tokens: dict[tuple[str, ...], Any]) -> None:
    theme = {
        "colors": tailwind_group(tokens, "color"),
        "spacing": tailwind_group(tokens, "space"),
        "borderRadius": tailwind_group(tokens, "radius"),
        "fontFamily": tailwind_group(tokens, "font"),
        "transitionDuration": tailwind_group(tokens, "motion"),
    }
    text = "module.exports = {\n  theme: {\n    extend: "
    text += json.dumps(theme, indent=6)
    text += "\n  }\n};\n"
    path.write_text(text, encoding="utf-8")


def write_theme_ts(path: Path, spec: dict[str, Any]) -> None:
    text = "export const theme = "
    text += json.dumps(spec.get("tokens", {}), indent=2)
    text += " as const;\n"
    path.write_text(text, encoding="utf-8")


def write_report(path: Path, spec: dict[str, Any], tokens: dict[tuple[str, ...], Any]) -> None:
    project = spec.get("project", {})
    name = project.get("name", "Convallaria Tokens") if isinstance(project, dict) else "Convallaria Tokens"
    categories = sorted({key[0] for key in tokens})
    lines = [
        f"# {name} Token Report",
        "",
        "## Generated Files",
        "",
        "- `tokens.json`",
        "- `tokens.css`",
        "- `tailwind.extend.js`",
        "- `theme.ts`",
        "",
        "## Categories",
        "",
    ]
    for category in categories:
        count = sum(1 for key in tokens if key[0] == category)
        lines.append(f"- `{category}`: {count} tokens")
    notes = spec.get("notes", [])
    if notes:
        lines.extend(["", "## Notes", ""])
        for note in notes:
            lines.append(f"- {note}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate(spec_path: Path, out_dir: Path) -> list[Path]:
    spec = load_spec(spec_path)
    tokens = flatten_tokens(spec["tokens"])
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = [
        out_dir / "tokens.json",
        out_dir / "tokens.css",
        out_dir / "tailwind.extend.js",
        out_dir / "theme.ts",
        out_dir / "tokens.report.md",
    ]
    write_tokens_json(outputs[0], spec, tokens)
    write_css(outputs[1], tokens)
    write_tailwind(outputs[2], tokens)
    write_theme_ts(outputs[3], spec)
    write_report(outputs[4], spec, tokens)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Path to a tokens-spec.json file.")
    parser.add_argument("--out", type=Path, default=Path("tokens"), help="Output directory.")
    args = parser.parse_args()

    try:
        outputs = generate(args.spec, args.out)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps({"outputs": [str(path) for path in outputs]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
