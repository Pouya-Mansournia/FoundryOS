# State-to-Capability Routing

Status: Phase 5 deliverable. Defines exactly how a state's `Allowed Capabilities` field (per `../state-machine/STATE_CONTRACT.md`) resolves to a real Agent/Skill call through `CAPABILITY_REGISTRY.md`, and fixes the Layer 2/Layer 7 boundary from `../../docs/architecture/adr/ADR-002-thinking-engine-separate-from-meta-agent.md` at the implementation level.

## The Boundary, Concretely

- **The state machine (Layer 3) decides *that* a capability is needed** — a state's `Allowed Capabilities` field names which Agent/Skill it may call and why, as already fixed when the state was defined (e.g. `EXISTING_SOLUTION_DISCOVERY`'s Allowed Capabilities names `02-market-research-skill`).
- **The Meta-Agent (Layer 7) decides *how* that call happens** — it resolves the named capability against `CAPABILITY_REGISTRY.md`, checks the call against that Agent's Forbidden Actions, and executes/collects the result.
- **The state never calls an Agent directly** — it requests a capability by name; routing is always mediated by the Meta-Agent, so no state can be rewritten around a specific Agent implementation, matching Layer 8's replaceability requirement.

## Routing Procedure

1. A state's Actions require capability `X` (e.g. "invoke `02-market-research-skill`").
2. Check `CAPABILITY_REGISTRY.md` for the Agent that owns `X` (`registry/SKILL_REGISTRY.md`'s Owning Agent column, read live) and that Agent's Allowed Tools list — confirm `X` is actually in it.
3. Check the call against that Agent's Forbidden Actions. If the call would violate one (e.g. a state asking CPO-Agent to set pricing), **reject the routing** — this is a routing-level rejection, recorded the same way an invalid state transition is recorded (per `../state-machine/TRANSITION_CONTRACT.md`'s pattern), not silently reinterpreted into something the Agent is allowed to do.
4. If the call passes, execute it, and record which capability was invoked and by which state in the run's `state-history.md` (extending that file's existing "Triggered by" field with a specific capability reference where applicable).
5. The Agent's output returns to the calling state, which incorporates it into that state's Output Schema — it does not get written anywhere durable directly (per `CAPABILITY_REGISTRY.md`'s Forbidden Actions default and `ADR-008`).

## Worked Mapping (Idea Discovery Registry)

| State | Named Capability | Registry Resolution | Forbidden-Action Check |
|---|---|---|---|
| `PROBLEM_FRAMING` | `01-discovery-skill` | CPO-Agent | Pass — problem framing is squarely CPO-Agent's domain |
| `EXISTING_SOLUTION_DISCOVERY` | `02-market-research-skill` | CPO-Agent | Pass |
| `ADJACENT_SOLUTION_DISCOVERY` | `02-market-research-skill` | CPO-Agent | Pass |
| `EVIDENCE_SYNTHESIS` | `critic-agent/CRITIC_AGENT.md` | Advanced-layer agent, not one of the 10 domain Agents — routed directly, no Forbidden-Action check needed (Critic Agent has no domain to overstep) | N/A |
| `DECISION_GATE` | `59-problem-solving-decision-modeling-skill` | CEO-Agent | Pass — this Skill is explicitly cross-cutting per `registry/SKILL_REGISTRY.md`'s own notes |

## What Happens on a Blocked Routing Request

See `runs/idea-discovery-demo-0001/orchestration-log.md` for a worked example: a deliberately-attempted out-of-bounds routing request (a state asking CFO-Agent's `07-finance-skill` to be invoked mid-Idea-Discovery, which is out of scope for this workflow entirely) is rejected and recorded, exactly mirroring Phase 2's invalid-transition-rejection demonstration. This is not a hypothetical safeguard — it is exercised the same way the state machine's own invalid transitions were.
