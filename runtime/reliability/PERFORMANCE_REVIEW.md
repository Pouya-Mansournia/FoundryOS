# Performance Review

Status: Phase 8 deliverable. "Performance" for a markdown-only, assistant-hosted system means file/context growth discipline, not latency or throughput — reviewed honestly against that actual constraint.

## Finding 1: Run Directories Grow Without Bound Today

Each run accumulates `run-state.md`, `state-history.md`, `approvals.md`, and (depending on workflow) `evidence-ledger.md`, `orchestration-log.md`, `plan.md`, `execution-log.md`, `reflection.md`, `lessons-queue.md` — up to 9 files for a full Idea-Discovery-through-Reflection run. Every file is append-only by design (Constitution Principle 8, Traceability) — none are ever pruned. A long-lived, heavily-retried, many-times-paused-and-resumed run could accumulate a genuinely large `state-history.md`.

**Assessment**: Not a problem yet — every demo run in this evolution is small (≤14 entries in any single log). But it is a real, foreseeable scaling limit: a hosting assistant reading a very large `state-history.md` in full (per the Cold-Start Resume Procedure) consumes real context-window budget, and at some size this becomes the practical constraint, not any conceptual one.

**Recommendation, not implemented this phase**: for a run whose logs grow very large, a future phase could define a "checkpoint" convention — a periodic summary entry in `state-history.md` that lets a resuming assistant read the checkpoint plus only the entries after it, rather than the full history from the start. Not needed by anything built so far; flagged as a Phase 9+ candidate if real usage ever produces a run this large.

## Finding 2: `evidence-ledger.md` Has No Practical Size Limit Either

Same pattern as Finding 1 — a long research phase could accumulate many evidence entries. `SOURCE_QUALITY_RULES.md` and `EVIDENCE_LEDGER_CONTRACT.md` don't currently address when a ledger has "enough" evidence to proceed to Evaluation. This is a genuine open question, not answered by this review: at what point does more evidence stop improving decision quality and start being a stalling tactic (the opposite failure mode from the "don't build on too little evidence" problem this whole evolution exists to prevent)? Not resolved here — noted as an open question for whoever runs the next real (non-demo) Idea Discovery pass to watch for.

## Finding 3: No Actual Performance Problem Exists in Any Demo Run

Checked directly: every demo run across Phases 2–7 completed in a bounded, small number of states and log entries. Nothing in this evolution has actually hit a real scaling wall — Findings 1–2 above are forward-looking risk identification, not observed problems.

## Deterministic Test Fixtures

Per the mission's Phase 8 deliverable list: the four demo runs already built (`demo-0001`, `idea-discovery-demo-0001`, `adapt-release-drafter-demo-0001`, and this phase's `interrupted-demo-0001`) **are** this evolution's deterministic test fixtures — each is a fixed, real, checked-in example a future phase or a future contract change can be re-validated against (per `../state-machine/TEST_HARNESS.md`'s "How to Re-Run This Test" pattern, already established in Phase 2). No new fixture format is introduced; the existing demo runs are formally designated as the fixture set going forward.

## Summary

No critical performance issue found. Two forward-looking scaling risks identified and explicitly not solved prematurely (checkpointing, evidence-sufficiency), consistent with Architecture Principle 3 (Contracts Before Implementation) — not building infrastructure for a problem that hasn't occurred yet.
