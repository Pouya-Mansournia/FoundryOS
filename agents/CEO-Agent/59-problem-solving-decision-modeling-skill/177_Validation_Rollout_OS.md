# 177_Validation_Rollout_OS

# Role

Act as:
- Experimentation Designer
- Program Manager
- Adversarial Reviewer of Its Own Output

---

# Objective

Design how the decision will actually be validated, sequence a staged rollout that learns before it commits, state uncertainty honestly, and check the whole packet against known reasoning failure modes before calling it done.

---

# Inputs

- Solution Options Matrix and selected formula(s) from `176_Solution_Formula_OS`
- Whatever validation infrastructure already exists (experimentation platform, staging environment, pilot sites, hardware-in-the-loop rigs)

---

# Phase 1 — Experiment and Validation Architecture

Choose the validation mode(s) that fit the decision: historical analysis, cohort analysis, A/B test, switchback test, pilot, simulation, digital twin, shadow mode, offline benchmark, hardware-in-the-loop test, staged rollout, canary deployment, expert review, pre-mortem, postmortem.

For the chosen plan, specify: hypothesis under test, validation method, test population/system, control or baseline, randomization unit, treatment, duration, sample requirement, primary metric, guardrails, stopping rule, rollback trigger, instrumentation, and interpretation rule.

Recommend shadow mode whenever a new decision model can be evaluated without touching production outcomes — it is the lowest-risk validation mode available and is underused relative to how often it applies.

---

# Phase 2 — Prioritization and Staged Rollout

Sequence by dependency and learning order, not arbitrary dates:
1. Define baseline
2. Instrument the system
3. Validate data quality
4. Implement minimum decision logic
5. Run offline or shadow validation
6. Launch a narrow pilot
7. Compare against baseline
8. Tune parameters
9. Expand segments
10. Automate
11. Monitor drift
12. Retire ineffective rules

Each stage needs: objective, dependency, expected learning, decision unlocked, owner, evidence threshold, exit criteria, rollback condition.

---

# Phase 3 — Uncertainty and Evidence Handling

Rate confidence (Very Low / Low / Medium / High / Very High) considering: data relevance, data quality, sample size, recency, causal strength, external validity, model sensitivity, stakeholder agreement.

Label every claim in the final packet as exactly one of: fact, calculation, inference, hypothesis, assumption, recommendation. Expose uncertainty — never smooth it away to sound more confident than the evidence supports.

---

# Phase 4 — Failure Mode Check

Before finalizing, check the packet against: solution-first reasoning; a metric with no definition or denominator; a proxy metric standing in for the real outcome; correlation presented as causation; an average hiding a segment split; double-counted benefits; sunk-cost reasoning; an arbitrary threshold with no rationale; false precision; an ROI claim missing real cost categories; missing guardrails; a local optimization harming the system; incompatible units; stock/flow metrics mixed together; mismatched time windows compared as if equivalent; selection bias; survivorship bias; Simpson's paradox; experiment contamination; overfitting; ignored operational burden or total cost of ownership; roadmap dates stated without dependencies; automation proposed before the underlying process is validated.

---

# Phase 5 — Output Contract

Assemble the final packet, scaled to stakes (concise / standard / deep — see `../SKILL.md`):

1. Decision Statement · 2. Context and Scope · 3. Facts, Assumptions, and Unknowns · 4. Current-State System Model · 5. Problem Decomposition · 6. Root-Cause and Causal Model · 7. Objective and Metric Tree · 8. Hypotheses · 9. Solution Options · 10. Selected Quantitative Models · 11. Scenario and Sensitivity Analysis · 12. Experiment or Validation Plan · 13. Recommendation · 14. Risks and Guardrails · 15. Staged Rollout · 16. Instrumentation and Monitoring · 17. Open Decisions · 18. Confidence Assessment

---

# Deliverables

- Experiment/Validation Plan with stopping rule and rollback trigger
- Staged Rollout Plan with exit criteria per stage
- Confidence Assessment with every claim labeled
- Completed 18-section Output Contract (sized to stakes)

---

# Gate Criteria

Does the plan have a stopping rule and a rollback trigger, not just a launch date? Does every stage have an exit criterion? Was the packet checked against the Phase 4 failure-mode list before being called final?

---

# Recursive Loop

Design Validation
↓
Sequence Rollout
↓
State Uncertainty
↓
Check Against Failure Modes
↓
Assemble Output Contract
↓
Repeat at Next Decision Gate
