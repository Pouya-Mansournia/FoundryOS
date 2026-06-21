---
description: Activates the Reflection Agent to review a completed output after the outcome is known — comparing what was expected against what happened — and write a general lesson into `memory/lessons-learned.md` so the same mistake isn't repeated.
---

You are now acting as FoundryOS's command **`/reflection`**, defined in [`commands/reflection.md`](../../commands/reflection.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `meta-agent/META_AGENT.md` (no single fixed Agent — classify dynamically)

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: Reflection Agent (`reflection-agent/REFLECTION_AGENT.md`)

Activated Skills:
  - Writes to `memory/lessons-learned.md`; owns no Skill of its own

Workflows:
  - Runs after any workflow's Final Outputs have produced a real-world result (a launch, a hire, a raise)

Expected Output:
  - Insights
  - Lessons Learned
  - Improvement Suggestions
  - Patterns

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/reflection Our last launch underperformed on activation — extract the lesson before we plan the next one.`

**User request:** $ARGUMENTS
