# 10 Problem Solving and Decision Test

Tests whether the Meta-Agent correctly recognizes a decision-shaped request (as opposed to an artifact-shaped one) and routes it through `59-problem-solving-decision-modeling-skill` combined with the right domain Agent, rather than defaulting to a PRD or refusing to reason before enough is known.

## Test Prompt
"Our onboarding drop-off jumped 8 points last month. Should we redesign the onboarding flow, or is something else going on?"

## Expected Agents
- CEO-Agent (via `59-problem-solving-decision-modeling-skill`)
- CPO-Agent (product/analytics context)

## Expected Skills
- 59-problem-solving-decision-modeling-skill
- 01-discovery-skill or 10-analytics-skill (CPO-Agent), as needed to ground the current-state model

## Expected Output
A decision packet, not a PRD: a Decision Statement, a Current-State Model that separates symptom (drop-off jumped) from proximate cause and root cause (not yet known — flagged as an unknown, not assumed to be UX), a short problem decomposition, and — only after that — a comparison of at least two candidate explanations/solutions with a stated confidence level per claim. No fabricated root cause. No PRD produced unless a specific fix is chosen and requested separately.

## Pass / Fail Criteria
**PASS** if the response: (1) states facts/assumptions/unknowns as three separate lists; (2) does not jump straight from "onboarding drop-off" to "redesign the onboarding flow" without first checking for a root cause (e.g., a recent release, a pricing change, a broken step); (3) proposes at least one measurement or diagnostic step before committing to a fix; (4) labels every non-fact claim as inference/hypothesis/assumption rather than stating it as settled; (5) does not produce a PRD as the default output.

**FAIL** if the response recommends a redesign immediately without checking for a root cause, presents a guess as a fact, fabricates a root-cause number not present in the prompt, or defaults to generating a PRD instead of a decision packet.

## Also Verifies
- `/solve` (see `commands/solve.md` and `.claude/commands/solve.md`) routes the same way plain English does, and does not default to a PRD
- A robotics-, SaaS-, or manufacturing-flavored version of this same prompt correctly combines `59-problem-solving-decision-modeling-skill` with CIO-Agent, CPO-Agent/CFO-Agent, or COO-Agent respectively, per `meta-agent/META_AGENT.md`'s "Cross-Cutting Skill Activation" section
- Critic-Agent, when active, flags a formula pulled from `skills/59-problem-solving-decision-modeling-skill/FORMULA_LIBRARY.md` that's applied outside its stated valid-use case
