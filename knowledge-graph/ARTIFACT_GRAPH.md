# Artifact Graph

## Purpose
Maps how the concrete deliverables Workflows produce depend on each other — which artifact is always built from another, so a downstream artifact built before its upstream dependency is stable is a structural warning sign, not just a sequencing preference.

## Nodes
Problem Statement, ICP & Personas, Competitor/Market Snapshot, PRD, Positioning Statement, Naming Shortlist, Brand Strategy Brief, Logo System & Brand Book, Design System & CMF Spec, Voice & Tone Guide, System/SaaS/AI Architecture, Hardware/Robotics Architecture (Mechanical/Electronics/Embedded), BOM, Manufacturing/NPI Plan, Financial Model, Pricing & Packaging, Campaign Copy & Social Assets, GTM Plan, Pitch Deck/Investor Narrative (with Narrative Arc), Org Structure, Employer Brand & Internal Voice Guide, Role Definition, Risk Register, Product Scorecard, Evaluation Metrics (AI), Roadmap, Brand Roadmap, **Decision Memo** (with its Problem Frame, Causal Model, Metric Tree, Hypothesis Register, Formula Sheet, Decision Matrix, Scenario Model, Experiment Plan, and Post-Decision Review).

## Relationships
- **PRD** is the hinge artifact — almost every downstream artifact in a product workflow depends on it, and it itself depends on Problem Statement + ICP
- **Architecture** (software, hardware, or AI) always follows PRD, never precedes it — an architecture built before requirements are stable is the single most common rework trigger across all five product workflows
- **Positioning Statement, Naming Shortlist, and Brand Strategy Brief** sit right after PRD and right before Architecture — CBO-Agent attaches identity to what CPO-Agent just defined before CTO-Agent/CIO-Agent build it, which is why these are upstream of Architecture, not a post-launch afterthought
- **Logo System & Brand Book** and **Design System & CMF Spec** depend on Brand Strategy Brief, and themselves become inputs Architecture/BOM should build against (UI components against Design System tokens; physical housing against the CMF Spec)
- **Financial Model** depends on whichever cost-generating artifact exists for the product type: Architecture's engineering cost (software), BOM's unit cost (hardware), or both
- **Pitch Deck / Investor Narrative** is a synthesis artifact — it depends on Financial Model, Product Scorecard, GTM Plan, and CBO-Agent's Narrative Arc + visual design simultaneously, which is why `06-fundraising-workflow` is unconditionally multi-agent
- **Campaign Copy & Social Assets** depends on Positioning Statement and Voice & Tone Guide, and itself feeds GTM Plan — positioning locked once, expressed consistently across every channel
- **Employer Brand & Internal Voice Guide** depends on Brand Strategy Brief and feeds Role Definition whenever a posting is externally visible
- **Roadmap** can refer to a product roadmap (CPO-Agent, depends on PRD), a strategic roadmap (CEO-Agent, depends on Vision/Strategy), or a **Brand Roadmap** (CBO-Agent, depends on Brand Strategy Brief + Positioning) — three related but distinct nodes; check which one a workflow means
- **Decision Memo** is not downstream of the other artifacts the way they're downstream of each other — it's produced by `59-problem-solving-decision-modeling-skill` directly off the raw Problem Statement, *before* a PRD, Architecture, or Financial Model necessarily exists, and its own Decision Matrix/Formula Sheet frequently becomes an input those other artifacts are built against (e.g. a build-vs-buy Decision Memo determines whether an Architecture node gets built at all)

## Dependencies
```
Problem Statement → ICP & Personas → PRD
PRD → Positioning Statement / Naming Shortlist / Brand Strategy Brief
Brand Strategy Brief → Logo System & Brand Book → Design System & CMF Spec → Voice & Tone Guide
PRD + Design System/CMF → Architecture (SW/HW/AI) → BOM (hardware only)
Architecture/BOM → Financial Model
Positioning Statement + Voice & Tone Guide → Campaign Copy & Social Assets
Financial Model + Campaign Copy → Pricing & Packaging → GTM Plan
PRD + Architecture → Roadmap (product)
Brand Strategy Brief + Positioning → Brand Roadmap
Financial Model + Product Scorecard + GTM Plan + Narrative Arc (CBO) → Pitch Deck / Investor Narrative
Vision/Strategy (CEO) → Strategic Roadmap → [feeds Problem Statement of the next cycle]
Brand Strategy Brief → Employer Brand & Internal Voice Guide
Org needs (implied by Architecture/BOM/Roadmap scope) + Employer Brand → Role Definition
Risk Register is produced alongside every artifact above it, not just at the end
```

## Graph Structure
```
Problem Statement
       ↓
ICP & Personas ──────────┐
       ↓                  │ (also feeds GTM Plan directly)
      PRD                 │
       ↓                  │
Positioning / Naming /     │
Brand Strategy Brief       │
       ↓                  │
Logo System & Brand Book   │
       ↓                  │
Design System & CMF Spec   │
       ↓        ↓          │
Voice & Tone   Architecture │
   Guide       (SW/HW/AI)   │
       │           ↓        │
       │       BOM (hardware only)
       │           ↓        │
       │      Financial Model
       │           ↓        │
       └──→ Campaign Copy & Social Assets
                    ↓        │
        Pricing & Packaging ←┘
                    ↓
                GTM Plan
                    ↓
        ├──────────────→ Pitch Deck / Investor Narrative
        │                  (also pulls Product Scorecard +
        │                   CBO-Agent's Narrative Arc)
        ↓
    Roadmap ──── Brand Roadmap
        ↓
Employer Brand & Internal Voice Guide
        ↓
Role Definition (if headcount implied)

Risk Register: attached at every node above, not a single terminal artifact
```

## Examples
A robotics product's artifact chain runs `Problem Statement → ICP → PRD → Naming & CMF Spec (CBO-Agent) → (Mechanical + Electronics + Embedded Architecture, integrated via 41-mechatronics-skill, built against that CMF) → BOM → Manufacturing/NPI Plan → Financial Model`. If `06-fundraising-workflow` then needs a Pitch Deck, it pulls Financial Model, Product Scorecard, GTM Plan, and CBO-Agent's Narrative Arc from this chain rather than regenerating any of them — exactly the dependency `knowledge-graph/WORKFLOW_GRAPH.md` describes at the workflow level.
