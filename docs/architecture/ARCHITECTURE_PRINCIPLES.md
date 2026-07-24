# FoundryOS Architecture Principles

Status: Phase 1 deliverable. Operational rules that keep `FOUNDRYOS_CONSTITUTION.md`'s principles and `TARGET_ARCHITECTURE.md`'s layer contracts enforceable in practice, day to day, phase to phase.

## 1. Extension Over Replacement

Every new layer (Layers 1–13 in `TARGET_ARCHITECTURE.md`) is built by extending, adapting, or wrapping an existing component wherever one exists. A phase that proposes replacing an existing `AGENT.md`, `SKILL.md`, `WORKFLOW.md`, Command, or Memory file wholesale must justify it explicitly in that phase's ADR and get human approval before doing so — this is the exception path, not the default.

## 2. One Reasoning Model

FoundryOS must not end up with two competing ways to reason about a product decision. Where the target architecture's vocabulary would otherwise duplicate something FoundryOS already ships (evidence classification, decision records, reflection), the existing vocabulary is adopted and extended, and the mapping is written down explicitly (see ADR-003). No phase may introduce a second, parallel scheme "for the new system" while the old one keeps running unreconciled.

## 3. Contracts Before Implementation

Every layer's contract (owns / never / boundary, as defined in `TARGET_ARCHITECTURE.md`) is fixed before the layer is implemented. A phase may not begin writing a state machine, evidence ledger, or execution runtime whose behavior contradicts its own layer's contract; if implementation reveals the contract was wrong, the contract is amended first (via ADR), then implementation resumes.

## 4. Module Boundaries Are Enforced at the Narrowest Point

Concretely: the Meta-Agent (Layer 7) may not read or write Evidence Engine (Layer 4) state directly except through the interface Layer 4 exposes; Specialized Agents (Layer 8) may not write to `memory/` (Layer 13) directly — they return output to whatever orchestration layer called them, and that layer routes durable output through the Decision/Reflection path. This is checked manually until Phase 8 (Runtime Reliability) can check it mechanically.

## 5. Versioning Policy

- FoundryOS's own product versioning (`VERSION.md`, `VERSIONING.md`) is authoritative for the shipped product. This evolution's phase numbering is a separate, parallel track.
- The two are reconciled explicitly, not silently, whenever a phase changes what a user of FoundryOS actually experiences. Concretely: Phase 6 (Execution Runtime) is expected to trigger a `VERSION.md` update per ADR-002, because it fulfills FoundryOS's own already-announced `v5.0.0` roadmap item. Phases 1–5, 7–9 are not expected to trigger a product version bump on their own merits unless a specific phase's completion changes shipped user-facing behavior.
- Any change to an existing public contract (the structure of an `AGENT.md`, `SKILL.md`, `WORKFLOW.md`, Command, or Memory file) follows FoundryOS's existing `VERSIONING.md` classification (major/minor/patch) for that change, not a new scheme invented by this evolution.

## 6. Migration Policy

- Migrations are additive and optional-by-default. A new state-machine-backed variant of a workflow (e.g. Idea Discovery in Phase 3) is added alongside the existing prose workflow; nothing is forced to migrate until it has been proven and a separate, explicit decision is made to deprecate the prose version — and even then, deprecation follows FoundryOS's existing `VERSIONING.md` deprecation rules, not silent removal.
- Before modifying an existing public contract: identify consumers (which Commands, Workflows, or other Skills reference it), document the impact, provide a compatibility path, add validation, and record the change in the compatibility log.

## 7. Architecture Decision Records

This is the first ADR format/location introduced into the FoundryOS repository (confirmed absent during Phase 0's audit — no prior ADR convention existed). Location: `docs/architecture/adr/ADR-NNN-short-title.md`, numbered sequentially, never renumbered or deleted once merged (a superseded ADR is marked "Superseded by ADR-NNN," not removed). Each ADR states: Context, Decision, Alternatives Considered, Consequences, Status.

This is distinct from the evolution track's own process decision log, which tracks *process* decisions about how the evolution itself is run (e.g. "where do these docs live"). `docs/architecture/adr/` tracks *architecture-content* decisions about FoundryOS's target design — the two are cross-referenced, never merged into one file, so a future reader can tell "why did we choose this folder layout" (evolution log) apart from "why does the Evidence Engine live separately from Memory" (architecture ADR).

The eight ADRs required by the governing mission prompt are filed under `docs/architecture/adr/`:
- ADR-001 — Why a Reasoning State Machine instead of a linear prompt pipeline
- ADR-002 — Why the Product Thinking Engine is separate from the Meta-Agent
- ADR-003 — Why Evidence is stored separately from Memory
- ADR-004 — Why phase transitions require human approval
- ADR-005 — Why run state is persistent and resumable
- ADR-006 — Why the first workflow is Idea Discovery
- ADR-007 — How existing Agents/Skills are integrated
- ADR-008 — How permanent memory promotion works

## 8. Product Engineering Focus, Enforced

Any new Layer 1–13 component must remain usable for software, hardware, AI, robotics, service, platform, or hybrid products. A phase deliverable that only makes sense for one product type (e.g. a state hardcoded to "sprint planning") must be generalized or explicitly scoped as domain-specific and optional, never adopted as the default shape of a core layer.
