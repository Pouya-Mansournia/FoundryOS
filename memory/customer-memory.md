# Customer Memory

## Purpose
Persistent context on who the customer actually is, based on real discovery and usage evidence — so the ICP doesn't quietly drift between workflow runs or get re-guessed each time.

## Stored Information
- Current ICP and personas, with the evidence basis (interviews, usage data, sales feedback) and last-validated date
- Jobs-to-be-done, ranked by frequency/severity as last assessed
- Recurring feedback themes (feature requests, complaints, churn reasons) with frequency counts
- Known adoption barriers and what's been tried to address them

## Update Rules
- ICP changes require a stated reason (new segment outperforming, original segment not converting) — never silently redefine the ICP without logging why in `decision-log.md`
- Feedback themes should be aggregated, not logged as individual quotes — one line per recurring theme with a running count, refreshed at least monthly
- Churn reasons should be categorized consistently over time (e.g., price, missing feature, poor onboarding, lost to competitor) so trend lines are comparable

## Usage
Read by CPO-Agent (`01-discovery-skill`) at the start of any discovery or PRD pass to check whether the stated ICP still matches evidence. Read by CRO-Agent and CMO-Agent during `07-go-to-market-workflow` to keep messaging aligned to who's actually buying, not who was originally assumed to buy.

## Relationships
- Checked against `market-memory.md` — is the ICP still who competitors are winning, or has the market moved?
- Feeds `product-memory.md` — roadmap priorities should trace back to a specific JTBD or feedback theme here, not a one-off request
- Feeds `lessons-learned.md` when an ICP assumption turns out to be wrong after a launch
- Read alongside `community-memory.md` when community sentiment is being checked against broader customer health signals, since the two should tell a consistent story

## Examples
```
[2026-01-15] ICP validated via 14 customer interviews: confirmed mid-market
            ops teams, 50-500 employees, as primary segment
[2026-04-03] Feedback theme: "onboarding too long" — 11 mentions in 6 weeks,
            up from 3/month baseline — escalated to product-memory.md
[2026-05-20] Churn reason logged: 4 of last 6 churns cited "missing
            integration with [category] tool" — candidate for next PRD
```
