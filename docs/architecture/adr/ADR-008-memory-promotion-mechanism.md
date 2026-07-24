# ADR-008 — How Permanent Memory Promotion Works

## Context
`memory/lessons-learned.md` and `memory/decision-log.md` already describe promotion conventions in prose ("a lesson only gets added here once an outcome is known," "log at time made, not retroactively"), but nothing enforces them — there is no schema validator, no approval gate, no distinction enforced between raw research and validated knowledge (confirmed in Phase 0's audit).

## Decision
Formalize the existing convention into an explicit promotion gate (already stated in `../FOUNDRYOS_CONSTITUTION.md`'s Memory Policy):
```
Raw Observation → Claim → Evidence → Evaluation → Validation → Human or Policy Approval → Memory Promotion
```
Every write to `memory/*.md` must be traceable to a specific Evidence Engine entry (Layer 4) and, for decisions, a Decision Engine record (Layer 6) or, for lessons, a completed Reflection Engine pass (Layer 11). Raw chain-of-thought is never stored — only concise, inspectable reasoning artifacts and decision/lesson records, matching what `memory/decision-log.md` and `memory/lessons-learned.md` already store today in practice.

## Alternatives Considered
- **Leave promotion as pure convention (status quo).** Rejected: cannot satisfy Constitution Principle 9 (Memory Stores Validated Knowledge) reliably — nothing currently prevents an unvalidated claim from being written to `memory/` by mistake.
- **Require every memory write to go through a human approval step, no exceptions.** Rejected as the sole mechanism: too heavy for low-stakes, clearly-validated updates (e.g. a routine lesson from a completed, unremarkable run) — Layer 1's Human Authority principle allows policy-based approval (a defined, human-set rule) as an alternative to a live human check on every single write, matching skill 59's existing "Concise / Standard / Deep" scaling-to-stakes pattern.

## Consequences
- Phase 7 implements the enforcement mechanism (whatever form Phase 2's persistence decision takes) and formalizes `memory/lessons-learned.md` and `memory/decision-log.md`'s existing conventions rather than introducing new files.
- Existing entries in `memory/*.md` are not retroactively re-validated or purged — the gate applies going forward from Phase 7's completion, consistent with Architecture Principle 6 (Migration Policy: additive, optional-by-default).

## Status
Accepted.
