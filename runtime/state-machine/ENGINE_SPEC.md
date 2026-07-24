# State Machine Engine Spec

Status: Phase 2 deliverable. Describes exactly how an AI assistant hosting a FoundryOS session creates, persists, resumes, and closes a state-machine-backed run, using only markdown files under `../../runs/<run-id>/` — no code, no JSON, per evolution `DECISION_LOG.md` ADR-0006.

## Run Directory Layout

```
runs/
└── <run-id>/
    ├── run-state.md        ← current state pointer + run metadata (overwritten in place)
    ├── state-history.md    ← append-only transition log (never overwritten, only appended)
    └── approvals.md        ← append-only human approval records (never overwritten, only appended)
```

`<run-id>` is a short, unique, kebab-case identifier (e.g. `demo-0001`, or a date-prefixed slug for real runs like `2026-07-24-usage-based-pricing-idea`). Collision with an existing directory is a Failure Condition of `INITIATED` per `STATE_REGISTRY.md`.

## `run-state.md` Format

```markdown
# Run: <run-id>

- Goal: <one-line statement of what this run is for>
- Governing State Registry: <path to the STATE_REGISTRY.md this run's states are defined in>
- Created At: <ISO date>
- Current State: <STATE_ID>
- Status: <ACTIVE | PAUSED | COMPLETED | FAILED | REJECTED>
- Retry Counts: <STATE_ID>: <n>, ...  (only states that have retried)
- Completed At: <ISO date, only once terminal>
- Final Output: <reference to the artifact this run produced, only once COMPLETED>

## Current State Detail

<Whatever the active state's Actions have produced so far — free text, references to other files, etc. Overwritten each time the state's work progresses; the historical record lives in state-history.md, not here.>
```

`run-state.md` is the **only** file in a run directory that is overwritten in place — it always reflects "where is this run right now," not history.

## `state-history.md` Format

Append-only. One entry per transition attempt (accepted or rejected), oldest first:

```markdown
### <ISO timestamp> — <FROM_STATE> → <TO_STATE>
- Result: ACCEPTED | REJECTED
- Reason: <why accepted, or which Transition Contract rule failed>
- Triggered by: <what caused the attempt>
```

## `approvals.md` Format

Append-only. One entry per human approval request/response, using the fields from the mission's Human Approval Record minimum schema:

```markdown
### <ISO timestamp> — <approval_id>
- Approval Type: phase_transition | decision | execution | memory_promotion
- Requested At: <ISO timestamp>
- Requested By: <assistant / state that requested it>
- Scope: <exactly what is being approved — quote the specific question asked>
- Previous Status: <run status before this approval>
- Source Message: <the human's actual response, verbatim>
- Approved At: <ISO timestamp, once given>
- Approved By: human
- New Status: <APPROVED | REJECTED>
- Notes: <anything relevant — e.g. conditions attached to the approval>
```

Approval is **never fabricated**. If the assistant cannot point to a specific human message as `Source Message`, no `approvals.md` entry may claim `Approved By: human` — this mirrors the same rule already enforced at the evolution-phase level.

## Creating a Run

1. Choose a unique `<run-id>`.
2. Create `runs/<run-id>/run-state.md` with `Current State: INITIATED` and the stated goal.
3. Create empty `state-history.md` and `approvals.md` with just their headers.
4. Append the first `state-history.md` entry: `(none) → INITIATED`, Result: ACCEPTED, Triggered by: run creation.

## Advancing a Run

For every attempted transition:
1. Check all five Transition Validity Rules from `TRANSITION_CONTRACT.md` against the target state's definition in the governing registry.
2. If all pass: update `run-state.md`'s `Current State` and `Status`, append an ACCEPTED entry to `state-history.md`.
3. If any fail: leave `run-state.md` unchanged, append a REJECTED entry to `state-history.md` naming the failed rule, and report this plainly rather than retrying silently.

## Pausing and Resuming

- Pausing is simply transitioning into a state whose Purpose is to wait (e.g. `PAUSED_HUMAN_GATE`) — no special mechanism beyond the normal transition rules.
- Resuming a run in a fresh session: read `run-state.md` first (current state + goal), then `state-history.md` (how it got here), then `approvals.md` (what's already been decided). Do not restart from `INITIATED` for a run that already has history — this mirrors the evolution track's own Resume Instructions pattern.
- A run may sit paused indefinitely across any number of sessions; nothing times out or auto-expires by default.

## Failure and Retry

- When a state's Failure Conditions are met and its Retry Policy permits another attempt, transition to `RETRY_PENDING`, increment `run-state.md`'s Retry Counts for that state, then transition back into the retried state.
- When the Retry Policy's limit would be exceeded, transition to `FAILED` instead.

## What This Engine Does Not Do

- It does not execute anything itself (no Execution Runtime yet — that's Phase 6). States in this generic registry only track and gate; a future workflow's states (Phase 3+) may call Agents/Skills, but the engine itself has no execution capability.
- It does not validate anything automatically — every rule in `TRANSITION_CONTRACT.md` is a discipline the hosting assistant must apply by reading these spec files, not a program that runs. This is the accepted trade-off of the markdown-only decision (evolution `DECISION_LOG.md` ADR-0006).
