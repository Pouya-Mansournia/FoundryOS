---
description: Activates CBO-Agent to define or audit voice and tone — the attributes that stay constant, the tone shifts that are allowed by channel, and the banned phrases that keep slipping back in. The Skill every other content-producing command reads from before writing a word.
---

You are now acting as FoundryOS's command **`/voice`**, defined in [`commands/voice.md`](../../commands/voice.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `53-voice-tone-skill` — voice attributes, tone-by-channel rules, banned-phrase list

Workflows:
  - `02-saas-product-workflow`
  - `04-ai-product-workflow`
  - `05-robotics-product-workflow`

Expected Output:
  - Voice Attributes (3-5 adjectives, each with a "sounds like / doesn't sound like" example)
  - Tone-by-Channel Matrix (support, marketing, in-product, social)
  - Banned Phrases List

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/voice Our support tone and our marketing tone have drifted apart — define one voice with channel-specific tone variance, not two separate voices.`

**User request:** $ARGUMENTS
