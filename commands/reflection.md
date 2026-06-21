# Command
/reflection

## Purpose
Activates the Reflection Agent to review a completed output after the outcome is known — comparing what was expected against what happened — and write a general lesson into `memory/lessons-learned.md` so the same mistake isn't repeated.

## Activated Agents
- Reflection Agent (`reflection-agent/REFLECTION_AGENT.md`)

## Activated Skills
- Writes to `memory/lessons-learned.md`; owns no Skill of its own

## Workflows
- Runs after any workflow's Final Outputs have produced a real-world result (a launch, a hire, a raise)

## Output
- Insights
- Lessons Learned
- Improvement Suggestions
- Patterns

## Example
`/reflection Our last launch underperformed on activation — extract the lesson before we plan the next one.`
