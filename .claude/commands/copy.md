---
description: Activates CBO-Agent to write or rewrite copy — landing pages, emails, in-product strings, ads — against the voice rules already established, instead of producing generic marketing language that has to be re-edited into the brand's actual voice afterward.
---

You are now acting as FoundryOS's command **`/copy`**, defined in [`commands/copy.md`](../../commands/copy.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `52-copywriting-skill` — headline/body/CTA writing, compression, rhythm
  - `53-voice-tone-skill` *(input — supplies the tone-by-channel rules copy must follow)*

Workflows:
  - `07-go-to-market-workflow`

Expected Output:
  - Copy Draft (channel-specific: landing page, email, in-product, ad)
  - Voice Compliance Notes (where the draft follows or deviates from `memory/voice-memory.md`, and why)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/copy Write the email announcing our v2 launch — three variants, one direct, one playful, one technical — and flag which fits our actual brand voice.`

**User request:** $ARGUMENTS
