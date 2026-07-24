# State History: interrupted-demo-0001

Append-only. Oldest first.

### 2026-07-24T14:00:00Z — (none) → INITIATED
- Result: ACCEPTED
- Reason: Run created with a non-empty goal and unique run_id.
- Triggered by: Run creation.

### 2026-07-24T14:00:10Z — INITIATED → IN_PROGRESS
- Result: ACCEPTED
- Reason: Goal recorded; Exit Conditions met.
- Triggered by: Goal statement non-empty.

### 2026-07-24T14:00:30Z — IN_PROGRESS → PAUSED_HUMAN_GATE
- Result: ACCEPTED
- Reason: Simulated need for human input, to set up the interruption test.
- Triggered by: Test-harness protocol (Phase 8).

--- SIMULATED SESSION INTERRUPTION HERE — see resumability-test.md for what happens next, read cold ---

### 2026-07-24T14:19:00Z — PAUSED_HUMAN_GATE → IN_PROGRESS
- Result: ACCEPTED
- Reason: A human response was recorded in `approvals.md` (approval-interrupted-demo-0001-01) after the simulated interruption, satisfying `PAUSED_HUMAN_GATE`'s Exit Conditions.
- Triggered by: Resume, following the Cold-Start Resume Procedure in `runtime/reliability/FAILURE_RECOVERY_AND_TIMEOUT_POLICY.md`.

### 2026-07-24T14:20:00Z — IN_PROGRESS → COMPLETED
- Result: ACCEPTED
- Reason: Test objective (prove cold-start resume works) achieved; `IN_PROGRESS`'s Exit Conditions met.
- Triggered by: Resumability test completing successfully.
