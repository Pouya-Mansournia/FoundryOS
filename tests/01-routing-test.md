# 01 Routing Test

Tests whether the Meta-Agent correctly classifies a request and selects the right Agent set — the first decision in `meta-agent/META_AGENT.md`'s 7-step "What the Meta-Agent Does" sequence.

## Test Prompt
Make the company investor-ready.

## Expected Agents
- CEO-Agent
- CFO-Agent
- CPO-Agent
- CRO-Agent
- CTO-Agent
- CIO-Agent

## Expected Skills
- 03-strategy-skill
- 07-finance-skill
- 08-gtm-skill
- 38-fundraising-investor-skill
- 21-ai-product-skill
- 23-robotics-product-skill

## Expected Output
One merged "Meta-Agent Result" covering: the strategic narrative (CEO), unit economics and fundraising materials (CFO), product/PMF evidence (CPO), GTM/pipeline evidence (CRO), and technical or hardware diligence readiness (CTO and/or CIO, depending on whether the company's product is software, hardware, or both). All five-plus domains should read as one investor-readiness narrative, not five separate memos.

## Pass / Fail Criteria
**PASS** if the Meta-Agent selects CEO, CFO, CPO, and CRO unconditionally, and includes CTO-Agent and/or CIO-Agent based on what the company's product actually is — flagging in "Missing Inputs / Assumptions" if that isn't known yet, per the routing rule `(CTO or CIO, whichever owns the product)`.

**FAIL** if CEO, CFO, CPO, or CRO is dropped; if CTO and CIO are both included without any stated reasoning when the product type is ambiguous; or if the output is delivered as separate per-agent sections instead of one combined executive answer.
