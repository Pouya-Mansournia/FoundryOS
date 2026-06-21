# Example: Team Scaling & Org Design at 15 People

**Prompt:** *"We just crossed 15 people and hiring is starting to feel chaotic — help us design the org structure, set up a real hiring system, and figure out what culture and operating cadence should look like at this stage."*

---

## Meta-Agent Result

### 1. Request Classification
Business / Company operating system — multi-agent (the company-building sub-case: CEO + COO + CHRO + CBO + CFO).

### 2. Selected Agents
`CEO-Agent` → `COO-Agent` → `CHRO-Agent` → `CBO-Agent` → `CFO-Agent`

### 3. Selected Skills
- `13-corporate-os-skill`, `12-company-bible-skill`, `19-raci-meeting-skill` (CEO-Agent) — org structure, governance, ownership
- `09-operations-skill`, `16-artifact-template-skill` (COO-Agent) — operating cadence, SOPs
- `39-people-culture-skill` (CHRO-Agent) — hiring system, leveling, performance, culture
- `53-voice-tone-skill`, `51-storytelling-skill` (CBO-Agent) — employer brand and internal narrative
- `07-finance-skill` (CFO-Agent) — headcount budget reality check

### 4. Agent Execution Order
CEO-Agent → COO-Agent → CHRO-Agent → CBO-Agent → CFO-Agent

### 5. Combined Executive Answer

**Org structure & governance (CEO):** At 15 people, the right structure is still flat — two or three functional leads reporting directly, not a third layer of management that doesn't have enough people underneath it to justify itself yet. What's actually breaking isn't headcount, it's ownership: decisions are getting re-litigated or quietly dropped because nobody is the named owner. Build the RACI matrix now, scoped to the five decisions that keep coming back up in meetings — not a company-wide org chart exercise. If there's a board or formal investors, this is also the point to formalize a monthly update cadence, even if it's been informal so far.

**Operating cadence & SOPs (COO):** Fifteen people is the threshold where tribal knowledge stops scaling — the third or fourth new hire can no longer learn "how we do things" just by sitting near someone who knows. Write SOPs for the two or three processes that are both highest-frequency and highest-risk if done wrong (onboarding, the deploy/release process, whatever the most error-prone recurring task is) — not everything. Over-documenting at this stage trades speed for process that isn't earning its cost yet. One weekly leadership sync plus one monthly all-hands is enough cadence; adding more meetings now is a tax on a company that's still small enough to coordinate informally most of the time.

**Hiring system, leveling, and culture (CHRO):** This is the most time-sensitive piece, because the next five hires are about to happen with or without a system. Define a leveling framework before posting the next role, not after — retrofitting comp bands onto people already hired creates an equity problem that takes years to unwind and shows up first as your best early hires feeling underpaid relative to who comes in next. Standardize the interview loop and scorecard across roles so the hiring bar doesn't drift between the first PM hire and the fifth. On culture: write down the three to five operating values that are *already* true — how the founders actually make decisions and treat people today — rather than aspirational ones. This is close to the last moment that's possible to do accurately; past ~25-30 people, culture starts being defined by what new hires observe rather than by what the founders do, and if it isn't written down before then, it drifts without anyone deciding it should. Move performance conversations to a lightweight quarterly cadence now — annual review is too infrequent once the team is too big for founders to informally track everyone's trajectory by memory.

**Employer brand & internal voice (CBO):** The next ten to fifteen hires will form their first impression of the company from the job posting and onboarding materials, not from osmosis — so those need one consistent voice now, not whatever tone each interviewer happens to write a posting in. Write a one-page internal narrative — why this company, why now, what stage this is honestly — once, and reuse it across postings rather than improvising it per requisition. This needs to stay in sync with what CHRO-Agent just wrote down as the real operating values; an employer-brand narrative that oversells the culture relative to what new hires actually experience in week one is worse than not having one.

**Budget reality check (CFO):** Before CHRO-Agent's leveling framework gets finalized and communicated to any candidate, it needs to be checked against actual runway — comp bands set without a budget ceiling produce offers the company can't sustain past the first few hires. Model fully-loaded cost per hire (base, benefits, tooling, and ramp-time cost before the person is net-productive), not just salary, when sizing the next two quarters of hiring against current burn.

### 6. Contradictions / Conflicts
CHRO-Agent's leveling framework implicitly assumes hiring continues at the current pace for the next two quarters; CFO-Agent's budget check may not support that pace without either extending the runway assumption or slowing hiring. Flagged for reconciliation before comp bands are finalized and shared with candidates — this is exactly the kind of cross-agent contradiction the Meta-Agent should surface rather than let each agent's plan ship independently.

### 7. Missing Inputs / Assumptions
- Current burn rate and runway were not provided; assumed a moderate ~18-month runway as a conservative default. A shorter runway would materially change the CFO recommendation and likely cap near-term hiring pace.
- Assumed no formal leveling or interview standardization exists yet, based on "hiring is starting to feel chaotic" — if a partial system already exists, CHRO-Agent's work is a refinement, not a build-from-zero.
- Assumed there is no board requiring formal governance yet; if there is, CEO-Agent's monthly update cadence recommendation becomes a near-term requirement, not a nice-to-have.

### 8. Risks
- Comp inequity baked in by ad hoc early offers, discovered later by the people it affects most — the highest-likelihood risk if leveling isn't locked before the next hire.
- Founder-dependent culture quietly diluting as new hires outnumber people who experienced the company pre-system, with nobody noticing until it's already happened.
- Process either over-built (new SOPs that slow the team down without reducing real risk) or under-built (the chaos that prompted this request in the first place continuing unaddressed).
- Hiring at a pace the financial model doesn't actually support, discovered at the offer stage rather than the planning stage.

### 9. Next Actions
1. CHRO-Agent defines the leveling framework and standardized interview loop before the next role is posted (immediate).
2. CFO-Agent models fully-loaded cost-per-hire against current runway before CHRO-Agent's comp bands are finalized (immediate, blocks #1 from being communicated externally).
3. CEO-Agent drafts a RACI matrix scoped to the five most-contested recurring decisions, not a full org chart exercise (this week).
4. COO-Agent documents SOPs for the two highest-risk recurring processes only (this week).
5. CBO-Agent writes the one-page employer-brand narrative, checked against CHRO-Agent's actual (not aspirational) culture values, before the next job posting goes out (this week).
