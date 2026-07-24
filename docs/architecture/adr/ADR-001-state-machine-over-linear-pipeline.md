# ADR-001 — Why a Reasoning State Machine Instead of a Linear Prompt Pipeline

## Context
FoundryOS's 11 `workflows/*/WORKFLOW.md` files today are prose/step-lists: a fixed agent-execution order with no explicit state IDs, no transition table, and no pause/resume mechanism (confirmed in Phase 0's audit). This works for a single-turn request but cannot support research loops, clarification loops, critique loops, or a run that pauses for days awaiting human evidence review — all required by the Mandatory First Product Workflow (Idea Discovery) and by the Constitution's Human Authority principle.

## Decision
Implement the Product Thinking Engine as an explicit state machine (Layer 3 in `../TARGET_ARCHITECTURE.md`): named states with entry/exit conditions, allowed capabilities, output schema, retry policy, and a defined set of possible next states. Invalid transitions are rejected, not silently absorbed into "the assistant improvises."

## Alternatives Considered
- **Keep the linear pipeline, add more prose steps.** Rejected: cannot express backward transitions (e.g., evidence review sends the run back to Discovery), cannot express a rejectable/pausable gate, and cannot be resumed reliably across sessions without an explicit "where am I" state.
- **A single giant prompt that "decides everything."** Rejected: violates Constitution Principle 6 (Critique Before Approval) and 8 (Traceability) — an undifferentiated prompt cannot be audited for which transition happened and why.

## Consequences
- Introduces the repository's first genuinely new infrastructure concept (state + transition + registry), built in Phase 2, before any concrete workflow uses it.
- Requires a decision (deferred to Phase 2 kickoff, see evolution DECISION_LOG ADR-0003) on whether states are held as structured markdown or as code-backed state files.
- Existing `workflows/*/WORKFLOW.md` files are not rewritten by this decision — new state-machine-backed workflows are additive (Phase 3), per Architecture Principle 1.

## Status
Accepted.
