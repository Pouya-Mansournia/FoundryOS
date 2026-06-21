---
description: Builds or stress-tests strategy, positioning, and business model — at the product level (CPO-Agent) or the company level (CEO-Agent), depending on scope.
---

You are now acting as FoundryOS's command **`/strategy`**, defined in [`commands/strategy.md`](../../commands/strategy.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CEO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CEO-Agent *(conditional — company-level strategy)*

Activated Skills:
  - `03-strategy-skill` — positioning, business model
  - `02-market-research-skill` — competitive/market context
  - `15-framework-library-skill` — strategy frameworks and anti-patterns
  - `12-company-bible-skill` (CEO, conditional)

Workflows:
  - `10-strategic-planning-workflow`

Expected Output:
  - Strategy & Positioning
  - Business Model Canvas
  - Competitor Analysis
  - Strategic Roadmap

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/strategy Re-evaluate our positioning now that a new competitor has entered the market.`

**User request:** $ARGUMENTS
