# Planning Engine

Status: Phase 6 deliverable. Implements Layer 9 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md), extending `planner-agent/PLANNER_AGENT.md`'s existing milestone/roadmap output into a formal contract a state-machine-backed run can consume directly. Structured markdown only, per evolution `DECISION_LOG.md` ADR-0006.

## Gate: Planning Never Begins Before an Approved Decision

Per the mission's explicit Phase 6 restriction and Constitution Principle 7 (Human Authority): a Planning Engine artifact (`plan.md`, below) may only be created once a `runtime/decision/DECISION_RECORD_CONTRACT.md`-conformant Decision Record exists with `Human Approval Status: APPROVED`. A plan with no cited, approved decision behind it is not valid.

## Plan Schema

```markdown
# Plan: <run-id>

- Decision Reference: <decision_id from the approved Decision Record this plan implements>
- Created At: <ISO timestamp>

## Milestones
### M1 — <name>
- Goal: <what this milestone achieves>
- Tasks: [T1, T2, ...]
- Acceptance Criteria: <specific, checkable — not "works correctly">

## Tasks
### T1 — <name>
- Milestone: M1
- Description: <what, specifically>
- Dependencies: [<other task IDs that must complete first>]
- Owner: <responsible Agent/Skill/human>
- Acceptance Criteria: <specific, checkable>
- Rollback Point: <what "undo this task" means concretely, or "not reversible" stated explicitly if true>
- Risk: <what could go wrong>

## Validation Steps
<how the plan as a whole will be checked before/during execution — may reference `../evaluation/EVALUATION_ENGINE.md`>

## Rollback Plan (Whole-Plan Level)
<what undoing the entire plan means, if every task's individual rollback isn't sufficient>
```

## Task Dependency Model

Tasks form a directed graph via `Dependencies`. A task may not begin execution (see `../execution/EXECUTION_RUNTIME_SPEC.md`) until every task it depends on has completed with its Acceptance Criteria met. A dependency cycle is invalid — same discipline as `../state-machine/STATE_REGISTRY.md`'s no-orphan-states rule, applied to tasks instead of states.

## Rollback Points Are Mandatory, Not Optional

Every task states a Rollback Point, even if that point is "not reversible — see Major Risks in the governing Decision Record." An unstated rollback point is treated the same as an unstated Revisit Condition on a Decision Record (`../decision/DECISION_RECORD_CONTRACT.md`) — a gap to flag, not a default to silently accept.

## Relationship to `planner-agent/PLANNER_AGENT.md`

This does not replace the existing Planner Agent — `PLANNER_AGENT.md` remains the source of planning *judgment* (sequencing, resourcing, critical-path reasoning) for both prose-based Commands/Workflows and state-machine-backed runs. This Plan Schema is the *artifact format* a state-machine-backed run's planning state produces, whether authored by a human, by the Planner Agent's judgment applied through this schema, or both — matching Phase 5's pattern of formalizing a shape without displacing the existing agent that already does the underlying reasoning.
