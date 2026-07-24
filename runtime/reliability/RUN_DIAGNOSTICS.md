# Run Diagnostics

Status: Phase 8 deliverable. Structured logs, run diagnostics, and state-transition metrics for Layer 3 (Reasoning State Machine) and every layer built on top of it. Structured markdown only, per ADR-0006 — diagnostics here means a documented inspection procedure an assistant runs manually, not automated telemetry.

## Structured Logs — What Already Exists, Made Explicit

Every run's logs are already structured, append-only, and consistently formatted (per `../state-machine/ENGINE_SPEC.md`, `../orchestration/STATE_TO_CAPABILITY_ROUTING.md`, `../execution/EXECUTION_LOG_CONTRACT.md`). Phase 8 does not introduce new log files — it defines how to *read* the existing ones diagnostically:

| Log | What it answers |
|---|---|
| `state-history.md` | What state is this run really in, and how did it get there? |
| `approvals.md` | What has a human actually approved, and when? |
| `evidence-ledger.md` | What is this run's reasoning actually based on? |
| `orchestration-log.md` | What real capabilities were invoked, and were any blocked? |
| `execution-log.md` | What real actions were taken, and were any rejected? |
| `reflection.md` / `lessons-queue.md` | What was learned, and did it actually get promoted or correctly rejected? |

## Run Diagnostic Procedure

To diagnose any run's health:

1. **State Consistency Check**: `run-state.md`'s `Current State` must equal the `TO_STATE` of `state-history.md`'s last `ACCEPTED` entry. A mismatch means `run-state.md` was edited out of band — a serious integrity failure, per Constitution Principle 8 (Traceability).
2. **Terminal Check**: if `Current State` is a terminal state (`COMPLETED`/`FAILED`/`REJECTED`/`ARCHIVED`), confirm no further entries exist after it in `state-history.md` — a terminal state with further activity after it is also an integrity failure.
3. **Approval Coverage Check**: every transition in `state-history.md` whose target state has a Human Approval Requirement must have a corresponding `approvals.md` entry with a timestamp at or before that transition.
4. **Provenance Check** (where applicable): every claim in a `decision-record.md` traces to an `evidence_id` that actually exists in `evidence-ledger.md` (already exercised concretely in Phase 4).

See `AUDIT_TRAIL_VERIFICATION.md` for this procedure run against all existing demo runs.

## State-Transition Metrics (Computed by Reading the Log, Not Automated)

For any run, a quick health summary is derived by counting `state-history.md` entries:

- Total transitions attempted
- ACCEPTED vs. REJECTED count (a high rejection rate on a real run, unlike a deliberate test probe, would indicate a badly-defined state or a routing/registry mismatch worth fixing)
- Retries per state (from `RETRY_PENDING` entries)
- Time-in-state (difference between consecutive timestamps) — flags unusually long dwell times worth investigating, distinct from a deliberate, expected pause

## Cost and Tool Usage Tracking

Already captured structurally by `orchestration-log.md` (which capability/Agent was invoked, per entry) and `execution-log.md` (what action was taken). Phase 8 adds no new field — it defines the aggregation: counting entries per Agent/Skill across a run's `orchestration-log.md` gives a tool-usage summary; this evolution has no token/dollar cost model to attach (markdown-only, no metered API calls of its own), so "cost" here means *decision and execution volume*, not currency — a run that needed 15 capability routings to reach a decision is more expensive, in the sense this system can actually measure, than one that needed 3.
