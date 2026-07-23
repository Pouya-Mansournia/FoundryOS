# GIF Storyboard

Status: **frames 1 & 3 rendered** as `images/demo.gif` (hand-built terminal typing animation, no chat UI needed for those two beats). Frames 2 and 4–10 are still **prompt-only** — they require a real chat-interface screen recording, not something an image generator or hand-built SVG can produce. Full context lives in [`docs/SHOWCASE.md`](../../docs/SHOWCASE.md#4-gif-storyboard) — this file extracts the storyboard so it can be handed to whoever records the rest.

10 seconds, 10 frames, ~1s each. Production note: screen-record a real session (terminal + a generic AI chat interface) rather than fully fabricating UI in a design tool — it'll look more credible and takes less effort than building 10 mockups from scratch. Capture with any screen recorder, trim and convert with `ffmpeg` or a GIF-specific tool (Kap, Gifski), keep it under ~3MB so it loads fast in a README.

| # | Frame | On-screen content | Caption |
|---|---|---|---|
| 1 | Terminal | `git clone https://github.com/<you>/FoundryOS.git` typed and run | — |
| 2 | File browser / upload dialog | Repository folder dragged into a generic AI assistant's project/upload panel | "Drop it into your AI assistant" |
| 3 | Chat input | User types `/cpo Build a SaaS startup` | — |
| 4 | Meta-Agent badge | A small "Meta-Agent: classifying..." indicator pulses in indigo | "Meta-Agent activates" |
| 5 | Agent badges | CPO-Agent badge appears (and CTO/CRO if multi-agent) with a brief highlight animation | "Agents selected" |
| 6 | Skill chips | 4–5 skill-name chips fade in under the agent badge | "Skills selected" |
| 7 | Roadmap card | A 3-phase roadmap card slides/fades into view | "Roadmap" |
| 8 | PRD card | A PRD card appears beside or below it | "PRD" |
| 9 | Metrics card | A small KPI scorecard appears | "Metrics" |
| 10 | Success card | All cards settle, a green checkmark and closing line appear | **"Built with FoundryOS"** |

**Brand-focused variant (`demo-brand.gif`):** swap frame 3's command for `/brand Define our name, logo, and voice` and frame 5's badge for a single magenta CBO-Agent badge — same 10-beat structure, useful as a second GIF if the README wants to show the brand layer specifically rather than only product/technical work.

---

Once recorded, save as `assets/images/demo.gif` (and `demo-brand.gif` for the variant) and wire into README near the top, above or beside the architecture diagram.
