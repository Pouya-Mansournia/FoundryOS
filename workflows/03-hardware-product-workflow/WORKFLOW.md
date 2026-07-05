# 03 Hardware Product Workflow

## Purpose
Take a physical product from requirements through a manufacturable, costed plan — the default path whenever the deliverable is a BOM, not a deploy.

## Inputs
- What the device does and the environment it operates in
- Target unit volume and target unit cost, if known
- Whether this is a brand-new design or a revision of an existing product
- Any regulatory/compliance context (medical, industrial, consumer)

## Meta-Agent
Classified as **robotics/hardware** (or **operations** if the request is purely about manufacturing an already-designed product). The Meta-Agent should confirm volume and target cost early — both materially change which DFM and supplier decisions CIO-Agent and COO-Agent make, and a plan built without them is a guess dressed up as a plan.

## Agent Execution Order
```
Meta-Agent
   ↓
CPO-Agent     (PRD, requirements)
   ↓
CIO-Agent     (hardware design, DFM, NPI handoff)
   ↓
CBO-Agent     (CMF, packaging, unboxing — the physical brand expression)
   ↓
COO-Agent     (manufacturing ramp, supply chain)
   ↓
CFO-Agent     (BOM cost, CAPEX, unit economics)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CPO-Agent | `01-discovery-skill`, `04-prd-skill` |
| CIO-Agent | `22-hardware-product-skill`, `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill`, `35-npi-manufacturing-skill` *(shared with COO)* |
| CBO-Agent | `54-color-psychology-skill`, `44-design-system-skill`, `57-brand-assets-management-skill` |
| COO-Agent | `35-npi-manufacturing-skill` *(shared with CIO)*, `09-operations-skill`, `18-stage-gate-skill`, `28-risk-management-skill` |
| CFO-Agent | `07-finance-skill` |

## Artifacts Produced
PRD, BOM, DFM/DFA Review, CMF (Color/Material/Finish) Spec, Packaging & Unboxing Design, EVT/DVT/PVT Plan, Supply Chain & Supplier Qualification Plan, Manufacturing Ramp Plan, Cost Analysis (unit cost + CAPEX), Risk Register, Production-Readiness Roadmap.

## Validation
`18-stage-gate-skill` (COO-Agent) gates the plan at each phase boundary (EVT → DVT → PVT → production) — nothing advances to the next phase without an explicit go/no-go. `35-npi-manufacturing-skill` is the shared deliverable between CIO-Agent and COO-Agent and should appear once, jointly owned, not duplicated. If `critic-agent/` is active, run it against the BOM and supplier plan specifically for single-source-of-failure risk. Any single-source vs. dual-source or make-vs-buy call at a phase gate should run through `59-problem-solving-decision-modeling-skill` (TCO and reliability formulas from `FORMULA_LIBRARY.md`) rather than being decided on unit cost alone.

## Risks
- BOM costed against design-stage assumptions that don't survive DFM review, breaking the unit economics CFO-Agent already modeled
- Single-sourced critical components with no qualified second supplier
- Regulatory/compliance requirements discovered after tooling is committed instead of during PRD
- CMF and packaging decided after tooling is locked, forcing a costly mold change instead of a CBO-Agent pass during DFM

## Final Outputs
One merged plan: PRD → BOM → CMF & Packaging → Manufacturing Plan → Cost Analysis → Risks → Production-Readiness Roadmap, with `35-npi-manufacturing-skill` credited once as a CIO/COO joint deliverable.

## Example Prompt
*"We have a working prototype of a hardware device and need a plan to take it through DFM, NPI, and into a costed production run."*
