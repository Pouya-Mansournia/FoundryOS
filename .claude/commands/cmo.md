---
description: Activates CMO-Agent for demand generation, brand/content, and the customer-success loop that retains customers after CRO-Agent's motion acquires them.
---

You are now acting as FoundryOS's command **`/cmo`**, defined in [`commands/cmo.md`](../../commands/cmo.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CMO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CMO-Agent

Activated Skills:
  - `37-marketing-customer-success-skill` — demand gen, content, onboarding, retention, health dashboards

Workflows:
  - `07-go-to-market-workflow`

Expected Output:
  - Demand Gen & Content Plan
  - Campaign Calendar
  - Onboarding & Retention Plan
  - Customer Health Dashboard

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/cmo Build a 90-day demand-generation and retention plan for our product launch.`

**User request:** $ARGUMENTS
