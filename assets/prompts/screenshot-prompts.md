# README Screenshot Prompts

Status: **prompt-only** — these need either an AI image generator or a quick UI mockup pass in a design tool, since they depict specific card layouts and data, not a diagrammatic composition that can be hand-built from primitives. Full context (shared design language, legal note on not reproducing real product UIs) lives in [`docs/SHOWCASE.md`](../../docs/SHOWCASE.md#3-readme-screenshot-prompts) — this file extracts just the four prompts so they can be handed to an image model or designer one at a time.

**Shared frame for all four:** a generic dark chat interface (rounded window, no real product's chrome) with a command typed at the top and a structured **Meta-Agent Result** rendered below it as collapsible cards (not a wall of text) — the same nine-section shape documented in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Canvas: 1920×1080 (16:9). Background `#0B0E14`, indigo `#7C5CFF` accents, per the shared design-language table in `docs/SHOWCASE.md`.

---

## 1. `cpo-saas.png` — `/cpo Build a SaaS startup`

> Command bar shows `/cpo Build a SaaS startup` in monospace with a small CPO-Agent badge (indigo). Below it, four result cards in a 2×2 grid: **Selected Agents & Skills** (CPO-Agent · Discovery, Market Sizing, PRD, Product Scorecard), **Roadmap** (a condensed 3-phase horizontal timeline), **PRD** (a scrollable card showing Problem Statement / ICP / Requirements headers, text truncated with a fade), **Metrics** (a small scorecard with 3–4 KPI tiles, e.g. activation rate, retention, NPS placeholders — generic numbers, not real benchmarks). A green "Generated in 1 pass" tag in a corner.

## 2. `robotics-warehouse.png` — `/robotics Design a warehouse robot`

> Command bar shows `/robotics Design a warehouse robot` with a multi-agent badge row (CPO · CIO · CTO · COO · CFO — five small indigo pills). Below it, five result cards: **Mechanical Architecture** (a simplified isometric robot wireframe icon, not a real CAD render), **Electronics** (a small block diagram: sensors → controller → actuators), **Embedded** (a code-adjacent card showing a firmware module list), **Manufacturing** (a horizontal NPI stage-gate strip: DVT → PVT → MP), **Roadmap** (timeline card). Layout: a 3-column masonry grid since five cards don't divide evenly into a clean grid otherwise.

## 3. `gtm-launch.png` — `/gtm Create a launch strategy`

> Command bar shows `/gtm Create a launch strategy` with CRO-Agent + CMO-Agent badges. Below it, four cards: **Channels** (a small horizontal bar chart comparing 4 generic channel types — paid, organic, partner, sales-led — placeholder values), **Messaging** (a card with a one-line positioning statement and 3 supporting bullets), **Pricing** (a 3-tier pricing card, generic tier names like "Starter / Growth / Enterprise"), **Metrics** (funnel visualization: Awareness → Consideration → Conversion → Retention, with a conversion-rate label at each step). 2×2 grid, same visual weight as Example 1 for series consistency.

## 4. `brand-identity.png` — `/brand Define our naming and identity`

> Command bar shows `/brand Define our naming and identity` with a single CBO-Agent badge in magenta (`#C026D3`) instead of indigo, visually flagging this as the brand layer rather than a core domain Agent. Below it, four cards: **Archetype & Naming** (a card showing one chosen brand archetype, e.g. "The Pioneer," next to a shortlist of 3 generic placeholder names with one struck through and marked "trademark conflict — rejected"), **Positioning** (a one-line positioning statement card, same visual treatment as the Messaging card in Example 3 for series consistency), **Logo System** (a small grid of 3 abstract placeholder glyph variations — primary mark, monochrome, favicon-scale — not a finished logo, clearly labeled "concepts"), **Voice** (a small card listing 3 tone adjectives, e.g. "direct, technical, unhyped," plus one example banned phrase struck through). 2×2 grid, same dimensions as the other three examples so the four screenshots read as one consistent set when placed side by side in the README.

---

Once rendered, drop the four files in this same `assets/prompts/` sibling location — `assets/images/screenshots/cpo-saas.png`, `robotics-warehouse.png`, `gtm-launch.png`, `brand-identity.png` — and wire them into README's Screenshots section in place of the "Coming soon" note.
