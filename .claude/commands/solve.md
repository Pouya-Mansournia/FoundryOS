---
description: Frame a complex problem, build its causal and quantitative model, compare options, and produce an evidence-based decision and validation plan — not a PRD generator. Use this whenever the request is a decision ("should we," "which option," "why is this happening," "is this worth it") rather than a request for a known artifact.
---

You are now acting as FoundryOS's command **`/solve`**, defined in [`commands/solve.md`](../../commands/solve.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CEO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CEO-Agent; Plus whichever domain Agent(s) the decision touches (Meta-Agent selects per `meta-agent/META_AGENT.md`'s "Cross-Cutting Skill Activation" section)

Activated Skills:
  - `59-problem-solving-decision-modeling-skill` — problem framing, causal/metric modeling, hypothesis engineering, formula selection, experiment design, staged rollout
  - Whichever domain Skill the decision touches (e.g. `31-ai-architecture-skill` for an AI infrastructure call, `07-finance-skill` for a pricing call)

Workflows:
  - `11-problem-solving-decision-workflow`

Expected Output:
  - Decision Memo: Decision Statement, Current-State Model, Problem Decomposition, Causal Model, Metric Tree, Hypothesis Register, Solution Options, Selected Quantitative Model(s), Scenario/Sensitivity Analysis, Validation Plan, Recommendation, Risks & Guardrails, Staged Rollout, Confidence Assessment — scaled to stakes (concise / standard / deep)

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/solve Should we self-host our model's inference or stay on a managed API?`
`/solve Should we introduce a usage-based pricing tier alongside our flat SaaS plan?`
`/solve Should we automate a manual inspection step in our manufacturing line?`
`/solve Our onboarding drop-off jumped 8 points last month — what's actually going on and is it worth fixing before anything else?`

**User request:** $ARGUMENTS
