#!/usr/bin/env python3
"""Generate Mihomo rule providers from the canonical Surge application lists."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
UNSUPPORTED = {"USER-AGENT", "URL-REGEX", "OR"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    changed = []
    skipped = 0
    for surge in sorted((ROOT / "Surge/rules").glob("*.list")):
        rules = []
        for line in surge.read_text(encoding="utf-8").splitlines():
            if not line:
                continue
            if line.split(",", 1)[0] in UNSUPPORTED:
                skipped += 1
                continue
            rules.append(line)
        if not rules:
            raise ValueError(f"no compatible rules in {surge.name}")
        target = ROOT / "Clash/rules" / f"{surge.stem}.yaml"
        content = yaml.safe_dump({"payload": rules}, allow_unicode=True, sort_keys=False, width=120)
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            changed.append(surge.stem)
            if args.write:
                target.write_text(content, encoding="utf-8")
    print(f"Clash rules changed: {', '.join(changed) or 'none'}; Surge-only entries: {skipped}")
    return 0 if args.write or not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
