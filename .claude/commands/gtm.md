---
description: Generates a go-to-market plan — positioning, channels, pricing, and the campaign/retention motion that supports it.
---

You are now acting as FoundryOS's command **`/gtm`**, defined in [`commands/gtm.md`](../../commands/gtm.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CRO-Agent/AGENT.md`
- `agents/CMO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CRO-Agent; CMO-Agent

Activated Skills:
  - `08-gtm-skill` — channel strategy, funnel, GTM metrics
  - `36-pricing-sales-skill` — pricing, packaging, sales motion
  - `37-marketing-customer-success-skill` — demand gen, onboarding, retention

Workflows:
  - `07-go-to-market-workflow`

Expected Output:
  - Positioning & Messaging
  - Channel Strategy
  - Pricing & Packaging
  - Sales Process & Pipeline
  - Campaign Calendar

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/gtm Build a go-to-market plan for launching our product in a new vertical.`

**User request:** $ARGUMENTS
