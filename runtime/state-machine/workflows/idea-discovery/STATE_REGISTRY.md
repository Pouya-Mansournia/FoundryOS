# Idea Discovery — State Registry (Phase 3)

Status: Phase 3 deliverable. The first concrete, product-shaped state machine built on the Phase 2 generic engine (`../../STATE_CONTRACT.md`, `../../TRANSITION_CONTRACT.md`, `../../ENGINE_SPEC.md`). Implements the Mandatory First Product Workflow. Extends — does not replace — `workflows/01-new-product-workflow/WORKFLOW.md` and `skills/01-discovery-skill/SKILL.md` (see the additive cross-references added to both in this phase, and `docs/architecture/adr/ADR-006-idea-discovery-first-workflow.md`).

Every state follows the 13-field contract. `FAILED` and `RETRY_PENDING` are reused from `../../STATE_REGISTRY.md` unchanged — any state below may transition into them per the generic engine's rules; they are not redefined here.

**Enforces at the structural level:** Constitution Principle 2 (Problem Before Solution) and Principle 3 (Research Before Reinvention) — this registry makes it structurally impossible to reach `DECISION_GATE` without first passing through existing/adjacent/historical-attempt discovery.

---

## IDEA_RECEIVED

- **Purpose:** Entry state. Captures the raw idea/problem/goal as given, unfiltered.
- **Entry Conditions:** A run has been created (see `../../ENGINE_SPEC.md`) with a non-empty idea statement.
- **Required Inputs:** `idea_statement` (the raw input, verbatim).
- **Actions:** Record the idea statement in `run-state.md` exactly as given — no reframing yet.
- **Allowed Capabilities:** None beyond recording.
- **Output Schema:** `idea_statement` field populated.
- **Exit Conditions:** Idea statement is non-empty.
- **Failure Conditions:** Idea statement is empty or unintelligible.
- **Retry Policy:** Immediate retry with a corrected statement; no limit.
- **Possible Next States:** `IDEA_CLARIFICATION`, `FAILED`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## IDEA_CLARIFICATION

- **Purpose:** Resolve ambiguity in the raw idea before framing it as a problem — per Meta-Agent's existing "ask only critical clarification questions" principle (`meta-agent/META_AGENT.md`).
- **Entry Conditions:** `IDEA_RECEIVED` completed.
- **Required Inputs:** The recorded idea statement.
- **Actions:** Identify missing critical inputs (who has this problem, how do we know, what's assumed vs. known); ask the human only if the gap would otherwise make later states pure guesswork, per Constitution Principle 1 (Goal First) — otherwise state the assumption and proceed, matching the Meta-Agent's existing default.
- **Allowed Capabilities:** May invoke `01-discovery-skill`'s clarification questions.
- **Output Schema:** `clarified_idea` (idea statement plus explicit assumptions where no question was asked).
- **Exit Conditions:** Idea is specific enough to frame a problem statement from.
- **Failure Conditions:** Critical ambiguity remains unresolved after a reasonable clarification attempt.
- **Retry Policy:** Up to 2 retries (re-ask/re-clarify); then `FAILED`.
- **Possible Next States:** `PROBLEM_FRAMING`, `RETRY_PENDING`, `FAILED`
- **Human Approval Requirement:** None (clarifying questions are not approval gates).
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## PROBLEM_FRAMING

- **Purpose:** Separate the real problem, the human's assumed solution, and the desired outcome — Constitution Principle 2, structurally enforced (the state's Output Schema requires all three fields distinctly, so they cannot be collapsed into one).
- **Entry Conditions:** `IDEA_CLARIFICATION` completed.
- **Required Inputs:** `clarified_idea`.
- **Actions:** Run `01-discovery-skill`'s problem-statement work; explicitly separate "what the human asked for" from "the underlying problem" from "the outcome that would count as success."
- **Allowed Capabilities:** May invoke CPO-Agent's `01-discovery-skill`.
- **Output Schema:** `problem_statement`, `assumed_solution` (may be null if the human only stated a problem), `desired_outcome`.
- **Exit Conditions:** All three fields populated (assumed_solution may be explicitly "none stated").
- **Failure Conditions:** Cannot separate problem from solution from the given input even after clarification.
- **Retry Policy:** 1 retry looping back to `IDEA_CLARIFICATION` for more input; then `FAILED`.
- **Possible Next States:** `DISCOVERY_PLAN`, `IDEA_CLARIFICATION` (backward loop), `FAILED`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** May read `memory/product-memory.md` for prior related framing.
- **Memory Write Policy:** None.

## DISCOVERY_PLAN

- **Purpose:** Decide what needs to be researched before any solution is proposed — the explicit plan for the three discovery states that follow, per Constitution Principle 3.
- **Entry Conditions:** `PROBLEM_FRAMING` completed.
- **Required Inputs:** `problem_statement`.
- **Actions:** Enumerate what existing-solution, adjacent-solution, and historical-attempt research is actually needed for this specific problem (not a generic checklist).
- **Allowed Capabilities:** May invoke `02-market-research-skill`, `15-framework-library-skill`.
- **Output Schema:** `discovery_plan` (a short, specific research agenda for the next three states).
- **Exit Conditions:** Plan names at least one concrete thing to check in each of the three upcoming discovery states.
- **Failure Conditions:** No researchable questions can be identified (rare — usually indicates `PROBLEM_FRAMING` was too vague and should be revisited).
- **Retry Policy:** 1 retry looping back to `PROBLEM_FRAMING`; then `FAILED`.
- **Possible Next States:** `EXISTING_SOLUTION_DISCOVERY`, `PROBLEM_FRAMING` (backward loop), `FAILED`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## EXISTING_SOLUTION_DISCOVERY

- **Purpose:** Research existing products/competitors that already address this problem — Constitution Principle 3's first, most direct check.
- **Entry Conditions:** `DISCOVERY_PLAN` completed.
- **Required Inputs:** `discovery_plan`.
- **Actions:** Invoke `02-market-research-skill` (routed through `../../orchestration/STATE_TO_CAPABILITY_ROUTING.md`, Phase 5); for every claim produced, classify it per `../../evidence/EVIDENCE_LEDGER_CONTRACT.md`'s canonical vocabulary and append it to this run's `evidence-ledger.md` (Phase 4's formal ledger, superseding Phase 3's provisional `evidence.md` pattern referenced below).
- **Allowed Capabilities:** May invoke `02-market-research-skill`; may append to this run's own `evidence-ledger.md` only (never `memory/*.md` directly).
- **Output Schema:** `existing_solutions` (list of found solutions, each with a classified evidence entry).
- **Exit Conditions:** At least a genuine attempt at existing-solution research is recorded, even if the answer is "none found."
- **Failure Conditions:** Research capability unavailable (e.g. no live web access and no prior knowledge sufficient).
- **Retry Policy:** 1 retry with a narrower research question; then proceed with `existing_solutions: none found, low confidence` rather than blocking indefinitely — matches the Meta-Agent's existing "default to assumption over stalling" principle.
- **Possible Next States:** `ADJACENT_SOLUTION_DISCOVERY`, `RETRY_PENDING`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** May read `memory/market-memory.md`.
- **Memory Write Policy:** None (writes only to this run's `evidence-ledger.md`).

## ADJACENT_SOLUTION_DISCOVERY

- **Purpose:** Research substitutes, manual workarounds, and adjacent-category solutions — the second Constitution Principle 3 check, broader than direct competitors.
- **Entry Conditions:** `EXISTING_SOLUTION_DISCOVERY` completed.
- **Required Inputs:** `existing_solutions`.
- **Actions:** Same as `EXISTING_SOLUTION_DISCOVERY`'s Actions, scoped to substitutes/workarounds/adjacent tools instead of direct competitors.
- **Allowed Capabilities:** Same as `EXISTING_SOLUTION_DISCOVERY`.
- **Output Schema:** `adjacent_solutions` (list, each with a classified evidence entry).
- **Exit Conditions:** Same pattern as `EXISTING_SOLUTION_DISCOVERY`.
- **Failure Conditions:** Same pattern.
- **Retry Policy:** Same pattern.
- **Possible Next States:** `HISTORICAL_ATTEMPT_DISCOVERY`, `RETRY_PENDING`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** May read `memory/market-memory.md`.
- **Memory Write Policy:** None.

## HISTORICAL_ATTEMPT_DISCOVERY

- **Purpose:** Check whether this problem was already attempted before (internally or by others) and failed — Constitution Principle 3's third check, the one most often skipped without an explicit gate.
- **Entry Conditions:** `ADJACENT_SOLUTION_DISCOVERY` completed.
- **Required Inputs:** `adjacent_solutions`.
- **Actions:** Check `memory/lessons-learned.md` and `memory/decision-log.md` for prior related attempts; ask the human directly if internal history isn't captured in memory; classify and record findings the same way as the two prior discovery states.
- **Allowed Capabilities:** May read `memory/lessons-learned.md`, `memory/decision-log.md`; may append to `evidence-ledger.md`.
- **Output Schema:** `historical_attempts` (list, each with a classified evidence entry, or explicitly "none found").
- **Exit Conditions:** Same pattern as the prior two discovery states.
- **Failure Conditions:** Same pattern.
- **Retry Policy:** Same pattern.
- **Possible Next States:** `EVIDENCE_SYNTHESIS`, `RETRY_PENDING`
- **Human Approval Requirement:** None.
- **Memory Read Policy:** `memory/lessons-learned.md`, `memory/decision-log.md`.
- **Memory Write Policy:** None (writes only to `evidence-ledger.md`).

## EVIDENCE_SYNTHESIS

- **Purpose:** Combine the three discovery states' findings into one coherent picture before showing it to the human — Constitution Principle 5 (Evidence Before Confidence) and Principle 6 (Critique Before Approval) applied together.
- **Entry Conditions:** `HISTORICAL_ATTEMPT_DISCOVERY` completed.
- **Required Inputs:** `existing_solutions`, `adjacent_solutions`, `historical_attempts`, this run's full `evidence-ledger.md`.
- **Actions:** Synthesize findings into a draft Idea Discovery Brief (see `IDEA_DISCOVERY_BRIEF_TEMPLATE.md`); run `critic-agent/CRITIC_AGENT.md` over the draft, checking specifically that every claim carries a classification label per ADR-003 ("treat an unlabeled claim as a finding on its own").
- **Allowed Capabilities:** May invoke `critic-agent/CRITIC_AGENT.md`.
- **Output Schema:** `idea_discovery_brief_draft` (full brief per the template) + `critic_findings`.
- **Exit Conditions:** Draft brief exists and has been critiqued; any blocking Critic red flag has been addressed or explicitly carried forward as a stated risk.
- **Failure Conditions:** The evidence is too thin to synthesize into any coherent brief.
- **Retry Policy:** 1 retry looping back to `DISCOVERY_PLAN` for a narrower/deeper pass; then `FAILED`.
- **Possible Next States:** `USER_EVIDENCE_REVIEW`, `DISCOVERY_PLAN` (backward loop), `FAILED`
- **Human Approval Requirement:** None yet — this is preparation for the human review in the next state.
- **Memory Read Policy:** `memory/lessons-learned.md` (for Critic's pattern-check).
- **Memory Write Policy:** None.

## USER_EVIDENCE_REVIEW

- **Purpose:** Present the synthesized evidence to the human before any further product design — the workflow's core anti-premature-building gate.
- **Entry Conditions:** `EVIDENCE_SYNTHESIS` completed.
- **Required Inputs:** `idea_discovery_brief_draft`, `critic_findings`.
- **Actions:** Present the draft brief and Critic findings plainly; do not proceed to design anything further in this turn.
- **Allowed Capabilities:** None beyond presentation.
- **Output Schema:** N/A — this state's output is the presentation itself, consumed by the human.
- **Exit Conditions:** The brief and findings have been presented.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A.
- **Possible Next States:** `WAITING_FOR_USER_EXPERIENCE`
- **Human Approval Requirement:** Entering this state IS the trigger for the human-input wait that follows.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## WAITING_FOR_USER_EXPERIENCE

- **Purpose:** Pause state — wait for the human's real-world experience, constraints, or reaction to the evidence, per the mission's explicit "Receive Human Experience and Constraints" step. This is the required pause before deeper product design (this phase's completion gate).
- **Entry Conditions:** `USER_EVIDENCE_REVIEW` completed.
- **Required Inputs:** None — this state performs no work; it waits.
- **Actions:** None.
- **Allowed Capabilities:** None.
- **Output Schema:** N/A.
- **Exit Conditions:** A human response has been recorded in `approvals.md`.
- **Failure Conditions:** N/A — may remain paused indefinitely, across sessions, per `../../ENGINE_SPEC.md`'s resume protocol.
- **Retry Policy:** N/A.
- **Possible Next States:** `USER_EXPERIENCE_INTEGRATION`, `ARCHIVED` (human declines to continue at all)
- **Human Approval Requirement:** Leaving this state requires the recorded human response.
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## USER_EXPERIENCE_INTEGRATION

- **Purpose:** Fold the human's actual experience/constraints/reaction into the brief before the decision gate — the human's input is not just logged, it changes the brief.
- **Entry Conditions:** `WAITING_FOR_USER_EXPERIENCE` completed with a response that isn't a full decline.
- **Required Inputs:** The recorded human response.
- **Actions:** Revise the draft brief with the human's input; flag any place the human's experience contradicts the research findings, per Constitution Principle 6.
- **Allowed Capabilities:** None beyond revising the brief.
- **Output Schema:** `idea_discovery_brief` (final, revised — no longer "draft").
- **Exit Conditions:** Brief reflects the human's input and any contradictions are explicitly flagged, not silently resolved.
- **Failure Conditions:** Human input directly invalidates the problem framing itself (rare — usually means looping back further).
- **Retry Policy:** 1 retry looping back to `PROBLEM_FRAMING` if the human's input reframes the problem entirely; then proceed anyway with the reframing noted.
- **Possible Next States:** `DECISION_GATE`, `PROBLEM_FRAMING` (backward loop)
- **Human Approval Requirement:** None additional (already satisfied entering this state).
- **Memory Read Policy:** None.
- **Memory Write Policy:** None.

## DECISION_GATE

- **Purpose:** The terminal decision point — commits to one of six explicit outcomes rather than defaulting to "build it."
- **Entry Conditions:** `USER_EXPERIENCE_INTEGRATION` completed.
- **Required Inputs:** `idea_discovery_brief` (final).
- **Actions:** Evaluate the final brief against the six possible outcomes; select one and state why, with the alternatives considered, per Constitution Principle 8 (Traceability). Where the choice is non-trivial or high-stakes, invoke `59-problem-solving-decision-modeling-skill` for the decision packet rather than deciding on unexamined intuition, matching `workflows/01-new-product-workflow/WORKFLOW.md`'s existing Validation section.
- **Allowed Capabilities:** May invoke `59-problem-solving-decision-modeling-skill`.
- **Output Schema:** `decision_gate_outcome` — one of `USE_EXISTING | ADAPT_EXISTING | COMBINE_SOLUTIONS | CONTINUE_NEW_PRODUCT_DISCOVERY | PAUSE_FOR_VALIDATION | REJECT_OR_ARCHIVE`, plus reasoning, alternatives considered, and remaining assumptions.
- **Exit Conditions:** An outcome has been selected and justified.
- **Failure Conditions:** The brief is insufficient to select any outcome responsibly.
- **Retry Policy:** 1 retry looping back to `USER_EVIDENCE_REVIEW` for more human input; then `FAILED`.
- **Possible Next States:** `COMPLETED` (for `USE_EXISTING`, `ADAPT_EXISTING`, `COMBINE_SOLUTIONS`, `CONTINUE_NEW_PRODUCT_DISCOVERY`), `WAITING_FOR_USER_EXPERIENCE` (for `PAUSE_FOR_VALIDATION` — loops back to wait for more validation), `ARCHIVED` (for `REJECT_OR_ARCHIVE`), `FAILED`
- **Human Approval Requirement:** The outcome itself is a recommendation per Constitution Principle 7 (Human Authority) — real product-design work downstream (outside this workflow's scope) should not begin without the human separately approving that next step; this state records the recommendation, not a fabricated go-ahead.
- **Memory Read Policy:** `memory/decision-log.md` (for consistency with prior related decisions).
- **Memory Write Policy:** None directly — promotion to `memory/decision-log.md` happens via the Decision Engine (Phase 4) and Reflection path (Phase 7), not written here.

## ARCHIVED

- **Purpose:** Terminal state — the idea is explicitly not being pursued right now (either `REJECT_OR_ARCHIVE` from `DECISION_GATE`, or an outright decline at `WAITING_FOR_USER_EXPERIENCE`).
- **Entry Conditions:** Reached only from `DECISION_GATE` or `WAITING_FOR_USER_EXPERIENCE` with an explicit human-backed reason.
- **Required Inputs:** The reason for archiving.
- **Actions:** Record the final brief (or draft) and the reason for archiving, so it can be found again if revisited later — never silently deleted.
- **Allowed Capabilities:** None beyond the closing write.
- **Output Schema:** `run-state.md`'s `Final Output` populated with the archived brief and reason.
- **Exit Conditions:** N/A — terminal.
- **Failure Conditions:** N/A.
- **Retry Policy:** N/A.
- **Possible Next States:** none (terminal).
- **Human Approval Requirement:** Already satisfied (archiving is itself a human-backed decision).
- **Memory Read Policy:** None.
- **Memory Write Policy:** None directly — a future reflection pass may promote "why this was archived" as a lesson via the proper Phase 7 path.

---

## Reachability Check

`IDEA_RECEIVED` → `IDEA_CLARIFICATION` → `PROBLEM_FRAMING` → `DISCOVERY_PLAN` → `EXISTING_SOLUTION_DISCOVERY` → `ADJACENT_SOLUTION_DISCOVERY` → `HISTORICAL_ATTEMPT_DISCOVERY` → `EVIDENCE_SYNTHESIS` → `USER_EVIDENCE_REVIEW` → `WAITING_FOR_USER_EXPERIENCE` → `USER_EXPERIENCE_INTEGRATION` → `DECISION_GATE` → {`COMPLETED` | `WAITING_FOR_USER_EXPERIENCE` | `ARCHIVED` | `FAILED`}. Every state is reachable from `IDEA_RECEIVED`; backward loops (`PROBLEM_FRAMING`, `DISCOVERY_PLAN`, `IDEA_CLARIFICATION`) all point to states already reachable forward. No orphan states. Terminal states: `ARCHIVED`, `COMPLETED` (reused from the generic registry), `FAILED` (reused).

## Evidence Note (Formalized in Phase 4, Routed Through Orchestration in Phase 5)

Each run's `evidence-ledger.md` (append-only, same pattern as `state-history.md`/`approvals.md`) holds classified claims per `../../evidence/EVIDENCE_LEDGER_CONTRACT.md`'s canonical vocabulary, scored per `../../evidence/SOURCE_QUALITY_RULES.md`. Agent calls that produce evidence are routed through `../../orchestration/STATE_TO_CAPABILITY_ROUTING.md`. (Historical note: Phase 3 originally used a provisional, unscored `evidence.md` file for the demo run before Phase 4 formalized the schema — see `runs/idea-discovery-demo-0001/evidence.md` vs. `evidence-ledger.md` for both versions, kept side by side rather than deleted.)
