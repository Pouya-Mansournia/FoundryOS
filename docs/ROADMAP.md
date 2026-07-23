# Roadmap

This is the big-picture version of where FoundryOS has been and where it's headed. For the detailed, file-by-file history, see [`CHANGELOG.md`](../CHANGELOG.md); for current counts, see [`VERSION.md`](../VERSION.md); for the versioning policy behind these numbers (and why the public release is v4.0.0, not v1.0.0), see [`VERSIONING.md`](../VERSIONING.md).

## v1 — The Core System (shipped)

Modules → Skills → Agents → Meta-Agent. The foundational bet: that founder/operator knowledge compresses well into small, composable units, and that a Meta-Agent reading live ownership files can route any request without a human manually picking specialists. 121 Modules, 41 Skills, 9 Agents, 1 Meta-Agent.

## v2 — Workflows & the Advanced Layer (shipped)

Two additions on top of the core: named, reusable **Workflows** for the most common request shapes (10 of them), and an **Advanced Layer** — Memory, Reflection Agent, Critic Agent, Planner Agent, Knowledge Graph — that lets the system accumulate context and self-critique across runs instead of starting fresh every time. See [`ADVANCED_LAYER.md`](../ADVANCED_LAYER.md).

## v3 — Commands & Onboarding (shipped)

A **Command Layer** (`commands/`, 26 slash commands) that exposes every Agent, Workflow, and Advanced-Layer component as a short, memorable trigger — and a full beginner-onboarding doc set (`INSTALL.md`, environment-specific setup guides, `FAQ.md`, `GETTING_STARTED.md`, `TUTORIALS.md`) so someone with zero prior context can go from a ZIP download to a working session in minutes, in Claude, ChatGPT, Cursor, or Windsurf.

## v4 — FoundryOS Rebrand & Brand Operating System (shipped)

Two changes that shipped together deliberately, not as two separate releases: the rename from the prior working title to **FoundryOS** (tagline: "Build Anything. Think Like a Team."), and a full **Brand Operating System** integrated into every existing layer rather than appended as an isolated feature.

- **Rebrand & restructure** — new identity, `docs/`/`assets/` restructure, and an architecture-diagram fix (the system's own diagram now ends at Artifacts, not Commands, since Artifacts are what you actually walk away with).
- **CBO-Agent** — a 10th domain Agent (Chief Brand Officer), running by default in 9 of the 10 Workflows (conditional in `09-hiring-workflow`), sitting directly after CPO-Agent so identity attaches to a product before it's built or sold.
- **17 new brand Skills** (`42-brand-strategy-skill` through `58-brand-roadmap-skill`) — strategy, naming, positioning, brand book, logo system, design system, content, voice/tone, color psychology, typography, UI system, community, social assets, storytelling, copywriting, asset management, and roadmap sequencing.
- **6 new Memory files** (`brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`) plus cross-references added to every existing Memory file with a natural brand connection point.
- **`BRAND_GRAPH.md`** — a 6th Knowledge Graph file mapping how the 17 brand Skills, CBO-Agent, the 6 brand Memory files, and the brand-specific Artifacts interconnect.
- **13 new Commands** (`/brand`, `/logo`, `/naming`, `/tagline`, `/story`, `/design-system`, `/identity`, `/community`, `/website`, `/copy`, `/voice`, `/colors`, `/social-assets`), bringing the total from 26 to 39.
- Reflection, Critic, and Planner agents extended to evaluate brand consistency, challenge naming/positioning/visual-identity decisions, and sequence brand rollouts alongside product and company roadmaps.

Counts after v4: 175 Modules, 58 Skills, 10 Agents, 13 Memory files, 6 Knowledge Graphs, 39 Commands. See [`VERSION.md`](../VERSION.md) for the full table and [`brand/BRAND_OS.md`](../brand/BRAND_OS.md) for the Brand OS charter.

## v4.1 — Problem Solving & Decision Modeling (shipped)

A reusable **reasoning and decision layer** — explicitly not another PRD template. Adds the discipline of framing an ambiguous problem, modeling the current state and its causal chain before proposing a fix, building a metric tree, engineering falsifiable hypotheses, comparing solution options, and selecting the right reusable quantitative formula for the decision at hand.

- **`59-problem-solving-decision-modeling-skill`** — a cross-cutting reasoning engine owned by CEO-Agent that combines with whichever domain Agent(s) a decision touches, rather than replacing them (a robotics decision runs it alongside CIO-Agent, a pricing decision alongside CFO-Agent and CRO-Agent).
- **A 29-formula reusable quantitative library** (`skills/59-problem-solving-decision-modeling-skill/FORMULA_LIBRARY.md`) — unit economics, funnels, capacity, reliability, quality/yield, experimentation, prioritization (RICE/ICE/WSJF), TCO, and more, each domain-neutral with stated assumptions and misuse warnings.
- **`11-problem-solving-decision-workflow`** — the reasoning layer the other 10 Workflows call into at their own decision/prioritization/validation gates, and which can also run standalone for a decision that isn't shaped like any of the other 10 request types.
- **The `/solve` command** — frames the problem and produces a decision packet, never defaulting to a PRD or other fixed artifact.
- Critic Agent, Planner Agent, and Reflection Agent extended to check formula misuse and causal claims, sequence a decision's staged rollout, and backfill a Decision Record's actual outcome once known.

Counts after v4.1: 179 Modules, 59 Skills, 10 Agents, 11 Workflows, 13 Memory files, 6 Knowledge Graphs, 40 Commands. See [`VERSION.md`](../VERSION.md) for the full table.

## v5.0.0-preview.1 — MCP Declaration Layer (shipped)

A **pre-release tag** toward the v5.0.0 major, not the complete major itself — see [`VERSIONING.md`](../VERSIONING.md) §11 for the new `vX.0.0-preview.N` convention this release introduces. Ships the first of the three capabilities originally scoped under v5.0.0 below.

- **`mcp-layer/MCP_LAYER.md`** — a declaration contract: a Skill can name a specific real-world data or action need (`## MCP Tool Request`: Need / Category / If-unavailable) instead of guessing silently. No FoundryOS-shipped runtime or execution — the request is fulfilled by whichever MCP-capable assistant is running the session, or falls back to the Meta-Agent's existing Missing Inputs/Assumptions handling.
- **`knowledge-graph/MCP_GRAPH.md`** — a 7th Knowledge Graph file, mapping requests back to their triggering Command and forward to the Artifact they improve.
- **The `/mcp` command** — drafts or reviews a request for a given step; command total 40 → 41.

Counts after v5.0.0-preview.1: 179 Modules, 59 Skills, 10 Agents, 11 Workflows, 13 Memory files, 7 Knowledge Graphs, 1 MCP Layer (declaration only), 41 Commands. See [`VERSION.md`](../VERSION.md) for the full table.

## v5.0.0 — Runtime & Execution Engine (planned)

The next major version, not an incremental one — it adds an actual execution layer underneath the knowledge system, rather than extending an existing one. See [`VERSIONING.md`](../VERSIONING.md) for why this is a MAJOR rather than a MINOR. The MCP-declaration piece originally scoped here shipped early as v5.0.0-preview.1 above; what's left before the plain `v5.0.0` tag is cut:

- **Runtime layer** — state held across the steps of a Workflow, instead of every step starting from a fresh prompt with no memory of where it is in the sequence.
- **Execution engine** — runs a Workflow's steps in order, checks each against Validation and the Critic Agent, calls the real MCP tools a Skill declared via `mcp-layer/MCP_LAYER.md` instead of relying on a human's host assistant to do it ad hoc, and advances automatically.
- **Autonomous workflows** — multi-step workflows that span sessions without a human re-prompting between every step (e.g. "take this PRD all the way through stage-gate sign-off" run unattended), and closed-loop execution where an Agent's output automatically triggers the next Agent once it passes Validation and the Critic Agent.
- Tighter integration between `25-prompt-loop-skill` and the Reflection/Critic/Planner agents so the recursive improvement loop runs without a manual trigger each time.

## Future Vision

The long-run goal is a system where running the same kind of decision twice is visibly cheaper and better the second time — not because a human remembered to check old notes, but because Memory, Reflection, and the Knowledge Graph make that continuity structural. The core system should stay legible enough that anyone can open any file and understand exactly why the system did what it did; growth in capability should come from adding well-scoped layers (the way Workflows, the Advanced Layer, and Commands were each added on top of a stable core), not from making any single layer harder to reason about.

## How to influence this roadmap

Open an issue describing the gap you've hit, or propose a change directly — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
