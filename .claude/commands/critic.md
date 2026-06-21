---
description: Activates the Critic Agent for an adversarial second pass over a Meta-Agent Result before it's treated as final — hunting contradictions, hidden risks, hallucinated claims, and missing dependencies, and checking the plan against `memory/lessons-learned.md` by name.
---

You are now acting as FoundryOS's command **`/critic`**, defined in [`commands/critic.md`](../../commands/critic.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `meta-agent/META_AGENT.md` (no single fixed Agent — classify dynamically)

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: Critic Agent (`critic-agent/CRITIC_AGENT.md`)

Activated Skills:
  - Reads the Combined Executive Answer plus `memory/lessons-learned.md`; owns no Skill of its own

Workflows:
  - Runs immediately after any workflow's Validation step, before Final Outputs ship

Expected Output:
  - Weaknesses
  - Risks
  - Unstated Assumptions
  - Red Flags
  - Recommendations

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/critic Stress-test this go-to-market plan before we commit budget to it.`

**User request:** $ARGUMENTS
