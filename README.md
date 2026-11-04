# proxy-configs public rules

This repository contains the public Surge strategy template and application routing rules. Server addresses, node passwords, airport subscription links, and personal `[Host]` mappings remain in the separate private runtime profile.

## Layout

- `Surge/CoreVision_Surge.conf`: original `[General]` settings, application policy groups, and the ordered `[Rule]` references. The former `routing.dconf` has been merged into this file.
- `Surge/rules/*.list`: custom matchers classified by application or function. Maintained public upstream sets are linked directly from the main profile.

## Applications and order

Apple Intelligence and local direct exceptions are evaluated first. AI rules precede Google rules so dedicated AI traffic keeps its policy. The main applications are Apple, AI, YouTube, Google, Microsoft, BiliBili, Netflix, Disney, HBO, TikTok, Telegram, Steam, Epic, Xbox, PlayStation, Cryptocurrency, and GlobalScholar. Unmatched foreign services use `ForeignMedia`; China and local direct rules have separate lists. The final policy is `漏网之鱼`.

Each application group offers automatic selection, manual selection, Hong Kong, US, Japan, Taiwan, Singapore, static IP, and direct routing. The runtime's `[Proxy]` section supplies the actual nodes. A public profile alone has no purchased nodes.

The rule migration deduplicated exact local matchers, removed custom app matchers already covered by the same application's maintained public set, and retained custom process, IP, and domain rules that the upstream sets did not cover. When an upstream set changes, review overlaps before changing the custom lists.

The airport issues short-lived links, so the private node snapshot is refreshed only when a valid link is available. An unsuccessful refresh preserves the last working private profile.
