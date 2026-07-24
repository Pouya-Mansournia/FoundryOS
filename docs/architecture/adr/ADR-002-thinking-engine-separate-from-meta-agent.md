# ADR-002 — Why the Product Thinking Engine Is Separate from the Meta-Agent

## Context
`meta-agent/META_AGENT.md` today does two conceptually different jobs at once: it classifies what kind of request this is (thinking work) and it selects/sequences/merges Agent output (orchestration work). The target architecture's core rule — "the Product Thinking Engine owns the reasoning process; the Meta-Agent does not own product truth, it coordinates execution" — is currently blurred in the shipped system.

## Decision
Treat the Product Thinking Engine (Layer 2) and Reasoning State Machine (Layer 3) as owning the reasoning process — what state the run is in, what's been decided, what evidence exists — and the Meta-Agent Orchestrator (Layer 7) as owning only routing: which Agent/Skill runs next, in what order, with what inputs, and how their outputs get merged. The Meta-Agent consumes the Thinking Engine's current state; it does not decide product truth itself.

## Alternatives Considered
- **Keep them merged, as today.** Rejected: makes it impossible to swap or extend the reasoning process (e.g., add a new discovery loop) without touching orchestration logic, and vice versa — violates Constitution Principle 11 (Backward-Compatible Evolution) by coupling two things that should evolve independently.
- **Replace the Meta-Agent with the Thinking Engine.** Rejected: the Meta-Agent's routing/merging logic (agent selection, execution order, contradiction detection across agent outputs) is mature and unrelated to product-truth reasoning; replacing it would lose working infrastructure for no benefit.

## Consequences
- Phase 5 (Meta-Agent & Existing Agent Integration) must draw this boundary explicitly via an adapter layer, not a rewrite of `meta-agent/META_AGENT.md`.
- Until Phase 2/3 build the actual Thinking Engine/State Machine, the Meta-Agent continues to do both jobs informally for existing (non-state-machine-backed) workflows — this is accepted as the status quo for legacy paths, not retrofitted immediately.

## Status
Accepted.
