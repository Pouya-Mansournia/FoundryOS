# 11 Problem Solving and Decision Workflow

## Purpose
Frame an ambiguous problem, build its causal and quantitative model, compare options, and produce an evidence-based decision and validation plan — for any request that's actually a decision ("should we," "which option," "why is this happening," "is this worth it") rather than a request for a known artifact. Unlike `01`-`10`, this workflow isn't shaped around a product type; it's the reasoning discipline those ten call into at their own decision, prioritization, and validation gates, and it can also run standalone.

## Inputs
- The decision that needs to be made, and who owns it
- Whatever evidence, data, or prior context already exists (and an honest list of what doesn't)
- Constraints (budget, timeline, regulatory, technical) and the decision deadline
- Reversibility — is this a two-way door or a one-way door

## Meta-Agent
Classified as **multi-agent by default**, anchored by CEO-Agent's `59-problem-solving-decision-modeling-skill`, combined with whichever domain Agent(s) the decision actually touches (see `meta-agent/META_AGENT.md`'s "Cross-Cutting Skill Activation" section). This workflow does not default to producing a PRD, a BOM, or any other fixed artifact — its output is a decision packet.

## Agent Execution Order
```
Meta-Agent
   ↓
CEO-Agent        (frame the decision, build the causal/metric model — 59-problem-solving-decision-modeling-skill)
   ↓
Domain Agent(s)  (whichever of CPO/CTO/CIO/COO/CFO/CRO/CBO the decision touches, in their normal relative order)
   ↓
CFO-Agent        (if a quantitative/financial formula is in scope and CFO-Agent wasn't already included above)
   ↓
Critic-Agent     (stress-test the causal claims, formulas, and guardrails before the decision ships)
   ↓
Planner-Agent    (turn the Staged Rollout Plan into a dated roadmap)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CEO-Agent | `59-problem-solving-decision-modeling-skill` |
| CPO-Agent (if product-shaped) | `01-discovery-skill`, `10-analytics-skill`, `27-product-scorecard-skill` |
| CTO-Agent / CIO-Agent (if technical/hardware-shaped) | Whichever architecture or hardware Skill the decision touches |
| COO-Agent (if operational) | `09-operations-skill`, `14-validation-skill`, `28-risk-management-skill` |
| CFO-Agent (if the decision has real financial stakes) | `07-finance-skill` |
| CRO-Agent (if pricing/growth-shaped) | `36-pricing-sales-skill`, `08-gtm-skill` |

## Artifacts Produced
Decision Memo (Decision Statement through Confidence Assessment), Problem Frame, Causal Model, Metric Tree, Hypothesis Register, Formula Sheet (from `skills/59-problem-solving-decision-modeling-skill/FORMULA_LIBRARY.md`), Decision Matrix, Scenario Model, Experiment or Validation Plan, Staged Rollout Plan.

## Validation
`14-validation-skill` (COO-Agent) and this workflow's own Phase 4 failure-mode check (in `177_Validation_Rollout_OS.md`) both run before the decision ships — the most common failure here is a plausible-sounding causal story with no separated fact/inference/hypothesis labeling. If `critic-agent/` is active, run it specifically against the Formula Sheet for misapplied formulas and double-counted benefits, and against the Hypothesis Register for falsifiability.

## Risks
- Solution-first reasoning — a fix proposed before the root cause is modeled
- A metric with no denominator, owner, or data source, used to justify the decision anyway
- Correlation presented as causation in the causal chain
- False precision — a confident number produced from a weak or fabricated input
- A staged rollout with a launch date but no rollback trigger
- The decision packet defaulting into a PRD or other fixed-template artifact instead of staying a decision packet

## Final Outputs
One merged decision packet: Decision Statement → Current-State Model → Problem Decomposition → Causal Model → Metric Tree → Hypotheses → Solution Options → Selected Quantitative Model(s) → Scenario/Sensitivity → Validation Plan → Recommendation → Risks/Guardrails → Staged Rollout → Instrumentation → Open Decisions → Confidence Assessment, scaled to stakes (concise / standard / deep per `skills/59-problem-solving-decision-modeling-skill/SKILL.md`).

## Example Prompt
*"We think our onboarding drop-off is a UX problem, but I'm not sure — help us figure out what's actually going on and whether it's worth fixing before anything else."*
