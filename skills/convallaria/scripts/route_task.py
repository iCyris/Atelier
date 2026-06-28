#!/usr/bin/env python3
"""Suggest Convallaria subskill routes for a user request."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    name: str
    resource: str
    outputs: list[str]
    keywords: list[str]


ROUTES = [
    Route(
        "pack",
        "subskills/pack/SKILL.md",
        ["BRAND.md", "LOGO_SPEC.md", "tokens/", "logo/", "asset-manifest.json", "handoff/"],
        [
            "complete brand",
            "brand pack",
            "brand kit",
            "identity system",
            "from brand to assets",
            "end to end",
            "deliverable assets",
            "brand generation",
            "brand system",
        ],
    ),
    Route(
        "refine",
        "subskills/refine/SKILL.md",
        ["DESIGN.md", "report.html"],
        [
            "design system",
            "design refine",
            "extract",
            "reverse engineer",
            "screenshot",
            "website style",
            "tokens from",
            "formalize",
        ],
    ),
    Route(
        "concept",
        "subskills/concept/SKILL.md",
        ["BRAND.md"],
        [
            "brand",
            "identity",
            "positioning",
            "naming",
            "moodboard",
            "visual direction",
            "personality",
        ],
    ),
    Route(
        "logo",
        "subskills/logo/SKILL.md",
        ["LOGO_SPEC.md", "logo/"],
        [
            "logo",
            "wordmark",
            "mark",
            "favicon",
            "app icon",
            "svg",
            "lockup",
        ],
    ),
    Route(
        "images",
        "subskills/images/SKILL.md",
        ["images/", "image-manifest.json"],
        [
            "compress",
            "optimize image",
            "webp",
            "avif",
            "resize",
            "metadata",
            "responsive image",
        ],
    ),
    Route(
        "tokens",
        "subskills/tokens/SKILL.md",
        ["tokens/"],
        [
            "css variables",
            "tailwind",
            "style dictionary",
            "theme.ts",
            "tokens.json",
            "design token",
        ],
    ),
    Route(
        "audit",
        "subskills/audit/SKILL.md",
        ["DESIGN_QA.md", "screenshots/"],
        [
            "visual qa",
            "audit",
            "compare",
            "responsive check",
            "design drift",
            "screenshot check",
        ],
    ),
    Route(
        "export",
        "subskills/export/SKILL.md",
        ["asset-manifest.json", "brand-pack/"],
        [
            "package",
            "handoff",
            "brand pack",
            "manifest",
            "zip",
            "deliver",
        ],
    ),
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def score_route(route: Route, text: str) -> int:
    score = 0
    for keyword in route.keywords:
        key = keyword.lower()
        if key in text:
            score += 3 if " " in key else 1
    return score


def suggest_routes(text: str) -> list[dict[str, object]]:
    normalized = normalize(text)
    scored = []
    for route in ROUTES:
        score = score_route(route, normalized)
        if score:
            scored.append(
                {
                    "route": route.name,
                    "score": score,
                    "resource": route.resource,
                    "outputs": route.outputs,
                }
            )
    scored.sort(key=lambda item: (-int(item["score"]), str(item["route"])))
    if not scored:
        scored.append(
            {
                "route": "routing",
                "score": 0,
                "resource": "routing.md",
                "outputs": ["task plan"],
            }
        )
    return scored


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", nargs="+", help="User request text to classify")
    args = parser.parse_args()
    request = " ".join(args.request)
    print(json.dumps({"request": request, "suggestedRoutes": suggest_routes(request)}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
