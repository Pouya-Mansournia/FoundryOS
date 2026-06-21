# Example: Building a Brand and Identity System from Scratch

**Prompt:** *"We're three founders with a funded seed round and no brand yet — we need a name, a logo system, a design system, and a brand book before our first hire shows up. Build the brand."*

---

## Meta-Agent Result

### 1. Request Classification
Brand foundation — multi-skill, single-agent (CBO-Agent owns all of it, but the chain is deep).

### 2. Selected Agents
`CEO-Agent` (ratifies the final identity) → `CBO-Agent`

### 3. Selected Skills
- `42-brand-strategy-skill` — archetype and brand strategy brief
- `47-naming-skill` — name generation and screening
- `48-positioning-skill` — positioning statement
- `43-brand-book-skill` — brand book structure
- `46-logo-system-skill` — wordmark/symbol/lockup system
- `44-design-system-skill`, `54-color-psychology-skill`, `55-typography-skill` — design tokens and rationale
- `57-brand-assets-management-skill` — versioned asset library
- `58-brand-roadmap-skill` — sequences the rollout

### 4. Agent Execution Order
CEO-Agent (strategic framing, one paragraph) → CBO-Agent (full chain below, sequential — each Skill's output is the next one's input)

### 5. Combined Executive Answer

**Strategic framing (CEO):** A funded seed company with no brand yet has a short, real window — every day without one, ad hoc decisions (a Slack handle, a placeholder deck title, a GitHub org name) start hardening into a brand by accident. Treat this as a one-week sprint, not a background task.

**Archetype and strategy (CBO — `42-brand-strategy-skill`):** Brand Strategy Brief recommends "the calm expert" archetype — confident, precise, unhurried — based on the product category (infrastructure tooling sold to technical buyers who distrust hype). This becomes the filter every downstream decision gets checked against.

**Naming (CBO — `47-naming-skill`):** Eight candidates generated and screened for trademark conflict, domain availability, and fit with "calm expert." Two survive screening; one is recommended based on pronounceability and a clean `.dev`/`.com` domain pair.

**Positioning (CBO — `48-positioning-skill`):** Positioning statement locks the category claim (infrastructure tooling for X) and the one differentiator the archetype supports — reliability over speed-of-feature-shipping, stated explicitly so it can be defended later when a competitor ships faster but flakier.

**Brand book and logo (CBO — `43-brand-book-skill`, `46-logo-system-skill`):** Wordmark-led system (no separate symbol yet — premature for a 3-person company with no product surface that needs an app icon). Usage rules cover minimum size and clear space; misuse examples included pre-emptively since there's no one yet to catch drift.

**Design system (CBO — `44-design-system-skill`, `54-color-psychology-skill`, `55-typography-skill`):** A restrained palette (one primary, one accent, neutral grays) chosen explicitly against the category's blue-enterprise convention — rationale documented in `memory/design-memory.md` so the next hire doesn't relitigate it. Type scale picked for technical-documentation legibility first, marketing-page polish second.

**Asset packaging and roadmap (CBO — `57-brand-assets-management-skill`, `58-brand-roadmap-skill`):** Versioned asset library (v1.0) with file formats for deck, web, and social. Brand Roadmap sequences what ships this week (logo, one-pager, deck template) versus what's deliberately deferred (full brand book detail, a symbol mark, merchandise) until there's a team large enough for drift to be a real risk.

### 6. Contradictions / Conflicts
None identified. Naming, positioning, and visual choices all trace back to the same archetype decision made in step one — the test of internal consistency this Workflow is designed to pass.

### 7. Missing Inputs / Assumptions
- Assumed no existing informal brand usage (social handles, a placeholder deck) needs to be reconciled. If one exists, add a migration step before this roadmap ships.
- Assumed the founders have final say on the recommended name — no separate legal trademark-clearance step run yet; flagged as a pre-launch gate, not skipped.

### 8. Risks
- Premature investment in a symbol mark or merchandise before the company has a customer-facing surface that needs one — deliberately deferred in the roadmap, not an oversight.
- Archetype lock-in risk: if the actual customer base turns out to value speed over reliability, "calm expert" may need revisiting — flagged for `reflection-agent/` to check against real customer feedback in 90 days, not assumed correct indefinitely.

### 9. Next Actions
1. Run trademark clearance on the recommended name before any public use (founders, this week).
2. Finalize and version the logo system v1.0 in the asset library (CBO).
3. Apply the design system to the one-pager and deck template — the two surfaces that exist before any hire starts (CBO).
4. Re-check the archetype against real customer language in `memory/customer-memory.md` at the 90-day mark (Reflection-Agent).
