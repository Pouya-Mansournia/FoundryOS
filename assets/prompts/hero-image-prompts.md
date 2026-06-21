# Hero Image Prompts

Status: **prompt-only** — these are large, illustrative mood-setting images, not diagrammatic compositions. They're deliberately left as prompts for an AI image generator (or a designer) rather than hand-built from SVG primitives, since getting an illustrative scene to look intentional rather than crude needs an actual image model. Full context lives in [`docs/SHOWCASE.md`](../../docs/SHOWCASE.md#9-hero-images) — this file extracts the two prompts.

Two larger illustrative images, distinct from the architecture diagram (which is informational, and which *is* rendered for real — see `assets/images/foundryos-architecture-dark.png`). These are used at the very top of the README, above the fold, and optionally on a project landing page.

---

## 1. `hero-one-answer.png` — "One coherent answer"

> A wide hero illustration (2400×1000) on `#0B0E14`. Left third: a scattered, slightly chaotic cluster of small gray text fragments and disconnected dots, suggesting nine or ten separate, unrelated answers — labeled faintly underneath, small and muted: "before." Right two-thirds: the same elements pulled into a single clean, organized vertical card stack (echoing the Meta-Agent Result cards from the screenshot prompts), glowing softly in indigo, labeled "after." A single thin indigo line sweeps left to right connecting the two halves, narrowing as it crosses the canvas — visually compressing chaos into order. No text other than the two small "before" / "after" labels — let the composition carry the meaning.

## 2. `hero-brand-thread.png` — "Brand runs through everything"

> A wide hero illustration (2400×1000) on `#0B0E14`, structured as a cutaway/cross-section rather than a left-right split. A vertical stack of six thin horizontal bands (representing Modules, Skills, Agents, Workflows, Memory, Knowledge Graph) in muted slate gray, each band slightly transparent. A single magenta (`#C026D3`) ribbon weaves through all six bands at a slight diagonal, visibly passing *through* each one rather than sitting beside the stack — this is the visual argument for "brand isn't bolted on, it threads through every layer." At the bottom, the ribbon gathers into a small cluster of finished-looking outputs: a tiny logo mark, a tiny color swatch row, a tiny text snippet in a distinct typeface — concrete artifacts, not abstract icons. No labels needed if the composition reads clearly; if labels are added, keep them to the six band names in small monospace type along the left edge only.

---

Once rendered, save under `assets/images/` as `hero-one-answer.png` and `hero-brand-thread.png`, and place Hero 1 at the top of README above the fold. Hero 2 is optional — use it if the README wants to make the brand-integration argument visually rather than only in prose.
