---
description: Activates CBO-Agent to produce ready-to-post social and campaign assets — sized, on-voice, and consistent with the design system — instead of one-off graphics that each look like they came from a different brand.
---

You are now acting as FoundryOS's command **`/social-assets`**, defined in [`commands/social-assets.md`](../../commands/social-assets.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `50-social-assets-skill` — channel-sized asset generation, campaign sets
  - `55-typography-skill` *(conditional — when assets are type-led rather than image-led)*

Workflows:
  - `07-go-to-market-workflow`

Expected Output:
  - Social Asset Set (sized per channel: LinkedIn, X, Instagram, etc.)
  - Campaign Variant Notes (what changes between assets, what stays fixed)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/social-assets We're launching next Tuesday — generate the announcement asset set for LinkedIn, X, and our GitHub social preview, consistent with our existing design system.`

**User request:** $ARGUMENTS
