# Command
/voice

## Purpose
Activates CBO-Agent to define or audit voice and tone — the attributes that stay constant, the tone shifts that are allowed by channel, and the banned phrases that keep slipping back in. The Skill every other content-producing command reads from before writing a word.

## Activated Agents
- CBO-Agent

## Activated Skills
- `53-voice-tone-skill` — voice attributes, tone-by-channel rules, banned-phrase list

## Workflows
- `02-saas-product-workflow`
- `04-ai-product-workflow`
- `05-robotics-product-workflow`

## Output
- Voice Attributes (3-5 adjectives, each with a "sounds like / doesn't sound like" example)
- Tone-by-Channel Matrix (support, marketing, in-product, social)
- Banned Phrases List

## Example
`/voice Our support tone and our marketing tone have drifted apart — define one voice with channel-specific tone variance, not two separate voices.`
