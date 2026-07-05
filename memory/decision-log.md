# Decision Log

## Purpose
A single chronological record of every material decision made across all Agents, regardless of domain — the one place to answer "what did we decide, when, and why" without having to check nine different memory files.

## Stored Information
- Date, the decision itself, which Agent(s) made it, and the stated reasoning
- What alternative(s) were considered and rejected, where relevant
- Links to the domain-specific memory file the decision also belongs to (e.g., a pricing decision logs here *and* gets detail in a future pricing-specific memory file, if one is added)
- Outcome, backfilled once known (did the decision work out — this is what makes the log useful in hindsight, not just an audit trail)

### Decision Record (for decisions run through `59-problem-solving-decision-modeling-skill`)
Decisions produced with the problem-solving and decision-modeling Skill log the fuller record below instead of a one-line entry, so the quantitative model and its assumptions survive past the moment the decision was made:
```
Decision ID
Date
Decision Owner
Decision Statement
Context
Options Considered
Selected Option
Evidence
Assumptions
Quantitative Model            (which formula(s) from FORMULA_LIBRARY.md, and the inputs used)
Expected Outcome
Guardrails
Confidence
Review Date
Actual Outcome                (backfilled)
Lesson                        (backfilled — feeds lessons-learned.md the same way any other entry does)
```

## Update Rules
- Log the decision at the time it's made, not retroactively — retroactive logging tends to rationalize the decision instead of recording it honestly
- Every entry needs a stated reason; "we decided X" without "because Y" is not a useful log entry
- Revisit entries older than one quarter to backfill the outcome field where it's now known — this is what turns a log into a learning system feeding `lessons-learned.md`

## Usage
Read by `reflection-agent/REFLECTION_AGENT.md` as the primary input for finding patterns across decisions. Read by CEO-Agent when a new decision appears to conflict with a past one, to check whether the past decision was ever formally reversed.

## Relationships
- Cross-cutting — every other memory file's "Update Rules" reference logging the change here first when it represents a real decision, not a routine data refresh
- Feeds `lessons-learned.md` directly: an entry with a poor outcome backfilled is a lessons-learned candidate
- Feeds `knowledge-graph/ARTIFACT_GRAPH.md` as the audit trail behind why an artifact exists in its current form
- The Decision Record format above is written by `skills/59-problem-solving-decision-modeling-skill/`'s Output Contract (Decision Statement through Confidence Assessment) and read back by `critic-agent/CRITIC_AGENT.md` (to check claims against history) and `reflection-agent/REFLECTION_AGENT.md` (to backfill Actual Outcome and Lesson once known)

## Examples
```
[2026-03-01] DECISION: Move governance to monthly board cadence (was
            informal weekly). Reason: board now includes outside investors
            post-seed; weekly was never going to scale. Outcome: TBD.
[2026-04-22] DECISION: Hold pricing steady despite new lower-priced
            competitor. Reason: CFO-Agent's unit economics showed matching
            their price would break gross margin. Outcome (60 days later):
            no measurable increase in lost deals attributed to price.
```
