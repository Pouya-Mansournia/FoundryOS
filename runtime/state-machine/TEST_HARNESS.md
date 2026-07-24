# Minimal Test Harness (Phase 2)

Status: Phase 2 deliverable. Since state persistence is structured markdown, not code (evolution `DECISION_LOG.md` ADR-0006), there is no executable test suite. This document defines the manual test protocol and the acceptance checklist Phase 2's completion gate requires: **a small test workflow must demonstrate valid transitions, invalid-transition rejection, pause, resume, and human approval.**

## Protocol

A demo run is created under `../../runs/demo-0001/` using only the generic `STATE_REGISTRY.md` (no domain-specific states — this proves the engine, not a product workflow). The demo run must exercise, in order:

1. **Run creation** — `INITIATED` entered correctly.
2. **A valid forward transition** — `INITIATED → IN_PROGRESS`.
3. **An attempted invalid transition** — a transition to a State ID not in the current state's Possible Next States, or to a valid target whose Entry Conditions aren't met — rejected, recorded, and the run's current state unchanged.
4. **A pause** — `IN_PROGRESS → PAUSED_HUMAN_GATE`.
5. **A resume gated on approval** — an `approvals.md` entry recording a real human response, then `PAUSED_HUMAN_GATE → IN_PROGRESS`.
6. **Completion** — `IN_PROGRESS → COMPLETED` (via `APPROVED` or directly, per the registry).

## Acceptance Checklist

- [ ] `run-state.md` at every point reflects exactly one current state, matching the last ACCEPTED entry in `state-history.md`.
- [ ] Every transition attempt (accepted or rejected) has a corresponding `state-history.md` entry — none silently applied, none silently dropped.
- [ ] The rejected transition's entry names which Transition Contract rule failed.
- [ ] The rejected attempt did not change `run-state.md`'s Current State.
- [ ] The pause state (`PAUSED_HUMAN_GATE`) has no Actions and performs no work while waiting.
- [ ] The resume transition only occurs after a genuine `approvals.md` entry exists with a real `Source Message` — not fabricated.
- [ ] The run reaches a terminal state (`COMPLETED`, `REJECTED`, or `FAILED`) with an empty Possible Next States list, matching `STATE_REGISTRY.md`'s Terminal States section.
- [ ] Nothing in the demo run wrote to `memory/*.md` directly (per Memory Write Policy on every state — durable writes require the Reflection/Learning path, not built until Phase 7).

## How to Re-Run This Test

Delete `runs/demo-0001/` (or create a new `runs/demo-NNNN/`) and repeat the Protocol section above, following `ENGINE_SPEC.md` exactly. Any future change to `STATE_CONTRACT.md`, `TRANSITION_CONTRACT.md`, or `STATE_REGISTRY.md` should be re-validated against this checklist before being treated as complete.

## Result of the Phase 2 Run

See `../../runs/demo-0001/` — `run-state.md`, `state-history.md`, and `approvals.md` — for the executed demo satisfying every item above.
