# Retry and Escalation Behavior (Orchestration Layer)

Status: Phase 5 deliverable. Extends `../state-machine/STATE_CONTRACT.md`'s per-state Retry Policy with orchestration-level rules for what happens when a *delegated Agent call itself* fails or produces a blocker, as opposed to the state's own logic failing.

## Distinguishing Two Kinds of Failure

1. **State-level failure** — already covered by `../state-machine/STATE_REGISTRY.md`'s per-state Failure Conditions/Retry Policy (e.g. `EXISTING_SOLUTION_DISCOVERY` retries once with a narrower question, then proceeds with "none found, low confidence").
2. **Agent-call-level failure** — the capability was routed correctly (per `STATE_TO_CAPABILITY_ROUTING.md`) but the Agent's own output is unusable: contradicts itself, cites no classifiable evidence, or hits an Evaluation Engine blocker (`../evaluation/EVALUATION_ENGINE.md`'s blocker list). This phase adds explicit handling for case 2, which the state contract alone doesn't fully cover.

## Orchestration-Level Retry Rules

- An Agent-call-level failure gets **one retry** with the same capability and a refined request (e.g. asking `02-market-research-skill` a narrower question) before escalating — mirrors the pattern already used at the state level, kept consistent rather than inventing a second retry scheme.
- A retry that fails the same way twice is **not** retried a third time automatically — this matches `../state-machine/STATE_REGISTRY.md`'s `RETRY_PENDING` state's general "don't retry indefinitely" discipline.

## Escalation Rules

An Agent-call-level failure escalates (rather than silently failing the whole run) when:
- The failure is a genuine Evaluation Engine **blocker** (not just "no evidence found," which the state's own retry-then-proceed logic already handles) — e.g. a CFO-Agent call surfaces "impossible economics." Blockers always escalate to a human-gate state (e.g. `PAUSED_HUMAN_GATE` in the generic registry, or `WAITING_FOR_USER_EXPERIENCE` if within Idea Discovery), never silently absorbed into "proceed with lower confidence."
- The routing itself was rejected per `STATE_TO_CAPABILITY_ROUTING.md` (an out-of-bounds capability request) — this always escalates as a **design defect to report**, not a run-time failure to retry, since it means the state's Allowed Capabilities field was wrong when the state was defined, not that the Agent had a bad day.
- Two consecutive Agent-call-level failures on the same capability request.

## What Escalation Looks Like

Escalation means: pause the run (transition to the nearest defined human-gate state per the governing registry), record what triggered escalation in `state-history.md` with the same rejection-recording pattern already established, and report plainly to the human what's blocked and why — never invent a workaround that bypasses the blocker just to keep the run moving, per Constitution Principle 7 (Human Authority).

## Relationship to Existing Agent Escalation Language

Some `AGENT.md` files already imply escalation informally (e.g. CIO-Agent's "shared accountability with COO-Agent on production ramp" suggests handoff points). This policy does not contradict or need to rewrite those — it adds the *state-machine-specific* escalation mechanism (pausing a run, recording it in `state-history.md`) on top of whatever domain-specific escalation an Agent's own prose already describes, per Architecture Principle 1 (Extension Over Replacement).
