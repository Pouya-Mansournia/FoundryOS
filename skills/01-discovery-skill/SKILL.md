# 01 Discovery Skill

## What this skill does
Helps define the problem, customer, ICP, persona, JTBD, user journey, and discovery questions.

## Source Modules
- 01_Discovery_OS
- 14_Framework_Library_OS
- 83_Research_OS
- 57_Gap_Analysis_OS
- 56_Contradiction_Detector_OS

## Output
- Problem Statement
- Assumptions
- ICP
- Personas
- JTBD
- User Journey
- Interview Questions
- Opportunity Hypothesis
- Gaps
- Risks

## State-Machine-Backed Variant (FoundryOS Evolution, Phase 3)

This skill's Problem Statement and discovery work are reused (not duplicated) by `runtime/state-machine/workflows/idea-discovery/STATE_REGISTRY.md`'s `PROBLEM_FRAMING` state, extended with an explicit gate requiring existing/adjacent/historical-solution research before any product design proceeds.
