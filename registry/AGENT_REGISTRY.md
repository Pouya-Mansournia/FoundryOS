# Agent Registry

This registry is the canonical reference for every Agent in FoundryOS. Each Agent owns a fixed set of Skills (see [SKILL_REGISTRY.md](SKILL_REGISTRY.md)) and is the unit the Meta-Agent routes work to. Skill ownership shown here mirrors the live `agents/{Role}-Agent/AGENT.md` files — if the two ever disagree, the AGENT.md files win.

Total: **10 Agents** managing **59 Skills** (one Skill, `35-npi-manufacturing-skill`, is intentionally co-owned by COO-Agent and CIO-Agent), under **1 Meta-Agent**.

---

## CEO-Agent

**Purpose:** Owns company identity, governance, and the orchestration layer that keeps every other agent's output aligned with one strategy and one narrative.

**Responsibilities:**
- Maintain the company's vision, mission, values, and brand identity as a durable reference document
- Define org structure, governance model, and board-level reporting cadence
- Assign ownership through RACI and structure the recurring reviews that keep execution accountable
- Hold the meta-orchestration layer that sequences phases and coordinates agents across the whole OS

**Skills:**

| Skill | What It Does |
|---|---|
| `12-company-bible-skill` | Captures vision, mission, values, and long-term identity as a durable reference |
| `13-corporate-os-skill` | Defines org structure, governance, and board-level reporting; preserves institutional knowledge |
| `19-raci-meeting-skill` | Assigns ownership across functions and structures recurring reviews/meetings |
| `40-meta-orchestration-skill` | Orchestrates FoundryOS end to end — phase sequencing, agent coordination, recursive improvement |
| `59-problem-solving-decision-modeling-skill` | Frames ambiguous problems, builds causal/metric models, and selects reusable quantitative formulas for an evidence-based decision |

**Typical Outputs:** Vision & Mission, Values & Principles, Org Structure, Governance Model, OKRs/KPIs, Board Update Template, RACI Matrix, Decision Log, Lifecycle Orchestration Plan, Full Module Map / System Index, Decision Memo & Quantitative Decision Model

**Dependencies:** None upstream — CEO-Agent runs first in any multi-agent flow and sets the strategic framing every other agent aligns to. Every other agent's output should trace back to CEO-Agent's stated strategy.

---

## CPO-Agent

**Purpose:** Owns the product: customer discovery, market position, product strategy, requirements, and the scorecards that prove product-market fit.

**Responsibilities:**
- Run customer discovery — problem statements, ICP, personas, JTBD, user journeys
- Size the market and benchmark the opportunity against competitors and industry standards
- Build and stress-test product strategy, positioning, and business model
- Turn a validated opportunity into a structured PRD
- Define what to measure and track toward product-market fit

**Skills:**

| Skill | What It Does |
|---|---|
| `01-discovery-skill` | Defines the problem, customer, ICP, persona, JTBD, and discovery questions |
| `02-market-research-skill` | Sizes the market, profiles competitors, benchmarks the opportunity |
| `03-strategy-skill` | Builds and stress-tests core strategy, positioning, and business model |
| `04-prd-skill` | Turns a validated opportunity into a structured PRD |
| `10-analytics-skill` | Defines what to measure and builds dashboards for product/engineering/business health |
| `15-framework-library-skill` | Supplies standard frameworks, patterns, and anti-patterns for each OS stage |
| `27-product-scorecard-skill` | Scores product health against PMF, retention, and reliability metrics |

**Typical Outputs:** ICP & Personas, JTBD, TAM/SAM/SOM, Competitor Analysis, UVP, Business Model Canvas, PRD, North Star Metric, Product Scorecard

**Dependencies:** Consumes CEO-Agent's strategic framing. Feeds CTO-Agent / CIO-Agent (what to build), CRO-Agent / CMO-Agent (positioning), and CFO-Agent (pricing inputs).

---

## CTO-Agent

**Purpose:** Owns the technology stack: system and software architecture, AI/ML systems, and engineering execution.

**Responsibilities:**
- Define system, software, data, and AI architecture and review it for scalability and security
- Convert architecture and requirements into an executable engineering plan
- Own SaaS product architecture and modern software engineering practice (CI/CD, microservices)
- Design AI/ML systems: data strategy, model selection, evaluation, governance
- Maintain technical documentation and the cross-artifact knowledge graph; run recursive improvement loops on technical artifacts

**Skills:**

| Skill | What It Does |
|---|---|
| `05-architecture-skill` | Defines system, software, data, AI, and hardware architecture; reviews for scalability/security |
| `06-engineering-execution-skill` | Converts architecture and requirements into an executable engineering plan |
| `17-diagram-skill` | Generates the right diagram/visualization for a given artifact |
| `20-technical-documentation-skill` | Produces formal technical documentation (SRS, architecture docs, API specs) |
| `21-ai-product-skill` | Defines data, model, and evaluation strategy for an AI feature, plus governance |
| `24-saas-product-skill` | Defines multi-tenant SaaS architecture and engineering/data/AI foundations |
| `25-prompt-loop-skill` | Runs recursive discover/validate/refine loops across artifacts |
| `26-knowledge-graph-skill` | Maps how every artifact, decision, and module connects |
| `29-software-engineering-skill` | Applies modern software engineering practice; reviews for evolvability |
| `30-data-architecture-skill` | Designs data models, pipelines, and governance feeding analytics/AI |
| `31-ai-architecture-skill` | Designs AI system architecture (RAG, MLOps, evaluation, safety) |

**Typical Outputs:** System Architecture, Tech Stack, ADRs, WBS/Backlog/Sprint Plan, SaaS Architecture, Data Models, AI Architecture (RAG/MLOps), SRS, Knowledge Graph

**Dependencies:** Consumes CPO-Agent's PRD/requirements. Works alongside CIO-Agent when hardware or robotics is in scope. Feeds COO-Agent (turn the design into an operating plan) and CFO-Agent (cost of engineering).

---

## CIO-Agent

**Purpose:** Chief Innovation Officer — owns cross-domain hardware innovation: hardware and robotics product design, mechanical/electronics/embedded engineering, mechatronics integration, and the NPI handoff that turns R&D into shippable hardware.

**Responsibilities:**
- Lead hardware and robotics product design end to end, including sensing, navigation, and safety/reliability
- Own mechanical, electronics, and embedded engineering as one integrated mechatronics discipline
- Run DFM/DFA review and regulatory compliance checks for hardware
- Own the NPI handoff that turns validated R&D into shippable hardware (shared accountability with COO-Agent on production ramp)

**Skills:**

| Skill | What It Does |
|---|---|
| `22-hardware-product-skill` | Carries hardware from DFM through NPI and regulatory compliance to production |
| `23-robotics-product-skill` | Covers the robotics stack — sensing, embedded control, mechanical, electronics — with safety built in |
| `32-embedded-skill` | Designs firmware, RTOS, and driver layer for embedded hardware |
| `33-mechanical-skill` | Handles mechanical design validation — tolerancing, FEA, DFM |
| `34-electronics-skill` | Designs PCB, power, and signal integrity against EMC/regulatory requirements |
| `35-npi-manufacturing-skill` *(shared with COO-Agent)* | Runs NPI from EVT/DVT/PVT through manufacturing ramp and supplier qualification |
| `41-mechatronics-skill` | Integrates mechanical, electronics, and embedded into one validation pass into NPI |

**Typical Outputs:** DFM/DFA Review, BOM, EVT/DVT/PVT Plan, Robotics Architecture, GD&T Specification, FEA Results, PCB Design Review, Firmware Architecture, NPI Plan, Regulatory Compliance Plan

**Dependencies:** Consumes CPO-Agent's product requirements. Works alongside CTO-Agent on system-level architecture. Hands off to COO-Agent for manufacturing ramp (co-owns `35-npi-manufacturing-skill`). Feeds CFO-Agent (hardware cost structure, CAPEX).

---

## COO-Agent

**Purpose:** Owns operations: manufacturing, supply chain, NPI, process governance, scaling logistics, and risk.

**Responsibilities:**
- Define SOPs, supply chain, procurement, and manufacturing flow
- Run stage-gate go/no-go reviews from discovery through production readiness
- Validate every artifact for gaps, contradictions, and missing dependencies before it passes a gate
- Plan scaling — portfolio, geography, partnerships, compounding growth loops
- Maintain the risk register and crisis/resilience plans

**Skills:**

| Skill | What It Does |
|---|---|
| `09-operations-skill` | Defines operating procedures, supply chain, and manufacturing flow, plus contingency plans |
| `11-scaling-skill` | Plans portfolio, geography, partnership, and compound-growth scaling |
| `14-validation-skill` | Audits every artifact for gaps/contradictions before a stage gate |
| `16-artifact-template-skill` | Provides canonical templates and tracks artifact dependencies |
| `18-stage-gate-skill` | Runs go/no-go reviews at each phase boundary through production readiness |
| `28-risk-management-skill` | Identifies, registers, and mitigates risk; builds resilience against shocks |
| `35-npi-manufacturing-skill` *(shared with CIO-Agent)* | Runs NPI from EVT/DVT/PVT through manufacturing ramp and supplier qualification |

**Typical Outputs:** SOPs, Supply Chain Plan, Stage Gate Checklist, Go/No-Go Decision, Risk Register, Scaling Roadmap, Production Readiness Assessment, NPI Plan

**Dependencies:** Consumes CTO-Agent's / CIO-Agent's feasible designs. Co-owns `35-npi-manufacturing-skill` with CIO-Agent for hardware production ramp. Feeds CFO-Agent (operating cost structure).

---

## CFO-Agent

**Purpose:** Owns the numbers: unit economics and financial planning, plus the fundraising and investor narrative built on top of them.

**Responsibilities:**
- Model unit economics, pricing, P&L, cash flow, CAPEX/OPEX, burn rate, and runway
- Build scenario analysis (best/base/worst case)
- Prepare the fundraising narrative, data room, and investor/board communication

**Skills:**

| Skill | What It Does |
|---|---|
| `07-finance-skill` | Models unit economics, pricing, and financial scenarios |
| `38-fundraising-investor-skill` | Prepares fundraising narrative, data room, and investor/board communication |

**Typical Outputs:** Unit Economics, P&L, Cash Flow, Burn Rate / Runway, Scenario Analysis, Pitch Narrative, Data Room Checklist, Investor Update Template

**Dependencies:** Consumes cost/scope inputs from CTO-Agent / CIO-Agent / COO-Agent and the revenue model from CPO-Agent / CRO-Agent. Feeds CRO-Agent (pricing) and CEO-Agent (board/investor narrative).

---

## CRO-Agent

**Purpose:** Owns revenue: go-to-market motion and pricing, and the sales pipeline that turns positioning into bookings.

**Responsibilities:**
- Plan channel strategy, funnel design, and sales process/pipeline
- Set the pricing and packaging model
- Align the GTM motion with customer success and retention

**Skills:**

| Skill | What It Does |
|---|---|
| `08-gtm-skill` | Plans how the product reaches, converts, and retains customers |
| `36-pricing-sales-skill` | Sets pricing/packaging and builds the sales motion around it |

**Typical Outputs:** Positioning & Messaging, Channel Strategy, Sales Process & Pipeline, Pricing Strategy & Packaging, GTM Metrics

**Dependencies:** Consumes CFO-Agent's pricing economics and CPO-Agent's positioning. Feeds CMO-Agent (campaigns) and CFO-Agent (revenue forecast).

---

## CMO-Agent

**Purpose:** Owns demand and retention: marketing campaigns and the customer success loop that keeps acquired customers. (Brand strategy, identity, and voice belong to CBO-Agent — CMO-Agent executes campaigns inside the brand system CBO-Agent defines, it doesn't define the system itself.)

**Responsibilities:**
- Plan demand generation, content, and campaign calendars
- Run onboarding and retention programs
- Track customer health through dashboards

**Skills:**

| Skill | What It Does |
|---|---|
| `37-marketing-customer-success-skill` | Plans demand gen/content alongside onboarding/retention, with health dashboards |

**Typical Outputs:** Demand Gen & Content Plan, Campaign Calendar, Onboarding & Retention Plan, Customer Health Dashboard

**Dependencies:** Consumes CRO-Agent's GTM motion and CPO-Agent's positioning. Typically runs in parallel with CRO-Agent.

---

## CBO-Agent

**Purpose:** Owns the brand: strategy, identity systems, voice, visual design, content, community, and the rollout roadmap. Where CPO-Agent owns what the product does, CBO-Agent owns what it means and how it's recognized.

**Responsibilities:**
- Define brand strategy, archetype, and architecture, and audit the gap between brand intent and current state
- Compile the brand book — guidelines and governance that keep every surface on-brand
- Build the design system (components, tokens, color, typography, UI patterns) and the logo system that sits inside it
- Name the company, product, or feature, and screen candidates for trademark/domain conflicts
- Define positioning and category claim in close coordination with CPO-Agent and CRO-Agent
- Own the brand narrative — storytelling, voice, tone, and copywriting — and the content/social systems that distribute it
- Design community strategy and engagement, and manage the brand asset library
- Sequence brand rollout into a dated roadmap with health metrics

**Skills:**

| Skill | What It Does |
|---|---|
| `42-brand-strategy-skill` | Defines brand archetype, architecture, and audits brand intent vs. current state |
| `43-brand-book-skill` | Compiles the brand book — guidelines and governance |
| `44-design-system-skill` | Builds the reusable design system — components, tokens, layout rules |
| `45-content-system-skill` | Plans content structure, cadence, and taxonomy |
| `46-logo-system-skill` | Designs the logo system — mark, lockups, construction grid, usage rules |
| `47-naming-skill` | Generates and screens naming candidates |
| `48-positioning-skill` | Defines category claim, differentiation, and positioning statement |
| `49-community-skill` | Designs community structure, engagement, and moderation |
| `50-social-assets-skill` | Produces platform-specific social templates and calendar |
| `51-storytelling-skill` | Builds the brand's origin story and narrative arc |
| `52-copywriting-skill` | Writes headline systems and microcopy |
| `53-voice-tone-skill` | Defines brand voice and tone spectrum by channel |
| `54-color-psychology-skill` | Selects and validates the color palette |
| `55-typography-skill` | Sets type scale and font pairing |
| `56-ui-system-skill` | Extends the design system into iconography and motion |
| `57-brand-assets-management-skill` | Organizes the asset library, naming, and versioning |
| `58-brand-roadmap-skill` | Sequences brand rollout into a dated roadmap with metrics |

**Typical Outputs:** Brand Strategy Brief, Brand Book, Design System Spec, Logo System, Naming Shortlist, Positioning Statement, Origin Story, Voice Guidelines, Color Palette, Type Scale, Community Strategy, Brand Roadmap

**Dependencies:** Consumes CEO-Agent's vision/values and CPO-Agent's positioning inputs. Works alongside CRO-Agent and CMO-Agent on go-to-market messaging — CBO-Agent defines the identity, CMO-Agent and CRO-Agent activate it in campaigns and channels. Feeds every customer-facing Agent (CEO, CPO, CRO, CMO) a consistent name, voice, and visual system to build on.

---

## CHRO-Agent

**Purpose:** Owns the team: hiring, org design, compensation, performance, and culture as the company scales.

**Responsibilities:**
- Design hiring scorecards and interview loops
- Define org design, compensation/leveling, and performance review process
- Protect culture and operating values while the team scales

**Skills:**

| Skill | What It Does |
|---|---|
| `39-people-culture-skill` | Designs hiring, org structure, compensation, and performance system that scale the team without losing culture |

**Typical Outputs:** Hiring Scorecards & Interview Loops, Org Design, Compensation & Leveling Framework, Performance Review Process, Culture & Operating Values

**Dependencies:** Runs last in the default execution order — staffs whatever the combined plan from the other agents requires (headcount implied by CTO/CIO/COO scope, budget implied by CFO).

---

## Meta-Agent

**Purpose:** Central orchestrator for FoundryOS. Owns no domain content itself — it classifies the request, selects which of the 10 Agents and Skills should run, sequences them, and merges their output into one executive answer.

**Responsibilities:**
- Classify incoming requests and select the right Agent(s) and Skill(s) using the live AGENT.md files as the source of truth
- Sequence agent execution according to real dependencies, not arbitrary order
- Merge multi-agent output into a single coherent voice — never disconnected per-agent answers
- Detect contradictions between agents and missing inputs; ask only critical clarifying questions, otherwise proceed on a stated assumption

**Skills:** None directly owned. Reads and routes to Skills owned by the 9 Agents.

**Typical Outputs:** Meta-Agent Result — Request Classification, Selected Agents, Selected Skills, Agent Execution Order, Combined Executive Answer, Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, Next Actions. Full spec: [`meta-agent/META_AGENT.md`](../meta-agent/META_AGENT.md).

**Dependencies:** Depends on all 10 Agents and reads their live `AGENT.md` Skills lists at run time rather than a hardcoded map, since ownership has changed before and will change again.
