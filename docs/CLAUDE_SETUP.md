# Claude Setup

There are two ways to run FoundryOS with Claude. Method 1 is faster to start; Method 2 (Claude Code) gives you real slash commands.

## Method 1: Claude Projects

1. Go to claude.ai and create a **New Project**.
2. Open **Project Knowledge** and upload the entire `FoundryOS` folder (or as many files as the project allows — at minimum, upload `meta-agent/META_AGENT.md`, `registry/AGENT_REGISTRY.md`, `registry/SKILL_REGISTRY.md`, and the `commands/` folder).
3. Start any conversation in the project with:

   > Use FoundryOS as my operating system. Read `meta-agent/META_AGENT.md` and operate as the Meta-Agent for every request in this project.

4. From then on, just talk to Claude normally, or use a command:

   > `/cpo` Take this idea from a problem statement to a structured PRD: [describe your idea].

   > `/cto` Design the system architecture for a multi-tenant SaaS product.

   > `/robotics` Take this robotics concept from requirements through a manufacturing-ready BOM.

   > `/brand` Define our brand archetype, naming shortlist, and positioning statement from scratch.

Claude reads the command's file in `commands/` to know which Agents, Skills, and Workflow to use — you don't need to explain anything beyond the command itself.

## Method 2: Claude Code

Claude Code supports real custom slash commands backed by files on disk, which is the closest thing to a native command palette for this system. FoundryOS ships these ready to go — there's nothing to set up.

1. Open the `FoundryOS` folder in Claude Code (or copy it into an existing project).
2. That's it. The repo already contains a `.claude/commands/` folder with all 40 commands pre-built — Claude Code picks it up automatically, no copying required.
3. Type `/` to see the full list of available commands.
4. Run one:

   > `/prd` Write a PRD for a usage-based billing feature.

Each file in `.claude/commands/` isn't a flat copy of the matching `commands/{name}.md` spec — it's a thin wrapper around it. When you run `/prd`, Claude Code is instructed to first read the relevant Agent file(s) (e.g. `agents/CPO-Agent/AGENT.md`) and, for multi-Agent commands, `meta-agent/META_AGENT.md`, live off disk before answering — the same live-file-reading pattern the Meta-Agent itself uses, rather than a static prompt baked in at copy time. It also carries the full Purpose / Activated Agents / Activated Skills / Workflows / Output spec from `commands/{name}.md` inline, and points to the worked example in `QUICKSTART.md` for how Meta-Agent should merge results when more than one Agent is activated.

### Keeping it in sync
`commands/` (documentation-style specs) remains the source of truth; `.claude/commands/` (executable wrappers) is generated from it. If you add or edit a command spec under `commands/`, run:

```
python3 scripts/generate_claude_commands.py
```

from the repo root to regenerate every file in `.claude/commands/` to match. Don't hand-edit files inside `.claude/commands/` — they'll be overwritten on the next run. See [`README.md`](../README.md#claude-code-slash-commands) and [`CONTRIBUTING.md`](../CONTRIBUTING.md#how-to-add-a-command).
