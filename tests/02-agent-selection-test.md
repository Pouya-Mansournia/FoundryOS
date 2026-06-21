# 02 Agent Selection Test

Tests whether the Meta-Agent selects exactly the Agents a request needs — no relevant agent missing, no irrelevant agent pulled in. This is the precision/recall check on step 3 of "What the Meta-Agent Does."

## Test Prompt
Design a robotics product for warehouse inventory scanning.

## Expected Agents
- CPO-Agent
- CIO-Agent
- CTO-Agent
- COO-Agent

## Expected Skills
- 01-discovery-skill
- 04-prd-skill
- 23-robotics-product-skill
- 41-mechatronics-skill
- 05-architecture-skill
- 18-stage-gate-skill

## Expected Output
One merged executive answer covering product framing and PRD scope (CPO), robotics/mechatronics hardware architecture (CIO), fleet/navigation software architecture (CTO), and a stage-gate plan from prototype to production readiness (COO) — matching the shape of `examples/robotics-product-example.md`.

## Pass / Fail Criteria
**PASS** if CIO-Agent is selected as a first-class agent (not merged into or skipped in favor of CTO-Agent alone), and CFO-Agent, CRO-Agent, CMO-Agent, and CHRO-Agent are **not** selected, since nothing in the prompt touches financials, GTM, marketing, or hiring.

**FAIL** if CIO-Agent is missing or substituted by CTO-Agent for the hardware/mechatronics work; if any of CFO/CRO/CMO/CHRO is pulled in without a stated reason; or if the four selected agents' outputs are not merged into one answer.
