# 03 Skill Selection Test

Tests whether the Meta-Agent picks only the Skills relevant to the specific request from within an already-correct Agent, rather than defaulting to that Agent's entire Skill list. This is a direct test of behavior #4 in `meta-agent/META_AGENT.md`: *"Select the right Skills under each selected Agent... by reading that Agent's live AGENT.md Skills list and picking the ones relevant to the request (not the whole list by default)."*

## Test Prompt
Our embedded firmware is blowing the power budget on the new device — what's the path forward?

## Expected Agents
- CIO-Agent

## Expected Skills
- 32-embedded-skill
- 34-electronics-skill
- 41-mechatronics-skill

**Should NOT be selected:** `22-hardware-product-skill`, `23-robotics-product-skill`, `33-mechanical-skill`, `35-npi-manufacturing-skill` — CIO-Agent owns all seven, but this request is narrowly about firmware power draw, not the full hardware/robotics/NPI stack.

## Expected Output
A focused technical answer diagnosing the firmware/power-budget root cause (duty cycling, peripheral power states, clock gating) and the electronics-side mitigation (power design, rail budget) — not a full hardware product plan, BOM review, or NPI readiness assessment.

## Pass / Fail Criteria
**PASS** if the Meta-Agent selects only `32-embedded-skill`, `34-electronics-skill`, and `41-mechatronics-skill` (or a clearly justified subset/superset with stated reasoning), and the answer stays scoped to the power-budget problem.

**FAIL** if the Meta-Agent pulls in all seven of CIO-Agent's Skills by default, or if the answer drifts into unrelated territory (full BOM review, NPI scheduling, robotics navigation) that the prompt never asked about.
