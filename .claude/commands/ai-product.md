---
description: Runs the AI product workflow — requirements, AI/data architecture, and evaluation strategy. CIO-Agent joins only if on-device or edge inference is in scope.
---

You are now acting as FoundryOS's command **`/ai-product`**, defined in [`commands/ai-product.md`](../../commands/ai-product.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CTO-Agent/AGENT.md`
- `agents/CIO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CTO-Agent; CIO-Agent *(conditional — on-device/edge inference only)*

Activated Skills:
  - `01-discovery-skill`, `04-prd-skill` (CPO)
  - `21-ai-product-skill`, `31-ai-architecture-skill`, `30-data-architecture-skill` (CTO)
  - `32-embedded-skill` (CIO, conditional)

Workflows:
  - `04-ai-product-workflow`

Expected Output:
  - AI Architecture
  - Data & Evaluation Strategy
  - PRD

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/ai-product Define the data, model, and evaluation strategy for an AI feature that predicts customer churn.`

**User request:** $ARGUMENTS
