# Public proxy rules

This repository publishes application routing rules for Surge and Clash/Mihomo. It contains no proxy nodes or vendor subscription URLs. Runtime profiles and their policy groups are maintained in the private `aicorevision/proxy-configs` repository.

## Layout

- `Surge/custom/*.list`: editable rules carried over from the original profiles.
- `Surge/rules/*.list`: published application lists, merged with selected blackmatrix7 sources.
- `Clash/rules/*.yaml`: matching Mihomo rule-provider files generated from the Surge lists.
- `scripts/sync_rules.py`: updates and deduplicates the Surge lists.
- `scripts/build_clash_rules.py`: generates the Clash lists.
- `.github/workflows/check-rules.yml`: checks rule drift and parity.

The private Surge and Clash runtime profiles reference these public rule files directly. The main categories are Apple, AI, YouTube, Google, Microsoft, BiliBili, Netflix, Disney, HBO, TikTok, Telegram, Steam, Epic, Xbox, PlayStation, Cryptocurrency, and GlobalScholar. Unmatched foreign traffic uses `ForeignMedia`; China and local direct traffic have separate lists.

The catalog has 20 categories. The two clients share 5,125 ordered matchers. Surge retains 47 extra `USER-AGENT`, `URL-REGEX`, or `OR` rules that do not have equivalent generated Clash rules. Run `python3 scripts/sync_rules.py --write` and `python3 scripts/build_clash_rules.py --write` to publish reviewed upstream updates.
