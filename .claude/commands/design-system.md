---
description: Activates CBO-Agent to define or extend the design system — color, type, spacing, and component tokens for digital products, or the CMF (color/material/finish) spec for physical ones — so CTO-Agent and CIO-Agent have something concrete to build against instead of improvising visual decisions mid-implementation.
---

You are now acting as FoundryOS's command **`/design-system`**, defined in [`commands/design-system.md`](../../commands/design-system.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `44-design-system-skill` — tokens, components, CMF spec
  - `54-color-psychology-skill` — color rationale, not just hex values
  - `55-typography-skill` — type scale, pairing, voice-through-type
  - `56-ui-system-skill` — component-level application of the tokens above

Workflows:
  - `03-hardware-product-workflow`
  - `02-saas-product-workflow`

Expected Output:
  - Design System & Token Spec (or CMF Spec for hardware)
  - Color Rationale
  - Type Scale
  - Component Application Examples

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/design-system We have a logo and a color palette — turn it into a design token system our frontend team can actually implement, with a component-level example.`

**User request:** $ARGUMENTS
