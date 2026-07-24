# Execution Log Contract

Status: Phase 6 deliverable. Format for a run's `execution-log.md`, companion to `EXECUTION_RUNTIME_SPEC.md`.

## Format

Append-only. One entry per execution attempt, authorized or rejected:

```markdown
### <ISO timestamp> — <task_id>: <short description>
- Result: AUTHORIZED | REJECTED
- Decision Reference: <decision_id>  (must exist and be APPROVED for AUTHORIZED)
- Plan Reference: <plan.md task entry this corresponds to>
- Scope Check: <confirmed the action matches the task's Description exactly, or names the mismatch if REJECTED>
- Action Taken: <what was actually done, if AUTHORIZED — specific, e.g. "created file X" not "worked on the feature">
- Acceptance Criteria Met: YES | NO | N/A (REJECTED entries)
- Rollback Point: <restated from the plan, so this log is self-contained without cross-referencing back to plan.md for the critical fact of "how do we undo this">
- Artifact Reference: <path to whatever was created/modified, if anything>
```

## Why Rollback Point Is Restated Here, Not Just in `plan.md`

`plan.md` is written before execution and could, in principle, be revised later (though per `PLANNING_ENGINE.md` it generally shouldn't be, mirroring `DECISION_RECORD_CONTRACT.md`'s versioning discipline). `execution-log.md` is the permanent record of what rollback point applied *at the moment this specific action actually ran* — restating it here means a future reader doesn't have to trust that `plan.md` wasn't edited since.

## Artifact Tracking

Every `AUTHORIZED` entry's `Artifact Reference` is how this evolution satisfies the mission's "artifact tracking" deliverable — a durable pointer from the execution log back to the concrete thing produced, so a later Reflection pass (Phase 7) can find and evaluate it without re-deriving what happened from prose alone.
