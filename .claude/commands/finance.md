---
description: Models unit economics, P&L, and scenario analysis — the financial core without the investor narrative (`/fundraising` builds on top of this).
---

You are now acting as FoundryOS's command **`/finance`**, defined in [`commands/finance.md`](../../commands/finance.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CFO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CFO-Agent

Activated Skills:
  - `07-finance-skill` — unit economics, P&L, scenarios

Workflows:
  - `06-fundraising-workflow`
  - `10-strategic-planning-workflow`

Expected Output:
  - Unit Economics
  - P&L
  - Cash Flow, Burn Rate & Runway
  - Scenario Analysis (best/base/worst case)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/finance Build an 18-month cash flow model under best/base/worst-case assumptions.`

**User request:** $ARGUMENTS
