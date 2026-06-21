# Demo Video Storyboard

Status: **prompt-only** — a video production plan (screen recording + edit), not something an image generator produces. Full context lives in [`docs/SHOWCASE.md`](../../docs/SHOWCASE.md#5-demo-video-storyboard) — this file extracts the storyboard so it can be handed to whoever cuts the video.

30 seconds, 10 scenes, cinematic dark grade (slightly desaturated, high contrast, the look of a well-produced developer-tool launch video, not a corporate explainer). Suggested audio: a restrained, low-key synth/ambient bed with a soft transition "tick" on each scene cut — no voiceover needed if captions carry the narrative. Export at 1920×1080, H.264 mp4.

| Scene | Duration | Visual | Caption / on-screen text |
|---|---|---|---|
| 1 | 0:00–0:03 | GitHub repository page, slow push-in on the README header | "An operating system for founders." |
| 2 | 0:03–0:06 | Terminal, `git clone` command typed and executed | "Open source. No install." |
| 3 | 0:06–0:09 | Repository dragged into a generic AI assistant's project panel | "Works with the AI assistant you already use." |
| 4 | 0:09–0:13 | Chat input: `/robotics Design a warehouse robot` typed character-by-character | — |
| 5 | 0:13–0:17 | Agent badges cascade in: CPO → CIO → CTO → COO → CFO, each with a brief glow | "Five specialists. One answer." |
| 6 | 0:17–0:21 | Architecture diagram (`assets/images/foundryos-architecture-dark.png`) builds itself node-by-node along the indigo line | "Mechanical. Electronics. Embedded." |
| 7 | 0:21–0:24 | Roadmap card expands into a dated, multi-phase timeline | "A dated plan, not a wall of text." |
| 8 | 0:24–0:26 | Green checkmark, "Built with FoundryOS" card | — |
| 9 | 0:26–0:28 | Quick cut to a GitHub repo page with a star counter animating upward (generic placeholder count, not a real claimed number) | — |
| 10 | 0:28–0:30 | Closing card: logo mark + "FoundryOS" + "Open Source Agentic Operating System" on `#0B0E14` | — |

**Note on Scene 5:** the CPO→CIO→CTO→COO→CFO cascade is specific to the robotics example carried through this storyboard. For a cut that foregrounds Brand OS instead, insert a CBO badge (magenta `#C026D3`, distinct from the indigo core-Agent badges) immediately after CPO — naming and positioning happen right after product definition, before architecture — with the caption changing to "Six specialists. One answer."

---

Once cut, save as `assets/images/demo.mp4` and link from README (GitHub renders an mp4 inline if committed to the repo and referenced directly, or link out to a hosted copy if file size is a concern).
