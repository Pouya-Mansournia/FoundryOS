# 08 Company Building Workflow

## Purpose
Define or evolve the company itself — structure, operating cadence, KPIs, and culture — as distinct from any single product or fundraising motion. This is the workflow for "how should we be organized," not "what should we build."

## Inputs
- Current headcount and team structure, if any exists yet
- Stage of company (pre-seed idea stage vs. post-Series-A scaling — the right operating system differs a lot)
- Specific trigger, if any (just raised, just crossed a headcount threshold, post-incident reorg)
- Budget constraints from CFO-Agent's existing financial model, if one exists

## Meta-Agent
Classified as **business**, specifically the company-operating-system sub-case from the routing table (CEO + COO + CHRO + CBO + CFO). This workflow is agent-light but high-leverage — it produces the structure every other workflow's outputs eventually have to fit inside.

## Agent Execution Order
```
Meta-Agent
   ↓
CEO-Agent     (org structure, governance)
   ↓
COO-Agent     (operating cadence, SOPs)
   ↓
CHRO-Agent    (culture, people systems)
   ↓
CBO-Agent     (employer brand, internal voice & culture narrative)
   ↓
CFO-Agent     (budget reality check)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CEO-Agent | `13-corporate-os-skill`, `12-company-bible-skill`, `19-raci-meeting-skill` |
| COO-Agent | `09-operations-skill`, `16-artifact-template-skill` |
| CHRO-Agent | `39-people-culture-skill` |
| CBO-Agent | `53-voice-tone-skill`, `51-storytelling-skill` |
| CFO-Agent | `07-finance-skill` |

## Artifacts Produced
Org Structure & Reporting Lines, Governance Model & Board Cadence, RACI Matrix, Operating Cadence & SOPs, KPI/OKR Framework, Culture & Operating Values, Employer Brand & Internal Voice Guide, Budget Reality Check.

## Validation
`14-validation-skill` (COO-Agent) checks that the proposed org structure and operating cadence are actually affordable against CFO-Agent's budget — a governance model that assumes headcount the company hasn't funded is the most common failure here. If `critic-agent/` is active, run it against whether the proposed structure matches the company's actual stage, not an aspirational one two stages ahead. Structural trade-offs (centralize vs. federate a function, build vs. outsource a capability) belong in `59-problem-solving-decision-modeling-skill`'s options matrix, not decided by precedent alone.

## Risks
- Designing governance and process for the company's *next* stage instead of its current one, adding overhead before it's earned
- KPIs/OKRs defined without a clear owner per the RACI matrix, so nothing is actually accountable
- Culture work treated as a values poster instead of an operating system embedded in how decisions actually get made
- CHRO-Agent's culture work and CBO-Agent's internal voice built in parallel without talking to each other, so the values on the wall don't match how the company actually communicates day to day

## Final Outputs
One merged operating system: Org Structure → Governance → KPIs → Culture → Employer Brand, checked against budget reality, ready to run the company day to day.

## Example Prompt
*"We just crossed 15 people — help us design the org structure, KPIs, and operating cadence for this stage."*
