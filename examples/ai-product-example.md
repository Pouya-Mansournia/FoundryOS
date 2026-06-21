# Example: Shipping an AI Product Feature

**Prompt:** *"We want to ship an AI feature that auto-drafts customer support replies from past ticket history. Help us plan it."*

This example illustrates the AI-product use case for an early-stage SaaS company; substitute your own product context.

---

## Meta-Agent Result

### 1. Request Classification
Product + Technology (AI feature), with a strategic-fit check — multi-agent.

### 2. Selected Agents
`CPO-Agent` → `CTO-Agent` → `CEO-Agent` (alignment check, runs in parallel rather than blocking)

### 3. Selected Skills
- `01-discovery-skill` (CPO-Agent) — who is this for, what job does it replace
- `04-prd-skill` (CPO-Agent) — structure the feature as a PRD
- `21-ai-product-skill` (CTO-Agent) — data/model/evaluation strategy
- `31-ai-architecture-skill` (CTO-Agent) — RAG/MLOps design, safety plan
- `12-company-bible-skill` (CEO-Agent) — confirm fit with stated product identity

### 4. Agent Execution Order
CPO-Agent → CTO-Agent → CEO-Agent (alignment check on the combined output)

### 5. Combined Executive Answer

**Problem framing (CPO):** Support agents spend most of their handle time re-writing the same 30–40 answers with minor variation. The job to be done isn't "generate text," it's "cut average handle time without lowering CSAT." That's the metric the feature should be judged on, not draft quality in isolation.

**Scope (CPO → PRD):** v1 ships as a *draft assist*, not autosend — the agent reviews and edits before the reply goes out. This buys trust and a feedback loop (edited vs. accepted drafts) before any unsupervised mode is considered. Success metric: ≥30% reduction in average handle time on tickets where a draft was offered, with CSAT held flat or better.

**Data & model strategy (CTO):** Ground every draft in retrieval over the company's own closed tickets (RAG over the last 12–18 months, filtered to resolved/CSAT ≥4 tickets only — don't retrieve from bad outcomes). Start with a general-purpose model behind the retrieval layer rather than fine-tuning; fine-tuning is a v2 decision once there's an edit-distance dataset to train on. Evaluation harness: a held-out set of real tickets scored on factual grounding (did the draft reference real account/order data correctly) before anything else — hallucinated account details are the failure mode that kills trust fastest in support.

**AI architecture (CTO):** RAG pipeline with a strict citation requirement — every factual claim in a draft must trace to a specific retrieved ticket or account record, or the system should leave that line as a placeholder rather than guess. Log every draft, every edit, and every accept/reject as training signal for v2. Add a confidence gate: low-retrieval-confidence tickets don't get a draft at all rather than getting a bad one — silence is a better failure mode than a wrong answer here.

**Strategic fit (CEO):** Checked against the company's stated identity as a tool that makes support teams faster without replacing their judgment — the draft-assist framing (human-in-the-loop, not autosend) is consistent with that. Flag for the team: don't let v2 autosend ambitions creep into v1 messaging to customers: ship the trust-building version first.

### 6. Contradictions / Conflicts
None identified — CPO's "human-in-the-loop v1" and CTO's "confidence gate over guessing" reinforce the same trust-first posture.

### 7. Missing Inputs / Assumptions
- Assumed the company's support tool already has structured ticket history with resolution/CSAT tags. If tickets are unstructured free text only, add a tagging/cleanup pass before the RAG pipeline can be trusted.
- Assumed a single support product surface (not multi-product, multi-language). Multi-language support would change the retrieval and evaluation design materially — flag if that's in scope.

### 8. Risks
- Hallucinated account specifics (wrong order numbers, wrong dates) is the single highest-severity risk — mitigated by the citation-required design above, but worth a manual red-team pass before launch.
- Agent over-trust: if drafts are good 90% of the time, agents may stop reading the other 10% carefully. Track edit rate over time as an early-warning signal, not just acceptance rate.

### 9. Next Actions
1. Pull and tag 12–18 months of resolved tickets with CSAT ≥4 as the retrieval corpus (CPO + CTO, this week).
2. Build the confidence-gated RAG pipeline with citation enforcement (CTO, 2–3 week build).
3. Define the edit-distance logging schema before launch, not after — this is the v2 fine-tuning dataset (CTO).
4. Run a 2-week shadow mode (drafts generated but not shown to agents) to validate factual-grounding rate before any agent-facing launch (CPO + CTO).
