# 05 Full System Test

The end-to-end test: a single request that spans hardware production, fundraising, and hiring at once. This exercises routing, agent selection, skill selection, the documented Execution Order, shared-skill handling (`35-npi-manufacturing-skill`), contradiction detection, and missing-input handling all in one pass — nothing this test checks can be faked by getting any single layer right in isolation.

## Test Prompt
We're a 15-person startup with a hardware product (a robotics arm) about to enter mass production. We also want to raise a Series A in 3 months and need to double headcount. Give us a full plan.

## Expected Agents
- CEO-Agent
- CPO-Agent
- CIO-Agent
- COO-Agent
- CFO-Agent
- CHRO-Agent

`CRO-Agent` and `CMO-Agent` are not expected — nothing in the prompt touches GTM, pricing, or marketing. `CTO-Agent` is optional: include it only if the Meta-Agent identifies a distinct software/cloud layer beyond what CIO-Agent's `32-embedded-skill` already covers, and state why.

## Expected Skills
- 13-corporate-os-skill (CEO-Agent)
- 04-prd-skill (CPO-Agent)
- 22-hardware-product-skill, 41-mechatronics-skill, 35-npi-manufacturing-skill (CIO-Agent)
- 09-operations-skill, 18-stage-gate-skill, 28-risk-management-skill, 35-npi-manufacturing-skill (COO-Agent)
- 07-finance-skill, 38-fundraising-investor-skill (CFO-Agent)
- 39-people-culture-skill (CHRO-Agent)

## Expected Output
One merged executive answer that sequences production ramp, fundraising narrative, and hiring plan against a **single, consistent timeline and headcount/runway number** — not three independent plans that quietly assume different numbers. `35-npi-manufacturing-skill` should appear once as a shared CIO/COO deliverable, not twice as duplicated output. The answer should follow the documented Execution Order: CEO-Agent first, CPO-Agent next, CIO-Agent/COO-Agent next, CFO-Agent next, CHRO-Agent last.

## Pass / Fail Criteria
**PASS** if:
1. All six expected agents are selected and sequenced in the documented order (CEO → CPO → CIO/COO → CFO → CHRO).
2. `35-npi-manufacturing-skill` is run once and credited to both CIO-Agent and COO-Agent, not duplicated as two separate write-ups.
3. Section 6 (Contradictions/Conflicts) explicitly surfaces the tension between doubling headcount *before* a raise closes and a runway that hasn't been funded yet — this is the test's core contradiction-detection check (behavior #7 in `META_AGENT.md`).
4. Section 7 (Missing Inputs/Assumptions) flags at least one real unknown (current burn rate, current headcount, mass-production volume, target raise size) instead of silently assuming it away.
5. Next Actions are specific to this scenario's numbers and timeline, not generic startup advice.

**FAIL** if any expected agent is dropped or an unjustified agent (CRO, CMO) is added; if the headcount-vs-runway tension is missed entirely; if `35-npi-manufacturing-skill` output is duplicated rather than shared; or if the six agents' input reads as six disconnected plans instead of one.
