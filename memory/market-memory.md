# Market Memory

## Purpose
Persistent context on the market and competitive landscape, so CPO-Agent and CEO-Agent don't re-run market sizing or competitor analysis from zero every time a strategy or positioning question comes up.

## Stored Information
- Market sizing (TAM/SAM/SOM) as last calculated, with the date and methodology
- Competitor list with positioning notes, last-updated date, and known strengths/weaknesses
- Industry trends and shifts that materially affect strategy (regulatory changes, platform shifts, new entrants)
- Pricing benchmarks observed in the market

## Update Rules
- Re-validate market sizing at most quarterly, or immediately after a material market event (new well-funded competitor, regulatory change, platform shift)
- Mark stale entries explicitly (`STALE — last verified [date]`) rather than deleting them; a stale data point with a date is more useful than no data point
- New competitor entries require at minimum: what they do, who they target, and how they're priced — not just a name

## Usage
Read by CPO-Agent (`02-market-research-skill`) before any new market-sizing or competitor pass, to update rather than restart from scratch. Read by CEO-Agent and CRO-Agent during `10-strategic-planning-workflow` and `07-go-to-market-workflow` respectively, to ground positioning decisions in current competitive reality.

## Relationships
- Feeds `product-memory.md` (positioning decisions should trace back to a specific competitive read)
- Feeds `customer-memory.md` (ICP definitions should be checked against who competitors are actually winning)
- Checked against `company-memory.md` during strategy resets — does the stated identity still differentiate in the current market?
- Checked against `brand-memory.md` when a new competitor or category shift surfaces — a positioning statement that no longer differentiates is a brand-memory.md update, not just a market note

## Examples
```
[2026-02-10] TAM/SAM/SOM recalculated: TAM $4.2B (category), SAM $600M
            (target segment), SOM $40M (3-year realistic capture)
[2026-04-22] New competitor entered: well-funded, targets same ICP,
            priced ~30% below us — flagged for CRO-Agent pricing review
[2026-05-30] STALE — last verified 2026-02-10: TAM/SAM/SOM should be
            re-checked before any fundraising workflow run
```
