# Voice Memory

## Purpose
The brand's voice and tone rules by channel, kept current so every Agent writing customer-facing copy — a PRD's UI text, a pitch deck, a support reply — sounds like the same company said it.

## Stored Information
- Voice attributes currently in force (e.g., direct, technical, no jargon) and what they explicitly rule out
- Tone spectrum by channel — how voice flexes between, say, a technical doc and a social post, without breaking
- Words and phrases that are explicitly banned or discouraged, and why
- Examples of copy that got the voice right and copy that got corrected, kept side by side as a living reference

## Update Rules
- Update only on a deliberate voice/tone revision, with the old and new stated side by side
- Corrected-copy examples should be added whenever `53-voice-tone-skill` flags an off-voice piece, so the reference set grows from real mistakes, not hypotheticals
- Channel-specific tone notes should be added as new channels get used, not assumed to generalize automatically from an existing one

## Usage
Read by CBO-Agent before any voice or copywriting work. Read by CMO-Agent and CRO-Agent before campaign or sales copy ships, and by CTO-Agent/CPO-Agent for in-product UI text. Read by `critic-agent/` when checking an artifact for voice consistency.

## Relationships
- Downstream of `brand-memory.md` (voice is one expression of the strategy decided there) and closely paired with `content-memory.md`
- Feeds `lessons-learned.md` when an off-voice piece ships and gets caught post-launch instead of pre-launch
- Read alongside `design-memory.md` when voice and visual tone need to agree (a playful voice on a stark, formal layout reads as a mismatch)

## Examples
```
[2026-02-01] Voice attributes set: direct, technical, dry humor allowed
            sparingly — explicitly not "corporate friendly" or "hypey"
[2026-04-12] Banned phrase added: "revolutionary" — overused in the
            category, reads as noise to the target ICP
[2026-05-20] Off-voice correction: onboarding email rewritten — original
            used exclamation points the voice guide explicitly rules out
```
