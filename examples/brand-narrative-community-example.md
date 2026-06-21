# Example: Website, Narrative, and Community for a Launch

**Prompt:** *"We're launching our open-source project in three weeks. We need the website, a launch narrative that doesn't sound like every other 'we're excited to announce' post, and a community structure ready on day one."*

---

## Meta-Agent Result

### 1. Request Classification
Go-to-market / brand expression — multi-skill, primarily CBO-Agent with CRO-Agent for launch sequencing.

### 2. Selected Agents
`CBO-Agent` → `CRO-Agent` *(launch sequencing only)*

### 3. Selected Skills
- `51-storytelling-skill` — narrative arc
- `45-content-system-skill` — reuse across surfaces
- `56-ui-system-skill`, `44-design-system-skill` — website build
- `52-copywriting-skill` — page and launch copy
- `49-community-skill`, `50-social-assets-skill` — community structure and launch assets
- `08-gtm-skill` (CRO-Agent) — launch-day sequencing

### 4. Agent Execution Order
CBO-Agent (narrative first, then website and community in parallel — both depend on the narrative, not on each other) → CRO-Agent (sequences the launch-day motion)

### 5. Combined Executive Answer

**Narrative arc (CBO — `51-storytelling-skill`):** The arc avoids the generic "we're excited to announce" framing by leading with the specific problem that justified open-sourcing rather than keeping it internal — a real pain point the team hit twice before deciding the fix was generally useful, not a marketing-driven decision to "build a community." This becomes the spine of the README intro, the launch post, and the website hero — one story, reused per `45-content-system-skill`'s reuse map, not three different stories.

**Website (CBO — `56-ui-system-skill`, `44-design-system-skill`, `52-copywriting-skill`):** Hero section opens with the narrative's specific pain point, not a feature list. Three sections below it: what it does, why it's different from the closest existing alternative (named, not vague), and how to get started in under five minutes. Copy written against `memory/voice-memory.md` — direct, technical, no exclamation points in body copy even though it's a launch.

**Community structure (CBO — `49-community-skill`):** GitHub Discussions over Discord for this audience (technical, async-friendly, doesn't want another chat app) — channel structure: Announcements, Q&A, Show & Tell, Roadmap Feedback. Moderation model: founders respond to every first-week post personally, no bot-only responses, because the first 50 interactions set the tone the rest of the community will follow.

**Launch assets (CBO — `50-social-assets-skill`):** Asset set sized for X, LinkedIn, and the GitHub social preview card, all built from the same narrative hook and the existing design system — no separate visual language invented just for launch day.

**Launch sequencing (CRO — `08-gtm-skill`):** Day-of sequence: README and website live first, launch post second (so early clickers land on a working site, not a placeholder), community channels opened third (so the first real visitors arrive to an active space, not an empty one).

### 6. Contradictions / Conflicts
None identified. Narrative, website copy, and community tone all derive from the same voice rules, checked against `memory/voice-memory.md` at each step rather than written independently and reconciled after the fact.

### 7. Missing Inputs / Assumptions
- Assumed the project has no prior public presence to reconcile (no existing Discord, no prior README framing that contradicts the new narrative). If one exists, add a reconciliation pass before launch.
- Assumed "three weeks" is firm. If it slips, the sequencing in step 5 still holds — don't launch the post before the website is live regardless of date.

### 8. Risks
- First-week community tone risk is the highest-severity item — an unanswered first post or a careless one sets a precedent that's expensive to reverse. Founders responding personally for the first week is a deliberate mitigation, not a nice-to-have.
- Narrative risk: if the "pain point we hit twice" framing reads as manufactured rather than genuine, it undermines the whole launch. Verify the story is told with enough specificity (what broke, when, what the workaround cost) that it can't be mistaken for marketing copy.

### 9. Next Actions
1. Finalize the narrative arc and get founder sign-off that the specific details are accurate, not embellished (CBO, this week).
2. Build the website against the existing design system — no new visual decisions invented mid-build (CBO).
3. Stand up GitHub Discussions with the four-channel structure before any public mention of the project (CBO).
4. Lock the launch-day sequence (site → post → community) with CRO-Agent and confirm DNS/hosting is ready a day ahead of schedule, not the same day.
