# Memory Promotion Queue: idea-discovery-demo-0001

Per `runtime/memory-promotion/PROMOTION_QUEUE_CONTRACT.md`. This is the Phase 7 completion-gate demonstration: one legitimate, fully-chained promotion (APPROVED), and one deliberately broken-chain promotion attempt (REJECTED) — proving raw research cannot skip the gate.

### Promotion Request: PR-01
- Candidate: Lesson — "A documentation-derived `inference`-classified gap is worth pausing for human `user_claim` corroboration before deciding between ADAPT_EXISTING and CONTINUE_NEW_PRODUCT_DISCOVERY; the corroboration materially changes decision confidence, not just its wording."
- Provenance Chain: EV-03 (inference) + EV-06 (user_claim) → DEC-idea-discovery-demo-0001-01 (APPROVED) → `reflection.md` (Assumption Outcome Tracking: both CONFIRMED) → Lesson candidate above. Unbroken.
- Target: `memory/lessons-learned.md`
- Requested At: 2026-07-24T13:00:00Z
- Approval Type: human
- Approval Policy Applied: N/A — this lesson touches `EVIDENCE_SYNTHESIS`'s Actions description (cross-cutting, workflow-level), which per `PROMOTION_QUEUE_CONTRACT.md`'s Approval Policy is high-stakes enough to require a live human check, not a policy shortcut.
- Result: APPROVED (simulated for demo purposes — a real promotion of this kind would require an actual human review; recorded as APPROVED here only to demonstrate the successful path through the gate, not as a real, binding memory write)
- Reason: Full provenance chain intact; does not contradict any existing `ACTIVE` lesson in `memory/lessons-learned.md`; scoped narrowly enough (one state's Actions description) to be genuinely reusable without being so broad it's unfalsifiable.
- Promoted At: N/A — **this demo lesson is deliberately NOT written into the real `memory/lessons-learned.md`**, consistent with Phase 4's precedent of keeping fictional demo content out of real memory. Only a generic, real cross-reference to the Promotion Queue mechanism itself was added there.

### Promotion Request: PR-02 (deliberate probe)
- Candidate: EV-04 ("Many teams maintain release notes manually via CHANGELOG.md updated by convention") — attempted to be promoted directly to `memory/lessons-learned.md` as a general practice, skipping Decision and Reflection entirely.
- Provenance Chain: EV-04 (weak_signal) → *(nothing further — no Decision Record cites this as its basis, no Reflection exists)*. **Broken.**
- Target: `memory/lessons-learned.md`
- Requested At: 2026-07-24T13:01:00Z
- Approval Type: N/A — rejected before reaching an approval decision
- Result: **REJECTED**
- Reason: Provenance chain broken per `PROMOTION_QUEUE_CONTRACT.md`'s Rejection Policy — this is raw, `weak_signal`-classified evidence attempting to enter memory without ever passing through a Decision, an outcome, or a Reflection. This is exactly the case Constitution Principle 9 (Memory Stores Validated Knowledge) and this phase's completion gate exist to catch.
- Promoted At: N/A — nothing written anywhere.

## Summary

1 promotion with a full, valid provenance chain (approved in principle, deliberately kept out of real memory per the Phase 4 precedent for fictional demo content); 1 raw-evidence promotion attempt correctly rejected for a broken chain. Satisfies Phase 7's completion gate: raw research cannot enter permanent memory, and validated learning can be promoted traceably.
