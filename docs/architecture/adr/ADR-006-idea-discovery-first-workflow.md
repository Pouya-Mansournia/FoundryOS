# ADR-006 — Why the First Workflow Is Idea Discovery

## Context
The governing mission designates a specific Mandatory First Product Workflow (Idea Received → ... → Decision Gate, with outcomes like USE_EXISTING / ADAPT_EXISTING / COMBINE_SOLUTIONS / CONTINUE_NEW_PRODUCT_DISCOVERY / PAUSE_FOR_VALIDATION / REJECT_OR_ARCHIVE). FoundryOS already has a partial, prose version of this: `workflows/01-new-product-workflow/WORKFLOW.md` and `skills/01-discovery-skill/SKILL.md` cover problem/customer discovery, but neither currently forces existing-solution research before product design, nor exposes an explicit decision gate that can end in "don't build this."

## Decision
The first Reasoning State Machine vertical slice (Phase 3) implements Idea Discovery, reusing and extending `01-discovery-skill` and `01-new-product-workflow` rather than building a parallel discovery process. This directly enforces Constitution Principle 3 (Research Before Reinvention) and Principle 2 (Problem Before Solution) as a hard gate — the state machine cannot skip to product design without passing through existing/adjacent/historical-attempt discovery first.

## Alternatives Considered
- **Start with a different vertical slice (e.g. a decision-modeling workflow) since skill 59 is already closer to a state-machine shape.** Rejected: skill 59 already runs standalone for decisions; the bigger gap and bigger risk (premature building) is in *new product* discovery, which is FoundryOS's stated core use case per `README.md`'s Quick Start.
- **Build a net-new Idea Discovery process instead of extending `01-discovery-skill`.** Rejected: violates Architecture Principle 1 (Extension Over Replacement) — duplicates working content for no reason.

## Consequences
- Phase 3's states (`IDEA_RECEIVED` through `DECISION_GATE`/`ARCHIVED`) must be designed as a superset of what `01-discovery-skill` and `01-new-product-workflow` already do, not a rewrite.
- The Decision Gate's six outcomes must be reachable from real evidence review, meaning Phase 3 has an implicit dependency on at least a minimal version of the Evidence Engine (Layer 4) — flagged for Phase 3 kickoff, may require a thin Phase 4 slice pulled earlier if Phase 3 can't produce a meaningful gate without it.

## Status
Accepted.
