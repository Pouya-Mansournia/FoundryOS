# 09 Community Test

Tests whether `49-community-skill` and `50-social-assets-skill` produce a community structure and assets that are grounded in the existing voice and design system, rather than a generic "set up a Discord" answer that could apply to any project.

## Test Prompt
We're open-sourcing our internal tool next month. Set up the community side of the launch.

## Expected Agents
- CBO-Agent

## Expected Skills
- 49-community-skill
- 50-social-assets-skill
- 53-voice-tone-skill *(input — read before community copy is written)*

## Expected Output
A community structure with a specific platform recommendation justified against the audience (not a default Discord recommendation regardless of fit), a moderation model that names who responds and how in week one, and a launch asset set that uses the existing design system rather than inventing new visuals for the occasion.

## Pass / Fail Criteria
**PASS** if the platform choice is justified against audience fit rather than assumed, if the moderation model names specific first-week ownership, and if launch assets are visually consistent with `memory/design-memory.md` and `memory/identity-memory.md`.

**FAIL** if the platform is chosen by default without justification, if moderation ownership is vague ("the team will respond"), or if launch assets introduce a visual style inconsistent with the existing brand.
