# 06 Brand Routing Test

Tests whether the Meta-Agent auto-activates CBO-Agent and the right brand Skills when a request signals Brand/Identity/Logo/Naming/Tagline/Voice/Typography/Design-System/Community/Social-Assets/Website/Marketing-Identity/Visual-Identity/Storytelling/Positioning intent — even when the request never says the word "brand."

## Test Prompt
We need a name for our new product line, and our current logo doesn't feel right for it anymore.

## Expected Agents
- CBO-Agent

## Expected Skills
- 47-naming-skill
- 46-logo-system-skill
- 42-brand-strategy-skill *(upstream — the archetype must be checked before a new name or logo direction is screened against it)*

## Expected Output
A naming shortlist plus a logo-direction assessment that explicitly checks the new product line against the existing brand archetype in `memory/brand-memory.md`, rather than treating naming and the logo refresh as two unrelated requests.

## Pass / Fail Criteria
**PASS** if CBO-Agent is selected without the word "brand" appearing anywhere in the prompt, `47-naming-skill` and `46-logo-system-skill` are both selected, and the output reads the existing archetype before proposing new direction.

**FAIL** if CBO-Agent is missed entirely (naming and logo treated as generic, agent-less writing tasks), if only one of the two skills fires, or if the new naming/logo direction is proposed without checking it against the existing brand strategy already on file.
