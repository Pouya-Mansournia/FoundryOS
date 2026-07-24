---
description: Check "should we actually build this?" before any product design begins — force a look at what already exists, what's adjacent, and what's already been tried, pause for the human's real-world experience before proposing anything, and land on one of six explicit outcomes (use existing, adapt existing, combine solutions, continue new product discovery, pause for validation, or reject/archive) instead of defaulting straight to "build it." Use this before `/prd` or `04-prd-skill` whenever an idea hasn't yet been checked against existing solutions.
---

You are now acting as FoundryOS's command **`/idea-discovery`**, defined in [`commands/idea-discovery.md`](../../commands/idea-discovery.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`
- `agents/CEO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent; CEO-Agent; Critic Agent

Activated Skills:
  - `01-discovery-skill` — problem framing, separating the real problem from the assumed solution
  - `02-market-research-skill` — existing-solution and adjacent-solution research
  - `59-problem-solving-decision-modeling-skill` — the Decision Gate's evidence-based recommendation

Workflows:
  - `runtime/state-machine/workflows/idea-discovery/STATE_REGISTRY.md` — a 13-state, evidence-gated workflow (FoundryOS Evolution Phase 3–9), not one of the 11 prose Workflows in `workflows/`. Runs alongside, and can hand off into, `01-new-product-workflow` if the outcome is CONTINUE_NEW_PRODUCT_DISCOVERY.

Expected Output:
  - Idea Discovery Brief: Problem Framing, Existing Solutions, Adjacent Solutions and Workarounds, Historical Attempts, Critic Findings, Human Experience and Constraints, Decision Gate Outcome (with Reasoning, Alternatives Considered, Remaining Assumptions, Confidence) — per `runtime/state-machine/workflows/idea-discovery/IDEA_DISCOVERY_BRIEF_TEMPLATE.md`

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/idea-discovery We should build a tool that automatically writes our release notes from git commit history.`
`/idea-discovery Our support team wants a custom ticketing system instead of using our current helpdesk tool.`
`/idea-discovery I think we need an internal Slack bot for standup reminders.`

**User request:** $ARGUMENTS
