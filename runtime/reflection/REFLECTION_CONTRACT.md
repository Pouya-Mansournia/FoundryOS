# Reflection Contract

Status: Phase 7 deliverable. Implements Layer 11 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md), formalizing `reflection-agent/REFLECTION_AGENT.md`'s existing role — run only once an outcome is known, backfill the Decision Record, extract reusable lessons — into a checkable schema. Structured markdown only, per ADR-0006.

## Gate: Reflection Requires a Known Outcome

Per `reflection-agent/REFLECTION_AGENT.md`'s existing rule ("a lesson only gets added here once an outcome is known") and Constitution Principle 10 (Continuous Learning): a Reflection artifact may only be produced once the Decision Record it reflects on has a real, observed `Actual Outcome` — not a projection, not "presumably it worked." A reflection written before the outcome is known is not valid input to Learning (Layer 12).

## Reflection Schema

```markdown
# Reflection: <run-id> / <decision_id>

## Expected vs. Actual
- Expected Outcome: <from the Decision Record>
- Actual Outcome: <what really happened, observed>
- Difference: <the gap between them, stated plainly — "none" is a valid, useful answer too>

## Assumption Outcome Tracking
<for each Remaining Assumption in the Decision Record:>
- Assumption: <as stated>
- Outcome: CONFIRMED | REFUTED | STILL_UNVERIFIED
- Evidence: <what confirmed or refuted it>

## Root Cause (if Difference is non-trivial)
- What Happened: <the specific mechanism, not just "it didn't work">
- Why: <the actual cause — a wrong assumption, missing evidence, an evaluation criterion that was underweighted, an execution step that didn't match the plan>
- Category: successful_assumption | failed_assumption | unexpected_effect | evaluation_gap | execution_gap

## Required Corrections
<what should change in future decisions/evaluations/state definitions as a result — specific enough to act on, not "be more careful next time">

## Reusable Lesson Candidate
<see `../learning/LESSON_MODEL.md` — the draft lesson this reflection produces, if any>
```

## Reflection Is Not a Summary

Per the mission's explicit requirement: "Reflection must not merely summarize activity. It must explain what should change in future decisions." A Reflection artifact with an empty or vague `Required Corrections` field is incomplete, even if every other field is filled in.

## Relationship to `reflection-agent/REFLECTION_AGENT.md`

This does not replace the Reflection Agent — it is the artifact format that agent's existing judgment (comparing decision-log entries, extracting patterns) now produces, whether inside a state-machine-backed run or via the Agent's existing prose-based usage against `memory/decision-log.md` directly. Non-blocking, matching the existing Agent's description: it "does not block or gate any workflow in real time."
