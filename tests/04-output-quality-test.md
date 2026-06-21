# 04 Output Quality Test

Tests whether the Combined Executive Answer itself meets the bar set by the Meta-Agent's Output Format and Operating Principles — not just whether routing was correct. Routing can be perfect and the output can still fail this test.

## Test Prompt
Build a GTM strategy.

## Expected Agents
- CPO-Agent
- CRO-Agent
- CMO-Agent

## Expected Skills
- 03-strategy-skill
- 08-gtm-skill
- 36-pricing-sales-skill
- 37-marketing-customer-success-skill

## Expected Output
A single "Meta-Agent Result" containing all nine sections defined in `meta-agent/META_AGENT.md` (Request Classification, Selected Agents, Selected Skills, Agent Execution Order, Combined Executive Answer, Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, Next Actions), where the Combined Executive Answer reads as one voice and every recommendation is specific enough to act on this week — a named channel, a named ICP segment, a stated pricing direction — not generic advice.

## Pass / Fail Criteria
**PASS** if all nine sections are present; CPO, CRO, and CMO's input reads as one merged plan rather than three stitched-together blocks; "Missing Inputs / Assumptions" states what was assumed (e.g. ICP, deal size, sales motion) rather than silently guessing; and zero generic-advice phrases ("increase brand awareness," "monitor the market," "iterate based on feedback") appear anywhere in the answer.

**FAIL** if any of the nine sections is missing or merged into another; if the answer is organized by agent ("CPO says... CRO says... CMO says...") instead of by topic; if assumptions are made without being stated; or if any recommendation is generic enough to apply to any company's GTM strategy unchanged.
