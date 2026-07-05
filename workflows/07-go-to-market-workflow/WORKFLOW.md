# 07 Go-To-Market Workflow

## Purpose
Turn a validated product into a repeatable path to revenue — positioning, channels, pricing, and a funnel with metrics attached — rather than a list of marketing tactics with no model behind them.

## Inputs
- ICP and the job-to-be-done the product solves, if already defined by a prior CPO-Agent pass
- Whether the motion is self-serve, sales-assisted, or enterprise (changes channel and pricing shape entirely)
- Any existing pricing hypothesis or competitive pricing context
- Launch timeline, if there's a fixed date to plan against

## Meta-Agent
Classified as **revenue**, with brand, marketing, and product as supporting agents. This workflow assumes CPO-Agent's discovery and CBO-Agent's positioning groundwork already exist (from `01-new-product-workflow` or a prior product/brand pass) — if they don't, the Meta-Agent should flag that ICP/positioning is a missing input and route to CBO-Agent for a fresh positioning pass rather than letting CRO-Agent invent one from scratch.

## Agent Execution Order
```
Meta-Agent
   ↓
CBO-Agent     (positioning & messaging, campaign voice)
   ↓
CRO-Agent     (channel strategy, pricing, pipeline)
   ↓
CMO-Agent     (demand gen, campaigns — built inside CBO-Agent's voice)
   ↓
CPO-Agent     (positioning check, metrics definition)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CBO-Agent | `48-positioning-skill`, `52-copywriting-skill`, `50-social-assets-skill` |
| CRO-Agent | `08-gtm-skill`, `36-pricing-sales-skill` |
| CMO-Agent | `37-marketing-customer-success-skill` |
| CPO-Agent | `03-strategy-skill`, `10-analytics-skill` |

## Artifacts Produced
Positioning & Messaging, Campaign Copy & Social Assets, Channel Strategy, Sales Process & Pipeline, Pricing & Packaging, Demand Gen & Campaign Calendar, Funnel/Conversion Metrics, Launch Plan.

## Validation
`14-validation-skill` (COO-Agent) checks that the channel strategy and the pricing model are consistent with each other and with the ICP — for example, a self-serve channel paired with an enterprise-only pricing tier is a contradiction this step should catch. If `critic-agent/` is active, run it against the funnel metrics specifically: are they vanity metrics (impressions, signups) or metrics that actually predict revenue (activation, paid conversion)? Channel prioritization itself is a weighted-decision-score problem — run it through `59-problem-solving-decision-modeling-skill` rather than ranking channels on gut feel.

## Risks
- Positioning and messaging decided without re-checking the ICP CPO-Agent originally validated
- Pricing set independently of CFO-Agent's unit economics, producing a GTM plan the company can't actually afford to run
- Funnel metrics chosen for ease of measurement rather than predictive power
- Positioning re-litigated by every channel and campaign instead of locked once by CBO-Agent, producing inconsistent claims across the funnel

## Final Outputs
One merged GTM plan: Positioning → Channels → Pricing → Funnel → Launch Plan, with metrics that trace back to revenue, not just activity, and messaging that stays consistent from the first ad to the close.

## Example Prompt
*"Build a go-to-market strategy for our product — positioning, channels, pricing, and how we'll measure whether it's working."*
