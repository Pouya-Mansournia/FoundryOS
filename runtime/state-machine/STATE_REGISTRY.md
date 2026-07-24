# Generic State Registry (Phase 2 — Engine Core Only)

Status: Phase 2 deliverable. These are **generic lifecycle states** used to build and prove the state-machine engine itself. They are deliberately domain-free — no Idea Discovery, no product-specific states. Per the mission's Phase 2 restriction ("do not yet implement the entire product discovery workflow — build the generic engine first"), the concrete Idea Discovery state set is Phase 3's deliverable and will live in its own registry, reusing this engine.

Every state below follows the 13-field contract in [`STATE_CONTRACT.md`](STATE_CONTRACT.md).

---

## INITIATED

- **Purpose:** Entry state for any run. Confirms the run has a stated goal and is ready to begin real work.
- **Entry Conditions:** A run has been created with a non-empty goal/input statement.
- **Required Inputs:** `goal` (free text — what this run is for).
- **Actions:** Record the goal and creation metadata in `run-state.md`.
- **Allowed Capabilities:** May read `docs/architecture/` and this state machine's own contracts. May not call any Agent/Skill yet.
- **Output Schema:** `run-state.md` populated with `run_id`, `goal`, `created_at`, `current_state: INITIATED`.
- **Exit Conditions:** Goal statement is non-empty and the run has a unique `run_id`.
- **Failure Conditions:** Goal statement is empty or the run cannot be assigned a unique ID (collision with an existing `runs/<run-id>/`).
- **Retry Policy:** Retry immediately with a corrected goal statement or a new ID; no limit (this is a data-entry failure, not a systemic one).
- **Possible Next States:** `IN_PROGRESS`, `FAILED`
- **Human Approval Requirement:** None to enter or leave this state.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None — writes only to this run's own `run-state.md`.

## IN_PROGRESS

- **Purpose:** Generic "work is happening" state — a stand-in for whatever domain-specific states a future workflow (e.g. Idea Discovery) defines in its own registry.
- **Entry Conditions:** Prior state was `INITIATED` or a retry of `IN_PROGRESS` itself.
- **Required Inputs:** The goal from `INITIATED`.
- **Actions:** Whatever work this run's domain requires (left abstract at the engine-core level; a concrete workflow's registry replaces this state with its own specific states in Phase 3+).
- **Allowed Capabilities:** May call Layer 8 (Agents/Skills) per the Meta-Agent's existing routing; may read the Evidence Engine (once it exists, Phase 4) but may not write `memory/*.md` directly.
- **Output Schema:** Whatever artifact this run's work produces, referenced (not embedded) from `run-state.md`.
- **Exit Conditions:** The work item this state represents is either complete, needs human input, or has failed.
- **Failure Conditions:** The work could not be completed with available inputs/capabilities.
- **Retry Policy:** Up to 2 automatic retries with the same inputs; a 3rd failure transitions to `FAILED` rather than retrying indefinitely.
- **Possible Next States:** `PAUSED_HUMAN_GATE`, `RETRY_PENDING`, `FAILED`, `APPROVED`, `COMPLETED`
- **Human Approval Requirement:** None to enter; leaving toward `APPROVED` requires a recorded approval (see Transition Contract rule 4).
- **Memory Read Policy:** May read `memory/*.md` for context (consistent with how Agents/Skills already do this today).
- **Memory Write Policy:** None — durable writes happen only via the Decision/Reflection path, never from this state directly.

## PAUSED_HUMAN_GATE

- **Purpose:** The run is waiting on an explicit human decision before it may proceed — the mechanism the Mandatory First Product Workflow's evidence-review pause requires.
- **Entry Conditions:** Reached only from a state whose work has produced something requiring human review or approval.
- **Required Inputs:** A clear statement of what's being asked of the human (recorded in `run-state.md`'s current status).
- **Actions:** None — this state performs no work; it exists to wait.
- **Allowed Capabilities:** None beyond reading/reporting the run's current status.
- **Output Schema:** N/A (waiting state).
- **Exit Conditions:** A human response has been recorded in `approvals.md`.
- **Failure Conditions:** N/A — a pause does not fail; it may remain indefinitely.
- **Retry Policy:** N/A.
- **Possible Next States:** `IN_PROGRESS` (resumed, continue), `REJECTED` (human declines to proceed), `FAILED` (human indicates the run cannot continue for an external reason)
- **Human Approval Requirement:** Entering this state IS the request for approval; leaving it requires the approval record.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## RETRY_PENDING

- **Purpose:** Intermediate bookkeeping state between a failed attempt and a retry, so the retry count and reason are recorded before work resumes.
- **Entry Conditions:** A state failed and its Retry Policy permits another attempt.
- **Required Inputs:** The failure reason from the failed state.
- **Actions:** Increment the retry counter for the originating state; record what will differ on the next attempt, if anything.
- **Allowed Capabilities:** None beyond updating `run-state.md`'s retry counter.
- **Output Schema:** Updated retry count + reason, referenced back to the originating state.
- **Exit Conditions:** Retry counter updated and within the originating state's Retry Policy limit.
- **Failure Conditions:** Retry counter would exceed the originating state's limit.
- **Retry Policy:** N/A (this state doesn't retry itself).
- **Possible Next States:** the originating state (retried), `FAILED` (limit exceeded)
- **Human Approval Requirement:** None.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## APPROVED

- **Purpose:** A decision or output produced during the run has received the human approval required to be treated as final for its scope.
- **Entry Conditions:** A recorded approval exists in `approvals.md` covering the specific thing being approved.
- **Required Inputs:** The approval record.
- **Actions:** None — records that the gate has cleared.
- **Allowed Capabilities:** None.
- **Output Schema:** Reference to the approval record.
- **Exit Conditions:** Immediate — this is typically a pass-through state toward `COMPLETED` or back into further `IN_PROGRESS` work the approval unblocks.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A.
- **Possible Next States:** `IN_PROGRESS`, `PLANNING`, `COMPLETED`
- **Human Approval Requirement:** Already satisfied to enter this state.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## PLANNING

- **Purpose:** Produce a `runtime/planning/PLANNING_ENGINE.md`-conformant plan for an approved decision — Phase 6 addition, generic (any workflow reaching an approved decision that requires real-world action may use this state).
- **Entry Conditions:** Reached only from `APPROVED` — a Decision Record with `Human Approval Status: APPROVED` must exist.
- **Required Inputs:** The approved Decision Record's `decision_id`.
- **Actions:** Produce `plan.md` per `runtime/planning/PLANNING_ENGINE.md`'s schema — milestones, tasks, dependencies, acceptance criteria, rollback points.
- **Allowed Capabilities:** May invoke `planner-agent/PLANNER_AGENT.md`'s judgment; may read the Decision Record and its cited evidence.
- **Output Schema:** `plan.md` referencing the decision.
- **Exit Conditions:** Every task has acceptance criteria and a stated rollback point (or explicit "not reversible").
- **Failure Conditions:** Cannot produce a plan whose tasks have well-defined acceptance criteria from the decision as given.
- **Retry Policy:** 1 retry looping back to `APPROVED` to re-check the decision's scope; then `FAILED`.
- **Possible Next States:** `EXECUTING`, `APPROVED` (backward loop), `FAILED`
- **Human Approval Requirement:** None additional — planning inherits the decision's existing approval; execution authorization is checked per-task at `EXECUTING`.
- **Memory Read Policy:** None beyond the Decision Record.
- **Memory Write Policy:** None.

## EXECUTING

- **Purpose:** Perform authorized actions from `plan.md`, one task at a time, per `runtime/execution/EXECUTION_RUNTIME_SPEC.md`'s Authorization Gate — Phase 6 addition.
- **Entry Conditions:** `PLANNING` completed with a valid `plan.md`.
- **Required Inputs:** `plan.md`, the task(s) to execute.
- **Actions:** For each task whose Dependencies are satisfied: check the Execution Authorization Gate (approved decision + plan entry + scope match); if it passes, perform the action and record it in `execution-log.md`; if it fails, reject and record why, per `runtime/execution/EXECUTION_LOG_CONTRACT.md`.
- **Allowed Capabilities:** Whatever the task's Owner field specifies (an Agent/Skill, routed per `runtime/orchestration/STATE_TO_CAPABILITY_ROUTING.md` if it's an Agent capability).
- **Output Schema:** `execution-log.md` entries; artifacts referenced from them.
- **Exit Conditions:** All tasks either completed with acceptance criteria met, or the plan's Rollback Plan has been applied for any that failed.
- **Failure Conditions:** A task's acceptance criteria are not met after execution and its rollback point has been applied.
- **Retry Policy:** Per-task: 1 retry with the same authorization (already granted, does not need re-approval) if the failure looks transient; else `FAILED` for that task, which per `PLANNING_ENGINE.md`'s dependency model blocks any task depending on it.
- **Possible Next States:** `COMPLETED`, `FAILED`
- **Human Approval Requirement:** Already satisfied per-task via the Authorization Gate; no additional gate to exit this state, since exiting just means "all authorized work is done or explicitly rolled back."
- **Memory Read Policy:** None beyond the plan and decision.
- **Memory Write Policy:** None directly — same as every other state; durable promotion of what was executed happens via Reflection (Phase 7).

## REJECTED

- **Purpose:** Terminal state — a human explicitly declined to approve continuing.
- **Entry Conditions:** Reached only from `PAUSED_HUMAN_GATE` with a recorded rejection.
- **Required Inputs:** The rejection record (an `approvals.md` entry with `new_status: REJECTED`).
- **Actions:** None.
- **Allowed Capabilities:** None.
- **Output Schema:** N/A.
- **Exit Conditions:** N/A — terminal.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A — a rejected run is not retried; a new run is created if the goal is revisited later.
- **Possible Next States:** none (terminal).
- **Human Approval Requirement:** Already satisfied (the rejection itself is the recorded human decision).
- **Memory Read Policy:** None.
- **Memory Write Policy:** None directly — a rejected run's reasoning may later be read by Reflection (Layer 11) as input to a lesson, but that write goes through the Reflection/Learning promotion path, not this state.

## FAILED

- **Purpose:** Terminal state — the run could not complete for reasons that retries could not resolve.
- **Entry Conditions:** Reached from any state whose Failure Conditions were met and whose Retry Policy is exhausted (or has none).
- **Required Inputs:** The failure reason.
- **Actions:** None.
- **Allowed Capabilities:** None.
- **Output Schema:** N/A.
- **Exit Conditions:** N/A — terminal.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A.
- **Possible Next States:** none (terminal).
- **Human Approval Requirement:** None.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None directly — same as `REJECTED`, a failure's cause is legitimate Reflection input via the proper promotion path, not a direct write.

## COMPLETED

- **Purpose:** Terminal state — the run achieved its goal.
- **Entry Conditions:** Reached from `IN_PROGRESS` or `APPROVED` once the goal is satisfied.
- **Required Inputs:** The final output/artifact this run produced.
- **Actions:** Record the final output reference and closing timestamp.
- **Allowed Capabilities:** None beyond the closing write to `run-state.md`.
- **Output Schema:** `run-state.md`'s `current_state: COMPLETED`, `completed_at`, `final_output` fields populated.
- **Exit Conditions:** N/A — terminal.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A.
- **Possible Next States:** none (terminal).
- **Human Approval Requirement:** Whatever approval already applied upstream (via `APPROVED`, if that path was taken).
- **Memory Read Policy:** None.
- **Memory Write Policy:** None directly — durable promotion of anything from a completed run goes through Reflection/Learning (Phase 7), never a direct write from this state.

---

## Terminal States

`REJECTED`, `FAILED`, `COMPLETED` — each has an empty Possible Next States list, explicitly stated per Universal Rule 3 in `STATE_CONTRACT.md`.

## Reachability Check

- `INITIATED` → `IN_PROGRESS`, `FAILED` ✓ (both defined below)
- `IN_PROGRESS` is reachable from `INITIATED`, `APPROVED`, and retries of itself ✓
- `PAUSED_HUMAN_GATE` reachable from `IN_PROGRESS` ✓
- `RETRY_PENDING` reachable from any state whose Retry Policy fires (here, `IN_PROGRESS`) ✓
- `APPROVED` reachable from `PAUSED_HUMAN_GATE`'s resume path (via `IN_PROGRESS`, which is where "resumed, continue" lands) — note: `APPROVED` is directly reachable only where a state's Possible Next States lists it (`IN_PROGRESS`); this is intentional, since approval is requested from `PAUSED_HUMAN_GATE` but recorded before the transition back into work.
- `PLANNING` reachable from `APPROVED` ✓ (Phase 6 addition)
- `EXECUTING` reachable from `PLANNING` ✓ (Phase 6 addition)
- `REJECTED`, `FAILED`, `COMPLETED` reachable as documented above, now also from `PLANNING`/`EXECUTING` per their Possible Next States ✓

No orphan states in this registry.
