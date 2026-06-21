# Example: Investor Readiness

**Prompt:** *"Make us investor-ready — we're raising a Series A in the next quarter."*

---

## Meta-Agent Result

### 1. Request Classification
Business / Fundraising — multi-agent, the broadest routing pattern in the system.

### 2. Selected Agents
`CEO-Agent` → `CPO-Agent` → `CTO-Agent` (technology-led product; `CIO-Agent` would replace CTO here if the product were hardware/robotics) → `CFO-Agent` → `CRO-Agent`

### 3. Selected Skills
- `12-company-bible-skill`, `13-corporate-os-skill` (CEO-Agent) — vision/governance narrative and board structure
- `27-product-scorecard-skill` (CPO-Agent) — PMF and retention evidence
- `05-architecture-skill` (CTO-Agent) — technical diligence readiness
- `07-finance-skill`, `38-fundraising-investor-skill` (CFO-Agent) — unit economics, data room, pitch narrative
- `08-gtm-skill` (CRO-Agent) — growth motion and pipeline evidence

### 4. Agent Execution Order
CEO-Agent → CPO-Agent → CTO-Agent → CFO-Agent → CRO-Agent

### 5. Combined Executive Answer

**Narrative (CEO):** Series A investors aren't buying the idea anymore — they're buying evidence the idea is working and the team can execute the next stage. The company bible and governance materials should compress into a single, tight strategic narrative: why now, why this team, what's been proven since seed, what the Series A actually buys (specific milestones, not "growth"). Board structure and decision-making process should be presentable in one slide — sloppy governance reads as founder-overload risk to investors.

**Product evidence (CPO):** Lead with the product scorecard, not feature lists. Investors want PMF signal: retention curves (cohort, not blended), NPS or equivalent, and a clear north star metric trend over the last 2–3 quarters. If retention is still noisy, be upfront about why and what's being done — a credible "here's the plan" beats a hidden weak metric that surfaces in diligence anyway.

**Technical diligence readiness (CTO):** Have the system architecture and ADRs (architecture decision records) ready to walk a technical investor or their diligence consultant through in 30 minutes — what's built, what's deliberately not built yet, and why. The single most common Series A technical red flag is an architecture that can't credibly scale 10x without a rewrite; if that's true here, name it and show the plan rather than letting it surface as a surprise.

**Financials (CFO):** Unit economics need to be defensible at the cohort level, not just blended — CAC, LTV, gross margin, and burn multiple by cohort, with the assumptions visible, not buried. Data room should be assembled before the first investor meeting, not during diligence — cap table, financials, customer contracts, IP assignments, and the metrics above, organized and ready. The pitch narrative's "ask" (amount, use of funds, runway it buys) should map directly to milestones the CEO's narrative already promised — a mismatch between the ask and the story is one of the fastest ways to lose investor confidence mid-process.

**Growth evidence (CRO):** Pipeline and CAC-payback data should back up whatever growth claim is in the deck. If the GTM motion is still being figured out, say so explicitly and show the experiments in flight rather than presenting an immature motion as a proven one — sophisticated investors will probe this in the first meeting.

### 6. Contradictions / Conflicts
None identified, but one dependency flagged: CFO's "ask" must be locked only after CEO's milestone narrative and CPO's/CRO's evidence are finalized — building the ask first and the story around it second is a common ordering mistake.

### 7. Missing Inputs / Assumptions
- Assumed a software/SaaS product (CTO-Agent routed for technical diligence). If the product is hardware or robotics, swap in CIO-Agent and add `22-hardware-product-skill` / `41-mechatronics-skill` to diligence prep — hardware diligence focuses on BOM cost curves and manufacturing readiness, not just software architecture.
- Assumed this is a priced equity round, not a bridge/SAFE. Bridge rounds compress most of this into a faster, lighter version focused mainly on runway math.
- No current burn rate, runway, or retention numbers were provided — the financial and product sections above describe what to prepare, not a verdict on whether the company is currently fundable. Provide actuals for a real assessment.

### 8. Risks
- The most common reason a "ready" deck still fails diligence is a metrics mismatch between the pitch and the data room — same metric, different number, different slide. Reconcile every number across both before the first meeting.
- Governance gaps (no real board cadence, informal cap table management) are a disproportionately large red flag relative to their actual operational importance — fix the appearance and the substance together.

### 9. Next Actions
1. Lock the one-paragraph strategic narrative and the specific milestone set the raise funds (CEO, this week).
2. Pull cohort retention and unit economics with assumptions documented, not just headline numbers (CPO + CFO).
3. Assemble the data room now, before the first investor meeting, not in response to a diligence request (CFO).
4. Reconcile every metric that appears in both the deck and the data room (CFO + CPO + CRO, final pass before outreach starts).
