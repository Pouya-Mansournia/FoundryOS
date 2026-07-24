# ADR-005 — Why Run State Is Persistent and Resumable

## Context
FoundryOS today is stateless per conversation turn — nothing about an in-progress Idea Discovery run (which state it's in, what evidence has been collected, what's awaiting human review) survives between sessions except whatever the human happens to paste back in. The Mandatory First Product Workflow explicitly requires pausing for human evidence review before deeper product design — which is meaningless without something durable to pause and resume.

## Decision
A run's state (current state ID, transition history, collected evidence references, pending approvals) is persisted, not just held in a single conversation's context. The exact storage mechanism (structured markdown vs. code-backed state files) is decided at Phase 2 kickoff per evolution DECISION_LOG ADR-0003 — this ADR fixes *that persistence must exist and support resume*, not the file format.

## Alternatives Considered
- **Rely on the human re-pasting context each session.** Rejected: fragile, loses traceability (Constitution Principle 8), and cannot support the pause states the Mandatory First Product Workflow requires (`WAITING_FOR_USER_EXPERIENCE`, etc.).
- **Persist only the final artifact, not the state history.** Rejected: loses the ability to show which transitions happened and why (Layer 3's requirement), and cannot support backward transitions (a research loop sending the run back to an earlier state).

## Consequences
- Introduces the repository's first persistent run-state concept — a `runs/` directory or equivalent, per the mission's suggested structure, adapted to whatever format Phase 2 chooses.
- Requires a state-history log (append-only) distinct from the current-state pointer, so resumed runs can show provenance, not just current status — mirrors the pattern `PHASE_STATUS.md`/`DECISION_LOG.md` already use for the evolution track itself.

## Status
Accepted.
