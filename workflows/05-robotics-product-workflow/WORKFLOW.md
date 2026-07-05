# 05 Robotics Product Workflow

## Purpose
Take a robotics product from requirements through a manufacturable system that spans mechanical, electronics, embedded, and fleet/navigation software — the most cross-domain workflow in the system, since robotics is the one product category that always needs hardware and software agents working from the same architecture at once.

## Inputs
- The task the robot performs and the environment it operates in (structured/unstructured, indoor/outdoor, human-proximate or not)
- Target unit volume and cost, and whether this is a single unit, small fleet, or mass-production scale
- Safety/reliability bar required (human-proximate operation raises this materially)
- Whether fleet-level software (navigation, orchestration across multiple units) is in scope

## Meta-Agent
Classified as **robotics**, the canonical multi-agent case in the routing table (CIO + CTO + CPO + COO). CIO-Agent owns the physical robot — mechanical, electronics, embedded, and the integrated mechatronics pass; CTO-Agent owns anything above the single unit — fleet software, navigation stack, cloud orchestration. The Meta-Agent should keep these two distinct rather than collapsing robotics entirely into either agent.

## Agent Execution Order
```
Meta-Agent
   ↓
CPO-Agent     (PRD, task definition)
   ↓
CIO-Agent     (mechanical / electronics / embedded / mechatronics)
   ↓
CTO-Agent     (fleet / navigation / orchestration software)
   ↓
CBO-Agent     (naming, CMF, human-robot interaction voice/cues)
   ↓
COO-Agent     (manufacturing ramp, supply chain)
   ↓
CFO-Agent     (cost model, unit economics)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CPO-Agent | `01-discovery-skill`, `04-prd-skill` |
| CIO-Agent | `23-robotics-product-skill`, `32-embedded-skill`, `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill` |
| CTO-Agent | `05-architecture-skill` (fleet/navigation/system architecture) |
| CBO-Agent | `47-naming-skill`, `54-color-psychology-skill`, `53-voice-tone-skill` |
| COO-Agent | `35-npi-manufacturing-skill` *(shared with CIO)*, `09-operations-skill`, `18-stage-gate-skill` |
| CFO-Agent | `07-finance-skill` |

## Artifacts Produced
PRD, Robotics System Architecture, Embedded/Firmware Architecture, Mechanical Design & FEA Results, Electronics/PCB Design Review, Fleet/Navigation Software Architecture, Robot Naming & CMF Spec, Human-Robot Interaction Voice/Cue Guide, Manufacturing & NPI Plan, Cost Model, Safety/Reliability Plan.

## Validation
`18-stage-gate-skill` (COO-Agent) gates mechanical/electronics/embedded integration before fleet software locks against it — a navigation stack built against a hardware spec that later changes is the single most expensive mistake in this workflow. If `critic-agent/` is active, run it specifically against safety/reliability claims for human-proximate operation before any pilot deployment. Hardware trade-offs with real TCO/reliability stakes (e.g. a component or subsystem choice with materially different cost, weight, or failure-rate profiles) should run through `59-problem-solving-decision-modeling-skill` before committing rather than being decided on intuition.

## Risks
- Fleet/navigation software (CTO-Agent) developed against a hardware spec that hasn't been validated by CIO-Agent yet
- Safety case treated as a late add-on instead of a design input from the PRD stage
- GTM and commercial motion (CRO-Agent) is not in this workflow's default execution set — if go-to-market depth is needed beyond a launch framing, add CRO-Agent explicitly rather than assuming COO-Agent's plan covers it
- Lights, sounds, and motion cues designed ad hoc per engineer instead of a coherent CBO-Agent-defined interaction language — inconsistent HRI cues undermine the trust a safety case depends on

## Final Outputs
One merged plan: PRD → System Architecture → Embedded/Mechanical/Electronics Architecture → Naming & CMF → Manufacturing Plan → Cost Model, with mechanical, electronics, and embedded work shown as one integrated mechatronics pass rather than three independent designs.

## Example Prompt
*"Design a robotics product for warehouse inventory scanning — from PRD through hardware architecture, fleet software, and a manufacturing plan."*
