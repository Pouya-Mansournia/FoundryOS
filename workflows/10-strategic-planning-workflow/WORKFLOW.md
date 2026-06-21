# 10 Strategic Planning Workflow

## Purpose
Set or revisit the company's direction for a defined horizon (quarter, year, multi-year) — vision, strategy, scenarios, and the trade-offs between them — as distinct from any single product, fundraising, or hiring decision.

## Inputs
- Planning horizon (quarterly OKRs vs. annual strategy vs. multi-year vision differ a lot in depth)
- Current state: traction, runway, team size, competitive position
- Any forcing function (board meeting, planning offsite, post-mortem on a missed target)
- Known constraints or non-negotiables going in (e.g., runway floor, headcount cap)

## Meta-Agent
Classified as **business**, the broadest and most CEO-Agent-centric of the ten workflows. Unlike `01-new-product-workflow`, this workflow is not about building one thing — it's about choosing *which* things to build and in what order, which is why CFO-Agent's scenario modeling and COO-Agent's trade-off framing sit earlier in the sequence than in product-specific workflows.

## Agent Execution Order
```
Meta-Agent
   ↓
CEO-Agent     (vision, strategic framing)
   ↓
CFO-Agent     (scenario modeling, what's affordable)
   ↓
CPO-Agent     (product strategy implications)
   ↓
CBO-Agent     (brand/positioning implications, rollout roadmap)
   ↓
COO-Agent     (execution trade-offs, scaling implications)
   ↓
CRO-Agent     (commercial/revenue implications)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CEO-Agent | `12-company-bible-skill`, `13-corporate-os-skill` |
| CFO-Agent | `07-finance-skill` |
| CPO-Agent | `03-strategy-skill`, `27-product-scorecard-skill` |
| CBO-Agent | `58-brand-roadmap-skill`, `48-positioning-skill` |
| COO-Agent | `11-scaling-skill`, `28-risk-management-skill` |
| CRO-Agent | `08-gtm-skill` |

## Artifacts Produced
Vision & Strategic Narrative, Scenario Analysis (best/base/worst case), Strategic Roadmap, Brand Roadmap & Positioning Implications, Explicit Trade-off Log (what we're choosing *not* to do and why), KPI/OKR Set for the horizon, Risk Register.

## Validation
`14-validation-skill` (COO-Agent) checks that the roadmap is actually affordable under CFO-Agent's base-case scenario, not just the optimistic one — the most common strategic-planning failure is a roadmap sized to best-case revenue. If `critic-agent/` is active, run it specifically against the trade-off log: are the rejected options genuinely worse, or just less discussed?

## Risks
- Strategy set against best-case financial scenario instead of base case, leaving no margin if growth comes in lower than hoped
- Trade-offs implied but never stated explicitly, so the team later relitigates decisions that were already made
- KPIs that measure activity (features shipped) instead of the strategic outcome they're supposed to serve (retention, margin, market position)
- A strategic pivot (new market, new ICP, new category claim) decided without checking whether the existing brand and positioning still fit, leaving the identity a step behind the strategy

## Final Outputs
One merged strategic plan: Vision → Strategy → Scenarios → Roadmap → Brand Implications → Trade-offs → KPIs → Risks, with every trade-off stated explicitly rather than left implicit.

## Example Prompt
*"Help us set strategy for the next year — where should we focus, what should we explicitly not do, and what are the KPIs that tell us it's working."*
