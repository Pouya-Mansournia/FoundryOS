---
description: Runs the hardware product workflow end to end — requirements through mechanical/electronics design, BOM, NPI, and the cost model behind it.
---

You are now acting as FoundryOS's command **`/hardware`**, defined in [`commands/hardware.md`](../../commands/hardware.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CIO-Agent/AGENT.md`
- `agents/COO-Agent/AGENT.md`
- `agents/CFO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CIO-Agent; COO-Agent; CFO-Agent

Activated Skills:
  - `01-discovery-skill`, `04-prd-skill` (CPO)
  - `22-hardware-product-skill`, `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill`, `35-npi-manufacturing-skill` (CIO)
  - `35-npi-manufacturing-skill`, `09-operations-skill`, `18-stage-gate-skill`, `28-risk-management-skill` (COO)
  - `07-finance-skill` (CFO)

Workflows:
  - `03-hardware-product-workflow`

Expected Output:
  - BOM
  - Manufacturing / NPI Plan
  - Cost Analysis
  - Roadmap

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/hardware Take this hardware concept from requirements through a BOM and manufacturing plan.`

**User request:** $ARGUMENTS
