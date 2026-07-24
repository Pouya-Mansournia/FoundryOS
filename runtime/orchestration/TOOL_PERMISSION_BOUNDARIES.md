# Tool Permission Boundaries

Status: Phase 5 deliverable. Fixes what a delegated Agent call may and may not touch during a state-machine-backed run, extending `../../docs/architecture/TARGET_ARCHITECTURE.md`'s Module Boundaries summary rule to the orchestration layer specifically.

## Boundaries

| Resource | Read | Write |
|---|---|---|
| `memory/*.md` | Allowed, per each state's Memory Read Policy (`../state-machine/STATE_CONTRACT.md`) | **Never** directly from a delegated Agent call — durable writes go through the Decision Engine (`../decision/DECISION_RECORD_CONTRACT.md`, for approved decisions) or the Reflection/Learning promotion path (Phase 7) |
| This run's `evidence-ledger.md` | Allowed | Allowed, append-only, per `../evidence/EVIDENCE_LEDGER_CONTRACT.md` |
| This run's `run-state.md` / `state-history.md` / `approvals.md` | Allowed | Only the orchestrating Meta-Agent layer writes these, never a delegated Agent directly |
| Other Agents' output within the same run | Allowed, if the calling state's Required Inputs name it | N/A |
| `mcp-layer/MCP_LAYER.md`-declared external tools | Allowed to *declare* a need (unchanged from existing MCP behavior) | N/A — FoundryOS still executes nothing itself; unchanged by this evolution, per that layer's existing "declaration only" scope |
| Another run's files (`runs/<other-run-id>/`) | **Never** | **Never** — runs are isolated from each other unless a future phase explicitly defines a cross-run reference mechanism (not built; out of scope) |

## Why This Matters at the Orchestration Layer Specifically

Phase 4's Evidence/Decision contracts already forbid direct `memory/*.md` writes at the *state* level. This phase adds the same rule at the *Agent-call* level, because a delegated Agent call is where an existing Skill's prose (e.g. `01-discovery-skill/SKILL.md`, which was never written with this boundary in mind) could, if followed too literally by a hosting assistant, attempt something like "update `memory/product-memory.md` with this finding." The boundary here is what tells the orchestration layer to intercept that and route it through the proper channel instead — a discipline check, not a code-enforced one, per the markdown-only decision.

## Escalation on Boundary Violation Attempt

If a delegated Agent call's output *asks* to write somewhere out of bounds (e.g. a Skill's own prose instructs "log this in memory"), the Meta-Agent orchestration layer intercepts it, does not perform the write, and instead either (a) routes the content through the proper Decision/Reflection path if it's genuinely durable-worthy, or (b) holds it in the run's own state if it's just working context. This is never silently dropped — see `runs/idea-discovery-demo-0001/orchestration-log.md` for the demonstrated case.
