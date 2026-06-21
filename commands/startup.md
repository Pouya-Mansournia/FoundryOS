# Command
/startup

## Purpose
The broadest command — runs the full founder lifecycle on a new idea, from problem statement through a buildable, fundable plan. Equivalent to handing the request to the Meta-Agent with no scope restriction; the Meta-Agent decides which Agents actually run.

## Activated Agents
- Meta-Agent selects from all 10 Agents based on the request (typically CEO, CPO, CBO (naming/positioning, right after CPO), then CTO/CIO depending on product type, CFO, CRO)

## Activated Skills
- Determined dynamically — see `meta-agent/META_AGENT.md` for routing logic

## Workflows
- `01-new-product-workflow`
- `08-company-building-workflow`

## Output
- Problem Statement & PRD
- Naming & Positioning (CBO)
- Architecture (software, hardware, or AI — as applicable)
- Financial Model
- GTM Plan
- Org Structure
- Roadmap

## Example
`/startup Help me go from idea to a fundable, buildable plan for [describe your idea].`
