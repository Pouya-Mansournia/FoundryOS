# 08 Storytelling & Voice Test

Tests whether CBO-Agent produces a narrative arc and copy that match the voice rules in `memory/voice-memory.md` rather than defaulting to generic, archetype-less marketing language — and whether `53-voice-tone-skill` is checked *before* `51-storytelling-skill`/`52-copywriting-skill` produce output, not after.

## Test Prompt
Write our company's origin story for the About page, and make sure it doesn't read like every other startup's "we started in a garage" story.

## Expected Agents
- CBO-Agent

## Expected Skills
- 51-storytelling-skill
- 53-voice-tone-skill
- 45-content-system-skill

## Expected Output
An origin story with at least one specific, non-generic detail (a real decision point, a real cost of not solving the problem earlier) rather than templated startup-origin language, written in the tone-by-channel register `memory/voice-memory.md` specifies for the About page, and explicitly checked against the banned-phrases list before being returned.

## Pass / Fail Criteria
**PASS** if the story contains specific, checkable detail instead of generic founder-story tropes, if it matches the documented voice register, and if it avoids every phrase on the banned-phrases list in `memory/voice-memory.md`.

**FAIL** if the output reads as interchangeable with a generic AI-written founder story, if it ignores the voice register entirely, or if a banned phrase slips through unflagged.
