---
description: Runs the SaaS product workflow end to end — requirements, multi-tenant architecture, pricing, and the metrics that prove retention and PMF.
---

You are now acting as FoundryOS's command **`/saas`**, defined in [`commands/saas.md`](../../commands/saas.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CTO-Agent/AGENT.md`
- `agents/CRO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CTO-Agent; CRO-Agent

Activated Skills:
  - `01-discovery-skill`, `04-prd-skill`, `10-analytics-skill` (CPO)
  - `24-saas-product-skill`, `05-architecture-skill`, `30-data-architecture-skill` (CTO)
  - `36-pricing-sales-skill`, `08-gtm-skill` (CRO)

Workflows:
  - `02-saas-product-workflow`

Expected Output:
  - PRD
  - SaaS Architecture
  - Pricing & Packaging
  - Metrics & Dashboard

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/saas Take this SaaS idea from PRD through architecture and pricing.`

**User request:** $ARGUMENTS
