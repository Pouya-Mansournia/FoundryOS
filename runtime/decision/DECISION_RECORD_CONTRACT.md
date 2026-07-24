# Decision Record Contract

Status: Phase 4 deliverable. Implements Layer 6 (Decision Engine) of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md), formalizing the free-text Decision Record schema `memory/decision-log.md` already uses (produced today by `skills/59-problem-solving-decision-modeling-skill/SKILL.md`'s Decision Memo), per `../../docs/architecture/adr/ADR-003` and the mission's Layer 6 spec. Structured markdown only, per evolution `DECISION_LOG.md` ADR-0006.

## Formal Schema

```markdown
### Decision: <short title> (<decision_id>)
- Date: <ISO date>
- Decision Owner: <human or role responsible>
- Decision Statement: <what was decided, one or two sentences>
- Context: <what prompted this decision>
- Evidence: [<evidence_id>, ...]  — every cited evidence_id must exist in a real evidence-ledger.md; a decision citing no evidence is a hypothesis, not a decision
- Alternatives Considered: <the other options weighed>
- Rejected Alternatives: <which, and why specifically>
- Trade-offs: <what was given up by choosing this option>
- Remaining Assumptions: <what's still unverified, using the Evidence Ledger's classification vocabulary>
- Major Risks: <what could go wrong>
- Confidence: Concise | Standard | Deep  (per skill 59's existing Output Modes — reused, not replaced)
- Human Approval Status: PENDING | APPROVED | REJECTED
- Revisit Conditions: <what would trigger re-opening this decision — a specific, checkable condition, not "if things change">
- Next State / Next Action: <what happens once this decision clears>
- Actual Outcome: <backfilled later by Reflection, Phase 7 — empty at creation>
- Lesson: <backfilled later by Reflection, Phase 7 — empty at creation>
```

This is the same shape `memory/decision-log.md` already documents in prose — Phase 4 does not invent new fields, it fixes them as a checked contract (every decision must have all of them, not just the ones that seemed relevant) and makes `Evidence` a real, checkable list of `evidence_id`s rather than free narrative.

## Traceability Requirement

A decision is **traceable and reproducible from stored evidence** (this phase's completion gate) only if:
1. Every claim in `Decision Statement`, `Context`, and `Trade-offs` can be traced to a specific `evidence_id` in the run's `evidence-ledger.md`, or is explicitly marked as the decision-maker's own judgment (not evidence-backed).
2. `Rejected Alternatives` names the specific evidence that made each alternative less favorable — not just "we preferred X."
3. A different reader, given only the cited `evidence_id`s and this record, would understand *why* this decision followed from that evidence — not just *that* it did.

See `../../runs/idea-discovery-demo-0001/decision-record.md` for a worked example satisfying all three.

## Reversibility and Revisit Conditions

Every decision states a `Revisit Conditions` field — a specific, checkable trigger (e.g. "revisit if Release Drafter ships native monorepo support" — not "revisit if things change"). This is what makes a decision genuinely reversible per Constitution Principle 11 (Backward-Compatible Evolution) applied to product decisions, not just architecture ones: a decision without a stated revisit condition is effectively treated as permanent by default, which is rarely actually intended.

## Versioning

A decision is never edited in place once `Human Approval Status` moves past `PENDING`. If a decision needs to change, a new decision record is created, its `Context` states which prior `decision_id` it supersedes, and the prior record's own status is annotated (not deleted) to point forward — the same append-only, never-delete discipline already used for `state-history.md`, `approvals.md`, and `evidence-ledger.md`.

## Relationship to `memory/decision-log.md`

Per Target Architecture Layer 6's boundary (distinct from Layer 13's stricter Memory Promotion gate), a Decision Record with `Human Approval Status: APPROVED` **may** be written to `memory/decision-log.md` directly — this mirrors how skill 59 already works today. It does not need to pass through the full Reflection/Learning promotion path Layer 13 requires for general lessons, because a decision record already carries its own evidence citations and human approval; that is its validation. What Reflection (Phase 7) adds later is backfilling `Actual Outcome` and `Lesson` once the outcome is known — it does not gate the initial write.
