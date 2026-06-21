# 04 AI Product Workflow

## Purpose
Take an AI/ML feature from a stated job-to-be-done to a data strategy, model architecture, and evaluation plan that can be trusted before it ships — the default path whenever the core deliverable is a model, not just a UI on top of one.

## Inputs
- The job the AI feature replaces or augments, and the metric it should move
- What data exists today (volume, structure, quality, labels) to ground or train on
- Whether the feature runs purely in the cloud or partly on embedded/edge hardware
- Risk tolerance for the failure mode (a wrong suggestion vs. a wrong medical/safety-critical output are very different bars)

## Meta-Agent
Classified as **technology** with an AI-specific sub-path. CIO-Agent is **conditional**, not default: it only joins if the feature runs on embedded or edge hardware (on-device inference, sensor fusion). For a cloud-only AI feature, CTO-Agent alone covers data, model, and evaluation strategy — the Meta-Agent should state explicitly whether CIO-Agent was included or excluded and why, rather than defaulting either way.

## Agent Execution Order
```
Meta-Agent
   ↓
CPO-Agent     (job to be done, PRD scope)
   ↓
CTO-Agent     (data/model/evaluation strategy, AI architecture)
   ↓
CBO-Agent     (AI voice, persona, output copy — how the feature talks to users)
   ↓
CIO-Agent     (only if on-device/edge inference is in scope)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CPO-Agent | `01-discovery-skill`, `04-prd-skill` |
| CTO-Agent | `21-ai-product-skill`, `31-ai-architecture-skill`, `30-data-architecture-skill` |
| CBO-Agent | `53-voice-tone-skill`, `52-copywriting-skill` |
| CIO-Agent *(conditional)* | `32-embedded-skill` — only if inference runs on hardware CIO-Agent owns |

## Artifacts Produced
PRD scoped to a measurable job-to-be-done, Data Strategy (sourcing, labeling, retrieval), AI/MLOps Architecture, AI Voice & Persona Guide, Output Copy Templates, Evaluation Harness & Metrics, Safety/Guardrail Plan, Roadmap (v1 assisted → v2 autonomous, if applicable), Risk Register.

## Validation
`14-validation-skill` (COO-Agent) checks that the evaluation metric actually measures the job-to-be-done stated in the PRD — the most common AI-product failure is optimizing a proxy metric (draft quality) instead of the real one (handle time, conversion, safety). If `critic-agent/` is active, run it specifically against hallucination/failure-mode risk before any user-facing launch.

## Risks
- Shipping without a held-out evaluation set, so "it looks good in the demo" stands in for real measurement
- No confidence gate — the system guesses on low-confidence inputs instead of abstaining
- Treating fine-tuning as a v1 decision when a retrieval/grounding layer over a general-purpose model would de-risk launch faster
- The feature's tone and how it communicates uncertainty left to whatever the model defaults to, instead of a CBO-Agent-defined persona — inconsistent AI voice erodes trust faster than a wrong answer does

## Final Outputs
One merged plan: PRD → Data Strategy → AI Architecture → Voice & Persona → Evaluation Metrics → Roadmap → Risks, with the evaluation metric traced back explicitly to the PRD's stated job-to-be-done.

## Example Prompt
*"We want to add an AI feature that drafts responses from historical data — help us plan the data strategy, model approach, and how we'd know it's working before launch."*
