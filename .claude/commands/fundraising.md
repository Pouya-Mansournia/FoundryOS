---
description: Generates the artifacts needed to be investor-ready — the financial model, product scorecard, and pitch narrative a fundraising conversation runs on.
---

You are now acting as FoundryOS's command **`/fundraising`**, defined in [`commands/fundraising.md`](../../commands/fundraising.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CEO-Agent/AGENT.md`
- `agents/CFO-Agent/AGENT.md`
- `agents/CPO-Agent/AGENT.md`
- `agents/CRO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CEO-Agent; CFO-Agent; CPO-Agent; CRO-Agent

Activated Skills:
  - `38-fundraising-investor-skill` — pitch narrative, data room, investor comms
  - `07-finance-skill` — financial model, scenarios
  - `27-product-scorecard-skill` — PMF/retention scoring
  - `08-gtm-skill` — traction narrative

Workflows:
  - `06-fundraising-workflow`

Expected Output:
  - Pitch Narrative
  - Financial Model & Scenario Analysis
  - Data Room Checklist
  - Product Scorecard
  - Investor Update Template

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/fundraising Get us investor-ready for a raise in the next few months.`

**User request:** $ARGUMENTS
