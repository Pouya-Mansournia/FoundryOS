# Agent Capability Registry

Status: Phase 5 deliverable. Implements Layer 8's contract requirement from [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md) and `../../docs/architecture/adr/ADR-007-existing-agent-integration.md`: every Agent gets a Purpose/Allowed Inputs/Allowed Outputs/Allowed Tools/Forbidden Actions/Required Evidence/Failure Behavior/Escalation Behavior contract, **without modifying a single `AGENT.md` file**.

## Why This Registry Lives Outside `agents/`

ADR-007 offered two paths: extend each `AGENT.md` with new subsections, or build an external adapter. This registry takes the **external adapter** path — it derives the Layer 8 contract shape from each `AGENT.md`'s already-live content (per `meta-agent/META_AGENT.md`'s existing "read the live file, don't hardcode" pattern) plus a small set of reasonable, explicitly-labeled defaults for the fields no `AGENT.md` currently states (Forbidden Actions, Required Evidence, Escalation Behavior). This keeps this phase's blast radius at zero production-file edits for the ten Agents, satisfying the mission's explicit Phase 5 restriction: "do not rewrite existing agents if adapters can preserve them." If a specific Agent's default later proves wrong in real use, correcting it here costs nothing; correcting a wrong assumption baked into ten separate `AGENT.md` files would have cost much more.

## Contract Shape (per Agent)

| Field | Source |
|---|---|
| Purpose | Read live from `agents/{Role}-Agent/AGENT.md`'s `## Purpose` (or equivalent framing at the top of the file) |
| Allowed Inputs | Derived from the Agent's `Dependencies` section ("consumes X from Y") in `registry/AGENT_REGISTRY.md` |
| Allowed Outputs | Read live from the Agent's `Typical Outputs` |
| Allowed Tools | The Agent's own `Skills` list, read live — an Agent may only act through a Skill it's listed as owning |
| Forbidden Actions | **Default (this registry, not the AGENT.md):** an Agent may not act outside its stated domain (e.g. CPO-Agent may not set pricing — that's CFO-Agent's `07-finance-skill`), may not write to `memory/*.md` directly (per `../../docs/architecture/adr/ADR-008-memory-promotion-mechanism.md` — Layer 8 output returns to the calling orchestration layer, which routes durable writes through Decision/Reflection), and may not fabricate human approval |
| Required Evidence | **Default:** any claim the Agent's output makes must be classifiable per `../evidence/EVIDENCE_LEDGER_CONTRACT.md`'s vocabulary when that output feeds a state-machine-backed run; free-form use outside a run (e.g. a direct `/cpo` command) is unaffected |
| Failure Behavior | **Default:** report what's missing/unavailable rather than guessing silently, matching the Meta-Agent's existing "ask only critical clarification questions, otherwise state the assumption" principle |
| Escalation Behavior | **Default:** on repeated failure (see `RETRY_ESCALATION_POLICY.md`) or on encountering a genuine Evaluation Engine blocker, escalate to a human-gate state rather than proceeding on a guess |

## Registry (Summary)

Purpose/Allowed Outputs/Allowed Tools columns are live pointers, not copies — always read the cited file at call time, per the Meta-Agent's existing Source of Truth policy (`meta-agent/META_AGENT.md` §Source of Truth).

| Agent | Purpose/Outputs/Tools | Forbidden Actions (default) | Required Evidence (default) | Escalation (default) |
|---|---|---|---|---|
| CEO-Agent | `agents/CEO-Agent/AGENT.md` | May not make product-level or technical decisions belonging to CPO/CTO/CIO-Agent | Strategic claims classifiable per Evidence Ledger vocabulary | Escalate to human on any governance/board-level decision |
| CPO-Agent | `agents/CPO-Agent/AGENT.md` | May not set architecture (CTO/CIO) or pricing (CFO) | Discovery claims classifiable | Escalate when `EXISTING_SOLUTION_DISCOVERY`-class research is inconclusive (see Idea Discovery registry) |
| CTO-Agent | `agents/CTO-Agent/AGENT.md` | May not set product scope (CPO) or hardware feasibility (CIO) alone | Architecture claims classifiable | Escalate on unresolved feasibility risk |
| CIO-Agent | `agents/CIO-Agent/AGENT.md` | May not set software-only architecture (CTO) alone | Hardware/DFM claims classifiable | Escalate on safety/regulatory blockers |
| COO-Agent | `agents/COO-Agent/AGENT.md` | May not override a stage-gate rejection unilaterally | Operational claims classifiable | Escalate any go/no-go rejection to human |
| CFO-Agent | `agents/CFO-Agent/AGENT.md` | May not set product/GTM scope | Financial claims classifiable | Escalate when unit economics fail a blocker threshold |
| CRO-Agent | `agents/CRO-Agent/AGENT.md` | May not set pricing unilaterally (CFO owns pricing economics) | GTM claims classifiable | Escalate on pipeline-blocking risk |
| CMO-Agent | `agents/CMO-Agent/AGENT.md` | May not define brand identity (CBO) | Campaign claims classifiable | Escalate on brand-inconsistency risk |
| CBO-Agent | `agents/CBO-Agent/AGENT.md` | May not set product scope (CPO) or pricing (CFO) | Brand claims classifiable | Escalate on trademark/legal risk found during naming |
| CHRO-Agent | `agents/CHRO-Agent/AGENT.md` | May not set headcount budget unilaterally (CFO owns budget) | People-plan claims classifiable | Escalate on compensation/legal risk |
| Meta-Agent | `meta-agent/META_AGENT.md` | May not invent a state transition (per `../state-machine/TRANSITION_CONTRACT.md`); may not bypass the Thinking Engine per `../../docs/architecture/adr/ADR-002-thinking-engine-separate-from-meta-agent.md` | N/A — routes, does not itself produce domain claims | Escalate any ambiguous approval question to the human, never assume |

## Relationship to the Meta-Agent's Existing Routing

This registry does not replace `meta-agent/META_AGENT.md`'s Agent Routing Rules or Execution Order — those remain exactly as they are for prose-based (non-state-machine) requests. This registry is consulted specifically when a **state-machine-backed run** (Idea Discovery today, more in future phases) needs to delegate a bounded task to an Agent, per `STATE_TO_CAPABILITY_ROUTING.md`.
