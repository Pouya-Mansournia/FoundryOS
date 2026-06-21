# Example: SaaS Dashboard Architecture

**Prompt:** *"Design SaaS dashboard architecture — a customer-facing analytics dashboard for our B2B platform."*

---

## Meta-Agent Result

### 1. Request Classification
Technology (SaaS / data architecture), customer-facing — multi-agent.

### 2. Selected Agents
`CPO-Agent` → `CTO-Agent` → `CMO-Agent` (customer-facing, so brought in for messaging/onboarding fit)

### 3. Selected Skills
- `04-prd-skill` (CPO-Agent) — what the dashboard needs to answer for the customer
- `24-saas-product-skill`, `30-data-architecture-skill`, `17-diagram-skill` (CTO-Agent) — multi-tenant architecture, data model, ERD/diagram output
- `37-marketing-customer-success-skill` (CMO-Agent) — onboarding and adoption plan since this is customer-facing, not internal

### 4. Agent Execution Order
CPO-Agent → CTO-Agent → CMO-Agent

### 5. Combined Executive Answer

**Requirements (CPO):** Before architecting anything, the PRD needs to pin down which question the dashboard answers for the customer — "is my account healthy," "where is my spend going," or "what should I do next" are three different dashboards with different data models and different update latencies. Defaulting to "show everything" produces a dashboard nobody opens twice. Recommend scoping v1 to the single highest-frequency question your support/success team gets asked, validated with 5–8 customer interviews before any schema work starts.

**Multi-tenant SaaS architecture (CTO):** Tenant isolation at the data layer (row-level security keyed on tenant_id, not application-layer filtering alone — a missed WHERE clause shouldn't be able to leak another customer's data). Read path separated from the transactional write path: dashboard queries hit a denormalized analytics store (star schema, pre-aggregated where possible) rather than querying production OLTP tables directly, so a slow dashboard query can never degrade the core product. Billing/usage metering, if the dashboard shows usage-based data, should be its own service with its own SLA — don't let dashboard read load become a dependency for billing accuracy.

**Data architecture (CTO):** Event-driven ingestion from the product into the analytics store (CDC or an event bus, not nightly batch, if the dashboard needs same-day data — confirm this against the CPO's "which question" framing above; a "monthly spend trend" dashboard tolerates batch, a "is my integration broken right now" dashboard does not). Define the event schema and grain explicitly before building pipelines — retrofitting grain changes later means reprocessing history.

**Visualization (CTO):** Diagram output should include the ERD for the analytics schema and a sequence diagram for the ingestion path — both go in the technical documentation handed to the team building the actual dashboard UI, not just kept in an architect's head.

**Adoption (CMO):** A dashboard with zero usage is a wasted build. Plan an in-product nudge plus a one-time onboarding email pointing existing customers to it at launch, and instrument the dashboard itself (who opens it, how often, do they come back) — feed that back to CPO as the real success metric, not "we shipped it."

### 6. Contradictions / Conflicts
None identified — flagged one internal dependency instead: CTO's batch-vs-real-time ingestion choice depends directly on CPO's answer to "which question," so that decision should be locked before ingestion architecture is finalized.

### 7. Missing Inputs / Assumptions
- Assumed a B2B multi-tenant platform with one dashboard per tenant account (not a consumer/B2C use case). A B2C scale (millions of low-value tenants) would change the isolation and cost model significantly.
- Assumed the underlying product already emits structured events or has a queryable production database. If data currently lives only in scattered logs, add a data-collection phase before this architecture is buildable.

### 8. Risks
- Tenant data isolation is the highest-severity risk in any multi-tenant analytics surface — a single isolation bug is a trust-ending incident, not a bug ticket. Budget a dedicated security review of the row-level security implementation before launch.
- Cost risk: pre-aggregation and a separate analytics store add infrastructure cost; validate against expected customer willingness-to-pay for this feature before over-building for scale you don't have yet.

### 9. Next Actions
1. Run 5–8 customer interviews to pin the one question v1 answers (CPO, this week).
2. Lock batch-vs-real-time ingestion based on that answer, then define the event schema and grain (CTO).
3. Stand up the analytics store with row-level tenant isolation and have it security-reviewed before any customer-facing rollout (CTO).
4. Plan the in-product nudge and onboarding email for launch week, and instrument usage from day one (CMO).
