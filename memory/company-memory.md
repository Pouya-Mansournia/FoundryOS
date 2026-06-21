# Company Memory

## Purpose
Long-term context for who the company is — its identity, governance, and structure — so every Agent answer aligns with one stated company rather than the company being re-invented each time CEO-Agent runs.

## Stored Information
- Vision, mission, and values statement (the durable identity CEO-Agent's `12-company-bible-skill` produces)
- Org structure and reporting lines, as they exist today (not aspirational)
- Governance model and board cadence
- Major strategic pivots and the date/reason for each
- Current company stage (idea, pre-seed, seed, Series A+, scaling) and the date it last changed

## Update Rules
- Update only when something actually changes — a strategic pivot, a funding event, a stage transition, a governance change — not on every Meta-Agent run that merely references it
- When a value or stated identity conflicts with a new decision, log the conflict in `decision-log.md` before overwriting — don't silently replace stated identity with whatever the latest answer implied
- Each entry should be dated and should state what changed and why, not just the new state

## Usage
Read by CEO-Agent at the start of any run to ground governance and identity questions in what's actually true today. Read by every other Agent indirectly through CEO-Agent's strategic framing, since `08-company-building-workflow` and `10-strategic-planning-workflow` both depend on this file being current.

## Relationships
- Upstream of every workflow that starts with CEO-Agent
- Feeds `decision-log.md` whenever a strategic pivot or governance change occurs
- Read alongside `market-memory.md` when strategy is being reassessed, since identity and market position should be checked against each other
- Checked against `brand-memory.md` whenever a strategic pivot lands — a narrowed mission or new ICP should trigger a brand-memory.md review, not leave positioning quietly out of date

## Examples
```
[2026-03-01] Stage changed: pre-seed → seed (closed seed round)
[2026-05-14] Governance: moved from informal weekly sync to monthly board
            update cadence + quarterly OKR review, per 08-company-building-workflow
[2026-06-02] Pivot: narrowed stated mission from "general productivity tooling"
            to a specific vertical, after market-memory.md showed weak
            differentiation in the general case — see decision-log.md entry
            2026-06-02-01
```
