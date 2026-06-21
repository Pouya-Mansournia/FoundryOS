---
description: Activates CBO-Agent to design or run the community layer — structure, engagement cadence, and the social calendar — grounded in the voice rules already set in `memory/voice-memory.md` so community output doesn't establish a tone the brand hasn't sanctioned.
---

You are now acting as FoundryOS's command **`/community`**, defined in [`commands/community.md`](../../commands/community.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `49-community-skill` — community structure, engagement model
  - `50-social-assets-skill` *(conditional — when the community motion needs accompanying visual assets)*

Workflows:
  - `08-company-building-workflow`
  - `07-go-to-market-workflow`

Expected Output:
  - Community Structure (channels, roles, moderation model)
  - Engagement Cadence
  - Social Calendar (initial 4-6 weeks)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/community We just open-sourced our project — design the Discord/GitHub Discussions structure and the first month of engagement cadence.`

**User request:** $ARGUMENTS
