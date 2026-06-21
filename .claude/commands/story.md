---
description: Activates CBO-Agent to build the brand's narrative arc — origin story, the problem that justified starting the company, and the throughline that should show up consistently in pitch decks, About pages, and launch posts instead of being reinvented each time.
---

You are now acting as FoundryOS's command **`/story`**, defined in [`commands/story.md`](../../commands/story.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `51-storytelling-skill` — narrative arc, origin story structure
  - `45-content-system-skill` — how the arc gets reused across content surfaces

Workflows:
  - `06-fundraising-workflow`

Expected Output:
  - Narrative Arc (origin → tension → turning point → vision)
  - Origin Story (long and short versions)
  - Reuse Map (which surface uses which version of the story)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/story We pivoted twice before finding product-market fit — help me turn that into a pitch-deck narrative that reads as conviction, not indecision.`

**User request:** $ARGUMENTS
