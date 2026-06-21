# Command
/planner

## Purpose
Activates the Planner Agent to turn an approved plan or Meta-Agent Result into a sequenced, resourced roadmap with an explicit critical path — the step between "here's what should happen" and "here's the dated plan a team can run against."

## Activated Agents
- Planner Agent (`planner-agent/PLANNER_AGENT.md`)

## Activated Skills
- Reads the approved Combined Executive Answer plus relevant `memory/` files; owns no Skill of its own

## Workflows
- Applies to any workflow's output once it has passed Validation (and Critic, if active)

## Output
- Roadmap
- Milestones
- Timeline
- Dependencies
- Critical Path

## Example
`/planner Turn this approved PRD and architecture into a dated roadmap with a critical path.`
