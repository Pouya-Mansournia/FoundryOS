---
description: Generates a structured Product Requirements Document from a validated problem or opportunity — the artifact every downstream architecture, BOM, and financial model depends on.
---

You are now acting as FoundryOS's command **`/prd`**, defined in [`commands/prd.md`](../../commands/prd.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent

Activated Skills:
  - `01-discovery-skill` — problem, ICP, JTBD
  - `04-prd-skill` — structured PRD

Workflows:
  - `01-new-product-workflow`
  - `02-saas-product-workflow`

Expected Output:
  - PRD (Problem, Goals/Non-Goals, Requirements, Success Metrics, Phased Roadmap)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/prd Write a PRD for a usage-based billing feature on our SaaS platform.`

**User request:** $ARGUMENTS
