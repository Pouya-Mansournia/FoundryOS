# Failure Recovery and Timeout Policy

Status: Phase 8 deliverable. Formalizes resumability (already designed into `../state-machine/ENGINE_SPEC.md` since Phase 2) into a tested procedure, and adds a staleness policy for long-paused runs — this phase's completion gate: **interrupted runs can recover safely, and state history remains trustworthy.**

## Failure Recovery — Already Designed, Now Tested

Every state's Retry Policy and the `FAILED`/`RETRY_PENDING` states (Phase 2) already define what happens when a state's own work fails. This phase adds the missing piece: recovering a run that was interrupted **not by a state failing, but by the hosting session simply ending** (the assistant's session closed, the user came back three days later) — a different failure mode than anything Phase 2–7 tested directly.

## Cold-Start Resume Procedure (Formalized)

1. Read `run-state.md` — get `Current State` and `Goal`. Do not assume anything about how the run got there yet.
2. Read `state-history.md` in full — reconstruct the actual path taken, including any rejected attempts (these are informative, not noise).
3. Read `approvals.md` — establish what's actually been approved, with real timestamps and real `Source Message`s. Never assume an approval exists that isn't recorded here.
4. Run the Run Diagnostic Procedure's State Consistency Check (`RUN_DIAGNOSTICS.md`) — confirm `run-state.md` and `state-history.md` agree before doing anything else.
5. Only then, resume: apply the current state's Actions per its definition in the governing registry, exactly as if this were the same session — the state machine has no notion of "session," only of state.

This is exercised for real in `runs/interrupted-demo-0001/` (see that run's `resumability-test.md`) — a run deliberately left paused, then resumed via steps 1–5 above with no access to any prior "memory" of the run beyond its own files.

## Timeout / Staleness Policy for Paused Runs

Per `../state-machine/STATE_REGISTRY.md`'s `PAUSED_HUMAN_GATE` definition (Phase 2): "may remain paused indefinitely" — this is intentional, per Constitution Principle 7 (Human Authority): FoundryOS never auto-expires a pending human decision. This phase adds an **advisory**, not enforced, staleness flag:

- A run paused for longer than is typical for its context (e.g. weeks, for something that looked urgent) is worth surfacing to the human as "this is still waiting on you" when the run is next touched — a courtesy check, not an automatic transition to `FAILED`/`ARCHIVED`.
- No run is ever auto-failed or auto-archived purely due to elapsed time. Any transition out of a paused state still requires the same approval/evidence the state's contract already demands.

## Failure Recovery for a Genuinely Corrupted Run

If the State Consistency Check (step 4 above) fails — `run-state.md` and `state-history.md` disagree — the run is **not** silently "fixed" by picking one as authoritative. It is flagged, and `state-history.md` (the append-only, harder-to-tamper-with-accidentally log) is treated as the source of truth for reconstructing what `run-state.md` *should* say, with the correction itself recorded as a new `state-history.md` entry (`Result: ACCEPTED`, `Reason: "integrity correction — run-state.md did not match state-history.md's last entry"`) — never a silent overwrite with no trace.

## Relationship to This Phase's Completion Gate

"Interrupted runs can recover safely" = the Cold-Start Resume Procedure above, tested for real. "State history remains trustworthy" = the State Consistency Check applied across every existing run, with results in `AUDIT_TRAIL_VERIFICATION.md`.
