# Workflow Graph

## Purpose
Maps how the 10 Workflows relate to each other — which ones are general-purpose versus specialized, which ones consume another workflow's output as their starting input, and which ones sit above the rest as ongoing, periodic passes rather than one-off runs.

## Nodes
`01-new-product-workflow`, `02-saas-product-workflow`, `03-hardware-product-workflow`, `04-ai-product-workflow`, `05-robotics-product-workflow`, `06-fundraising-workflow`, `07-go-to-market-workflow`, `08-company-building-workflow`, `09-hiring-workflow`, `10-strategic-planning-workflow`.

## Relationships
- **01 is the general case**; **02, 03, 04, 05 are specializations** of it for a specific product type (SaaS, hardware, AI, robotics respectively) — each skips or adds Agents relative to 01 based on what that product type actually needs
- **06 (Fundraising) and 07 (GTM) are consumers**, not originators — they assume a product (from 01/02/03/04/05) and a company (from 08) already exist, and build a narrative or motion on top of what those produced — 07 specifically also assumes CBO-Agent's positioning groundwork already exists, flagging it as a missing input and routing back to CBO-Agent if it doesn't
- **08 (Company Building) and 10 (Strategic Planning) are foundational/periodic** — they're not triggered by a single product decision, they set the structure and direction the product-specific workflows operate inside
- **09 (Hiring) is triggered by**, not sequenced before, the others — a hiring need surfaces as a side effect of 01/03/05 (headcount to build something) or 08 (headcount to operate at the new structure)
- **CBO-Agent runs inside 9 of the 10 workflows by default** — naming/positioning in 01, in-product voice in 02, CMF/packaging in 03, AI persona in 04, naming/CMF/HRI cues in 05, narrative arc in 06, positioning/messaging first in 07, employer brand in 08, brand/positioning implications in 10. **09 (Hiring) is the deliberate exception** — CBO-Agent is conditional there, brought in only if a job posting is externally visible, consistent with 09's stated design as the most agent-light workflow in the system

## Dependencies
| Workflow | Assumes As Input (from) |
|---|---|
| 01 New Product | Company identity exists (or is being defined alongside, via CEO-Agent) |
| 02 SaaS Product | Can run standalone or as the CTO-path specialization of 01 |
| 03 Hardware Product | Can run standalone or as the CIO-path specialization of 01 |
| 04 AI Product | Can run standalone or nested inside 02 (an AI feature within a SaaS product) |
| 05 Robotics Product | Can run standalone or as the combined CIO+CTO specialization of 01 |
| 06 Fundraising | PRD/Architecture from 01-05 (product evidence), structure from 08 (company evidence), narrative arc from CBO-Agent |
| 07 Go-To-Market | ICP/positioning from 01-05's CPO-Agent and CBO-Agent steps — flagged as missing input if absent |
| 08 Company Building | Independent — typically triggered by a headcount or stage threshold, not by another workflow's output |
| 09 Hiring | Triggered by headcount implied by 01, 03, 05, or 08; CBO-Agent joins only if the posting is externally visible |
| 10 Strategic Planning | Independent — periodic; its outputs (Roadmap, Trade-offs, Brand Implications) become the input the other 9 workflows execute within |

## Graph Structure
```
                         10-strategic-planning (periodic, sets direction)
                                    ↓
                         08-company-building (foundational structure)
                                    ↓
        ┌───────────────────────────────────────────────────┐
        ↓               ↓               ↓               ↓
  01-new-product   02-saas-product 03-hardware-product 05-robotics-product
        │  (general case; 02/03/04/05 specialize from it)         │
        └──────────────────────┬──────────────────────────────────┘
                                ↓
                      04-ai-product (often nested inside 02,
                                      or standalone if cloud-only)
                                ↓
              ┌─────────────────┴─────────────────┐
              ↓                                     ↓
     07-go-to-market                       06-fundraising
   (consumes product +                    (consumes product +
    positioning evidence)                   company evidence)
                                ↓
                        09-hiring (triggered as a side effect
                                    of headcount implied above)
```

## Examples
A hardware startup runs `10-strategic-planning-workflow` to set the year's direction, which informs `03-hardware-product-workflow` for the core product. Once that product has a BOM and a manufacturing plan, `06-fundraising-workflow` consumes it as technical diligence evidence, and the resulting headcount need (more manufacturing/ops staff) triggers `09-hiring-workflow` — four workflows chained from one strategic decision, exactly the scenario `tests/05-full-system-test.md` exercises.
