# Example: Problem Solving and Decision Modeling

Three short, worked decisions using `59-problem-solving-decision-modeling-skill`, triggered by `/solve` or `11-problem-solving-decision-workflow`. Each shows the reasoning and formula selection this Skill exists to produce — not a fabricated number, and not a PRD. Substitute your own numbers; the point is the method, not these specific figures.

---

## A — AI Infrastructure: Self-Host or Use a Managed Inference API?

**Prompt:** *"Should we self-host our model's inference or stay on a managed inference API?"*

### 1. Request Classification
Technology/cost decision with a TCO and capacity trade-off — multi-agent.

### 2. Selected Agents
`CEO-Agent` (decision framing) → `CTO-Agent` (AI architecture feasibility) → `CFO-Agent` (TCO)

### 3. Selected Skills
- `59-problem-solving-decision-modeling-skill` (CEO-Agent) — problem framing, TCO/break-even formula selection
- `31-ai-architecture-skill` (CTO-Agent) — hosting/MLOps feasibility

### 4. Combined Executive Answer

**Decision Statement:** Choose the inference hosting strategy (self-hosted infrastructure vs. a managed inference API) for a production AI feature at current and projected request volume.

**Current-State Model:** The symptom prompting this question is rising per-request inference cost on the managed API at current volume. Root cause isn't yet established — confirm this isn't actually a prompt/context-length efficiency problem before treating it as a hosting decision; switching infrastructure won't fix an inefficient request pattern.

**Options Compared:** (1) do nothing — stay on the managed API; (2) self-host on owned or rented GPU infrastructure; (3) hybrid — self-host baseline load, burst to the managed API for peaks; (4) stay managed but move to a smaller or distilled model.

**Selected Quantitative Models** (from `FORMULA_LIBRARY.md`):
- **Cost per Unit / Cost per Outcome (§8):** Cost per inference under each option, matched to the actual request-volume distribution — check p95 traffic bursts, not just the average, since averages hide the peak that actually drives infrastructure sizing.
- **Total Cost of Ownership (§27):** Self-hosting adds Infrastructure + Maintenance + Support (on-call ML-infra coverage) that the managed API's per-request price already absorbs — the most commonly under-counted term in this comparison.
- **Break-Even Volume (§4):** Compute the request volume at which self-hosting's fixed infrastructure cost crosses below the managed API's per-request cost — don't decide off today's volume alone if it's still growing.
- **Capacity Utilization / Headroom (§15):** Self-hosted GPU capacity sitting idle off-peak is a real cost the managed API doesn't carry — factor utilization rate into the effective cost-per-inference, not nameplate GPU cost.

**Recommendation:** Run the break-even calculation against actual current and projected volume before committing; if volume is still below break-even and growing, hold on the managed API and revisit next quarter against actual (not projected) volume.

### 5. Missing Inputs / Assumptions
Assumed request-volume data exists at the p95 level, not just an average. On-call/maintenance staffing cost for self-hosting not yet provided — the TCO comparison is directional, not final, until it is.

### 6. Risks
Migrating to self-hosted infrastructure while underestimating the on-call/maintenance burden (the most commonly dropped TCO term per `FORMULA_LIBRARY.md` §27); committing to self-hosting based on projected volume that doesn't materialize.

### 7. Confidence Assessment
Break-even volume: **calculation**, contingent on the cost inputs provided (labeled explicitly, not fabricated). On-call/maintenance burden: **assumption**, needs a real staffing-cost input before finalizing. Recommendation: **recommendation**, not yet a decision — needs the break-even data run against real volume.

---

## B — SaaS: Introduce a Usage-Based Pricing Tier?

**Prompt:** *"Should our SaaS product introduce a usage-based tier alongside our flat monthly plan?"*

### Selected Agents
`CEO-Agent` (`59-problem-solving-decision-modeling-skill`) → `CPO-Agent` (segmentation) → `CFO-Agent` (unit economics) → `CRO-Agent` (churn/GTM guardrail)

### Combined Executive Answer

**Decision Statement:** Decide whether to add a usage-based tier next to the existing flat plan, and if so, where to set the threshold.

**Metric Tree:** Strategic Objective (grow revenue without eroding margin) → Outcome Metric (net revenue per account) → Driver Metric (conversion into the new tier) → Operational Metric (cost-to-serve per usage unit) → Guardrail Metric (churn rate, held flat or better).

**Hypothesis:** If we add a usage-based tier for accounts above the current flat-plan's typical usage ceiling, then net revenue per account in that segment will increase by 15-25% within two billing cycles, because high-usage accounts are currently under-monetized relative to their infrastructure cost, while guardrail churn stays within ±1pt of baseline.

**Selected Quantitative Models:**
- **Unit Economics (§4) / Break-Even Volume:** Confirm `Unit Contribution` stays positive at the tier's lowest usage band — a common mistake is pricing the entry point of a usage tier below cost-to-serve.
- **Funnel Model (§6):** Model conversion from flat-plan to usage-tier separately from new-signup conversion — mixing the two funnels hides whether the tier cannibalizes existing accounts or grows the pie.
- **Threshold Decision Rule (§12):** The usage threshold itself needs stated rationale (e.g., set at the 80th percentile of current flat-plan usage) and a review cadence — not a number picked because it "felt right."

**Experiment Design:** A/B test or switchback across a segment of high-usage flat-plan accounts, with churn as the explicit guardrail and a stopping rule (halt rollout if churn moves more than 1pt against baseline).

**Recommendation:** Ship as an opt-in tier to the top-usage decile first (lowest blast radius), with the threshold review built into the 90-day check-in, not set-and-forget.

### Risks
Threshold set from intuition rather than the stated percentile rationale; cost-to-serve not actually measured, only assumed flat across usage bands (it usually isn't).

### Confidence Assessment
Revenue-lift magnitude (15-25%): **hypothesis**, not yet a calculation — falsifiable via the A/B test above. Cost-to-serve flatness: **assumption**, flagged for validation before the threshold is finalized.

---

## C — Manufacturing: Automate a Manual Inspection Step?

**Prompt:** *"Should we automate a manual visual inspection step on our production line?"*

### Selected Agents
`CEO-Agent` (`59-problem-solving-decision-modeling-skill`) → `COO-Agent` (operations) → `CIO-Agent` (automation feasibility) → `CFO-Agent` (payback)

### Combined Executive Answer

**Current-State Model:** Manual inspection currently catches defects at a known First Pass Yield; the symptom prompting this question is inspector fatigue late in shifts — establish whether the real problem is inspection capability or inspection capacity before assuming automation is the fix.

**Selected Quantitative Models:**
- **Quality and Yield (§18):** `First Pass Yield`, `Defect Rate`, `Rolled Throughput Yield` — baseline these before automating, so the "after" comparison isn't measured against an already-stale assumption.
- **Throughput / Cycle Time (§16):** Automated inspection's cycle-time change affects line throughput; check it doesn't just relocate the bottleneck downstream.
- **Total Cost of Ownership (§27) / Payback Period (§10):** `TCO` for the automated system (Acquisition + Integration + Maintenance + Downtime during cutover) against `Payback Period = Initial Investment / Periodic Net Benefit`, where the benefit is reduced false-accept cost (escaped defects) plus reduced labor cost, not labor cost alone.
- **False accept / false reject framing:** An automated inspector's false-reject rate (good units scrapped) has a real cost too — don't optimize only for catching more defects if it also scraps more good product.

**Recommendation:** Stage as EVT-style validation: run the automated inspector in shadow mode alongside human inspectors for one production run, compare false-accept/false-reject rates and cycle time against baseline, before removing the human step.

### Risks
Automating before the underlying process (why defects occur in the first place) is understood — automation validates faster inspection, not fewer defects. TCO omitting maintenance and downtime during cutover, the most commonly dropped terms per `FORMULA_LIBRARY.md` §27.

### Confidence Assessment
Baseline yield figures: **fact**, if measured; **assumption**, if estimated — label whichever is true before presenting the payback calculation. Payback period: **calculation**, contingent on the shadow-mode data confirming the assumed false-accept/false-reject rates.
