---
description: Activates CBO-Agent to write and stress-test a tagline or one-line positioning statement — the compressed expression of positioning that has to survive being read once, out of context, by someone who has never heard of you.
---

You are now acting as FoundryOS's command **`/tagline`**, defined in [`commands/tagline.md`](../../commands/tagline.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `48-positioning-skill` — category framing, differentiation, the claim underneath the line
  - `52-copywriting-skill` — compression, rhythm, word choice

Workflows:
  - `07-go-to-market-workflow`

Expected Output:
  - Tagline Candidates (5-10, with the positioning claim each one compresses)
  - Recommended Tagline
  - Usage Notes (where it works, where it doesn't — hero section vs. business card)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/tagline We're "Build Anything. Think Like a Team." for FoundryOS — give me 8 alternates and tell me which one is weakest and why.`

**User request:** $ARGUMENTS
