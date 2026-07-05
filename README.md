# FoundryOS

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Version](https://img.shields.io/badge/version-4.0.0-success.svg)](VERSION.md) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Contributor%20Covenant-ff69b4.svg)](CODE_OF_CONDUCT.md)

**Build Anything. Think Like a Team.**

*Open Source Agentic Operating System*

FoundryOS turns a large body of builder/operator knowledge into something an AI assistant can actually use: a structured stack of Modules, Skills, and Agents, coordinated by a single Meta-Agent that knows which specialist to call for any given request — and merges their output into one coherent answer instead of ten disconnected ones. On top of that core, a Workflows layer packages the most common request shapes into reusable sequences, an Advanced Layer adds memory and self-critique, a Brand Operating System threads identity and voice through everything the other Agents produce, and a Commands layer lets you trigger any of it with a short `/slash` command.

It's designed to be dropped into any AI assistant that can read a project's files — Claude, ChatGPT, Cursor, Windsurf, or any agentic coding/chat environment with file access — and used as a standing operating system for building anything: a company, a product, a piece of hardware, a brand, a go-to-market plan.

**Who it's for:** founders who want a structured starting point instead of a blank page; engineers and technical leads who need a CTO/CIO-level second opinion without hiring one yet; product managers who want PRDs, scorecards, and roadmaps in a consistent format; researchers and builders prototyping something new who need the right specialist framing without context-switching between five different mental models; teams who need a name, a logo, a voice, or a design system and don't yet have a CBO to ask; and teams who want their AI assistant to think like a full cross-functional org instead of one generalist.

---

## Architecture

```
179 Modules
      ↓
 59 Skills
      ↓
 10 Agents
      ↓
 1 Meta-Agent
      ↓
 11 Workflows
      ↓
 Memory
      ↓
 Reflection Agent
      ↓
 Critic Agent
      ↓
 Planner Agent
      ↓
 Knowledge Graph
      ↓
 Brand Intelligence
      ↓
 40 Commands
      ↓
 Artifacts
```

This is the layer inventory — what exists, bottom-up. Three things worth being precise about:

The actual runtime loop those middle five (Memory → Reflection → Critic → Planner → Knowledge Graph) run in is slightly different and is documented precisely in [`ADVANCED_LAYER.md`](ADVANCED_LAYER.md): Memory feeds the Planner, the Planner's roadmap executes, Reflection writes the outcome back into Memory, and the Critic checks new plans against Memory before they ship — the Knowledge Graph is the map of all of it, not a step in the sequence.

**Brand Intelligence is not a separate add-on bolted onto the end** — it's CBO-Agent's Skills, Memory files, and Artifacts woven into every layer above it (see [`brand/BRAND_OS.md`](brand/BRAND_OS.md) and [`knowledge-graph/BRAND_GRAPH.md`](knowledge-graph/BRAND_GRAPH.md)). It's listed as its own stripe in this diagram only because the Knowledge Graph layer needed an explicit name for "where brand connects everything else," not because brand work happens in a separate phase after the rest of the system has already run.

And the diagram ends at **Artifacts**, not Commands — Commands are how you trigger the system, Artifacts are what you actually walk away with (a PRD, a BOM, a financial model, a Brand Strategy Brief). Earlier versions of this diagram stopped at Commands, which described the entry point but not the output; see [`knowledge-graph/ARTIFACT_GRAPH.md`](knowledge-graph/ARTIFACT_GRAPH.md) for how Artifacts map back to the Workflows and Agents that produce them.

**Modules** are the atomic layer — 179 self-contained units of domain knowledge (e.g. `01_Discovery_OS`, `35_AI_Architecture_OS`, `42_Regulatory_OS`, `58_Brand_Roadmap_OS`, `176_Solution_Formula_OS`), numbered `00`–`177` with one legacy duplicate at `99` (flagged in [`AUDIT_REPORT.md`](AUDIT_REPORT.md)). Modules are never called directly; they're the raw material Skills are built from.

**Skills** (59) are reusable capabilities, each compiled from 3–12 Modules — `04-prd-skill`, `31-ai-architecture-skill`, `41-mechatronics-skill`, `46-logo-system-skill`. Every Skill has a defined input, source Modules, and output (see [`registry/SKILL_REGISTRY.md`](registry/SKILL_REGISTRY.md)). Seventeen of the 59 (`42` through `58`) are CBO-Agent's brand domain; one, `59-problem-solving-decision-modeling-skill`, is a cross-cutting reasoning engine (owned by CEO-Agent) rather than a domain — it frames a problem, builds a causal/metric model, and selects reusable quantitative formulas for a decision, and combines with whichever domain Skill(s) that decision touches instead of replacing them.

**Agents** (10) are C-suite-shaped owners of a cluster of Skills — CEO, CPO, CTO, CIO, COO, CFO, CRO, CMO, CBO, CHRO (see [`registry/AGENT_REGISTRY.md`](registry/AGENT_REGISTRY.md)). One Skill, `35-npi-manufacturing-skill`, is intentionally co-owned by CIO-Agent and COO-Agent because hardware NPI genuinely sits at the intersection of engineering and operations. CBO-Agent (Chief Brand Officer) sits directly after CPO-Agent in the default execution order, attaching name, voice, and visual identity to a product before anyone builds or sells it.

**Meta-Agent** (1) reads a request, classifies it, decides which Agent(s) and Skill(s) should run, sequences them, and merges their output into one executive answer — flagging contradictions and missing inputs instead of guessing silently. It auto-activates CBO-Agent on any request that signals brand, identity, naming, logo, tagline, voice, design system, community, or visual-identity intent, even if the word "brand" never appears, and combines `59-problem-solving-decision-modeling-skill` into any request that's actually a decision ("should we," "which option," "is this worth it") rather than a request for a known artifact. Full spec: [`meta-agent/META_AGENT.md`](meta-agent/META_AGENT.md).

**Workflows** (11) are named, reusable sequences for the most common request shapes — new product, SaaS, hardware, AI, robotics, fundraising, GTM, company building, hiring, strategic planning, and problem solving/decision modeling. CBO-Agent runs inside the original 10 by default in 9 of them (`09-hiring-workflow` treats it as conditional); the 11th, `11-problem-solving-decision-workflow`, is the reasoning layer those ten call into at their own decision gates and can also run standalone. See [`workflows/`](workflows).

**Advanced Layer** — Memory (13 persistent files: 7 cross-domain, 6 brand-specific), Reflection Agent, Critic Agent, Planner Agent, and a Knowledge Graph (6 files, including [`BRAND_GRAPH.md`](knowledge-graph/BRAND_GRAPH.md)) — lets the system accumulate context and self-critique across runs instead of starting from zero each time, including brand consistency, voice consistency, and narrative quality. Full explanation: [`ADVANCED_LAYER.md`](ADVANCED_LAYER.md).

**Commands** (40) expose every Agent, Workflow, and Advanced-Layer component as a short slash command — `/cpo`, `/saas`, `/critic`, `/fundraising`, `/brand`, `/logo`, `/voice`, `/solve`. A command is a pointer into logic that already exists; it adds no new behavior. See [`COMMANDS.md`](COMMANDS.md).

**Artifacts** are the concrete deliverables a run produces — PRD, System Architecture, BOM, Financial Model, GTM Plan, Roadmap, Brand Strategy Brief, Logo System, Design System, and so on. Every Artifact traces back to the Workflow and Agent(s) that produced it; see [`knowledge-graph/ARTIFACT_GRAPH.md`](knowledge-graph/ARTIFACT_GRAPH.md).

---

## Features

- **Multi-agent by default.** Real problems cut across domains; the system runs the right specialists in the right order instead of forcing one generalist persona to cover everything shallowly.
- **One coherent answer, not ten.** The Meta-Agent merges multi-agent output into a single voice and explicitly surfaces contradictions and missing inputs.
- **Reusable Workflows.** The 10 most common request shapes are pre-sequenced so they don't have to be re-derived from scratch every time.
- **Memory that compounds.** The Advanced Layer means the system gets measurably better at a given kind of decision the second time, not just the first.
- **Brand built in, not bolted on.** A full Brand Operating System — strategy, naming, identity, design system, voice, storytelling, and community — runs through CBO-Agent and attaches to every Workflow, not a standalone "marketing" afterthought.
- **Slash commands everywhere.** 39 commands give you a fast, explicit way to invoke any Agent, Workflow, or Advanced-Layer component.
- **Zero install, zero lock-in.** It's markdown. Works anywhere an AI assistant can read files; nothing to run, build, or host.
- **Fully generic templates.** No placeholder company, product, or example-brand names baked into the system — every template is written to be reused as-is for whatever you're actually building.

## Supported Environments

| Environment | Slash commands | Setup guide |
|---|---|---|
| Claude (Projects) | Via instruction | [`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md) |
| Claude Code | Native | [`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md) |
| ChatGPT (Projects / Custom GPT) | Via instruction | [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md) |
| Cursor | Via `.cursorrules` | [`docs/CURSOR_SETUP.md`](docs/CURSOR_SETUP.md) |
| Windsurf | Via `.windsurfrules` | [`docs/WINDSURF_SETUP.md`](docs/WINDSURF_SETUP.md) |
| Any other agentic environment with file access | Via instruction | Follow the Claude Projects pattern |

---

## Quick Start

1. Download and extract the repository — see [`INSTALL.md`](INSTALL.md).
2. Point your assistant at it using the setup guide for your environment (table above).
3. Run a command:

   > `/startup Help me go from idea to a fundable, buildable plan for [your idea].`

See [`GETTING_STARTED.md`](GETTING_STARTED.md) for the 30-second / 5-minute / 30-minute onboarding paths, and [`QUICKSTART.md`](QUICKSTART.md) for how the Meta-Agent's plain-English routing works if you'd rather not use a command.

## Commands

40 slash commands cover every Agent, Workflow, and Advanced-Layer component — `/cpo`, `/cto`, `/cio`, `/coo`, `/cfo`, `/cro`, `/cmo`, `/chro`, `/ceo`, `/planner`, `/critic`, `/reflection`, `/prd`, `/gtm`, `/fundraising`, `/startup`, `/company-builder`, `/saas`, `/hardware`, `/robotics`, `/ai-product`, `/strategy`, `/market`, `/finance`, `/architecture`, `/operations`, `/solve`, `/brand`, `/logo`, `/naming`, `/tagline`, `/story`, `/design-system`, `/identity`, `/community`, `/website`, `/copy`, `/voice`, `/colors`, `/social-assets`. Full table and usage: [`COMMANDS.md`](COMMANDS.md).

### Claude Code slash commands

The `commands/` folder above is documentation — Purpose, Activated Agents, Activated Skills, Workflows, Output, Example — written for a human (or any assistant) to read and follow. `.claude/commands/` is the executable layer on top of it: 40 matching files, in Claude Code's native slash-command format, that ship pre-built in this repo. Open the repo in Claude Code and `/cpo`, `/robotics`, `/brand`, and the rest just work — no setup step.

Each generated file is a thin wrapper, not a duplicate. It instructs Claude Code to read the relevant Agent file(s) (and `meta-agent/META_AGENT.md` for multi-Agent commands) live off disk before answering, carries the full command spec inline, and points to the Meta-Agent merge pattern in [`QUICKSTART.md`](QUICKSTART.md#worked-example) for commands that activate more than one Agent. This keeps `.claude/commands/` honest as the system evolves — it reads the Agent/Meta-Agent files as they exist today rather than freezing a snapshot of their content at generation time.

`commands/` remains the source of truth. If you add a new command or change an existing one, run `python3 scripts/generate_claude_commands.py` to regenerate `.claude/commands/` to match — see [`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md#method-2-claude-code) for how the two folders relate, and [`CONTRIBUTING.md`](CONTRIBUTING.md#how-to-add-a-command) for the full add-a-command checklist.

---

## Folder Structure

```
FoundryOS/
├── README.md                    ← you are here
├── INSTALL.md                   ← download + extract, then pick an environment
├── QUICKSTART.md                ← plain-English routing, example prompts
├── GETTING_STARTED.md           ← 30-second / 5-minute / 30-minute onboarding
├── COMMANDS.md                  ← full command table
├── FAQ.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md           ← Contributor Covenant v2.1
├── SECURITY.md                  ← vulnerability reporting process
├── .gitignore
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md        ← inconsistency / broken reference
│   │   └── feature_request.md   ← new Skill / Agent / Workflow / Command proposal
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/
│   └── commands/                ← 40 pre-built Claude Code slash commands (generated from commands/)
│       └── {name}.md
├── ADVANCED_LAYER.md            ← how Memory/Reflection/Critic/Planner/Graph interact
├── VERSION.md                   ← current version + structural roadmap
├── VERSIONING.md                ← versioning policy: major/minor/patch, release & tag rules
├── CHANGELOG.md                 ← version history, file-by-file
├── RELEASE_NOTES.md             ← publish-ready summary per version, for GitHub Releases
├── AUDIT_REPORT.md              ← v4.0 release audit (detailed)
├── FINAL_RELEASE_AUDIT.md       ← consolidated audit, auto-fix report, and publish checklist
├── LICENSE                      ← MIT
├── docs/                        ← secondary & reference documentation
│   ├── TUTORIALS.md             ← beginner / intermediate / advanced
│   ├── ROADMAP.md               ← v1 → v4 and future vision
│   ├── SHOWCASE.md              ← GitHub showcase kit: diagrams, banner & screenshot prompts
│   ├── EXAMPLES.md              ← index into examples/
│   ├── CLAUDE_SETUP.md
│   ├── CHATGPT_SETUP.md
│   ├── CURSOR_SETUP.md
│   └── WINDSURF_SETUP.md
├── assets/                      ← rendered visuals once produced — see docs/SHOWCASE.md for specs
├── brand/                       ← brand/BRAND_OS.md — the Brand OS charter and how it threads through every layer
├── skills/                      ← 59 Skills, each compiled from a Modules cluster (17 are CBO-Agent's brand domain,
│                                   1 — `59-problem-solving-decision-modeling-skill` — is a cross-cutting reasoning layer)
│                                   (no standalone modules/ folder — 179 module files live inside skills/{NN}-{name}-skill/)
│   └── {NN}-{name}-skill/
│       ├── SKILL.md
│       └── (source module files)
├── agents/                      ← 10 C-suite Agents, each owning a Skills cluster
│   └── {Role}-Agent/
│       ├── AGENT.md
│       └── (copies of owned skill folders)
├── meta-agent/
│   └── META_AGENT.md            ← the orchestrator
├── workflows/                   ← 11 named, reusable multi-agent sequences (10 product/company-shaped + 1 reasoning layer)
│   └── {NN}-{name}-workflow/
│       └── WORKFLOW.md
├── memory/                      ← 13 persistent context files (7 cross-domain, 6 brand-specific)
├── reflection-agent/
│   └── REFLECTION_AGENT.md
├── critic-agent/
│   └── CRITIC_AGENT.md
├── planner-agent/
│   └── PLANNER_AGENT.md
├── knowledge-graph/              ← 6 dependency-map files (incl. ARTIFACT_GRAPH.md, BRAND_GRAPH.md)
├── commands/                     ← 40 slash-command definitions
│   └── {name}.md
├── scripts/
│   └── generate_claude_commands.py  ← regenerates .claude/commands/ from commands/
├── registry/
│   ├── AGENT_REGISTRY.md        ← every Agent: mandate, skills, outputs, dependencies
│   └── SKILL_REGISTRY.md        ← every Skill: purpose, source modules, outputs, dependencies
├── examples/                     ← worked end-to-end runs
│   ├── ai-product-example.md
│   ├── robotics-product-example.md
│   ├── saas-dashboard-example.md
│   ├── investor-readiness-example.md
│   ├── manufacturing-plan-example.md
│   ├── team-scaling-example.md
│   ├── brand-identity-example.md
│   ├── brand-narrative-community-example.md
│   └── decision-modeling-example.md
└── tests/                        ← routing, agent-selection, and brand-consistency test specs
```

---

## Examples

| Example | Scenario | Agents Involved |
|---|---|---|
| [`ai-product-example.md`](examples/ai-product-example.md) | Shipping an AI product feature | CPO, CTO, CEO |
| [`robotics-product-example.md`](examples/robotics-product-example.md) | Designing a robotics product from scratch | CIO, CTO, CPO, COO |
| [`saas-dashboard-example.md`](examples/saas-dashboard-example.md) | Architecting a SaaS analytics dashboard | CTO, CPO, CMO |
| [`investor-readiness-example.md`](examples/investor-readiness-example.md) | Getting fundraising-ready | CEO, CFO, CPO, CRO, CTO |
| [`manufacturing-plan-example.md`](examples/manufacturing-plan-example.md) | Building a hardware manufacturing readiness plan | CIO, COO, CFO |
| [`team-scaling-example.md`](examples/team-scaling-example.md) | Designing org structure, hiring system, and culture at 15 people | CEO, COO, CHRO, CBO, CFO |
| [`brand-identity-example.md`](examples/brand-identity-example.md) | Building a brand, name, logo, and design system from zero | CEO, CBO |
| [`brand-narrative-community-example.md`](examples/brand-narrative-community-example.md) | Website, launch narrative, and community for an open-source launch | CBO, CRO |
| [`decision-modeling-example.md`](examples/decision-modeling-example.md) | Three worked decisions (AI inference hosting cost trade-off, SaaS pricing tier, manufacturing inspection automation) using `59-problem-solving-decision-modeling-skill` | CEO, CTO, CFO, COO |

See [`docs/EXAMPLES.md`](docs/EXAMPLES.md) for an indexed guide, including two scenarios (startup-building, GTM) shown as command walkthroughs rather than full example files.

## Screenshots

_Coming soon — this is a markdown-only system with no UI of its own, so "screenshots" means it running inside each supported assistant. The exact mockups, banner, GIF, and demo-video specs are already written up in [`docs/SHOWCASE.md`](docs/SHOWCASE.md); once rendered they land in `assets/`. They'll show: a Claude Project with FoundryOS loaded, a `/cpo` command running in Claude Code, and a Meta-Agent Result rendered end to end. If you'd like to contribute one from your own setup, see [`CONTRIBUTING.md`](CONTRIBUTING.md)._

---

## Roadmap

v1 shipped the core four layers (Modules → Skills → Agents → Meta-Agent). v2 added Workflows and the Advanced Layer. v3 added Commands and a full onboarding doc set. v4 is the FoundryOS rename, the `docs/`/`assets/` restructure, the Commands → Artifacts architecture fix, and a full Brand Operating System (CBO-Agent, 17 brand Skills, 6 brand Memory files, `BRAND_GRAPH.md`, and 13 brand Commands) integrated into every layer rather than appended as a tenth Agent that runs in isolation. v4.1 added a **Problem Solving and Decision Modeling** reasoning layer — `59-problem-solving-decision-modeling-skill` (CEO-Agent), a 29-formula reusable quantitative library, `11-problem-solving-decision-workflow`, and the `/solve` command — that frames ambiguous problems, builds causal and metric models, and selects the right quantitative formula for a decision instead of defaulting every request to a PRD. v5.0.0 (planned) is a Runtime, MCP/tool integration, and execution engine — autonomous, closed-loop workflows that don't need a human to re-prompt between steps. Full detail: [`docs/ROADMAP.md`](docs/ROADMAP.md). Versioning policy — what counts as major/minor/patch, and why the public release is v4.0.0 rather than v1.0.0: [`VERSIONING.md`](VERSIONING.md). Per-version publish notes: [`RELEASE_NOTES.md`](RELEASE_NOTES.md). Full v4.0 audit: [`AUDIT_REPORT.md`](AUDIT_REPORT.md). Consolidated final audit, auto-fix report, and GitHub publish checklist: [`FINAL_RELEASE_AUDIT.md`](FINAL_RELEASE_AUDIT.md).

## Community

This is an open-source-ready knowledge system. Contributions that add Modules, propose new Skills, refine Agent mandates, or add a new command are welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md), and use the issue/PR templates under [`.github/`](.github) to propose one or report a broken reference. Questions are probably already answered in [`FAQ.md`](FAQ.md). Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md); see [`SECURITY.md`](SECURITY.md) to report a vulnerability privately rather than via a public issue.

## License

MIT — see [`LICENSE`](LICENSE).
