# Command
/critic

## Purpose
Activates the Critic Agent for an adversarial second pass over a Meta-Agent Result before it's treated as final — hunting contradictions, hidden risks, hallucinated claims, and missing dependencies, and checking the plan against `memory/lessons-learned.md` by name.

## Activated Agents
- Critic Agent (`critic-agent/CRITIC_AGENT.md`)

## Activated Skills
- Reads the Combined Executive Answer plus `memory/lessons-learned.md`; owns no Skill of its own

## Workflows
- Runs immediately after any workflow's Validation step, before Final Outputs ship

## Output
- Weaknesses
- Risks
- Unstated Assumptions
- Red Flags
- Recommendations

## Example
`/critic Stress-test this go-to-market plan before we commit budget to it.`
