# State History: demo-0001

Append-only. Oldest first.

### 2026-07-24T10:00:00Z — (none) → INITIATED
- Result: ACCEPTED
- Reason: Run created with a non-empty goal statement and a unique run_id (`demo-0001`, no existing collision under `runs/`).
- Triggered by: Run creation (Phase 2 test-harness execution).

### 2026-07-24T10:01:00Z — INITIATED → IN_PROGRESS
- Result: ACCEPTED
- Reason: `IN_PROGRESS` is in `INITIATED`'s Possible Next States; `INITIATED`'s Exit Conditions met (goal non-empty, unique run_id assigned); `IN_PROGRESS`'s Entry Conditions met (prior state was `INITIATED`).
- Triggered by: Goal recorded successfully in `run-state.md`.

### 2026-07-24T10:02:00Z — IN_PROGRESS → REJECTED
- Result: REJECTED
- Reason: Transition Contract rule 1 failed — `REJECTED` does not appear in `IN_PROGRESS`'s Possible Next States list (`STATE_REGISTRY.md`: `PAUSED_HUMAN_GATE`, `RETRY_PENDING`, `FAILED`, `APPROVED`, `COMPLETED`). `REJECTED` is reachable only from `PAUSED_HUMAN_GATE`. Run's current state left unchanged at `IN_PROGRESS`.
- Triggered by: Deliberate test-harness probe (Phase 2 `TEST_HARNESS.md`, Protocol step 3) — not a real workflow event.

### 2026-07-24T10:03:00Z — IN_PROGRESS → PAUSED_HUMAN_GATE
- Result: ACCEPTED
- Reason: `PAUSED_HUMAN_GATE` is in `IN_PROGRESS`'s Possible Next States; entering it requires no prior approval per its Entry Conditions. The run's in-progress work item ("prove the engine") had reached a point requiring human review before continuing, per `IN_PROGRESS`'s Exit Conditions.
- Triggered by: State's Actions completing the "needs human input" branch.

### 2026-07-24T10:05:00Z — PAUSED_HUMAN_GATE → IN_PROGRESS
- Result: ACCEPTED
- Reason: A human response was recorded in `approvals.md` (approval-demo-0001-01) with `New Status: APPROVED`, satisfying `PAUSED_HUMAN_GATE`'s Exit Conditions and Transition Contract rule 4.
- Triggered by: Human approval received (see `approvals.md`).

### 2026-07-24T10:06:00Z — IN_PROGRESS → COMPLETED
- Result: ACCEPTED
- Reason: `COMPLETED` is in `IN_PROGRESS`'s Possible Next States; the work item ("prove the engine") was satisfied — this state-history file and `approvals.md` together demonstrate every item in `TEST_HARNESS.md`'s Acceptance Checklist. `COMPLETED`'s Required Inputs (final output reference) present.
- Triggered by: Test-harness protocol completion.
