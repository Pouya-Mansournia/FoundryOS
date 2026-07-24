# Idea Discovery Brief — Template

Status: Phase 3 deliverable. The required output artifact of the Idea Discovery state machine (produced in draft by `EVIDENCE_SYNTHESIS`, finalized by `USER_EXPERIENCE_INTEGRATION`). Every field below must be populated (or explicitly marked "none found" / "not applicable") before `DECISION_GATE` may be entered.

```markdown
# Idea Discovery Brief — <run-id>

## Idea (as received)
<the raw idea/problem statement, verbatim, from IDEA_RECEIVED>

## Problem Framing
- Problem Statement: <the real problem, separated from any assumed solution>
- Assumed Solution (as given): <what the human originally asked for, if anything — "none stated" if they only described a problem>
- Desired Outcome: <what success looks like>

## Existing Solutions
<from EXISTING_SOLUTION_DISCOVERY — each entry: name, what it does, why it does/doesn't fully solve the problem, evidence classification>

## Adjacent Solutions and Workarounds
<from ADJACENT_SOLUTION_DISCOVERY — substitutes, manual workarounds, adjacent-category tools, each with evidence classification>

## Historical Attempts
<from HISTORICAL_ATTEMPT_DISCOVERY — prior internal or external attempts at this problem, what happened, evidence classification — "none found" if genuinely none>

## Critic Findings
<from EVIDENCE_SYNTHESIS's Critic Agent pass — weaknesses, hidden assumptions, missing evidence, red flags>

## Human Experience and Constraints
<from USER_EXPERIENCE_INTEGRATION — what the human actually said when shown the evidence; any contradiction between their experience and the research, flagged explicitly, not resolved silently>

## Decision Gate Outcome
- Outcome: USE_EXISTING | ADAPT_EXISTING | COMBINE_SOLUTIONS | CONTINUE_NEW_PRODUCT_DISCOVERY | PAUSE_FOR_VALIDATION | REJECT_OR_ARCHIVE
- Reasoning: <why this outcome, specifically>
- Alternatives Considered: <the other outcomes weighed and why they were not selected>
- Remaining Assumptions: <what's still unverified>
- Confidence: <per skill 59's Output Modes, scaled to stakes>
```

## Notes

- This brief is the run's own artifact, referenced from `run-state.md`, not embedded in it — matching `../../ENGINE_SPEC.md`'s pattern of referencing rather than duplicating large content.
- This template does not replace `04-prd-skill`'s PRD template — a brief that reaches `CONTINUE_NEW_PRODUCT_DISCOVERY` hands off to `workflows/01-new-product-workflow/WORKFLOW.md` (which already produces a PRD via `04-prd-skill`), it does not produce a PRD itself. Idea Discovery's job ends at the decision, per Constitution Principle 2 (Problem Before Solution) — it does not design the solution.
