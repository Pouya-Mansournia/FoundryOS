# Memory Promotion Queue Contract

Status: Phase 7 deliverable. Implements Layer 13 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md) and formalizes the promotion gate already stated in `../../docs/architecture/FOUNDRYOS_CONSTITUTION.md`'s Memory Policy and `../../docs/architecture/adr/ADR-008-memory-promotion-mechanism.md`. This is the phase's completion gate made concrete: **raw research cannot enter permanent memory, and validated learning can be promoted traceably.**

## The Gate

```
Raw Observation → Claim → Evidence → Evaluation → Validation → Human or Policy Approval → Memory Promotion
```

Concretely, in terms of this evolution's actual artifacts:

```
evidence-ledger.md entry (Phase 4)
  → runtime/evaluation/EVALUATION_ENGINE.md pass (Phase 4)
  → DECISION_RECORD_CONTRACT.md decision, APPROVED (Phase 4)
  → execution + outcome observed (Phase 6)
  → REFLECTION_CONTRACT.md reflection (Phase 7, this phase)
  → LESSON_MODEL.md lesson (Phase 7)
  → Promotion Queue entry, approved (Phase 7)
  → memory/lessons-learned.md or memory/decision-log.md (real write)
```

A candidate that tries to skip any step (e.g. a `weak_signal`-classified evidence entry going straight to a memory write, with no Decision, no Reflection, no Lesson in between) is **rejected at the queue**, not silently promoted. This is the concrete mechanism that makes Constitution Principle 9 (Memory Stores Validated Knowledge) enforceable rather than aspirational.

## Promotion Queue Entry Schema

```markdown
### Promotion Request: <request_id>
- Candidate: <the Lesson or Decision content proposed for promotion>
- Provenance Chain: <evidence_id(s) → decision_id → reflection reference → lesson_id — must be unbroken>
- Target: memory/lessons-learned.md | memory/decision-log.md | (other memory file, if applicable)
- Requested At: <timestamp>
- Approval Type: human | policy
- Approval Policy Applied: <if policy-based — which rule justified skipping a live human check, e.g. "Concise-mode decision per skill 59's stakes scaling">
- Result: APPROVED | REJECTED
- Reason: <why>
- Promoted At: <timestamp, if APPROVED>
```

## Approval Policy

Per Constitution Principle 7 (Human Authority) and skill 59's existing Concise/Standard/Deep stakes-scaling precedent: a **low-stakes** lesson (narrow scope, low blast radius if wrong, e.g. "this specific tool's config quirk") may be promoted via a stated **policy** rule rather than requiring a live human check every time — but the policy itself must have been human-approved in advance (e.g. "lessons scoped to a single Skill's tactical detail, with an unbroken provenance chain and no contradicting existing lesson, may auto-promote"). A **high-stakes** lesson (broad scope, e.g. anything touching Constitution-level principles, cross-Agent behavior, or evaluation criteria) always requires a live human approval, no policy shortcut.

## Rejection Policy

A promotion request is rejected when:
- The provenance chain is broken (missing a step, e.g. no Decision Record behind the claim).
- The candidate contradicts an existing `ACTIVE` lesson without addressing the contradiction (the request must instead propose the existing lesson move to `SUPERSEDED`, explicitly, not just add a conflicting second lesson silently).
- The candidate is evidence-only, not yet reflected upon (i.e., attempting to promote directly from `evidence-ledger.md`, skipping Decision/Reflection entirely).

A rejection is recorded in the queue with the specific reason — same never-silently-drop discipline as every other gate in this evolution (invalid transitions, out-of-bounds routing, unauthorized execution, now unvalidated promotion).

## Knowledge Provenance in the Real Memory File

When a promotion is `APPROVED` and actually written to `memory/lessons-learned.md` or `memory/decision-log.md`, the real memory entry carries a provenance pointer back to the run (`runs/<run-id>/`) that produced it — so a future reader of real memory can trace a lesson back to its full evidentiary chain, not just trust it on faith.

## Stale Memory Handling

Distinct from a Lesson's own `Status` field (`LESSON_MODEL.md`): if a promoted memory entry is later found to be based on since-refuted evidence (an Assumption Outcome Tracking entry comes back `REFUTED` in a later run's Reflection), a new Promotion Request is filed marking the original entry `SUPERSEDED`, never silently edited or deleted in place — matching `memory/decision-log.md`'s own existing Update Rules ("log at time made, not retroactively").
