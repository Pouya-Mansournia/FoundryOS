# Transition Contract

Status: Phase 2 deliverable. Defines what makes a transition between states valid or invalid, and how it must be recorded. Companion to [`STATE_CONTRACT.md`](STATE_CONTRACT.md).

## What a Transition Is

A transition moves a run from one State ID to another. Every transition, whether it succeeds or is rejected, is an event — it is always recorded in the run's `state-history.md` (see [`ENGINE_SPEC.md`](ENGINE_SPEC.md)), never silently applied or silently refused.

## Transition Validity Rules

A transition from state `A` to state `B` is **valid** only if all of the following hold:

1. `B` appears in `A`'s **Possible Next States** list, as defined in the governing state registry.
2. `A`'s **Exit Conditions** are satisfied.
3. `B`'s **Entry Conditions** are satisfied.
4. If `A`'s **Human Approval Requirement** says leaving `A` requires approval, a corresponding approval record exists in the run's `approvals.md` (see `../../docs/architecture/adr/ADR-004-phase-transitions-require-human-approval.md` for why this is non-negotiable, applied here at the run level rather than the evolution-phase level).
5. `B`'s **Required Inputs** are present in the run's current state.

A transition failing **any** of these checks is **invalid** and must be **rejected**, not attempted anyway with a note. Rejection is itself recorded (see below) — it is evidence the engine is working correctly, not an error to hide.

## Transition Types

- **Forward transition** — the normal case, `A → B` where `B` represents progress.
- **Backward transition** — `A → C` where `C` is an earlier state in the conceptual flow (e.g. a critique loop sending a run back to research). Valid exactly like any other transition — backward is not special-cased as more or less strict, it just requires `C` to be listed in `A`'s Possible Next States like any other target.
- **Retry transition** — `A → A` (or `A → RETRY_PENDING → A`), governed by `A`'s Retry Policy and its Failure Conditions having been met.
- **Pause transition** — `A → PAUSED_*` states, always valid targets for any state whose work may need to wait on something external (typically a human).
- **Resume transition** — `PAUSED_* → B`, valid only once whatever the pause was waiting on (typically a recorded approval) exists.

## Recording a Transition

Every transition attempt — successful or rejected — appends one entry to the run's `state-history.md` with:

```
### <timestamp> — <FROM_STATE> → <TO_STATE>
- Result: ACCEPTED | REJECTED
- Reason: <why accepted, or which rule from "Transition Validity Rules" failed>
- Triggered by: <what caused the attempt — an action completing, a human message, a retry policy firing>
```

`state-history.md` is append-only. A rejected transition is never deleted or overwritten — it is evidence for Reflection (Layer 11) that a state's Actions or exit conditions may need revisiting, and evidence for the Constitution's Traceability principle.

## Invalid-Transition Handling

When a transition is rejected, the run's current state does not change. The assistant hosting the run must:
1. Record the rejection in `state-history.md` per the format above.
2. Report the rejection plainly (which rule failed, what's missing) rather than silently retrying with different parameters or inventing a new state.
3. Leave the run in its prior, valid state, awaiting whatever would make the transition valid (a missing input, a missing approval, unmet exit conditions).

## Relationship to Human Approval Records

When rule 4 applies, the approval record appended to `approvals.md` follows the schema in [`ENGINE_SPEC.md`](ENGINE_SPEC.md)'s Approvals section, itself derived from the mission's Human Approval Record minimum fields (`approval_id`, `approval_type`, `requested_at`, `approved_at`, `requested_by`, `approved_by`, `scope`, `previous_status`, `new_status`, `source_message`, `notes`).
