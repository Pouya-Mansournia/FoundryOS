# Run: demo-0001

- Goal: Prove the Phase 2 generic state-machine engine — exercise a valid transition, an invalid-transition rejection, a pause, a human-gated resume, and completion — without any product-specific content.
- Governing State Registry: `../../runtime/state-machine/STATE_REGISTRY.md`
- Created At: 2026-07-24T10:00:00Z
- Current State: COMPLETED
- Status: COMPLETED
- Retry Counts: (none)
- Completed At: 2026-07-24T10:06:00Z
- Final Output: This run itself — `state-history.md` and `approvals.md` are the evidence, checked against `../../runtime/state-machine/TEST_HARNESS.md`'s Acceptance Checklist.

## Current State Detail

Run reached `COMPLETED` after: INITIATED → IN_PROGRESS → (rejected attempt to REJECTED) → PAUSED_HUMAN_GATE → (human approval) → IN_PROGRESS → COMPLETED. Full detail in `state-history.md` and `approvals.md`.
