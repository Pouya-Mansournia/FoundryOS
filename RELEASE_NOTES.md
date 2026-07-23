# Release Notes

Canonical, publish-ready release notes — paste the relevant section directly into a GitHub Release when tagging. `CHANGELOG.md` is the detailed, file-by-file engineering record; this is the human-facing summary. See `AUDIT_REPORT.md` for the full audit this release notes section is drawn from.

---

## v5.0.0-preview.1 — MCP Declaration Layer

**Tag:** `v5.0.0-preview.1`

**This is a pre-release, not the full v5.0.0.** It ships the first of three capabilities originally scoped under the planned v5.0.0 major — a declarative **MCP Layer** letting a Skill name a specific real-world data or action need instead of guessing silently. A Runtime and an Execution Engine (the pieces that would make this autonomous) remain unshipped; the plain `v5.0.0` tag isn't cut until they land too. See `VERSIONING.md` §11 for the new pre-release tag convention this release introduces.

### What's new

- **`mcp-layer/MCP_LAYER.md`** — the declaration contract: any Skill can append an `## MCP Tool Request` (Need / Category / If-unavailable) instead of silently guessing at a live fact. FoundryOS itself still holds no state and executes nothing — whichever MCP-capable assistant is running the session (Claude Code, Cowork, or any other MCP client) fulfills the request, or the Meta-Agent's existing Missing Inputs/Assumptions handling absorbs the gap.
- **`knowledge-graph/MCP_GRAPH.md`**, a 7th Knowledge Graph file, mapping how a request connects the triggering Command to the Artifact it improves.
- **The `/mcp` command**, bringing the command total from 40 to 41.
- No new Runtime, no new Execution Engine, no new autonomous behavior — this release is documentation and a declaration format only, keeping FoundryOS's "zero install, it's markdown" claim true.

### Final counts

179 Modules · 59 Skills · 10 Agents · 1 Meta-Agent · 11 Workflows · 13 Memory files · 3 Advanced-Layer Agents · 7 Knowledge Graphs · 1 MCP Layer (declaration only) · 41 Commands (+ 41 generated Claude Code slash commands) · 9 Examples · 10 Test specs · 11 Onboarding docs.

### Upgrading

Nothing to migrate — purely additive and documentation-only. If you'd generated `.claude/commands/` locally before this release, re-run `python3 scripts/generate_claude_commands.py` to pick up `/mcp`. No Skill is required to emit an MCP Tool Request; existing runs behave exactly as before unless a Skill's output would genuinely benefit from a live external fact.

### What's still ahead

The plain `v5.0.0` tag ships once a Runtime (state held across Workflow steps) and an Execution Engine (steps that run in order, unattended) land on top of this declaration layer — see `docs/ROADMAP.md` and `VERSION.md`'s Roadmap section.

---

## v4.1.0 — Problem Solving & Decision Modeling

**Tag:** `v4.1.0`

Adds a reusable **reasoning and decision layer** — deliberately not another PRD template — that frames ambiguous problems, builds causal and metric models, engineers falsifiable hypotheses, compares solution options, and selects reusable quantitative formulas for an evidence-based decision.

### What's new

- **`59-problem-solving-decision-modeling-skill`** (CEO-Agent), a cross-cutting reasoning engine that combines with whichever domain Agent(s) a decision touches instead of replacing them.
- A **29-formula reusable quantitative library** (`FORMULA_LIBRARY.md`) — unit economics, funnels, capacity, reliability, quality/yield, experimentation, prioritization (RICE/ICE/WSJF), TCO, and more.
- **`11-problem-solving-decision-workflow`** and the **`/solve` command**, bringing the command total from 39 to 40.
- Critic, Planner, and Reflection agents extended to check formula misuse and causal claims, sequence staged rollouts, and backfill decision outcomes.
- A new worked example, `examples/decision-modeling-example.md` (AI infrastructure, SaaS pricing, and manufacturing-automation decisions).

### Final counts

179 Modules · 59 Skills · 10 Agents · 1 Meta-Agent · 11 Workflows · 13 Memory files · 3 Advanced-Layer Agents · 6 Knowledge Graphs · 40 Commands (+ 40 generated Claude Code slash commands) · 9 Examples · 10 Test specs · 11 Onboarding docs.

### Upgrading

Nothing to migrate. If you'd generated `.claude/commands/` locally before this release, re-run `python3 scripts/generate_claude_commands.py` to pick up `/solve`.

---

## v4.0.0 — Rebrand & Brand Operating System

**Tag:** `v4.0.0`

This release does two things at once: renames the project to **FoundryOS** ("Build Anything. Think Like a Team.") and ships a full **Brand Operating System** woven into every existing layer rather than bolted on.

### What's new

- A 10th domain Agent, **CBO-Agent** (Chief Brand Officer), running by default in 9 of 10 Workflows.
- **17 new Skills** covering brand strategy, naming, positioning, brand book, logo system, design system, content, voice/tone, color, typography, UI system, community, social assets, storytelling, copywriting, asset management, and roadmap sequencing.
- **6 new Memory files**, a **6th Knowledge Graph** (`BRAND_GRAPH.md`), and **13 new slash commands** (`/brand`, `/logo`, `/naming`, `/tagline`, `/story`, `/design-system`, `/identity`, `/community`, `/website`, `/copy`, `/voice`, `/colors`, `/social-assets`).
- Reflection, Critic, and Planner agents extended to evaluate brand consistency and sequence brand rollouts.
- A new worked example, `examples/team-scaling-example.md` (CEO → COO → CHRO → CBO → CFO), closing CHRO-Agent's previous example-coverage gap.
- Brand examples and onboarding touches added throughout every doc, plus new Logo Prompt and Hero Image asset specs in `docs/SHOWCASE.md`.
- Full open-source readiness pass: `.gitignore`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.github/ISSUE_TEMPLATE/`, `.github/PULL_REQUEST_TEMPLATE.md`, and README badges.

### Fixed in this release

- Corrected a repo-wide module-count error (documented as 172, actually 175) across 9 files.
- Removed a phantom top-level `modules/` folder reference from README's folder tree.
- Closed CHRO-Agent's example-coverage gap by adding `examples/team-scaling-example.md`.
- Verified, repo-wide: every Skill's Source Modules against the filesystem (58/58 clean), all internal markdown links (221 checked, 0 broken), every Agent/Skill slug referenced in `workflows/` and `tests/` (0 phantom references), and `commands/` ↔ `.claude/commands/` filename parity (39 = 39).

### Known issue carried forward (not blocking)

One pre-existing module-numbering collision at `99` — two files both use module number `99` (`skills/14-validation-skill/99_Master_Validator_OS.md` and `skills/40-meta-orchestration-skill/99_Universal_Founder_OS.md`). Dormant: nothing currently indexes modules by number, only by filename. See `AUDIT_REPORT.md` Items 1–2 for the full writeup and recommended fix.

### Final counts

175 Modules · 58 Skills · 10 Agents · 1 Meta-Agent · 10 Workflows · 13 Memory files · 3 Advanced-Layer Agents · 6 Knowledge Graphs · 39 Commands (+ 39 generated Claude Code slash commands) · 8 Examples · 9 Test specs · 11 Onboarding docs.

### Upgrading

Nothing to migrate — this is a markdown knowledge system with no runtime state. Re-download or re-pull the repo and re-point your assistant at it per `INSTALL.md`. If you'd generated `.claude/commands/` locally before this release, re-run `python3 scripts/generate_claude_commands.py` to pick up the 13 new brand commands.

---

## v3.0 — Commands & Onboarding

Added 26 slash commands (`commands/`), root `COMMANDS.md`, and the full beginner-onboarding doc set (`INSTALL.md`, four environment setup guides, `FAQ.md`, `GETTING_STARTED.md`, `EXAMPLES.md`, `TUTORIALS.md`, `ROADMAP.md`, `CONTRIBUTING.md`). Rewrote `README.md` and `QUICKSTART.md` to lead with slash commands. Added `SHOWCASE.md` as a GitHub presentation kit. See `CHANGELOG.md` for the full file-level detail.

## v2.0 — Advanced Layer

Added `workflows/` (10 sequences), `memory/` (7 persistent context files), `reflection-agent/`, `critic-agent/`, `planner-agent/`, and `knowledge-graph/` (5 dependency maps), plus `ADVANCED_LAYER.md` explaining how they interact. See `CHANGELOG.md` for the full file-level detail.

## v1.0 — Meta-Agent

Added `meta-agent/META_AGENT.md`, the central orchestrator that classifies requests, selects Agents and Skills, sequences execution, and merges output into one executive answer. Added the full v1 documentation layer (`README.md`, `QUICKSTART.md`, `VERSION.md`, `LICENSE`, both registries, 5 worked examples). See `CHANGELOG.md` for the full file-level detail.

## Pre-1.0 (v0.1 – v0.9)

Foundational buildout: 121 atomic Modules → 40 Skills → 9 C-suite Agents → the CIO-Agent hardware consolidation. See `CHANGELOG.md` for the full file-level detail of each milestone.
