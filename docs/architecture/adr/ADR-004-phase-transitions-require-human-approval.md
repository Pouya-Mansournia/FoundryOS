# ADR-004 — Why Phase Transitions Require Human Approval

## Context
The governing mission for this evolution is explicit: the coding agent must never automatically continue to the next phase, must stop at phase boundaries, and must resume only from an explicitly approved state. This mirrors Constitution Principle 7 (Human Authority) at the process level, not just the product-decision level.

## Decision
Every phase (0–9) ends in `AWAITING_APPROVAL` regardless of how confident the implementation is. The next phase begins only after an unambiguous human approval is recorded in the evolution's phase-tracking Approval Log. Ambiguous responses do not count as approval.

## Alternatives Considered
- **Auto-advance when acceptance criteria pass.** Rejected: acceptance criteria can be met while the human owner still wants to redirect scope, priorities, or sequencing — automation cannot know that. Also directly contradicts the mission's explicit instruction.
- **Batch multiple phases per approval ("approve phases 1–3 now").** Rejected as the default: each phase's deliverable can meaningfully change what the next phase should even build (e.g. Phase 2's format decision affects Phase 3's design). A human is free to explicitly grant a broader approval, but the system does not assume it.

## Consequences
- Every phase document must end with a specific, answerable approval question (not "let me know if this looks good").
- `PHASE_STATUS.md` is the single source of truth for whether approval has been given; a phase is never marked `COMPLETED` retroactively without a recorded approval event.

## Status
Accepted.
