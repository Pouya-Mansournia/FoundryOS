# Getting Started

Three speeds, depending on how much time you have right now.

## The 30-second version

1. Open Claude (or ChatGPT, Cursor, Windsurf).
2. Point it at the `FoundryOS` folder.
3. Type: `/startup Help me go from idea to a fundable, buildable plan for [your idea].`

That's it — the Meta-Agent figures out which specialists to call.

## The 5-minute version

1. Follow [`INSTALL.md`](INSTALL.md) to download and extract the repository.
2. Follow the setup guide for your environment ([`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md), [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md), [`docs/CURSOR_SETUP.md`](docs/CURSOR_SETUP.md), or [`docs/WINDSURF_SETUP.md`](docs/WINDSURF_SETUP.md)).
3. Skim [`COMMANDS.md`](COMMANDS.md) so you know which command matches what you're trying to do — product (`/cpo`, `/prd`), technical (`/cto`, `/architecture`), hardware/robotics (`/cio`, `/hardware`, `/robotics`), money (`/cfo`, `/finance`, `/fundraising`), growth (`/cro`, `/gtm`), brand/identity (`/brand`, `/logo`, `/naming`, `/voice`), people (`/chro`).
4. Run one command against something real you're actually working on.

## The 30-minute version

1. Do the 5-minute version first.
2. Read [`README.md`](README.md)'s Architecture section to understand the five layers: Modules → Skills → Agents → Meta-Agent → Workflows, plus the Advanced Layer on top (Memory, Reflection, Critic, Planner, Knowledge Graph) — see [`ADVANCED_LAYER.md`](ADVANCED_LAYER.md).
3. Open one full `workflows/*/WORKFLOW.md` file (try `workflows/01-new-product-workflow/WORKFLOW.md`) to see how a multi-agent sequence is actually structured end to end.
4. Try chaining commands the way a real plan would run: `/prd` → `/architecture` → `/finance` → `/critic` → `/planner`.
5. Skim [`docs/EXAMPLES.md`](docs/EXAMPLES.md) for full worked runs.

## Your first project, worked example

Say you're exploring a SaaS idea for internal tooling. A realistic first session:

```
You:  /prd We're building an internal tool that lets ops teams track vendor
      contracts and renewal dates. Help me write a PRD.

[Claude returns a PRD: problem statement, ICP, requirements, success metrics]

You:  /architecture Design the system architecture for this, multi-tenant,
      using the PRD above.

[Claude returns: system architecture, data model, tech stack]

You:  /critic Stress-test the PRD and architecture together before I share
      them with my co-founder.

[Claude returns: weaknesses, risks, unstated assumptions]
```

Three commands, one coherent thread, no need to re-explain context each time — that's the system working as intended. From here, see [`docs/TUTORIALS.md`](docs/TUTORIALS.md) for more structured walkthroughs.
