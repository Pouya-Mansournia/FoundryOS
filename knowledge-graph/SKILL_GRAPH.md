# Skill Graph

## Purpose
Maps how the 58 Skills relate to each other within and across the Agents that own them — which Skills form a chain inside one Agent's work, which Skills are cross-cutting and used by many Agents, and where the one shared-ownership Skill sits.

## Nodes
58 Skills, grouped by owning Agent per `registry/SKILL_REGISTRY.md`. Eight Skills are cross-cutting (used in service of multiple Agents' work rather than belonging to one domain): `14-validation-skill`, `15-framework-library-skill`, `16-artifact-template-skill`, `17-diagram-skill`, `25-prompt-loop-skill`, `26-knowledge-graph-skill`, `28-risk-management-skill`, `40-meta-orchestration-skill`. Seventeen Skills (`42` through `58`) belong to CBO-Agent's brand domain.

## Relationships
- **Within-Agent chains** — Skills owned by the same Agent are typically used in sequence, not independently. Example, CPO-Agent: `01-discovery-skill → 02-market-research-skill → 03-strategy-skill → 04-prd-skill → 10-analytics-skill → 27-product-scorecard-skill`
- **Cross-cutting Skills** attach to whichever Agent is active rather than running standalone — `17-diagram-skill` is invoked by CTO-Agent for architecture diagrams and by COO-Agent for process flow diagrams, for instance
- **Shared-ownership Skill** — `35-npi-manufacturing-skill` is the one Skill with two owning Agents (CIO-Agent and COO-Agent) and should be invoked once, jointly, not duplicated when both Agents are in the execution set
- **Brand chain** — CBO-Agent's 17 Skills form their own within-Agent sequence, e.g. `42-brand-strategy-skill → 47-naming-skill / 48-positioning-skill → 43-brand-book-skill → 46-logo-system-skill → 44-design-system-skill → 53-voice-tone-skill → 51-storytelling-skill / 52-copywriting-skill → 49-community-skill / 50-social-assets-skill → 58-brand-roadmap-skill` — strategy and naming come first, the rest are downstream expressions of it
- **Brand reaches into other Agents' chains**, the only domain besides the shared NPI skill to do so deliberately: `53-voice-tone-skill` is invoked by CTO-Agent/CPO-Agent for in-product copy, `54-color-psychology-skill` and CMF-adjacent brand skills by CIO-Agent for physical products, and `52-copywriting-skill`/`50-social-assets-skill` by CMO-Agent for campaign content

## Dependencies
| Skill | Depends On (output of) |
|---|---|
| `04-prd-skill` | `01-discovery-skill` (problem/ICP must exist first) |
| `05-architecture-skill` | `04-prd-skill` (architecture follows requirements, not the reverse) |
| `07-finance-skill` | Cost/scope inputs from `05-architecture-skill`, `06-engineering-execution-skill`, `09-operations-skill`, or CIO-Agent's hardware skills |
| `08-gtm-skill` | `03-strategy-skill` (positioning) and `07-finance-skill` (pricing economics) |
| `36-pricing-sales-skill` | `07-finance-skill` (unit economics ceiling/floor on price) |
| `38-fundraising-investor-skill` | `07-finance-skill`, `27-product-scorecard-skill`, `08-gtm-skill` (the narrative is built on top of all three) |
| `41-mechatronics-skill` | `33-mechanical-skill`, `34-electronics-skill`, `32-embedded-skill` (integrates the three) |
| `35-npi-manufacturing-skill` | `41-mechatronics-skill` or `22-hardware-product-skill` (manufacturing follows a validated design) |
| `18-stage-gate-skill` | Whatever artifact is being gated — runs after, not before, the artifact exists |
| `14-validation-skill` | Same — runs after an artifact exists, checking it rather than producing it |
| `47-naming-skill` / `48-positioning-skill` | `42-brand-strategy-skill` (archetype and strategy must exist before a name or position is chosen) |
| `46-logo-system-skill` | `43-brand-book-skill` and `42-brand-strategy-skill` (the mark expresses a strategy already set, not the reverse) |
| `44-design-system-skill` | `46-logo-system-skill` (the broader system extends the mark, not the other way around) |
| `53-voice-tone-skill` | `42-brand-strategy-skill` (voice is a strategy expression) and feeds `52-copywriting-skill` |
| `57-brand-assets-management-skill` | `46-logo-system-skill` and `44-design-system-skill` (the asset library packages and version-controls what those two skills produce) |
| `58-brand-roadmap-skill` | All 16 other brand Skills (it sequences the rollout of everything CBO-Agent has already decided) |

## Graph Structure
```
Discovery & Strategy        Build/Design               Operate & Scale         Money & Growth
01-discovery        ─┐    05-architecture  ─┐      09-operations    ─┐    07-finance      ─┐
02-market-research   │    06-engineering    │      11-scaling        │    08-gtm           │
03-strategy           │    21/24/31 (AI/SaaS)│      18-stage-gate     │    36-pricing-sales  │
04-prd                │    22/23/32/33/34/41 │      28-risk-mgmt      │    37-marketing-cs   │
10-analytics          │    (hardware/robotics)│      35-npi (shared)   │    38-fundraising    │
27-product-scorecard ─┘    20-technical-docs ─┘      14-validation ───┘    39-people-culture ─┘
                                                                                    13-corporate-os
                      Cross-cutting (attach to whichever Agent is active):
                      15-framework-library · 16-artifact-template · 17-diagram
                      25-prompt-loop · 26-knowledge-graph · 40-meta-orchestration
                      12-company-bible · 19-raci-meeting

                      Brand & Identity (CBO-Agent, 17 Skills):
                      42-brand-strategy ─┬─ 47-naming           ─┐
                                          └─ 48-positioning      │
                      43-brand-book ───────── 46-logo-system ────┤
                      44-design-system ── 54-color-psychology    │  reaches into
                      45-content-system ── 51-storytelling ─────┤  CTO/CIO/CMO/CHRO
                      52-copywriting ── 53-voice-tone ───────────┤  chains where a
                      49-community ── 50-social-assets ──────────┤  customer-facing
                      55-typography ── 56-ui-system ─────────────┤  surface ships
                      57-brand-assets-management (packages 46+44)│
                      58-brand-roadmap ─────────────────────────┘  (sequences all 16 above)

                      Note: skill 57 was originally drafted as a second
                      "logo-system-skill," colliding with skill 46. Renamed
                      to 57-brand-assets-management-skill — the asset
                      library/versioning function it actually performs.
                      Flagged in AUDIT_REPORT.md.
```

## Examples
A fundraising request invokes `38-fundraising-investor-skill`, which depends on `07-finance-skill` (the model), `27-product-scorecard-skill` (PMF evidence from CPO-Agent), and `08-gtm-skill` (pipeline evidence from CRO-Agent) — three Skills under three different Agents feeding one Skill's output, which is exactly why `06-fundraising-workflow` is unconditionally multi-agent. The deck's narrative arc and visual design pull `51-storytelling-skill` and `44-design-system-skill` from CBO-Agent the same way — a fifth Skill, fourth Agent, feeding the same artifact.
