# Resumability Test: interrupted-demo-0001

Proves `runtime/reliability/FAILURE_RECOVERY_AND_TIMEOUT_POLICY.md`'s Cold-Start Resume Procedure for real.

## Setup

The run was deliberately paused at `PAUSED_HUMAN_GATE` (see `state-history.md`'s third entry, 2026-07-24T14:00:30Z). A ~19-minute gap was then treated as a simulated session interruption — no assumption was carried forward about "what was I just doing," only the three run files themselves.

## Cold-Start Resume, Step by Step (as actually performed)

1. **Read `run-state.md`**: `Current State: PAUSED_HUMAN_GATE` *(at the time of resume, before this file was updated to its final COMPLETED state)*, `Goal`: prove cold-start resume. No other assumption made yet.
2. **Read `state-history.md` in full**: reconstructed the real path — `INITIATED → IN_PROGRESS → PAUSED_HUMAN_GATE`, all three ACCEPTED, no rejections. Confirmed this matches `run-state.md`'s `Current State`.
3. **Read `approvals.md`**: at the point of resume, this file was still empty (the pause was genuine — no approval existed yet). This correctly indicates the run should remain paused until a real response arrives, not be force-resumed.
4. **State Consistency Check** (`RUN_DIAGNOSTICS.md`): `run-state.md`'s `Current State` (`PAUSED_HUMAN_GATE`) matched `state-history.md`'s last `ACCEPTED` entry's `TO_STATE` (`PAUSED_HUMAN_GATE`). **PASS.**
5. **Resume**: once a real human response ("yes, resume it") was received and recorded as `approval-interrupted-demo-0001-01`, the transition `PAUSED_HUMAN_GATE → IN_PROGRESS` was applied per the normal Transition Contract rules — no special-casing required for the fact that time had passed.

## Result

The run resumed correctly using only its own three files, reaching `COMPLETED` with a fully consistent `state-history.md`. This directly satisfies Phase 8's completion gate: **the interrupted run recovered safely, and its state history remained trustworthy** (no gap, no contradiction, no fabricated approval — `approvals.md` was genuinely empty until the real response arrived).

## What This Proves (and What It Doesn't)

Proves: the file-based resume mechanism designed in Phase 2 and used implicitly by every subsequent phase's demo actually works when treated as a true cold read, not just "the same session remembering what it just did."
Does not prove: behavior under a truly corrupted run (`run-state.md` and `state-history.md` disagreeing) — that failure mode is specified in `FAILURE_RECOVERY_AND_TIMEOUT_POLICY.md`'s "Failure Recovery for a Genuinely Corrupted Run" section but not exercised by a real example in this phase, since deliberately corrupting a run file to test it would itself violate the never-fabricate, never-corrupt-data discipline this evolution has held throughout. Flagged as an accepted, deliberate gap, not an oversight.
