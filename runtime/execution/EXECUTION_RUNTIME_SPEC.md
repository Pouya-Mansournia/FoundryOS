# Execution Runtime Spec

Status: Phase 6 deliverable. Implements Layer 10 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md) — this is the gap FoundryOS's own `VERSION.md`/`docs/ROADMAP.md` already names as unshipped `v5.0.0` scope (see evolution `DECISION_LOG.md` ADR-0002). Structured markdown only, per ADR-0006: **this is a documented execution protocol an assistant follows, not an unattended background process.** See "What This Runtime Is Not" below for the honest scope boundary against FoundryOS's full `v5.0.0` vision.

## Execution Authorization Gate

An action may execute only if **all** of the following hold — this is the phase's completion gate, made mechanical-as-discipline:

1. A `runtime/decision/DECISION_RECORD_CONTRACT.md`-conformant Decision Record exists with `Human Approval Status: APPROVED`.
2. A `runtime/planning/PLANNING_ENGINE.md`-conformant `plan.md` exists, referencing that decision, with the specific task about to execute defined in it (Acceptance Criteria, Rollback Point, Dependencies all satisfied).
3. The action's scope matches the task's Description exactly — an execution that does *more* than the task describes is out of bounds, same principle as `runtime/orchestration/STATE_TO_CAPABILITY_ROUTING.md`'s Forbidden-Action check for Agent calls.

An action attempted without all three is **rejected**, recorded in `execution-log.md` (see `EXECUTION_LOG_CONTRACT.md`) with which condition failed, and not performed — same rejection discipline as every other gate in this evolution (invalid transitions, out-of-bounds capability routing, now unauthorized execution).

## What Counts as an "Action"

Per the mission's Layer 10 examples: creating or modifying code, creating design artifacts, updating documentation, running tests, creating experiments, preparing deployment, integrating external tools. Any of these, when performed as part of a state-machine-backed run, must pass the Execution Authorization Gate above — this applies regardless of how small the action seems; "just a small doc update" is not an exemption, since the gate's cost (checking three things already on file) is low precisely so there's no incentive to skip it for small actions.

## Bounded Scope, Not Unattended Autonomy

Once authorized, an approved plan's tasks may execute **in sequence, within the same session, without re-prompting the human between every single task** — this is what makes it meaningfully different from the ad hoc "propose one thing, wait, propose the next thing" pattern FoundryOS uses today. But every task still individually passes the Authorization Gate (has a plan entry, has acceptance criteria, has a rollback point) before it runs — bounded autonomy within pre-approved scope, not the human losing visibility into what's happening.

## What This Runtime Is Not

FoundryOS's own `docs/ROADMAP.md` describes the full `v5.0.0` Execution Engine as running "unattended," spanning sessions, and triggering the next Agent automatically once validation passes — genuinely autonomous, closed-loop execution with no assistant session live at all. **This Phase 6 deliverable does not build that.** It is a markdown-only protocol that requires an AI assistant to be actively hosting the session and reading these contracts to apply them — there is no daemon, no scheduler, no code that runs when nobody's watching. This is the same honest scope-labeling FoundryOS already used for `mcp-layer/MCP_LAYER.md` (a declaration contract, explicitly not a runtime) — Phase 6 is the equivalent honest label for planning/execution: a **protocol**, not an **engine** in the fully-automated sense.

## Audit Logging

Every execution attempt (authorized or rejected) is recorded in the run's `execution-log.md` per `EXECUTION_LOG_CONTRACT.md` — append-only, same pattern as every other log in this evolution.

## Rollback

If a task's Acceptance Criteria are not met after execution, its stated Rollback Point is applied before the plan proceeds — the plan does not continue past a failed task's unmet criteria by default; that itself would need a new authorized decision (e.g. "proceed anyway despite X" is a new decision, not a silent continuation).
