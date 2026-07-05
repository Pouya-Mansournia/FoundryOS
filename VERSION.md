# Version

## Current: v4.1

| Layer | Count |
|---|---|
| Modules | 179 (numbered `00`–`177`; one legacy duplicate at `99`, see `AUDIT_REPORT.md`) |
| Skills | 59 (17 of which, `42`-`58`, are CBO-Agent's brand domain; 1, `59-problem-solving-decision-modeling-skill`, is a cross-cutting reasoning layer) |
| Agents | 10 (incl. CBO-Agent) |
| Meta-Agents | 1 |
| Workflows | 11 (10 product/company-shaped + `11-problem-solving-decision-workflow`) |
| Memory Files | 13 (7 cross-domain + 6 brand) |
| Advanced-Layer Agents | 3 (Reflection, Critic, Planner) |
| Knowledge Graphs | 6 (5 original + `BRAND_GRAPH.md`) |
| Commands | 40 (26 original + 13 brand + `/solve`) |
| Onboarding Docs | 11 (`INSTALL.md` through `CONTRIBUTING.md`) |
| Brand Charter | 1 (`brand/BRAND_OS.md`) |

v1.0 was the first complete pass through the core four layers: every Module compiled into a Skill, every Skill owned by at least one Agent, and the Meta-Agent able to route any request across the full set without a human manually picking Agents. v2.0 added the **Workflows layer** (`workflows/`) and the **Advanced Layer** (`memory/`, `reflection-agent/`, `critic-agent/`, `planner-agent/`, `knowledge-graph/`) described in full in [`ADVANCED_LAYER.md`](ADVANCED_LAYER.md). v3.0 added the **Command Layer** (`commands/`, 26 slash commands, see [`COMMANDS.md`](COMMANDS.md)) and a full beginner-onboarding doc set so a complete beginner can get from a ZIP download to a working session in any of four supported environments. v4.0 is two changes shipped together — the rename to **FoundryOS** and a full **Brand Operating System** (CBO-Agent, 17 brand Skills, 6 brand Memory files, `BRAND_GRAPH.md`, 13 brand Commands) integrated into every existing layer rather than appended on top. v4.1 added a **Problem Solving and Decision Modeling** reasoning layer — a reusable engine for framing ambiguous problems, building causal/metric models, and selecting quantitative formulas, rather than another PRD template. See [`CHANGELOG.md`](CHANGELOG.md) for how it got here.

---

## Roadmap

### v2.0 — Workflows, Memory & Self-Critique (shipped)

- **Workflows layer** — 10 reusable, named sequences (`01-new-product-workflow` through `10-strategic-planning-workflow`) so common request shapes don't have to be re-derived by the Meta-Agent from scratch each time.
- **Memory layer** — 7 persistent files (`company-memory.md` through `lessons-learned.md`) that persist prior decisions, assumptions, and outcomes across sessions, so the system doesn't re-ask questions it's already been answered or re-litigate assumptions a founder already corrected.
- **Reflection Agent** — reviews completed outputs after the fact: did the assumptions hold up, what should change next time. Writes lessons into `memory/lessons-learned.md`.
- **Critic Agent** — an adversarial pass that stress-tests the Combined Executive Answer before it's returned, hunting for unstated assumptions, hidden risks, hallucinated claims, and missing dependencies.
- **Planner Agent** — turns an approved plan into a sequenced, resourced, dated roadmap with an explicit critical path (beyond original v2 scope, added because Memory + Critic without an execution layer left a gap between "approved plan" and "what a team actually runs against").
- **Knowledge Graph** — 5 files mapping how Modules, Skills, Agents, Workflows, and Artifacts relate (also beyond original scope, added as the reference map needed once 6 new top-level layers existed).

### v3.0 — Commands & Onboarding (shipped)

- **Command Layer** — 26 slash commands (`commands/`) exposing every Agent, Workflow, and Advanced-Layer component as a short, memorable trigger, plus a root `COMMANDS.md` index.
- **Onboarding doc set** — `INSTALL.md`, per-environment setup guides (`CLAUDE_SETUP.md`, `CHATGPT_SETUP.md`, `CURSOR_SETUP.md`, `WINDSURF_SETUP.md`), `FAQ.md`, `GETTING_STARTED.md`, `EXAMPLES.md`, `TUTORIALS.md`, `ROADMAP.md`, `CONTRIBUTING.md` — so a complete beginner can go from a ZIP download to a working session without prior context.
- `README.md` and `QUICKSTART.md` rewritten to lead with the Command Layer while keeping plain-English Meta-Agent routing as the no-syntax alternative.

### v4.0 — FoundryOS Rebrand & Brand Operating System (shipped)

- **Rebrand & restructure** — renamed to **FoundryOS** (tagline: "Build Anything. Think Like a Team."; subtitle: "Open Source Agentic Operating System"), with `docs/` and `assets/` folders created and every secondary doc moved into `docs/` with relative links fixed.
- **`brand/BRAND_OS.md`** — the Brand OS charter, the root document everything below traces back to.
- **CBO-Agent** — a 10th domain Agent (Chief Brand Officer), running by default in 9 of the 10 Workflows (conditional in `09-hiring-workflow`), seated directly after CPO-Agent so identity attaches to a product before it's built or sold.
- **17 new brand Skills** (`42-brand-strategy-skill` through `58-brand-roadmap-skill`) — strategy, naming, positioning, brand book, logo system, design system, content, voice/tone, color psychology, typography, UI system, community, social assets, storytelling, copywriting, asset management, roadmap sequencing.
- **6 new Memory files** (`brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`) plus cross-references added to every existing Memory file with a natural brand connection point.
- **`BRAND_GRAPH.md`** — a 6th Knowledge Graph file; `SKILL_GRAPH.md` also corrected (a drafting-stage slug error had `46-logo-design-skill` instead of `46-logo-system-skill` in two places).
- **13 new Commands** (`/brand`, `/logo`, `/naming`, `/tagline`, `/story`, `/design-system`, `/identity`, `/community`, `/website`, `/copy`, `/voice`, `/colors`, `/social-assets`), bringing the total from 26 to 39.
- Reflection, Critic, and Planner agents extended to evaluate brand consistency, challenge naming/positioning/visual-identity decisions, and sequence brand rollouts alongside product and company roadmaps.
- Brand examples and onboarding touches woven into `README.md`, `QUICKSTART.md`, `GETTING_STARTED.md`, `FAQ.md`, `CONTRIBUTING.md`, every `docs/*_SETUP.md` guide, and `docs/SHOWCASE.md`'s asset kit (new Logo Prompt and Hero Image sections, a Brand Intelligence node added to the architecture diagram, a 4th screenshot example).

### v4.1 — Problem Solving & Decision Modeling (shipped)

- **`59-problem-solving-decision-modeling-skill`** (CEO-Agent) — a reusable reasoning engine, not a document template: frames an ambiguous problem, builds a current-state and causal model before any solution is proposed, decomposes the problem, translates goals into a metric tree, engineers falsifiable hypotheses, generates and compares solution options, and selects the right reusable quantitative formula for the decision.
- **`skills/59-problem-solving-decision-modeling-skill/FORMULA_LIBRARY.md`** — 29 domain-neutral, reusable formula families (unit economics, funnels, capacity, reliability, experimentation, prioritization, TCO, and more), each with equation, variables, units, assumptions, valid/invalid use, and common mistakes.
- **`11-problem-solving-decision-workflow`** and the **`/solve` command** — the reasoning layer the other 10 Workflows call into at their own decision, prioritization, and validation gates (all 10 `workflows/*/WORKFLOW.md` files updated), and can also run standalone.
- Critic Agent, Planner Agent, and Reflection Agent extended to check formula misuse and causal claims, sequence a decision's staged rollout, and backfill a Decision Record's actual outcome — `memory/decision-log.md` extended with the full Decision Record structure this Skill produces.

### v5.0.0 — Runtime, MCP, Tool Integration & Execution Engine (planned)

This is the next MAJOR, not an incremental one — it changes what FoundryOS *is*, from a knowledge system read by a human or assistant to one with an actual execution layer underneath it. See [`VERSIONING.md`](VERSIONING.md) §9 for why this clears the bar for a major version rather than a minor one.

- **Runtime layer** — a way to hold state across steps of a Workflow instead of every step starting from a fresh prompt with no memory of where it is in the sequence.
- **MCP / tool integration** — Agents that can call real tools (not just produce text describing what a tool should do), the way this very session's Cowork environment already does for file and shell access.
- **Execution engine** — the mechanism that actually runs a Workflow's steps in order, checks them against Validation and the Critic Agent, and advances to the next step without a human re-prompting in between.
- **Autonomous workflows** — multi-step workflows that span sessions unattended (e.g. "take this PRD all the way through stage-gate sign-off"), and closed-loop execution where an Agent's output automatically triggers the next Agent once it passes Validation and the Critic Agent.
- Tighter integration between `25-prompt-loop-skill` and the Reflection/Critic/Planner agents so the recursive improvement loop runs unattended instead of requiring a manual trigger each time.

---

## Versioning Note

Skill-to-Agent ownership is expected to keep shifting as the system is used (it already has, twice, before v1.0 shipped). That's by design — Agents are deliberately thin so re-ownership is a metadata change, not a rewrite. Version numbers track structural milestones (a new layer, a new capability class), not every ownership reshuffle.

For the full policy this summary is drawn from — what counts as major/minor/patch, why v4.0.0 is the first public release and not v1.0.0, release naming, tagging, deprecation, and compatibility rules — see [`VERSIONING.md`](VERSIONING.md).
