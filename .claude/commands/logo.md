---
description: Activates CBO-Agent to design or evaluate a logo system — wordmark, symbol, lockups, and the usage rules that keep it consistent once other people start applying it.
---

You are now acting as FoundryOS's command **`/logo`**, defined in [`commands/logo.md`](../../commands/logo.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `46-logo-system-skill` — wordmark/symbol/lockup system, usage rules
  - `43-brand-book-skill` *(conditional — when the logo needs to be documented as part of a larger brand book, not delivered standalone)*
  - `57-brand-assets-management-skill` — versioning, file formats, deprecated-mark tracking

Workflows:
  - `01-new-product-workflow`
  - `03-hardware-product-workflow`

Expected Output:
  - Logo System (wordmark, symbol, lockups)
  - Usage Rules (minimum size, clear space, misuse examples)
  - Asset Package (file formats, version)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/logo Design a logo system for our brand archetype "the calm expert" — needs to work on a product label, a mobile app icon, and a conference banner.`

**User request:** $ARGUMENTS
