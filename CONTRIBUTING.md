# Contributing

FoundryOS is a knowledge system, not a codebase — "contributing" mostly means writing or refining markdown files inside an established structure. This guide covers what that structure is and how to add to it without breaking it.

## Before you start

Read [`README.md`](README.md)'s Architecture section and skim `knowledge-graph/KNOWLEDGE_GRAPH.md` so you know how Modules, Skills, Agents, Workflows, and the Advanced Layer depend on each other. Most contribution mistakes are dependency mistakes — adding a Skill no Agent owns, or a command that points at a Workflow that doesn't exist.

All participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Found a security-relevant issue (e.g. content that could cause an AI assistant to behave unsafely) rather than a normal inconsistency? Report it privately per [`SECURITY.md`](SECURITY.md) instead of opening a public issue. For everything else, use the templates under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE) to report an inconsistency or propose an addition, and [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) when you open a PR.

## Folder structure

```
skills/          {NN}-{name}-skill/SKILL.md — reusable capabilities, each built from 3-12 atomic Module
                 files that live inside the skill folder itself (42-58 are CBO-Agent's brand domain;
                 there's no standalone top-level modules/ folder — see README.md's Architecture section)
agents/          {Role}-Agent/AGENT.md — Skill ownership
meta-agent/      routing logic
workflows/       named multi-agent sequences
memory/          persistent context
reflection-agent/, critic-agent/, planner-agent/   advanced-layer agents
knowledge-graph/ dependency maps
commands/        slash-command definitions (documentation source of truth)
.claude/commands/ generated Claude Code slash commands — see scripts/generate_claude_commands.py
scripts/         maintenance scripts (currently: the .claude/commands/ generator)
registry/        canonical Agent/Skill reference tables
examples/, tests/  worked runs and routing test cases
docs/            setup guides, FAQ, roadmap, tutorials
assets/          diagrams, banners, social-preview source files
brand/           brand/BRAND_OS.md — the Brand OS charter
```

## Style guide

- **Markdown only.** No code, no executables.
- **Stay generic.** Never name a specific company, product, or brand — every example should be written so it's obviously reusable. If you need a placeholder, use "the company" or a generic descriptor like "a robotics startup."
- **Match the existing format exactly.** A new `SKILL.md` should look like the other 59 (this includes the 17 brand Skills, `42-brand-strategy-skill` through `58-brand-roadmap-skill`, and the cross-cutting `59-problem-solving-decision-modeling-skill` — same template, no special-casing). A new `commands/*.md` should follow the Purpose / Activated Agents / Activated Skills / Workflows / Output / Example template used by all 41 existing commands.
- **Use diagrams and arrows where they clarify a sequence or dependency** — see any `knowledge-graph/*.md` file for the house style (ASCII arrows, not embedded images).

## How to add a Skill

1. Create `skills/{NN}-{name}-skill/SKILL.md` with: What this skill does, Source Modules, Output.
2. Add it to the right Agent's `agents/{Role}-Agent/AGENT.md` Skills list.
3. Add a row to `registry/SKILL_REGISTRY.md`.
4. If it changes an Agent's typical outputs, update `registry/AGENT_REGISTRY.md` and `knowledge-graph/SKILL_GRAPH.md`.

## How to add an Agent

Think twice — the C-suite structure is intentionally stable (10 Agents as of this writing), and Skill ownership has been reassigned across existing Agents before rather than requiring a new one. CBO-Agent is the precedent for when a new Agent actually earns its place: brand/identity work didn't sit cleanly inside CPO-Agent's or CMO-Agent's mandate, so it got its own Agent and its own Skill range (`42`-`58`) instead of being grafted onto either. Conversely, `59-problem-solving-decision-modeling-skill` is the precedent for when a new *capability* does **not** warrant a new Agent — it's cross-cutting by nature (activates alongside whatever domain Agent a decision touches), so it was added as a Skill under the most fitting existing Agent (CEO-Agent, alongside `40-meta-orchestration-skill`) instead of becoming an 11th Agent. If a new Agent is genuinely warranted (a new mandate with no existing owner and no clean overlap), give it a non-overlapping mandate, add `agents/{Role}-Agent/AGENT.md`, and update `registry/AGENT_REGISTRY.md` plus the Meta-Agent's routing logic in `meta-agent/META_AGENT.md`.

## How to add a Command

1. Create `commands/{name}.md` following the existing template.
2. Ground every Activated Skill and Workflow reference in what's actually in `registry/AGENT_REGISTRY.md` and `workflows/` — don't invent a skill or workflow name.
3. Add a row to [`COMMANDS.md`](COMMANDS.md)'s table.
4. Run `python3 scripts/generate_claude_commands.py` to regenerate `.claude/commands/` so your new command is testable as a real Claude Code slash command. Don't hand-edit files inside `.claude/commands/` directly — they're generated output and will be overwritten the next time someone runs the script.

## How to add a Workflow

1. Create `workflows/{NN}-{name}-workflow/WORKFLOW.md` with the standard sections: Purpose, Inputs, Meta-Agent, Agent Execution Order, Skill Selection, Artifacts Produced, Validation, Risks, Final Outputs, Example Prompt.
2. Update `knowledge-graph/WORKFLOW_GRAPH.md` with its relationships to other Workflows.
3. Consider whether it needs a matching command in `commands/`.

## Pull request guidelines

- One logical change per PR — a new Skill, a new command, a doc fix. Don't bundle unrelated structural changes.
- State what you changed and why in the PR description, and list every file you touched, including registries and knowledge-graph files (these are easy to forget and the most common source of drift).
- Run the routing tests in `tests/` against your change where relevant, and describe the result in the PR.
- If your change affects the Architecture diagram or folder structure, update `README.md` in the same PR — don't leave documentation to a follow-up.

## Versioning

Structural milestones (a new layer, a new capability class) get a version bump in `VERSION.md` and an entry in `CHANGELOG.md`. Routine additions within an existing layer (one more Skill, one more example) don't require a version bump.
