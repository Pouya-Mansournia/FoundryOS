# Agent Graph

## Purpose
Maps how the 10 domain Agents, the Meta-Agent, and the 3 advanced-layer Agents (Reflection, Critic, Planner) depend on and feed each other — the relationships `registry/AGENT_REGISTRY.md` states in prose, shown here as a graph.

## Nodes
CEO-Agent, CPO-Agent, CTO-Agent, CIO-Agent, COO-Agent, CFO-Agent, CRO-Agent, CMO-Agent, CBO-Agent, CHRO-Agent, Meta-Agent, Reflection-Agent, Critic-Agent, Planner-Agent — 14 nodes total.

## Relationships
- **Meta-Agent** sits above all 10 domain Agents — it selects, sequences, and merges, but owns no Skills itself
- The 10 domain Agents form a dependency chain in the default Execution Order (see Graph Structure below), though not every Agent runs on every request
- **CIO-Agent ↔ COO-Agent** share a direct edge through `35-npi-manufacturing-skill` — the one deliberate cross-agent overlap in the system
- **CBO-Agent** sits directly after CPO-Agent in the default order — it attaches name, voice, and visual identity to what CPO-Agent just defined, before CTO-Agent/CIO-Agent build it or CRO-Agent/CMO-Agent sell it. It is in the default execution set for 9 of the 10 workflows; only `09-hiring-workflow` treats it as conditional, by design
- **Reflection-Agent, Critic-Agent, Planner-Agent** sit downstream of every domain Agent and the Meta-Agent — they consume outputs, they don't produce domain work themselves, and that now includes brand outputs (naming, positioning, voice, visual identity)

## Dependencies
| Agent | Upstream (consumes from) | Downstream (feeds) |
|---|---|---|
| CEO-Agent | None — runs first | CPO, CBO (identity ratification), CFO (board/investor narrative), all agents (strategic framing; also feeds every agent `59-problem-solving-decision-modeling-skill` whenever the request in their domain is decision-shaped) |
| CPO-Agent | CEO-Agent | CBO-Agent (what to name/position), CTO/CIO (what to build), CRO/CMO (positioning), CFO (pricing inputs) |
| CBO-Agent | CPO-Agent (product intent), CEO-Agent (strategic framing) | CTO/CIO (design tokens/CMF to build against), CRO/CMO/CHRO (voice and identity to sell and hire inside) |
| CTO-Agent | CPO-Agent, CBO-Agent (design tokens, voice) | COO (operating plan), CFO (cost of engineering) |
| CIO-Agent | CPO-Agent, CBO-Agent (CMF spec) | COO (co-owns NPI), CFO (hardware cost/CAPEX) |
| COO-Agent | CTO-Agent / CIO-Agent | CFO (operating cost structure) |
| CFO-Agent | CTO/CIO/COO (costs), CPO/CRO (revenue model) | CRO (pricing), CEO (investor narrative) |
| CRO-Agent | CFO-Agent (pricing economics), CPO-Agent (positioning), CBO-Agent (locked positioning/voice) | CMO (campaigns), CFO (revenue forecast) |
| CMO-Agent | CRO-Agent, CPO-Agent, CBO-Agent (voice/social assets) | — (typically runs in parallel with CRO, terminal node) |
| CHRO-Agent | Implied headcount/budget from all above, CBO-Agent (employer-brand voice, conditional) | — (runs last, terminal node) |
| Reflection-Agent | All Agents' past outputs + Memory (including brand memory files) | Critic-Agent, Planner-Agent (via lessons) |
| Critic-Agent | Meta-Agent Result (any Agent combination) | The original Agent(s) (via Recommendations) |
| Planner-Agent | Meta-Agent Result + Critic-Agent findings | Execution (outside the OS) |

## Graph Structure
```
                        Meta-Agent
                            ↓
   CEO-Agent ────────────────────────────────┐
       ↓                                     │
   CPO-Agent                                 │
       ↓                                     │
   CBO-Agent  (name, voice, visual identity   │ (strategic framing
       ↓       attached before it's built)    │  applies to all)
CTO-Agent ──┬── CIO-Agent                    │
       ↓    │       ↓                        │
       └──→ COO-Agent ←┘  (shared: 35-npi-manufacturing-skill)
              ↓
          CFO-Agent
              ↓
   CRO-Agent ──── CMO-Agent   (built inside CBO-Agent's identity)
              ↓
          CHRO-Agent  (terminal; CBO-Agent joins only if conditional)

  [ Meta-Agent Result ]
              ↓
        Critic-Agent  →  Recommendations back to originating Agent(s)
                          (including brand-consistency findings)
              ↓
       Planner-Agent  →  Roadmap / Milestones / Critical Path
                          (brand lock points included)
              ↑
      Reflection-Agent  (runs on a delay, after outcomes are known;
                          feeds lessons into Critic-Agent and Planner-Agent)
```

## Examples
A robotics product request runs `CPO-Agent → CIO-Agent → CBO-Agent (naming, CMF, HRI voice) → CTO-Agent → COO-Agent → CFO-Agent` per `05-robotics-product-workflow`. Once the Meta-Agent Result is produced, `Critic-Agent` checks it against `memory/lessons-learned.md` for known robotics failure modes (e.g., fleet software built against an unvalidated hardware spec, or interaction cues designed ad hoc instead of against `memory/voice-memory.md`) before `Planner-Agent` turns it into a dated roadmap.
