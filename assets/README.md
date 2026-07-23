# Assets

This folder is split into two halves, depending on whether the asset could be precisely hand-built from [`docs/SHOWCASE.md`](../docs/SHOWCASE.md)'s own specs or genuinely needs an AI image generator, screen recording, or a designer.

`docs/SHOWCASE.md` remains the **master showcase reference** — the full design language (colors, type, the legal note on not reproducing real products' logos), the original Mermaid/ASCII architecture diagram source, and every prompt's complete context live there. Nothing in this folder replaces it; this folder is the execution layer underneath it.

## `images/` — real, rendered files

These are actual PNGs, generated from SHOWCASE.md's exact specs (colors, layout, dimensions) via hand-built SVG rendered to PNG — not placeholders, not AI-generated, but real assets usable today.

| File | Source | Notes |
|---|---|---|
| `foundryos-architecture-dark.png` | Section 1 | 1600×1550, 5×3 grid + Brand Intelligence + Final Output rows, dark theme |
| `foundryos-architecture-light.png` | Section 1 | Same composition, light theme, for light-mode READMEs/docs sites |
| `foundryos-banner-dark.png` | Section 2 | README header strip, dark theme |
| `foundryos-banner-light.png` | Section 2 | Same composition, light theme |
| `social-preview.png` | Section 7 | 1280×640, includes the `Modules`/`Skills`/`Agents`/`Workflows`/`Brand` pill row — upload via GitHub *Settings → General → Social preview* (not auto-read from the repo) |
| `github-banner.png` | Section 2 | 1280×640, shares the banner's visual language without the pill row |
| `logo-primary.png` | Section 8 | 512×512, transparent, dark-slate nodes + indigo emphasis — legible on **light** backgrounds |
| `logo-on-dark.png` | Section 8 | 512×512, transparent, white nodes + indigo emphasis — for placement on **dark** surfaces (this repo's own banner/social preview) |
| `logo-monochrome.png` | Section 8 | 512×512, transparent, single flat dark color — print/letterhead/watermark use |
| `logo-favicon.png` | Section 8 | 64×64, dark rounded-square backdrop so it stays legible in any browser tab theme |
| `demo.gif` | `gif-storyboard.md` (terminal-only cut) | 900×560, ~22s, hand-rendered typing animation of the actual `/gtm` "See It In Action" run — generic terminal chrome, no real product UI, same design tokens as the diagrams above. Wired into the top of `README.md`. |
| `layer-stack-dark.svg` / `.png` | `README.md`'s Architecture section (not a SHOWCASE.md section — see note below) | 680×1060, the 14-layer **layer-inventory** stack (Modules → ... → MCP Layer → Artifacts), dark theme only. The `MCP Layer` node renders with a dashed border to flag its v5.0.0-preview.1 declaration-only status at a glance. |

Why these and not the others: each is a composition of rectangles, text, simple node-graph shapes, and flat color — fully specified in SHOWCASE.md down to hex values and pixel dimensions, so it could be rendered correctly without guessing at content. `demo.gif` follows the same rule: it's real terminal text and cursor motion, not a fabricated chat UI, so it could be built the same honest way as the static PNGs instead of requiring an actual screen recording.

**Note on `layer-stack-dark`:** don't confuse this with `foundryos-architecture-dark.png` above — that one renders SHOWCASE.md Section 1's **request-flow view** (top-down, what happens when a user runs a command). `layer-stack-dark` renders the separate **layer-inventory view** (bottom-up, what exists) from `README.md`'s own Architecture ASCII diagram, which SHOWCASE.md explicitly distinguishes as "same system, two honest framings, used for two different jobs." It isn't wired into `README.md` itself (which keeps the ASCII version inline for zero-dependency rendering on GitHub) — it's a supplementary visual for anyone who wants an image instead.

## `prompts/` — prompt and storyboard files, not yet rendered

These need either an actual AI image generator, a screen recording, or a designer — not something that should be faked with hand-drawn shapes, since the result would look obviously synthetic (illustrative scenes, real UI mockups with specific data, or motion/video content).

| File | What it's for |
|---|---|
| `screenshot-prompts.md` | The 4 README screenshot mockups (`/cpo`, `/robotics`, `/gtm`, `/brand`) — specific card layouts and data, best done with an image model or quick design-tool pass |
| `gif-storyboard.md` | The full 10-frame, 10-second, multi-app GIF (terminal → AI assistant chat UI) — the terminal-only beat (frames 1 and 3) now ships as `images/demo.gif`; frames 2 and 4–10, which require a real chat-interface screen recording, are still a production plan |
| `demo-storyboard.md` | The 30-second, 10-scene demo video — a screen-recording + edit production plan |
| `hero-image-prompts.md` | The 2 large illustrative hero images ("One coherent answer," "Brand runs through everything") — mood-setting scenes, not diagrams |
| `logo-prompts.md` | The original AI-generation prompt for the logo mark, kept as an alternative even though a real hand-built version already ships in `images/` |

Once any of these gets rendered, drop the result into `images/` under the filename referenced in that prompt file (each prompt file says where it goes), and update this table.

## Why the split

A project claiming "world-class GitHub repository" shouldn't ship ten broken image links, but it also shouldn't fake illustrative content with crude shapes just to claim every box is checked. Diagrammatic, fully-specified assets got built for real. Everything that needs actual creative production stayed honest as a prompt — usable immediately by anyone with an image model or five minutes with a screen recorder, and clearly labeled so nobody mistakes a prompt file for a missing deliverable.
