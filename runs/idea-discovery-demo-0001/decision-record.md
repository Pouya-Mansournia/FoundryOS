# Decision Record: idea-discovery-demo-0001

Formalized per `../../runtime/decision/DECISION_RECORD_CONTRACT.md`. This is the Phase 4 test proving Phase 4's completion gate: **a decision traceable and reproducible from stored evidence.**

### Decision: Adapt Release Drafter instead of building a new release-notes tool (DEC-idea-discovery-demo-0001-01)
- Date: 2026-07-24
- Decision Owner: human owner (this run's requester)
- Decision Statement: Adapt an existing tool (Release Drafter) to close its specific monorepo gap, rather than build a new release-notes tool from scratch.
- Context: The idea was originally framed as "build a tool that automatically writes our release notes from git commit history" (see `run-state.md`).
- Evidence: [EV-01, EV-02, EV-03, EV-05, EV-06]
- Alternatives Considered:
  - `USE_EXISTING` (adopt Release Drafter as-is) — evidence: EV-01 (fact, Release Drafter exists and works), EV-06 (user_claim, it doesn't fully meet this team's monorepo need). Rejected because EV-06 directly contradicts "as-is" being sufficient.
  - `CONTINUE_NEW_PRODUCT_DISCOVERY` (build new) — evidence against: EV-01 + EV-02 (fact, mature existing solutions already do most of this) + EV-05 (fact, no internal precedent suggesting existing tools were already ruled out for a good reason). Rejected because building new would re-solve problems EV-01/EV-02 show are already solved.
  - `COMBINE_SOLUTIONS` (Release Drafter + a separate monorepo splitter) — evidence: EV-03 (inference) + EV-06 (user_claim) locate the gap specifically at monorepo versioning, which is narrow enough that extending Release Drafter (`ADAPT_EXISTING`) is simpler than integrating two separate tools. Considered a viable close second, not selected.
- Rejected Alternatives: `USE_EXISTING` (rejected on EV-06), `CONTINUE_NEW_PRODUCT_DISCOVERY` (rejected on EV-01+EV-02+EV-05), `COMBINE_SOLUTIONS` (rejected as unnecessarily complex given `ADAPT_EXISTING` covers the same gap more simply), `PAUSE_FOR_VALIDATION` (rejected — EV-06 already provided the specific validation a pause would have sought), `REJECT_OR_ARCHIVE` (rejected — EV-05 shows no reason to abandon the underlying problem, which EV-06 confirms is real).
- Trade-offs: Adapting Release Drafter means depending on an external project's maintenance and extension points, versus full control from a from-scratch build — accepted, because EV-01's Quality Score (4) reflects it being actively maintained.
- Remaining Assumptions: (a) git/PR history is clean enough for reliable parsing — `assumption`, unverified, flagged by Critic during `EVIDENCE_SYNTHESIS`; (b) the monorepo gap is addressable via Release Drafter's extension points rather than requiring a fork — `hypothesis`, to be tested during actual adaptation work (out of this run's scope).
- Major Risks: If assumption (b) is wrong and the gap requires a fork rather than extension, the effort estimate for `ADAPT_EXISTING` is invalid and the decision should be revisited (see Revisit Conditions).
- Confidence: Standard (per skill 59's Output Modes — a real, moderately consequential engineering-process decision, not high-stakes/irreversible enough for Deep mode).
- Human Approval Status: APPROVED — see `approvals.md` entry approval-idea-discovery-demo-0001-01; the human's message directly supplied EV-06, which is the evidence this decision most depends on.
- Revisit Conditions: Revisit if (1) Release Drafter's extension points prove insufficient for the monorepo gap during actual adaptation work, or (2) Release Drafter ships native monorepo support (making the gap moot), or (3) Release Drafter's maintenance lapses (undermining EV-01's Quality Score of 4).
- Next State / Next Action: This run's `DECISION_GATE` transitioned to `COMPLETED` with this outcome recorded (see `state-history.md`). Actual adaptation work is out of this run's scope — it would be a new run under `workflows/01-new-product-workflow/WORKFLOW.md` or a future Planning Engine (Phase 6), not this Idea Discovery run.
- Actual Outcome (backfilled, Phase 7, simulated for demo purposes — see `reflection.md`): Extension Point #1 (config-per-package) closed the monorepo gap in 3 days without needing a fork; both remaining assumptions CONFIRMED.
- Lesson (backfilled, Phase 7): See `lessons-queue.md` Promotion Request PR-01 — a `user_claim`-classified corroboration of a documentation-derived `inference` materially raises decision confidence, not just decision wording; worth flagging explicitly when it happens.

## Reproducibility Check

A different reader given only `evidence-ledger.md`'s six entries and this record can reconstruct the reasoning: EV-01+EV-02 establish strong existing coverage → EV-03 identifies the one gap (inference-level) → EV-05 rules out "we already tried and rejected this" → EV-06 independently corroborates EV-03 at first-hand, human-reported strength and is exactly specific enough to make `ADAPT_EXISTING` (not `USE_EXISTING`, not a from-scratch build) the evidence-supported choice. No claim in this record lacks a citable `evidence_id`. This satisfies Phase 4's completion gate.

## Note on `memory/decision-log.md`

This decision record is **not** written into the repository's real `memory/decision-log.md` — it is demo/evolution-track content about a fictional release-notes idea, not a real FoundryOS product decision, and writing it into production memory would pollute real decision history with fabricated data. `memory/decision-log.md` instead received only a small, additive cross-reference to `../../runtime/decision/DECISION_RECORD_CONTRACT.md` for real decisions to use going forward.
