# 02 SaaS Product Workflow

## Purpose
Take a SaaS product from requirements to a priced, marketed, multi-tenant architecture — the default path for any product whose primary surface is a web/cloud application.

## Inputs
- What the product does and who it's for
- Whether it's B2B or B2C (changes pricing and GTM shape materially)
- Any existing tech stack or architecture constraints
- Target pricing model, if there's already a hypothesis (seat-based, usage-based, tiered)

## Meta-Agent
Classified as **product + technology**, with a revenue layer attached. This is the most software-only of the ten workflows — CIO-Agent is not in the default execution set unless the request turns out to involve an edge device or on-prem hardware component, in which case the Meta-Agent should flag that and add CIO-Agent rather than silently forcing it into CTO-Agent's scope.

## Agent Execution Order
```
Meta-Agent
   ↓
CPO-Agent     (PRD, what's being built)
   ↓
CBO-Agent     (positioning, naming, voice for the product surface)
   ↓
CTO-Agent     (SaaS/system architecture)
   ↓
CRO-Agent     (pricing, GTM motion)
   ↓
CMO-Agent     (demand, retention)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CPO-Agent | `01-discovery-skill`, `04-prd-skill`, `10-analytics-skill` |
| CBO-Agent | `48-positioning-skill`, `53-voice-tone-skill`, `44-design-system-skill` |
| CTO-Agent | `24-saas-product-skill`, `05-architecture-skill`, `30-data-architecture-skill` |
| CRO-Agent | `36-pricing-sales-skill`, `08-gtm-skill` |
| CMO-Agent | `37-marketing-customer-success-skill` |

## Artifacts Produced
PRD, Positioning Statement, In-Product Voice Guidelines, Multi-Tenant SaaS Architecture, Data Model, Analytics/Metrics Dashboard, Pricing & Packaging, GTM Plan, Campaign Calendar, Onboarding & Retention Plan.

## Validation
`14-validation-skill` (COO-Agent) checks that the pricing model and the architecture's cost-to-serve don't contradict each other — a common failure mode is pricing usage-based on a feature CTO-Agent built with flat infrastructure cost. If `critic-agent/` is active, have `CRITIC_AGENT.md` specifically stress-test the pricing-vs-cost-to-serve assumption before launch. Run `59-problem-solving-decision-modeling-skill` at the pricing-tier decision itself — a threshold decision (per-seat vs. usage-based) deserves the same rationale/sensitivity treatment as any other threshold, not an intuition call.

## Risks
- Architecture designed for one tenant pattern (e.g., shared schema) when the GTM motion implies another (e.g., enterprise needing isolated data) — surfaces late and expensively if not checked here
- Pricing model decided before unit economics are modeled, rather than the two informing each other
- Treating analytics as a launch afterthought instead of an architecture decision baked in from the PRD
- UI copy and in-product voice left to whoever's building the screen, instead of CBO-Agent's voice guidelines — produces a product that reads like five different writers

## Final Outputs
One merged plan: PRD → Positioning → SaaS Architecture → Analytics → Pricing → GTM → Retention Metrics, read as one product-to-revenue narrative rather than four separate workstreams.

## Example Prompt
*"Design the SaaS dashboard architecture and go-to-market plan for a new analytics product aimed at mid-market operations teams."*
