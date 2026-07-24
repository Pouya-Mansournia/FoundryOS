# State Contract

Status: Phase 2 deliverable of the FoundryOS Evolution initiative. Implements Layer 3 (Reasoning State Machine) of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md), per ADR-001 and the storage decision in evolution ADR-0006 (structured markdown only — no code, no JSON schema).

This file defines what every state in any FoundryOS state machine must specify. It is a template and a set of rules, not an implementation — the "engine" is the discipline an AI assistant follows when creating, reading, and updating files under `../../runs/<run-id>/`, per [`ENGINE_SPEC.md`](ENGINE_SPEC.md).

## Required Fields Per State

Every state definition (in a `STATE_REGISTRY.md`, whether the generic one in this folder or a future workflow-specific one, e.g. Phase 3's Idea Discovery registry) must specify all thirteen fields below. A state definition missing any field is invalid and must not be used in a run.

| Field | Meaning |
|---|---|
| **State ID** | A unique, stable, upper-snake-case identifier (e.g. `PAUSED_HUMAN_GATE`). Never reused for a different meaning once a run has referenced it. |
| **Purpose** | One or two sentences: what this state is for. |
| **Entry Conditions** | What must be true of the run (prior state, required fields already populated) for this state to be entered. |
| **Required Inputs** | What data/artifacts must exist before this state's Actions can run. |
| **Actions** | What happens while the run is in this state — the work performed, described precisely enough that two different assistants would do materially the same thing. |
| **Allowed Capabilities** | Which layers/agents/tools this state's Actions may call (e.g. "may read Evidence Engine entries; may not write Memory directly" — see Module Boundaries in `../../docs/architecture/TARGET_ARCHITECTURE.md`). |
| **Output Schema** | What this state must produce before it can exit — described as named fields/sections, not a formal JSON schema (per the markdown-only storage decision). |
| **Exit Conditions** | What must be true for the run to be allowed to leave this state normally. |
| **Failure Conditions** | What counts as this state failing, and what happens to the run when it does (see Retry Policy). |
| **Retry Policy** | Whether/how many times this state may be retried after failure, and what changes between attempts. |
| **Possible Next States** | The exhaustive list of State IDs this state may transition to. A transition to any State ID not on this list is invalid (see `TRANSITION_CONTRACT.md`). |
| **Human Approval Requirement** | Whether leaving this state requires a recorded human approval (per `../../docs/architecture/FOUNDRYOS_CONSTITUTION.md`'s Human Authority principle), and if so, what specifically is being approved. |
| **Memory Read Policy** | What, if anything, this state reads from `memory/*.md` or the (future) Evidence Engine. |
| **Memory Write Policy** | What, if anything, this state is allowed to write durably — per `../../docs/architecture/adr/ADR-008-memory-promotion-mechanism.md`, a state never writes to `memory/*.md` directly; it may only append to the current run's own files under `runs/<run-id>/`. |

## Universal Rules

1. **No implicit states.** A run's current state must always be one of the State IDs defined in whichever registry governs that run (`STATE_REGISTRY.md` here, or a workflow-specific registry in a later phase). "The assistant just improvised the next step" is not a valid state.
2. **No orphan states.** Every state except designated entry states must be reachable — i.e. appear in some other state's Possible Next States.
3. **Every terminal state is explicit.** A state with no Possible Next States is a terminal state and must say so explicitly, not leave the list empty by omission.
4. **A state's Actions never bypass its Allowed Capabilities.** If a state's Actions would need to write to `memory/*.md` directly, that state's definition is wrong — durable writes go through the Decision/Reflection path per `../../docs/architecture/adr/ADR-008-memory-promotion-mechanism.md`.

## Relationship to Existing FoundryOS Concepts

This contract does not replace `workflows/*/WORKFLOW.md`'s existing prose sequencing — those workflows remain valid and unaffected. A state-machine-backed workflow (starting with Idea Discovery in Phase 3) is a new, additive variant that happens to reuse the same underlying Agents/Skills, described with this stricter contract instead of prose. See `../../docs/architecture/ARCHITECTURE_PRINCIPLES.md` §2 (One Reasoning Model).
