# Commands

FoundryOS exposes its Agents and Workflows as **slash commands** — short, memorable triggers that tell whichever assistant you're using (Claude, ChatGPT, Cursor, Windsurf) exactly which Agents, Skills, and Workflows to activate, without you having to spell that out every time.

A command is just a pointer into the system you already have: every file in [`commands/`](commands) names its Activated Agents, Activated Skills, relevant Workflows, and expected Output, in the same format. None of them add new logic — they're a faster way to invoke logic that already exists in `agents/`, `workflows/`, and the advanced layer.

How to use one: type the command followed by your request, e.g. `/prd Write a PRD for a usage-based billing feature.` See [`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md), [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md), [`docs/CURSOR_SETUP.md`](docs/CURSOR_SETUP.md), or [`docs/WINDSURF_SETUP.md`](docs/WINDSURF_SETUP.md) for how slash commands work in each environment.

**Claude Code users:** these all work as real, native slash commands out of the box — the repo ships a pre-built [`.claude/commands/`](.claude/commands) folder generated from the files below, so there's no setup step. Type `/` in Claude Code to see the full list.

---

## Agent Commands

These activate one C-suite Agent directly.

| Command | Purpose | File |
|---|---|---|
| `/ceo` | Vision, governance, org structure, orchestration | [commands/ceo.md](commands/ceo.md) |
| `/cpo` | Product discovery, strategy, PRD | [commands/cpo.md](commands/cpo.md) |
| `/cto` | Software/system/AI architecture | [commands/cto.md](commands/cto.md) |
| `/cio` | Hardware & robotics design, mechatronics | [commands/cio.md](commands/cio.md) |
| `/coo` | Operations, supply chain, stage gates, risk | [commands/coo.md](commands/coo.md) |
| `/cfo` | Finance, unit economics, scenario modeling | [commands/cfo.md](commands/cfo.md) |
| `/cro` | Go-to-market motion, pricing, sales pipeline | [commands/cro.md](commands/cro.md) |
| `/cmo` | Demand generation, brand, customer success | [commands/cmo.md](commands/cmo.md) |
| `/chro` | Hiring, org design, culture | [commands/chro.md](commands/chro.md) |
| `/brand` | Full Brand OS pass: archetype, strategy, naming, positioning, voice, rollout | [commands/brand.md](commands/brand.md) |

## Advanced-Layer Commands

These activate the learning loop on top of the core system.

| Command | Purpose | File |
|---|---|---|
| `/planner` | Turn an approved plan into a dated roadmap | [commands/planner.md](commands/planner.md) |
| `/critic` | Adversarial pass before a plan ships | [commands/critic.md](commands/critic.md) |
| `/reflection` | Extract lessons after an outcome is known | [commands/reflection.md](commands/reflection.md) |
| `/mcp` | Declare or check a live external-data need against a connected MCP tool | [commands/mcp.md](commands/mcp.md) |

## Artifact & Workflow Commands

These activate a specific deliverable or a multi-agent Workflow.

| Command | Purpose | File |
|---|---|---|
| `/prd` | Product Requirements Document | [commands/prd.md](commands/prd.md) |
| `/gtm` | Go-to-market plan | [commands/gtm.md](commands/gtm.md) |
| `/fundraising` | Investor-ready fundraising artifacts | [commands/fundraising.md](commands/fundraising.md) |
| `/startup` | Idea → fundable, buildable plan (broadest command) | [commands/startup.md](commands/startup.md) |
| `/company-builder` | Company-level governance, SOPs, people systems | [commands/company-builder.md](commands/company-builder.md) |
| `/saas` | SaaS product, end to end | [commands/saas.md](commands/saas.md) |
| `/hardware` | Hardware product, end to end | [commands/hardware.md](commands/hardware.md) |
| `/robotics` | Robotics product, end to end | [commands/robotics.md](commands/robotics.md) |
| `/ai-product` | AI product, end to end | [commands/ai-product.md](commands/ai-product.md) |
| `/strategy` | Strategy, positioning, business model | [commands/strategy.md](commands/strategy.md) |
| `/market` | Market sizing & competitor benchmarking | [commands/market.md](commands/market.md) |
| `/finance` | Financial model & scenario analysis | [commands/finance.md](commands/finance.md) |
| `/architecture` | System/software/data/AI architecture | [commands/architecture.md](commands/architecture.md) |
| `/operations` | SOPs, supply chain, stage gates | [commands/operations.md](commands/operations.md) |

## Reasoning & Decision Commands

This activates the cross-cutting reasoning layer directly — for a decision, not a known artifact.

| Command | Purpose | File |
|---|---|---|
| `/solve` | Frame a problem, build its causal/quantitative model, compare options, decide | [commands/solve.md](commands/solve.md) |

## Brand Commands

These activate CBO-Agent for a specific brand deliverable. `/brand` (above, under Agent Commands) is the broadest entry point — use these 12 when you already know which piece of the Brand OS you need.

| Command | Purpose | File |
|---|---|---|
| `/logo` | Logo system: wordmark, symbol, lockups, usage rules | [commands/logo.md](commands/logo.md) |
| `/naming` | Name generation and screening | [commands/naming.md](commands/naming.md) |
| `/tagline` | Tagline / one-line positioning statement | [commands/tagline.md](commands/tagline.md) |
| `/story` | Brand narrative arc, origin story | [commands/story.md](commands/story.md) |
| `/design-system` | Design tokens / CMF spec, color, type, components | [commands/design-system.md](commands/design-system.md) |
| `/identity` | Logo + brand book + asset library, governed as one system | [commands/identity.md](commands/identity.md) |
| `/community` | Community structure, engagement cadence, social calendar | [commands/community.md](commands/community.md) |
| `/website` | Website as a synthesis of UI system, tokens, and copy | [commands/website.md](commands/website.md) |
| `/copy` | Landing page, email, in-product, and ad copy | [commands/copy.md](commands/copy.md) |
| `/voice` | Voice attributes, tone-by-channel, banned phrases | [commands/voice.md](commands/voice.md) |
| `/colors` | Color palette with psychological and competitive rationale | [commands/colors.md](commands/colors.md) |
| `/social-assets` | Sized, on-voice social and campaign asset sets | [commands/social-assets.md](commands/social-assets.md) |

---

## Choosing Between a Command and Plain English

Commands are a shortcut, not a requirement — the Meta-Agent can route a plain-English request on its own (see [`meta-agent/META_AGENT.md`](meta-agent/META_AGENT.md)). Use a command when you already know which Agent or Workflow you want; use plain English (or `/startup`) when you don't and want the Meta-Agent to decide.

## Composing Commands

Commands compose the same way Agents do. A realistic sequence: `/prd` → `/architecture` → `/finance` → `/critic` → `/planner`. Each command's "Workflows" section tells you which named Workflow in [`workflows/`](workflows) it corresponds to, so you can also just run the Workflow directly if you'd rather see the whole chain at once.

Brand commands compose into the same chains, not a separate track — a typical new-product sequence is `/prd` → `/naming` → `/identity` → `/design-system` → `/architecture` → `/critic` → `/planner`, with naming and identity attaching to the product before CTO-Agent or CIO-Agent build it. For a fundraising pass: `/finance` → `/story` → `/fundraising` → `/critic`, where `/story` supplies the narrative arc the deck is built around.

`/solve` composes differently — it usually runs *before* an artifact command, not after, since it's how you decide whether and what to build in the first place: `/solve` (should we do this, and how) → `/prd` or `/architecture` or `/finance` (build the artifact the decision called for) → `/critic` → `/planner`. It can also run standalone for a decision that never needs a downstream artifact at all.
