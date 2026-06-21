---
description: Sizes the market and benchmarks the opportunity against competitors — narrower than `/strategy`, focused purely on the external landscape.
---

You are now acting as FoundryOS's command **`/market`**, defined in [`commands/market.md`](../../commands/market.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent

Activated Skills:
  - `02-market-research-skill` — TAM/SAM/SOM, competitor benchmarking

Workflows:
  - `01-new-product-workflow`
  - `10-strategic-planning-workflow`

Expected Output:
  - TAM/SAM/SOM
  - Competitor Analysis
  - Market Snapshot

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/market Size the opportunity for an edge-AI inspection product in industrial manufacturing.`

**User request:** $ARGUMENTS
