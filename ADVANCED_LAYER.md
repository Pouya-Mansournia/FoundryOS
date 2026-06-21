# Advanced Layer

The Advanced Layer sits on top of the core FoundryOS (`modules/ → skills/ → agents/ → meta-agent/`) and the `workflows/` layer above it. Where the core system answers a request once, the Advanced Layer is what makes the system get better at answering similar requests the next time — it adds memory, self-critique, planning, and an explicit map of how everything connects.

It is entirely optional at runtime: every workflow in `workflows/` works without it. What it adds is continuity across runs and a second, adversarial pass before a plan ships.

## The Five Layers

### 1. Memory (`memory/`)
Long-term, persistent context across thirteen files. Company, market, customer, product, and technical history: `company-memory.md`, `market-memory.md`, `customer-memory.md`, `product-memory.md`, `technical-memory.md`. Cross-cutting decision and pattern tracking: `decision-log.md`, `lessons-learned.md`. Brand and identity state, owned primarily by CBO-Agent: `brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`. Every Agent reads relevant Memory before acting and (per each file's Update Rules) writes back to it when something material changes. Without Memory, every workflow run starts from zero; with it, the system accumulates institutional knowledge the way a real team does — including what the brand has said and looked like, not just what the product does.

### 2. Reflection Agent (`reflection-agent/`)
Runs after an outcome is known — a launch shipped and its metrics came in, a hire passed the 90-day mark, a name or positioning statement has had time to land with a real audience. Compares what was expected against what happened, and distills the gap into a general lesson written into `memory/lessons-learned.md` (or the relevant brand memory file, if the gap is about naming, voice, or identity rather than product or engineering). This is the layer that turns "we got this wrong once" into "we won't get this wrong again."

### 3. Critic Agent (`critic-agent/`)
Runs immediately after a Meta-Agent Result, before it's treated as final. An adversarial second pass: finds contradictions, hidden risks, hallucinated claims, and missing dependencies the original output didn't surface — including brand inconsistencies, like a naming claim or tone that quietly contradicts `memory/brand-memory.md` or `memory/voice-memory.md`. Checks new plans against `memory/lessons-learned.md` by name, so a known failure pattern gets caught before it repeats, not after.

### 4. Planner Agent (`planner-agent/`)
Runs after a plan exists and (ideally) after the Critic Agent has closed major gaps. Turns a Combined Executive Answer into an actual executable plan: task decomposition, dependency mapping, milestones, resourcing, and a stated critical path — including where in that path a brand decision (naming clearance, CMF sign-off, positioning approval) has to lock before everything downstream of it can proceed. The difference between "here's what should happen" and "here's the dated roadmap a team can run against."

### 5. Knowledge Graph (`knowledge-graph/`)
Not an agent — a map. `KNOWLEDGE_GRAPH.md` is the system-wide view; `ARTIFACT_GRAPH.md`, `AGENT_GRAPH.md`, `SKILL_GRAPH.md`, and `WORKFLOW_GRAPH.md` zoom into one layer each. Use it to answer "what does this depend on" and "what does this affect downstream" before changing anything, including before extending the system itself.

## How They Interact

```
        Modules
           ↓
         Skills
           ↓
         Agents
           ↓
       Meta-Agent
           ↓
       Workflows
           ↓
         Memory  ←──────────────────────────┐
           ↓                                 │
    Planner Agent                            │
           ↓                                 │
   Reflection Agent  ───────────────────────→│  (writes lessons back into Memory)
           ↓                                 │
     Critic Agent  ─────────────────────────→│  (checks against Memory before sign-off)
           ↓                                 │
    Knowledge Graph  (maps every edge above)
           ↓
     Improved System
```

In practice, the loop on a single request runs: **Meta-Agent produces a Result → Critic Agent stress-tests it against Memory → Planner Agent turns the approved plan into a roadmap → the plan executes → once an outcome is known, Reflection Agent writes a lesson back into Memory → the next Meta-Agent run on a similar request starts smarter.** The Knowledge Graph isn't part of this per-request loop — it's the reference map for understanding or extending the loop itself.

## Why This Layer Exists

The core system (Modules → Skills → Agents → Meta-Agent) is excellent at producing one good answer to one request. Without Memory, it has no way to know whether that answer turned out to be right, and without Reflection/Critic/Planner, it has no mechanism to improve or to catch its own mistakes before they ship. The Advanced Layer is what turns a stateless expert system into one that compounds — every run leaves the system slightly better equipped for the next one, which is the same property that makes an experienced team outperform a brand-new one solving the identical problem.

## Versioning Note
This layer corresponds to the v2 roadmap item described in [`VERSION.md`](VERSION.md) ("Memory layer, Reflection Agent, Critic Agent"). `planner-agent/` and `knowledge-graph/` extend beyond what v2 originally scoped — see [`CHANGELOG.md`](CHANGELOG.md) for when each was added.
