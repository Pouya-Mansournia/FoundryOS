---
description: Activates CBO-Agent to choose or audit a color palette with the psychological and competitive rationale behind each choice — not just hex values, but why this palette signals what the brand needs it to signal, and how it sits relative to competitors who may already own a color.
---

You are now acting as FoundryOS's command **`/colors`**, defined in [`commands/colors.md`](../../commands/colors.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `54-color-psychology-skill` — color rationale, emotional association, competitive color-mapping

Workflows:
  - `03-hardware-product-workflow`

Expected Output:
  - Color Palette (primary, secondary, accent, with hex/CMF values)
  - Rationale (per color: what it signals, what it avoids signaling)
  - Competitive Color Map (which competitors already occupy which colors)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/colors Our category is dominated by blue "trustworthy enterprise" palettes — help us pick a palette that still signals reliability but doesn't blend into the category.`

**User request:** $ARGUMENTS
