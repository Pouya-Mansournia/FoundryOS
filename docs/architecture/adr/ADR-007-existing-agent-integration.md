# ADR-007 — How Existing Agents/Skills Are Integrated

## Context
FoundryOS already has 10 mature Agents and 59 Skills with defined purposes, inputs, outputs, and dependencies (`registry/AGENT_REGISTRY.md`, `registry/SKILL_REGISTRY.md`). The target architecture's Layer 8 requires each Agent to have Purpose, Allowed Inputs/Outputs/Tools, Forbidden Actions, Required Evidence, and Failure/Escalation Behavior, and requires the state machine to depend only on an Agent's contract, never its implementation.

## Decision
Existing Agents and Skills are integrated via a **capability-registry adapter** (Phase 5), not rewritten. The adapter maps each `AGENT.md`'s existing "Responsibilities / Skills / Typical Outputs / Dependencies" sections onto the Layer 8 contract shape (Purpose / Allowed Inputs / Allowed Outputs / Allowed Tools / Forbidden Actions / Required Evidence / Failure Behavior / Escalation Behavior), filling genuine gaps (most current AGENT.md files don't state Forbidden Actions or Failure Behavior explicitly) by extending the AGENT.md files with new sections, not restructuring existing ones.

## Alternatives Considered
- **Rewrite all 10 AGENT.md files against the new contract shape immediately.** Rejected: high blast radius for a first pass, violates "do not repeat an audit unless the repository changed materially" and Architecture Principle 1 — extending existing sections is lower-risk and preserves everything already working (routing rules, execution order, dependency notes).
- **Leave Agents un-adapted and have the state machine call them ad hoc.** Rejected: reintroduces the exact coupling-to-implementation problem Layer 8's contract exists to prevent.

## Consequences
- Phase 5's adapter is additive: it may append new subsections to each `AGENT.md` (e.g. "## Forbidden Actions," "## Escalation Behavior") where missing, but does not remove or reorder existing content.
- The Meta-Agent's existing "read the live AGENT.md Skills list, don't hardcode it" pattern (already documented in `meta-agent/META_AGENT.md`'s Source of Truth section) is preserved and extended to also read the new contract sections live, not cached.

## Status
Accepted.
