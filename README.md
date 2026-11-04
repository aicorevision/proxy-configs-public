# proxy-configs public rules

This repository contains the public Surge and Clash strategy templates, application routing rules, and reusable Surge modules. Server addresses, node passwords, airport subscription links, controller secrets, and personal `[Host]` mappings remain in the separate private runtime repository.

## Layout

- `Surge/CoreVision_Surge.conf`: original `[General]` settings, application policy groups, and the ordered `[Rule]` references. The former `routing.dconf` has been merged into this file.
- `Surge/custom/*.list`: original custom matchers, kept as the editable source.
- `Surge/rules/*.list`: merged application rule files. The main profile references only these files in this repository.
- `scripts/sync_rules.py`: downloads the selected blackmatrix7 Surge lists, merges them with the custom source, removes exact duplicates and domain rules covered by a broader suffix in the same category, and writes the merged lists with `--write`.
- `Clash/CoreVision_Clash.template.yaml`: the same application groups and route order in Mihomo format, without nodes or controller secrets.
- `Clash/rules/*.yaml`: generated from the canonical Surge lists by `scripts/build_clash_rules.py`.

## Applications and order

Local direct exceptions are evaluated first. Apple Intelligence exceptions are merged into `Apple.list`, and AI rules precede Google rules so dedicated AI traffic keeps its policy. The main applications are Apple, AI, YouTube, Google, Microsoft, BiliBili, Netflix, Disney, HBO, TikTok, Telegram, Steam, Epic, Xbox, PlayStation, Cryptocurrency, and GlobalScholar. Unmatched foreign services use `ForeignMedia`; China and local direct rules have separate lists. The final policy is `漏网之鱼`.

Each application group offers automatic selection, manual selection, Hong Kong, US, Japan, Taiwan, Singapore, static IP, and direct routing. The runtime's `[Proxy]` section supplies the actual nodes. The private `aicorevision/proxy-configs` repository now has `Surge/CoreVision_Surge_next.conf` with the initial 59-node snapshot and references to this public profile. Subscribe to the private runtime profile to use the purchased nodes; the public profile is a reusable strategy and rule source.

The merged catalog has 20 categories with no duplicate exact matchers. Surge and Clash share 5,125 ordered matchers. Surge retains 47 additional rules using `USER-AGENT`, `URL-REGEX`, or `OR`, which are not converted automatically because the client semantics differ. It retains custom process, IP, and domain rules not covered by the selected upstream sets. GitHub Actions checks the upstream sources and generated Clash files daily; when a check reports drift, review the diff, run `python3 scripts/sync_rules.py --write`, then `python3 scripts/build_clash_rules.py --write` to publish updated snapshots.

The airport issues short-lived links, so the private node snapshot is refreshed only when a valid link is available. An unsuccessful refresh preserves the last working private profile.
