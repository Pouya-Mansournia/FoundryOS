---
description: The broadest command — runs the full founder lifecycle on a new idea, from problem statement through a buildable, fundable plan. Equivalent to handing the request to the Meta-Agent with no scope restriction; the Meta-Agent decides which Agents actually run.
---

You are now acting as FoundryOS's command **`/startup`**, defined in [`commands/startup.md`](../../commands/startup.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `meta-agent/META_AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: Meta-Agent selects from all 10 Agents based on the request (typically CEO, CPO, CBO (naming/positioning, right after CPO), then CTO/CIO depending on product type, CFO, CRO)

Activated Skills:
  - Determined dynamically — see `meta-agent/META_AGENT.md` for routing logic

Workflows:
  - `01-new-product-workflow`
  - `08-company-building-workflow`

Expected Output:
  - Problem Statement & PRD
  - Naming & Positioning (CBO)
  - Architecture (software, hardware, or AI — as applicable)
  - Financial Model
  - GTM Plan
  - Org Structure
  - Roadmap

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/startup Help me go from idea to a fundable, buildable plan for [describe your idea].`

**User request:** $ARGUMENTS
