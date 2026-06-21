---
description: Activates CBO-Agent to generate and screen name candidates — for a company, a product line, or a single feature — against trademark risk, domain availability, pronounceability, and fit with the brand archetype already in `memory/brand-memory.md`.
---

You are now acting as FoundryOS's command **`/naming`**, defined in [`commands/naming.md`](../../commands/naming.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `47-naming-skill` — name generation, screening, shortlist
  - `42-brand-strategy-skill` *(upstream — archetype must exist before names are screened against it)*

Workflows:
  - `01-new-product-workflow`
  - `05-robotics-product-workflow`

Expected Output:
  - Naming Shortlist (5-10 candidates with rationale)
  - Screening Notes (trademark, domain, pronounceability flags)
  - Recommended Name

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/naming We need a name for our new AI copilot feature — should feel precise and trustworthy, not playful.`

**User request:** $ARGUMENTS
