# Knowledge Graph

## Purpose
The master map of how everything in FoundryOS connects — Modules, Skills, Agents, Workflows, Artifacts, Memory, Brand Intelligence, and the advanced-layer Agents that learn from and critique the system's own output. The five companion graphs (`ARTIFACT_GRAPH.md`, `AGENT_GRAPH.md`, `SKILL_GRAPH.md`, `WORKFLOW_GRAPH.md`, `BRAND_GRAPH.md`) are zoomed-in views of one layer each; this file is the zoomed-out view that shows how those layers stack.

## Nodes
- **Module** — the atomic unit of domain knowledge (179 total, numbered `00`–`177` with one legacy duplicate at `99`)
- **Skill** — a grouped capability built from Modules (59 total, 17 of which are brand-specific, 1 of which — `59-problem-solving-decision-modeling-skill` — is a cross-cutting reasoning layer rather than a domain)
- **Agent** — a role that owns a fixed set of Skills (10 total, plus Meta-Agent — CBO-Agent is the brand domain owner)
- **Workflow** — a named, repeatable sequence of Agents solving one class of request (11 total; CBO-Agent sits in the original 10, by default in 9 and conditionally in `09-hiring-workflow`; `11-problem-solving-decision-workflow` runs the reasoning layer standalone)
- **Artifact** — a concrete output (PRD, Architecture, BOM, Financial Model, Brand Strategy Brief, Logo System, Design System, etc.)
- **Memory** — persistent context consumed and updated by Agents over time (13 files: 7 cross-domain, 6 brand-specific)
- **Reflection Agent / Critic Agent / Planner Agent** — the advanced-layer agents that operate *on* past outputs rather than producing new domain content, including brand outputs

## Relationships
- A **Module** is grouped into exactly one **Skill**
- A **Skill** is owned by one **Agent** (or two, in the single deliberate case of `35-npi-manufacturing-skill`)
- An **Agent** is selected into a **Workflow** by the Meta-Agent, in a defined execution order
- A **Workflow** run produces one or more **Artifacts**
- An **Artifact** updates relevant **Memory** files
- **Memory** is read by **Reflection Agent** to produce lessons, by **Critic Agent** to stress-test new outputs, and by **Planner Agent** to sequence execution realistically
- **Brand** is not a separate branch off this graph — CBO-Agent's Skills, Memory files, and Artifacts are woven into the same Module → Skill → Agent → Workflow → Artifact → Memory chain as every other domain. See `BRAND_GRAPH.md` for the brand-specific zoom-in.

## Dependencies
- Nothing above Module level is reachable without the Modules underneath it — the graph is strictly bottom-up in construction, top-down in execution
- Workflows depend on the Meta-Agent's live read of each Agent's current Skill list (see `meta-agent/META_AGENT.md`'s "Source of Truth") — this graph is a snapshot, not the authority
- The advanced layer (Reflection/Critic/Planner) depends on Memory being kept current; if Memory goes stale, the advanced layer degrades to producing generic advice instead of grounded learning

## Graph Structure
```
Module
  ↓ (grouped into)
Skill
  ↓ (owned by)
Agent
  ↓ (selected into, by Meta-Agent)
Workflow
  ↓ (executed, produces)
Artifact
  ↓ (recorded into)
Memory
  ↓ (read by)
Reflection Agent  →  Lessons Learned
Critic Agent      →  Stress-Tested Plan
Planner Agent     →  Executable Roadmap
  ↓ (all three feed back into)
Improved Output  (the next Workflow run starts smarter than the last)
```

## Examples
```
21-ai-product-skill (Skill)
  → owned by CTO-Agent
  → selected into 04-ai-product-workflow
  → produces "AI Architecture" + "Evaluation Metrics" (Artifacts)
  → recorded into memory/technical-memory.md and memory/product-memory.md
  → read by reflection-agent/ after launch outcome is known
  → "evaluation metric was a proxy, not the real goal" becomes a lesson
  → next 04-ai-product-workflow run starts with that lesson already in memory/lessons-learned.md
```
See `ARTIFACT_GRAPH.md`, `AGENT_GRAPH.md`, `SKILL_GRAPH.md`, `WORKFLOW_GRAPH.md`, and `BRAND_GRAPH.md` for the detailed view of each layer in this chain.
