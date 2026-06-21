# 01 New Product Workflow

## Purpose
Turn an unvalidated idea into a complete, fundable product plan — from problem statement to a named, positioned identity, a roadmap, a financial model, and a go-to-market motion — in one coherent pass instead of ten disconnected documents.

## Inputs
- A one- or two-sentence description of the idea or problem
- Whether the product is software, hardware, or both (if known — the Meta-Agent will ask if it isn't)
- Target customer or market, if already known
- Any hard constraints: timeline, budget, team size, existing IP

## Meta-Agent
Classified as **multi-agent** — the broadest classification in the system, since a "new product" request touches business framing, product definition, technical/hardware feasibility, operations, and finance before it's a real plan. The Meta-Agent's first job here is determining whether the product is software, hardware, or both; everything downstream of CPO-Agent depends on that answer, so it is the one clarifying question this workflow asks if it isn't already stated.

## Agent Execution Order
```
Meta-Agent
   ↓
CEO-Agent        (strategic framing)
   ↓
CPO-Agent        (problem, customer, PRD)
   ↓
CBO-Agent        (naming, positioning, identity foundation)
   ↓
CTO-Agent / CIO-Agent   (software or hardware feasibility — whichever owns the product)
   ↓
COO-Agent        (operating plan, stage gates)
   ↓
CFO-Agent        (unit economics, financial model)
   ↓
CRO-Agent / CMO-Agent   (go-to-market motion, on top of the identity CBO-Agent defined)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CEO-Agent | `12-company-bible-skill`, `13-corporate-os-skill` |
| CPO-Agent | `01-discovery-skill`, `02-market-research-skill`, `03-strategy-skill`, `04-prd-skill` |
| CBO-Agent | `48-positioning-skill`, `47-naming-skill`, `42-brand-strategy-skill` |
| CTO-Agent *(if software)* | `05-architecture-skill`, `06-engineering-execution-skill` |
| CIO-Agent *(if hardware/robotics)* | `22-hardware-product-skill` or `23-robotics-product-skill`, `41-mechatronics-skill` |
| COO-Agent | `09-operations-skill`, `18-stage-gate-skill` |
| CFO-Agent | `07-finance-skill` |
| CRO-Agent | `08-gtm-skill` |
| CMO-Agent | `37-marketing-customer-success-skill` |

## Artifacts Produced
Problem Statement, ICP & Personas, Competitor/Market Snapshot, PRD, Positioning Statement, Naming Shortlist, Brand Strategy Brief, System or Hardware Architecture, Stage-Gate Roadmap, Financial Model (unit economics + scenario), GTM Plan, Risk Register.

## Validation
`14-validation-skill` and `18-stage-gate-skill` (both COO-Agent) check the plan for gaps and contradictions before it's treated as final — specifically, that the PRD's scope, the architecture's feasibility, and the financial model's assumptions all agree with each other. If the `critic-agent/` layer is active, run `CRITIC_AGENT.md` over the Combined Executive Answer as a second, independent stress test before the plan ships.

## Risks
- Locking architecture before the PRD and ICP are validated, forcing a costly rebuild later
- CFO-Agent modeling a financial case on a revenue assumption CPO-Agent hasn't actually validated
- Treating "new product" as software-only when the idea is hardware or mixed, which silently drops CIO-Agent and produces an infeasible plan
- Naming or positioning chosen before CPO-Agent's discovery work is done, so the identity has to be redone once the real ICP is known

## Final Outputs
One merged executive plan: Problem Statement → ICP → PRD → Positioning & Naming → Architecture → Roadmap → Financial Model → GTM → Risks, sequenced and internally consistent, with assumptions and open questions stated explicitly rather than hidden.

## Example Prompt
*"We have an idea for a new product but nothing built yet — help us turn it into a complete plan from problem statement through go-to-market."*
