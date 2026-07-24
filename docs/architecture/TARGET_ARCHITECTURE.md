# FoundryOS Target Architecture

Status: Phase 1 deliverable. This is the forward-looking specification — what each layer must do and its boundary with its neighbors. A companion audit of what already exists and the concrete file-by-file mapping is maintained separately as evidence for why the spec looks like this; this document is the spec later phases implement against.

## Conceptual Hierarchy

```
Human Goal / Idea / Problem
  ↓
Product Thinking Engine
  ↓
Reasoning State Machine
  ↓
Evidence Engine
  ↓
Evaluation Engine
  ↓
Decision Engine
  ↓
Meta-Agent Orchestrator
  ↓
Specialized Agents / Skills / Tools
  ↓
Planning Engine
  ↓
Execution Runtime
  ↓
Validation and Observation
  ↓
Reflection Engine
  ↓
Learning Engine
  ↓
Memory Promotion
  ↓
Improved Future Decisions
```

**The Product Thinking Engine owns the reasoning process. The Meta-Agent does not own product truth — it coordinates execution.** This is the single most important boundary in the target architecture and the one most at risk of being blurred, because `meta-agent/META_AGENT.md` today informally does a bit of both (it classifies intent, which is thinking-engine territory, and it routes/merges, which is orchestrator territory). Phase 5 must draw this line explicitly rather than leave it implicit.

## Layer Contracts

Each layer below states: what it owns, what it must never do, and its boundary with the layer(s) it touches. Implementation location is deferred to the phase that builds it; this document only fixes the contract.

### Layer 1 — Constitution and Governance
Owns: purpose, principles, human-authority rules, compatibility rules, phase-approval policy, memory policy. Never: makes a product decision itself. Boundary: every other layer must be explainable as compliant with this layer; this layer never reaches down to enforce it computationally (that is Layer 7's job when routing, and Layer 6's job when recording a decision).
Existing: `FOUNDRYOS_CONSTITUTION.md` (this folder).

### Layer 2 — Product Thinking Engine
Owns: converting an initial input into a structured reasoning process (Goal Understanding → Problem Framing → Context Building → Discovery → Hypothesis Generation → Evidence Collection → Alternative Generation → Evaluation → Decision → Planning → Execution Readiness → Reflection → Learning). Must be agent-agnostic — it does not hardcode CPO/CTO/etc. Never: bypasses the state machine (Layer 3) to jump straight to an artifact. Boundary: hands off structured state to Layer 3 for execution; consumes Layer 4/5/6 outputs; never talks to Layer 8 (Specialized Agents) directly — that routing is Layer 7's job.
Existing seed: `meta-agent/META_AGENT.md`'s classification step + `skills/59-problem-solving-decision-modeling-skill/SKILL.md`'s problem-framing/hypothesis/decision-packet flow. Neither is yet expressed as an explicit, reusable interface independent of the Meta-Agent's routing responsibilities — that separation is this evolution's Phase 5 job.

### Layer 3 — Reasoning State Machine
Owns: the explicit implementation of the Thinking Engine's flow as states with entry conditions, required inputs, actions, allowed capabilities, output schema, exit/failure conditions, retry policy, possible next states, human-approval requirement, and memory read/write policy. Must support forward/backward transitions, research loops, clarification loops, critique loops, pause/resume, and reject invalid transitions. Never: allows an undefined transition to silently succeed. Boundary: every state's "Actions" step may call into Layer 8 (via Layer 7) and Layer 4/5/6; the state machine itself holds no domain knowledge.
Existing: none. Full gap — Phase 2 builds the generic engine (states/transitions/registry/persistence), Phase 3 builds the first concrete workflow (Idea Discovery) on top of it.

### Layer 4 — Evidence Engine
Owns: claims and their supporting material — source traceability, quality/relevance/confidence scoring, contradiction preservation, staleness detection, classification (see the minimum evidence object in the mission's Layer 4 spec, reconciled with skill 59's existing six-way vocabulary per ADR-003). Never: silently discards conflicting evidence or manufactures unsupported uniqueness claims. Boundary: written to by any state that collects evidence; read by Layers 5 and 6; never writes directly to Layer 13 (Memory Promotion) — evidence is not memory until validated.
Existing seed: skill 59's per-claim classification (fact/calculation/inference/hypothesis/assumption/recommendation), already checked by `critic-agent/CRITIC_AGENT.md`.

### Layer 5 — Evaluation Engine
Owns: comparing hypotheses/directions/options against transparent criteria (problem severity/frequency, user value, existing-solution coverage, differentiation, evidence quality, adoption friction, feasibility, complexity, economics, time-to-value, strategic alignment, regulatory risk, reversibility, uncertainty) and surfacing hard blockers rather than hiding them behind a score. Never: lets a high aggregate score mask a genuine blocker (no user problem, sufficient existing solution, missing critical evidence, unacceptable risk, impossible economics, no strategic fit). Boundary: consumes Layer 4's evidence; feeds Layer 6.
Existing seed: `14-validation-skill` (gap/contradiction audit), `18-stage-gate-skill` (go/no-go), `27-product-scorecard-skill` (scoring) — each is domain-scoped today; unifying the criteria contract is Phase 4's job.

### Layer 6 — Decision Engine
Owns: converting evaluated evidence into a traceable, versioned, reversible recommendation (decision, reason, evidence, alternatives considered, trade-offs, rejected alternatives, remaining assumptions, major risks, confidence, human-approval status, revisit conditions, next state). Never: records a decision without a stated reason and without a revisit condition. Boundary: reads Layer 4/5 output; writes to a formalized `memory/decision-log.md`; requires human approval per Layer 1's policy before a decision is treated as final for anything with real stakes.
Existing seed: `memory/decision-log.md`'s existing free-text Decision Record schema, already produced by skill 59's Decision Memo. Phase 4 formalizes it; does not replace it.

### Layer 7 — Meta-Agent Orchestrator
Owns: state execution coordination, agent/skill/tool selection, task delegation, result collection, retries, failure handling, human-approval requests. Never: bypasses the Thinking Engine (Layer 2/3), invents a state transition the state machine didn't define, or writes permanent memory without passing Layer 13's promotion rules. Boundary: sits between Layer 3 (which tells it what state is active and what's allowed) and Layer 8 (which it delegates bounded work to).
Existing: `meta-agent/META_AGENT.md` — already does most of this for the current prose-based system. Extended, not replaced, in Phase 5.

### Layer 8 — Specialized Agents and Skills
Owns: bounded domain work with a defined purpose, allowed inputs/outputs/tools, forbidden actions, required evidence, and failure/escalation behavior. Must remain replaceable — the state machine and orchestrator must not depend on a specific agent's implementation, only its contract. Never: makes a cross-domain decision that belongs to Layer 6.
Existing: `agents/` (10) + `skills/` (59) + `registry/`. Reused as-is; a capability-registry adapter is added in Phase 5, not a rewrite.

### Layer 9 — Planning Engine
Owns: translating an approved decision into milestones, tasks, dependencies, owners/responsible agents, acceptance criteria, risks, validation steps, rollback points. Never: begins planning before the relevant decision gate (Layer 6, human-approved per Layer 1) has cleared. Boundary: consumes Layer 6's approved decision; feeds Layer 10.
Existing: `planner-agent/PLANNER_AGENT.md` — already does this for Combined Executive Answers today. Extended in Phase 6.

### Layer 10 — Execution Runtime
Owns: performing approved actions (code/design/doc changes, tests, experiments, deployment prep, external-tool integration) bounded by approved scope, explicit acceptance criteria, repository constraints, safety limits, rollback support, and audit logs. Never: executes anything without an approved decision and explicit scope (Layer 1's Human Authority principle, enforced structurally here). Boundary: consumes Layer 9's plan; calls Layer 8's agents/tools and the MCP tools `mcp-layer/MCP_LAYER.md` already declares; reports to Layer 11.
Existing: none — this is the gap FoundryOS's own `docs/ROADMAP.md` already names under the unshipped `v5.0.0` Runtime + Execution Engine. Built in Phase 6, per ADR-002.

### Layer 11 — Reflection Engine
Owns: comparing expected vs. actual outcome, root cause, successful/failed assumptions, unexpected effects, reusable lessons, required corrections. Never: merely summarizes activity without explaining what should change in future decisions. Boundary: reads Layer 10's execution/validation results and Layer 6's decision record; writes to Layer 12.
Existing: `reflection-agent/REFLECTION_AGENT.md` — already does this, non-blocking, after an outcome is known. Extended in Phase 7.

### Layer 12 — Learning Engine
Owns: converting validated reflection into reusable knowledge (principles, research patterns, risk heuristics, state policies, agent-selection rules, validated domain knowledge, rejected patterns, updated decision criteria). Never: promotes anything that hasn't passed Layer 11's reflection and Layer 1's approval policy. Boundary: reads Layer 11; writes to Layer 13.
Existing: folded into `reflection-agent/REFLECTION_AGENT.md` + `memory/lessons-learned.md` today, with no separate promotion mechanism. Formalized in Phase 7.

### Layer 13 — Memory Promotion
Owns: the three-tier model (Temporary Run Memory → Validated Project Memory → Reusable Organizational Knowledge) and the promotion gate defined in `FOUNDRYOS_CONSTITUTION.md`'s Memory Policy. Never: stores raw chain-of-thought; never promotes without passing through Claim → Evidence → Evaluation → Validation → Approval. Boundary: writes to `memory/*.md`; every other layer that wants something remembered permanently must go through this gate, not write to `memory/` directly.
Existing: `memory/` (13 files), governed today only by prose convention. Enforcement added in Phase 7.

## Module Boundaries — Summary Rule

No layer skips its immediate neighbor. In particular:
- Layer 7 (Meta-Agent) never talks to Layer 2/3 (Thinking Engine) as if it owns reasoning — it consumes the Thinking Engine's output.
- Layer 8 (Agents/Skills) never writes directly to Layer 13 (Memory) — everything durable passes through Layer 6 (Decision) or Layer 11/12 (Reflection/Learning) first.
- Layer 10 (Execution Runtime) never acts without a Layer 9 (Planning) artifact that itself traces to a Layer 6 (Decision) that was human-approved per Layer 1.

This chain is what makes the system traceable end to end (Constitution Principle 8) and is the primary thing Phase 8 (Runtime Reliability) must be able to verify mechanically once Layers 2–13 have code/state behind them, not just prose.
