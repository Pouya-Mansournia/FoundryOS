# Execution Log: adapt-release-drafter-demo-0001

Append-only.

### 2026-07-24T12:06:00Z — T2: (probe) modify workflows/01-new-product-workflow/WORKFLOW.md
- Result: REJECTED
- Decision Reference: DEC-idea-discovery-demo-0001-01 (exists and is APPROVED — this alone does not authorize an arbitrary action)
- Plan Reference: **none** — `plan.md` has no task named "T2" and no task authorizes touching any file outside this run's directory
- Scope Check: FAILED — the only real task, T1, is explicitly scoped to `runs/adapt-release-drafter-demo-0001/` only; this probe attempted to modify a file entirely outside that scope
- Action Taken: none — rejected before any file was touched
- Acceptance Criteria Met: N/A
- Rollback Point: N/A — nothing was done
- Artifact Reference: none
- Notes: Deliberate Phase 6 test-harness probe, proving the Execution Authorization Gate actually blocks an action with no corresponding plan entry — mirrors the invalid-transition probe (Phase 2) and out-of-bounds-routing probe (Phase 5). This did not affect the run's real path; `state-history.md`'s real transitions are unaffected.

### 2026-07-24T12:08:00Z — T1: Produce adaptation research note
- Result: AUTHORIZED
- Decision Reference: DEC-idea-discovery-demo-0001-01 (APPROVED)
- Plan Reference: `plan.md` T1
- Scope Check: PASS — action matches T1's Description exactly (create one file, inside this run's own directory only)
- Action Taken: Created `adaptation-research-note.md` in this run's directory
- Acceptance Criteria Met: YES — file exists, names two concrete extension points, restates (does not resolve) the two open assumptions from the Decision Record
- Rollback Point: Delete `adaptation-research-note.md` (restated from `plan.md`, per `runtime/execution/EXECUTION_LOG_CONTRACT.md`'s rationale for restating it here)
- Artifact Reference: `runs/adapt-release-drafter-demo-0001/adaptation-research-note.md`

## Summary

1 authorized execution (T1, acceptance criteria met), 1 deliberately rejected unauthorized probe (T2, correctly blocked before any action was taken). Satisfies Phase 6's completion gate: no execution occurred without an approved decision and explicit, matching scope.
