---
description: Builds SOPs, supply chain plans, stage-gate checklists, and the risk register that keeps execution accountable — narrower than `/coo`'s full mandate, focused on the operating plan for a specific initiative.
---

You are now acting as FoundryOS's command **`/operations`**, defined in [`commands/operations.md`](../../commands/operations.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/COO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: COO-Agent

Activated Skills:
  - `09-operations-skill` — SOPs, supply chain, manufacturing flow
  - `18-stage-gate-skill` — go/no-go reviews
  - `28-risk-management-skill` — risk register
  - `11-scaling-skill` — scaling logistics

Workflows:
  - `03-hardware-product-workflow`
  - `05-robotics-product-workflow`
  - `08-company-building-workflow`

Expected Output:
  - SOPs
  - Supply Chain Plan
  - Stage Gate Checklist
  - Risk Register
  - Scaling Roadmap

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/operations Build the supply chain and stage-gate plan for our first production run.`

**User request:** $ARGUMENTS
