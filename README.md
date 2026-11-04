# proxy-configs public rules

This repository contains the public Surge strategy template and application routing rules. Server addresses, node passwords, airport subscription links, and personal `[Host]` mappings remain in the separate private runtime profile.

## Layout

- `Surge/CoreVision_Surge.conf`: original `[General]` settings, application policy groups, and the ordered `[Rule]` references. The former `routing.dconf` has been merged into this file.
- `Surge/custom/*.list`: original custom matchers, kept as the editable source.
- `Surge/rules/*.list`: merged application rule files. The main profile references only these files in this repository.
- `scripts/sync_rules.py`: downloads the selected blackmatrix7 Surge lists, merges them with the custom source, removes exact duplicates and domain rules covered by a broader suffix in the same category, and writes the merged lists with `--write`.

## Applications and order

Local direct exceptions are evaluated first. Apple Intelligence exceptions are merged into `Apple.list`, and AI rules precede Google rules so dedicated AI traffic keeps its policy. The main applications are Apple, AI, YouTube, Google, Microsoft, BiliBili, Netflix, Disney, HBO, TikTok, Telegram, Steam, Epic, Xbox, PlayStation, Cryptocurrency, and GlobalScholar. Unmatched foreign services use `ForeignMedia`; China and local direct rules have separate lists. The final policy is `漏网之鱼`.

Each application group offers automatic selection, manual selection, Hong Kong, US, Japan, Taiwan, Singapore, static IP, and direct routing. The runtime's `[Proxy]` section supplies the actual nodes. The private `aicorevision/proxy-configs` repository now has `Surge/CoreVision_Surge_next.conf` with the initial 59-node snapshot and references to this public profile. Subscribe to the private runtime profile to use the purchased nodes; the public profile is a reusable strategy and rule source.

The merged catalog currently has 20 categories with no duplicate exact matchers. It retains custom process, IP, and domain rules not covered by the selected upstream sets. GitHub Actions checks the upstream sources daily; when a check reports drift, review the diff and run `python3 scripts/sync_rules.py --write` to publish an updated snapshot.

The airport issues short-lived links, so the private node snapshot is refreshed only when a valid link is available. An unsuccessful refresh preserves the last working private profile.
