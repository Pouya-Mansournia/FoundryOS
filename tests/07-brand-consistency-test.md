# 07 Brand Consistency Test

Tests whether CBO-Agent's output stays consistent with previously established brand decisions across separate requests, rather than re-deriving the archetype, palette, or voice from scratch each time `memory/brand-memory.md`, `memory/identity-memory.md`, and `memory/design-memory.md` already hold an answer.

## Test Prompt
**Run 1:** Define our brand archetype and pick a color palette for our developer-tools company.
**Run 2 (separate session):** Now design a landing page for our new CLI tool.

## Expected Agents
- CBO-Agent (both runs)

## Expected Skills
- Run 1: `42-brand-strategy-skill`, `54-color-psychology-skill`
- Run 2: `56-ui-system-skill`, `44-design-system-skill`, `52-copywriting-skill`

## Expected Output
Run 2's landing page uses the same archetype, palette, and design tokens established in Run 1 — read from `memory/brand-memory.md` and `memory/design-memory.md` — without restating or silently changing them. If Run 2 proposes a palette or tone that contradicts Run 1, it must flag the contradiction explicitly rather than overwriting it quietly.

## Pass / Fail Criteria
**PASS** if Run 2 explicitly references the Run 1 archetype/palette decision (by name or by citing the memory file) and builds on it; if Run 2 ever needs to deviate, it states why and flags it as a deliberate brand evolution, not an accident.

**FAIL** if Run 2 invents a new palette or tone without checking memory first, if it contradicts Run 1 silently, or if it produces generic landing-page copy that could belong to any brand rather than this one.
