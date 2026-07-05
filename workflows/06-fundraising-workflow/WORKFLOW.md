# 06 Fundraising Workflow

## Purpose
Turn a company's actual traction and economics into a fundable narrative and a ready data room — the workflow for "make us investor-ready," not for the underlying product or financial work itself (which other workflows produce as inputs here).

## Inputs
- Round stage and target raise size, if known
- Current traction: revenue/usage, growth rate, retention — whatever evidence exists
- Current burn rate and runway
- Whether the product is software, hardware, or both (changes what technical diligence looks like)

## Meta-Agent
Classified as **finance**, but unconditionally multi-agent — fundraising readiness always needs CEO-Agent's narrative, CFO-Agent's numbers, CPO-Agent's product evidence, and CRO-Agent's pipeline evidence together; dropping any one of the four produces a one-sided pitch. CTO-Agent and/or CIO-Agent join only if technical/hardware diligence is in scope, and the Meta-Agent should state which one (or both) based on what the product actually is — flagging it as a missing input if that isn't yet known.

## Agent Execution Order
```
Meta-Agent
   ↓
CEO-Agent     (strategic narrative)
   ↓
CBO-Agent     (narrative arc, pitch deck visual design)
   ↓
CFO-Agent     (financial model, unit economics)
   ↓
CPO-Agent     (PMF evidence)
   ↓
CRO-Agent     (pipeline/GTM evidence)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CEO-Agent | `12-company-bible-skill`, `13-corporate-os-skill` |
| CBO-Agent | `51-storytelling-skill`, `44-design-system-skill` |
| CFO-Agent | `38-fundraising-investor-skill`, `07-finance-skill` |
| CPO-Agent | `27-product-scorecard-skill` |
| CRO-Agent | `08-gtm-skill` |

## Artifacts Produced
Fundraising Strategy & Round Structure, Financial Model (unit economics, scenario analysis, runway), Pitch Deck Narrative & Visual Design, Data Room Checklist, Product Scorecard (PMF evidence), Pipeline/GTM Evidence Summary, Risk Analysis.

## Validation
`14-validation-skill` (COO-Agent) checks that the narrative CEO-Agent is telling and the numbers CFO-Agent is showing actually agree — a common failure here is a growth story that the burn-rate math doesn't support. If `critic-agent/` is active, have it specifically red-team the pitch narrative for claims an investor's diligence would immediately puncture. Any ROI, TCO, or scenario claim in the deck should trace to `59-problem-solving-decision-modeling-skill`'s formula selection (`FORMULA_LIBRARY.md`) rather than an unsupported number — this is the single most common thing diligence catches.

## Risks
- Pitching a narrative the unit economics don't yet support
- Treating "investor-ready" as a deck-design problem instead of a traction-and-numbers problem
- Skipping technical/hardware diligence prep entirely when the product is hardware, because the default routing leans software-first if not corrected
- Deck design treated as a template exercise the night before the pitch instead of a CBO-Agent narrative-arc pass that makes the numbers land in the order investors actually process them

## Final Outputs
One merged investor-readiness narrative spanning strategy, narrative arc, numbers, product evidence, and pipeline evidence — read as one story, not four separate memos — plus a concrete data room checklist and a stated risk analysis.

## Example Prompt
*"Make the company investor-ready for a raise in the next few months — what do we need across the narrative, the numbers, and the data room?"*
