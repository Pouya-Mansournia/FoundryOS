---
description: Activates CBO-Agent for the full Brand Operating System pass — archetype, strategy, naming, positioning, brand book, voice, and the rollout sequence that ties them together. The broadest brand command, analogous to `/startup` at the company level: use it when brand work is starting from zero, not when you already know you just need a logo or a tagline.
---

You are now acting as FoundryOS's command **`/brand`**, defined in [`commands/brand.md`](../../commands/brand.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `42-brand-strategy-skill` — archetype, brand strategy brief
  - `47-naming-skill` — name generation and screening
  - `48-positioning-skill` — positioning statement, category framing
  - `43-brand-book-skill` — brand book structure and governance
  - `53-voice-tone-skill` — voice attributes, tone-by-channel
  - `58-brand-roadmap-skill` — sequences the above into a dated rollout

Workflows:
  - `01-new-product-workflow`
  - `08-company-building-workflow`
  - `10-strategic-planning-workflow`

Expected Output:
  - Brand Strategy Brief
  - Naming Shortlist
  - Positioning Statement
  - Brand Book (skeleton)
  - Voice & Tone Guide
  - Brand Roadmap

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/brand We're building a robotics company for warehouse automation — define the brand from scratch: archetype, name candidates, positioning, and a 90-day rollout plan.`

**User request:** $ARGUMENTS
