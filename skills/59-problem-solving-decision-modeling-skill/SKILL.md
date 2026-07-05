# 59 Problem Solving and Decision Modeling Skill

## What this skill does
A reusable **reasoning engine**, not a document template. Frames an ambiguous problem, builds a current-state and causal model before any solution is proposed, decomposes the problem into subproblems, translates goals into a measurable metric tree, engineers falsifiable hypotheses, generates and compares multiple solution options, selects the right reusable quantitative formula(s) for the decision at hand, designs the experiment or validation method, manages uncertainty explicitly, and sequences a staged rollout with rollback conditions. Works the same way across software, AI, robotics, hardware, SaaS, operations, logistics, manufacturing, product, growth, and strategy decisions — it is the discipline other Skills borrow when a decision needs to be made, not a replacement for any of them.

## Source Modules
- 174_Problem_Framing_OS
- 175_Causal_Metric_OS
- 176_Solution_Formula_OS
- 177_Validation_Rollout_OS

## Reference
- `FORMULA_LIBRARY.md` — 29 reusable, domain-neutral quantitative formula families (unit economics, funnels, capacity, reliability, experimentation, prioritization, and more), each with equation, variable definitions, units, assumptions, valid/invalid use, worked example, and common mistakes. Selected from, not dumped wholesale — see `176_Solution_Formula_OS.md`'s Formula Selection Protocol.

## Output
- Decision Statement, Context & Scope, Facts / Assumptions / Unknowns
- Current-State System Model, Problem Decomposition (Problem Tree), Root-Cause & Causal Model
- Objective & Metric Tree (Strategic Objective → Outcome → Driver → Operational → Diagnostic → Guardrail)
- Hypothesis Register (canonical If/Then/Because/While form)
- Solution Options Matrix (impact, confidence, effort, reversibility, opportunity cost)
- Selected Quantitative Model(s), with inputs, assumptions, and sensitivity stated explicitly
- Scenario Analysis (downside / base / upside)
- Experiment or Validation Plan, with stopping rule and rollback trigger
- Recommendation, Risks & Guardrails, Staged Rollout Plan, Instrumentation & Monitoring Plan
- Open Decisions, Confidence Assessment (per claim: fact / calculation / inference / hypothesis / assumption / recommendation)

## Output Modes
Scales with stakes, not a fixed template length:
- **Concise** — small, reversible, low-cost-of-delay decisions. Decision Statement, 1-2 options compared, one formula if relevant, a recommendation.
- **Standard** — normal decisions. Most sections above, sized to what the decision actually needs.
- **Deep** — strategic, irreversible, or high-blast-radius decisions. Full contract in `177_Validation_Rollout_OS.md`'s Output Contract, including scenario/sensitivity analysis and a staged rollout.

## Anti-Patterns This Skill Exists to Prevent
Solution-first reasoning (jumping from symptom to fix without a causal model); a metric with no definition, denominator, or owner; a proxy metric quietly standing in for the real outcome; correlation presented as causation; an average that hides a segment split that would change the decision; double-counted benefits; sunk-cost reasoning; an arbitrary threshold with no stated rationale; false precision on a number nobody actually measured; an ROI claim missing implementation or risk cost; a plan with no guardrail metric; a local optimization that helps one team and quietly harms the system it sits inside. Full list in `177_Validation_Rollout_OS.md`.

## Relationship to Other Skills
This Skill does not replace `04-prd-skill`, `07-finance-skill`, `09-operations-skill`, `28-risk-management-skill`, or any domain Skill — it is the reasoning layer that runs *before* and *alongside* them whenever a request is actually a decision ("should we," "which option," "is this worth it," "why is this happening") rather than a request to produce a known artifact. A PRD, a BOM, or a financial model can be the *output* of a run that used this Skill to get there; this Skill is never itself a PRD generator.
