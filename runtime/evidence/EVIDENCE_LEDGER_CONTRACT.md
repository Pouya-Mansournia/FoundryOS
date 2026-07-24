# Evidence Ledger Contract

Status: Phase 4 deliverable. Implements Layer 4 (Evidence Engine) of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md), formalizing the provisional per-run `evidence.md` convention Phase 3 used, per `../../docs/architecture/adr/ADR-003-evidence-separate-from-memory.md`. Structured markdown only, per evolution `DECISION_LOG.md` ADR-0006 — no JSON schema, no validator.

## Canonical Classification Vocabulary

Per ADR-003, this reconciles the target architecture's suggested vocabulary with the one `skills/59-problem-solving-decision-modeling-skill/SKILL.md` and `critic-agent/CRITIC_AGENT.md` already use in production. **The canonical vocabulary going forward is the union of both, not a fresh third one:**

| Canonical value | Meaning | Origin |
|---|---|---|
| `fact` | Independently verifiable, verified. Absorbs the target vocabulary's `verified_fact`. | skill 59 |
| `calculation` | Derived by arithmetic/quantitative reasoning from other evidence. | skill 59 |
| `inference` | A reasoned conclusion from available evidence, not independently verified itself. Absorbs `supported_inference`. | skill 59 |
| `hypothesis` | A falsifiable guess proposed for testing, not yet evidence of anything. | skill 59 |
| `assumption` | Something taken as true without direct evidence, stated so it can be challenged. Absorbs `system_assumption`. | skill 59 |
| `recommendation` | A proposed course of action, downstream of the evidence above — not itself a fact about the world. | skill 59 |
| `weak_signal` | Suggestive but not yet inference-grade — a single data point, an anecdote, a pattern noticed once. New; the target vocabulary named a real gap skill 59 didn't cover. | target architecture |
| `user_claim` | Reported directly by a human in this run, not independently re-verified. New; distinct from `assumption` because it has a specific, attributable source (the human), not a system-generated default. | target architecture |

`unknown` (from the target vocabulary) is **not** a classification value — an entry that cannot be classified as any of the above is not valid evidence. It is either researched further or explicitly logged as a **gap** (see Blockers in `../evaluation/EVALUATION_ENGINE.md`), never silently stored as "unknown."

Every claim entered into an evidence ledger must carry exactly one of the eight values above. This is the same check `critic-agent/CRITIC_AGENT.md` already performs ("treat an unlabeled claim as a finding on its own") — Phase 4 gives that existing check a fixed vocabulary to check against.

## Evidence Entry Schema

Every entry in a run's `evidence-ledger.md` (the Phase-4-formalized successor to Phase 3's provisional `evidence.md`) has these fields, adapted from the mission's minimum evidence object to markdown:

```markdown
### <evidence_id> — <short title>
- Claim: <the claim itself, one or two sentences>
- Classification: fact | calculation | inference | hypothesis | assumption | recommendation | weak_signal | user_claim
- Source Type: <e.g. public repository, documentation, human-reported, internal memory file, market report>
- Source Reference: <specific citation — URL, file path, or "reported by human in <state>">
- Source Date: <when the source itself was published/true, if known>
- Accessed At: <when this run collected it>
- Summary: <what it says, in this run's own words>
- Supports: [<evidence_id>, ...]  (other entries this strengthens)
- Contradicts: [<evidence_id>, ...]  (other entries this conflicts with — never silently dropped, see Contradiction Handling)
- Quality Score: <1–5, per Source Quality Rules>
- Relevance Score: <1–5, how directly this bears on the run's actual decision>
- Confidence Score: <1–5, combining classification strength + quality + relevance>
- Limitations: <what this evidence does NOT establish>
- Created In State: <the state ID that produced this entry>
- Created By: <which Skill/Agent/human produced it>
```

`evidence-ledger.md` is append-only, same pattern as `state-history.md`/`approvals.md` (see `../state-machine/ENGINE_SPEC.md`). An entry is never deleted, even if later contradicted — contradictions are recorded, not erased, per Constitution Principle 5 (Evidence Before Confidence) and Principle 8 (Traceability).

## Contradiction Handling

When a new entry contradicts an existing one:
1. Both entries remain in the ledger — neither is deleted or silently favored.
2. The new entry's `Contradicts` field names the conflicting `evidence_id`.
3. The conflict is surfaced explicitly wherever this evidence feeds an Evaluation (Layer 5) or Decision (Layer 6) — never resolved by quietly picking one and ignoring the other.
4. If one entry is later confirmed stale or wrong, it is not deleted — its `Limitations` field is updated to note the resolution, preserving the audit trail.

## Duplicate-Source Detection

Before adding a new entry, check whether its `Source Reference` matches an existing entry's. Two entries citing the same underlying source are marked as such (e.g. "same source as EV-01") rather than counted as independent corroboration — this specifically guards against the mission's "avoid unsupported uniqueness claims" and "distinguish first-party marketing from independent validation" requirements: a claim repeated by the same source twice is not stronger evidence than it was the first time.

## Staleness

An entry whose `Source Date` is old relative to how fast the claim's domain changes (e.g. a competitor pricing page cited a year ago) should be flagged in its `Limitations` field as potentially stale, and re-verified before being used to support a high-stakes Decision (Layer 6). This phase does not automate staleness detection (no code, per ADR-0006) — it is a discipline applied when an entry is read, not enforced on write.

## Relationship to Memory

Per `../../docs/architecture/adr/ADR-008-memory-promotion-mechanism.md`, entries in a run's `evidence-ledger.md` are **never** written directly to `memory/*.md`. They remain run-local until a completed Reflection pass (Phase 7) explicitly promotes a validated lesson — the ledger itself is Temporary/Validated-Run evidence, not Validated Project Memory.
