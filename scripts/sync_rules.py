#!/usr/bin/env python3
"""Merge maintained upstream Surge lists with private-origin custom rules."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1] / "Surge"
UPSTREAM = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge"
SOURCES = {
    "AppleIntelligence": [],
    "LocalDirect": [],
    "AI": ["OpenAI", "Claude", "Gemini"],
    "Apple": ["Apple"],
    "YouTube": ["YouTube"],
    "Google": ["Google"],
    "Microsoft": ["Microsoft"],
    "BiliBili": ["BiliBili"],
    "Netflix": ["Netflix"],
    "Disney": ["Disney"],
    "HBO": ["HBO"],
    "TikTok": ["TikTok"],
    "Telegram": ["Telegram"],
    "Steam": ["Steam"],
    "Epic": ["Epic"],
    "Xbox": ["Xbox"],
    "PlayStation": ["PlayStation"],
    "Cryptocurrency": ["Cryptocurrency"],
    "GlobalScholar": ["GlobalScholar"],
    "ChinaDirect": [],
    "ForeignMedia": [],
}


def entries(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith(("#", "//"))]


def covered_domain(rule: str, suffixes: set[str]) -> bool:
    if not (rule.startswith("DOMAIN,") or rule.startswith("DOMAIN-SUFFIX,")):
        return False
    domain = rule.split(",", 1)[1]
    return any(
        (domain == suffix and rule.startswith("DOMAIN,"))
        or (domain != suffix and domain.endswith("." + suffix))
        for suffix in suffixes
    )


def merge(local: list[str], upstream: list[str], seen: set[str]) -> tuple[list[str], int]:
    candidates = local + upstream
    suffixes = {r.split(",", 1)[1] for r in candidates if re.fullmatch(r"DOMAIN-SUFFIX,[^,]+", r)}
    output = []
    removed = 0
    for rule in candidates:
        if rule in seen or covered_domain(rule, suffixes):
            removed += 1
            continue
        seen.add(rule)
        output.append(rule)
    return output, removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    seen: set[str] = set()
    changed = []
    removed_total = 0
    for name, upstream_names in SOURCES.items():
        custom = ROOT / "custom" / f"{name}.list"
        local = entries(custom.read_text(encoding="utf-8")) if custom.exists() else []
        upstream = []
        for upstream_name in upstream_names:
            url = f"{UPSTREAM}/{upstream_name}/{upstream_name}.list"
            with urlopen(url, timeout=25) as response:
                upstream += entries(response.read().decode("utf-8"))
        merged, removed = merge(local, upstream, seen)
        removed_total += removed
        if not merged:
            raise ValueError(f"empty merged rule set: {name}")
        target = ROOT / "rules" / f"{name}.list"
        content = "\n".join(merged) + "\n"
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            changed.append(name)
            if args.write:
                target.write_text(content, encoding="utf-8")
    print(f"merged {len(SOURCES)} categories; deduplicated {removed_total} entries; changed: {', '.join(changed) or 'none'}")
    return 0 if args.write or not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
