# ADR-003 — Why Evidence Is Stored Separately from Memory

## Context
`skills/59-problem-solving-decision-modeling-skill/SKILL.md` already classifies every claim it produces as fact / calculation / inference / hypothesis / assumption / recommendation, and `critic-agent/CRITIC_AGENT.md` already treats an unlabeled claim as a finding. `memory/*.md` is durable, validated, and long-lived. These are not the same thing: most evidence collected during a run (competitor research, weak signals, user claims) is never meant to become permanent memory, and permanent memory should never hold raw, unvalidated research.

## Decision
Keep the Evidence Engine (Layer 4) and Memory Promotion (Layer 13) as distinct layers with a one-way gate between them: evidence flows into memory only after passing Evaluation (Layer 5), Decision (Layer 6), and — for durable lessons — Reflection/Learning (Layer 11/12), per the promotion gate in `../FOUNDRYOS_CONSTITUTION.md`'s Memory Policy. Evidence itself is never written directly to `memory/`.

The target architecture's suggested evidence-classification vocabulary (`verified_fact | supported_inference | weak_signal | user_claim | system_assumption | unknown`) is reconciled with, not duplicated against, the vocabulary FoundryOS already ships and the Critic Agent already checks (`fact | calculation | inference | hypothesis | assumption | recommendation`). Phase 4 must produce an explicit mapping table between the two and adopt one canonical vocabulary — the existing one is the default starting point, extended only where the target vocabulary names something the existing one genuinely can't express (e.g. "weak_signal" vs. "hypothesis" are not the same concept and may both be needed).

## Alternatives Considered
- **Treat Memory as the evidence store.** Rejected: would pollute `memory/*.md` with unvalidated, run-specific research, directly violating Constitution Principle 9 (Memory Stores Validated Knowledge).
- **Invent a second classification vocabulary from scratch, ignoring skill 59's.** Rejected: violates Architecture Principle 2 (One Reasoning Model) and would make the Critic Agent's existing checks and the new Evidence Engine's checks disagree on the same claim.

## Consequences
- Phase 4 owns producing the reconciliation table and the canonical vocabulary decision.
- Until Phase 4 ships, evidence collected in ad hoc runs continues to live only in that run's conversation/output, not in any persistent store — this is a known, accepted gap until Phase 2's run persistence and Phase 4's evidence ledger exist.

## Status
Accepted.
