---
description: Designs system, software, data, or AI architecture. CIO-Agent joins when hardware or robotics architecture is also needed.
---

You are now acting as FoundryOS's command **`/architecture`**, defined in [`commands/architecture.md`](../../commands/architecture.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CTO-Agent/AGENT.md`
- `agents/CIO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CTO-Agent; CIO-Agent *(conditional — hardware/robotics architecture)*

Activated Skills:
  - `05-architecture-skill`, `29-software-engineering-skill`, `30-data-architecture-skill`, `31-ai-architecture-skill` (CTO)
  - `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill` (CIO, conditional)

Workflows:
  - `02-saas-product-workflow`
  - `04-ai-product-workflow`
  - `03-hardware-product-workflow` *(conditional)*
  - `05-robotics-product-workflow` *(conditional)*

Expected Output:
  - System Architecture & Tech Stack
  - ADRs
  - Data Models
  - AI Architecture *(if applicable)*

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/architecture Design the system architecture for a multi-tenant SaaS analytics product.`

**User request:** $ARGUMENTS
