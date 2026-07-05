# Command
/solve

## Purpose
Frame a complex problem, build its causal and quantitative model, compare options, and produce an evidence-based decision and validation plan — not a PRD generator. Use this whenever the request is a decision ("should we," "which option," "why is this happening," "is this worth it") rather than a request for a known artifact.

## Activated Agents
- CEO-Agent
- Plus whichever domain Agent(s) the decision touches (Meta-Agent selects per `meta-agent/META_AGENT.md`'s "Cross-Cutting Skill Activation" section)

## Activated Skills
- `59-problem-solving-decision-modeling-skill` — problem framing, causal/metric modeling, hypothesis engineering, formula selection, experiment design, staged rollout
- Whichever domain Skill the decision touches (e.g. `31-ai-architecture-skill` for an AI infrastructure call, `07-finance-skill` for a pricing call)

## Workflows
- `11-problem-solving-decision-workflow`

## Output
- Decision Memo: Decision Statement, Current-State Model, Problem Decomposition, Causal Model, Metric Tree, Hypothesis Register, Solution Options, Selected Quantitative Model(s), Scenario/Sensitivity Analysis, Validation Plan, Recommendation, Risks & Guardrails, Staged Rollout, Confidence Assessment — scaled to stakes (concise / standard / deep)

## Example
`/solve Should we self-host our model's inference or stay on a managed API?`
`/solve Should we introduce a usage-based pricing tier alongside our flat SaaS plan?`
`/solve Should we automate a manual inspection step in our manufacturing line?`
`/solve Our onboarding drop-off jumped 8 points last month — what's actually going on and is it worth fixing before anything else?`
