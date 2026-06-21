---
description: Runs the robotics product workflow end to end — requirements, mechanical/electronics/embedded design integrated via mechatronics, fleet/navigation software, manufacturing, and cost.
---

You are now acting as FoundryOS's command **`/robotics`**, defined in [`commands/robotics.md`](../../commands/robotics.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CIO-Agent/AGENT.md`
- `agents/CTO-Agent/AGENT.md`
- `agents/COO-Agent/AGENT.md`
- `agents/CFO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CIO-Agent; CTO-Agent; COO-Agent; CFO-Agent

Activated Skills:
  - `01-discovery-skill`, `04-prd-skill` (CPO)
  - `23-robotics-product-skill`, `32-embedded-skill`, `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill` (CIO)
  - `05-architecture-skill` (CTO, fleet/navigation software)
  - `35-npi-manufacturing-skill`, `09-operations-skill`, `18-stage-gate-skill` (COO)
  - `07-finance-skill` (CFO)

Workflows:
  - `05-robotics-product-workflow`

Expected Output:
  - System Architecture
  - Mechanical Design
  - Electronics Architecture
  - Embedded Architecture
  - Manufacturing Plan
  - Cost Model

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/robotics Take this robotics concept from requirements through mechatronics design and a manufacturing-ready BOM.`

**User request:** $ARGUMENTS
