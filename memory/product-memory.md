# Product Memory

## Purpose
A running record of what's been built, what's been shipped, and what the product scorecard actually showed — so roadmap decisions are made against real product history instead of an idealized memory of it.

## Stored Information
- PRD history: what was scoped, what shipped, and what was cut, with dates
- Product scorecard trend over time (PMF signal, retention, reliability metrics)
- Features shipped vs. features that moved the North Star metric (these are not always the same list)
- Known scope cuts and the reason for each — useful context the next time a similar feature is proposed

## Update Rules
- Every PRD that reaches `04-prd-skill` sign-off gets an entry here, including ones that were later descoped — descoped work is still a record worth keeping
- Scorecard updates should include the metric, the value, and the comparison to the prior period, not just a snapshot
- When a shipped feature doesn't move the metric it was built for, log that explicitly — this is exactly the kind of signal `reflection-agent/` should pick up

## Usage
Read by CPO-Agent before any new PRD pass, to check whether a similar feature was already tried and what happened. Read by `reflection-agent/REFLECTION_AGENT.md` when looking for patterns across multiple product decisions.

## Relationships
- Fed by every workflow that produces a PRD (`01-new-product-workflow`, `02-saas-product-workflow`, `03-hardware-product-workflow`, `04-ai-product-workflow`, `05-robotics-product-workflow`)
- Feeds `lessons-learned.md` when a shipped feature underperforms its stated goal
- Cross-referenced by `knowledge-graph/ARTIFACT_GRAPH.md` to trace which PRD produced which downstream artifact
- Read alongside `design-memory.md` and `voice-memory.md` whenever a PRD reaches the build stage, so the shipped surface matches the current design tokens and voice instead of drifting from them

## Examples
```
[2026-02-01] PRD shipped: "draft-assist AI feature" — goal: -30% handle
            time. Result (60 days post-launch): -22% handle time, CSAT flat.
            Below target but directionally positive — kept, not reverted.
[2026-03-18] PRD descoped: "multi-language support" — cut from v1 scope,
            reason: retrieval/eval design wasn't ready, not a priority call
[2026-05-02] Scorecard: PMF signal score 7.2/10 (prior period 6.8/10),
            retention 84% (prior period 81%)
```
