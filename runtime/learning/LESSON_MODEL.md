# Lesson Model

Status: Phase 7 deliverable. Implements Layer 12 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md) — converts a validated Reflection into a reusable lesson, formalizing `memory/lessons-learned.md`'s existing curated (not raw-log) structure.

## Lesson Schema

```markdown
### Lesson: <short title> (<lesson_id>)
- Principle: <the general, reusable statement — not specific to the one run it came from>
- Provenance: <decision_id, reflection reference, evidence_ids that support it — full chain, per Constitution Principle 8 (Traceability)>
- Applicable Scope: <which Agent(s)/Skill(s)/state(s)/workflow(s) this should inform going forward>
- Status: ACTIVE | SUPERSEDED | RESOLVED
- Superseded By: <lesson_id, only if Status is SUPERSEDED>
- Confidence: <how strongly this generalizes — a lesson from one run is weaker than one confirmed across several>
```

## What Makes a Lesson "Reusable," Not Just "True"

A Reflection's `Required Corrections` field is specific to one run. A Lesson generalizes it: "Release Drafter's config-per-package extension point closed our monorepo gap in 3 days" (specific, run-bound) becomes "Before recommending CONTINUE_NEW_PRODUCT_DISCOVERY for a tooling gap, check whether the closest existing tool's extension points have already been evaluated — a documented gap is often addressable without a new build" (general, reusable — the kind of principle that should inform a *future* `EXISTING_SOLUTION_DISCOVERY` state's Actions, not just explain what happened once).

## Provenance Requirement

Every lesson must trace back through: Reflection → Decision Record → Evidence entries. A lesson with a broken chain (can't point to the specific decision and evidence it came from) fails the mission's "knowledge provenance" requirement and may not be promoted (see `../memory-promotion/PROMOTION_QUEUE_CONTRACT.md`).

## Staleness

A lesson's `Status` moves to `SUPERSEDED` (never deleted) when a later, better-evidenced lesson contradicts or refines it — same never-delete, always-append discipline as every other ledger in this evolution. A lesson that hasn't been reconfirmed by any subsequent run in a long time is not automatically stale (unlike evidence, which has a real staleness clock tied to external facts) — a lesson is a principle, and principles don't expire on a schedule, only when contradicted.
