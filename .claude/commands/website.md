---
description: Activates CBO-Agent to design the website as a synthesis artifact — UI system, copy, and design tokens applied to one customer-facing surface — rather than treating layout, words, and visuals as three separate handoffs that drift out of sync with each other.
---

You are now acting as FoundryOS's command **`/website`**, defined in [`commands/website.md`](../../commands/website.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CBO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CBO-Agent

Activated Skills:
  - `56-ui-system-skill` — page-level component application
  - `44-design-system-skill` — tokens the page is built against
  - `52-copywriting-skill` — headline, body, and CTA copy

Workflows:
  - `07-go-to-market-workflow`
  - `02-saas-product-workflow`

Expected Output:
  - Website Structure (sitemap, page-level wireframe intent)
  - Page Copy (headline, subhead, body, CTAs)
  - Component Spec (built against the existing design system)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/website Draft the homepage for our SaaS product launch — hero, three feature sections, pricing teaser, and footer, using our existing design tokens.`

**User request:** $ARGUMENTS
