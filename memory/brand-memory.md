# Brand Memory

## Purpose
Long-term record of the company's brand strategy — archetype, positioning, and naming decisions — so CBO-Agent builds on a stated identity instead of re-deriving one from scratch each time it runs.

## Stored Information
- Brand archetype and brand strategy brief history, with the date each was set or revised
- Positioning statement history — what changed, and what triggered the change (new market, new ICP, competitive response)
- Naming decisions: company/product/feature names chosen, finalist shortlists, and why the runners-up lost
- Brand audits: the stated gap between brand intent and current state, and what closed (or didn't close) it since the last audit

## Update Rules
- Update on every brand strategy brief sign-off, positioning change, or naming decision — not on every request that merely references the brand
- When a new positioning statement conflicts with the one on file, log the conflict in `decision-log.md` before overwriting — the old positioning is context, not noise
- Naming entries should record rejected candidates and the reason, so the same dead end isn't re-explored next time

## Usage
Read by CBO-Agent before any new brand strategy, positioning, or naming work. Read by CEO-Agent when ratifying a naming or positioning decision, since both agents need to agree before it ships. Read alongside `company-memory.md` whenever a strategic pivot is on the table, since identity and strategy should move together, not independently.

## Relationships
- Upstream of `identity-memory.md`, `design-memory.md`, `voice-memory.md`, `content-memory.md`, and `community-memory.md` — all five inherit from the strategy decided here
- Read alongside `market-memory.md` and `company-memory.md` when positioning is being reassessed
- Feeds `decision-log.md` whenever a positioning or naming conflict is resolved

## Examples
```
[2026-02-10] Brand strategy brief set: archetype "The Builder" — direct,
            technical, no-nonsense. Audience: technical founders, not
            generalist SMBs.
[2026-04-22] Naming decision: product named "Forge" — finalists "Anvil"
            and "Foundry" rejected for trademark conflict in target markets
[2026-06-02] Positioning revised: narrowed from "AI tooling for teams" to
            "AI tooling for technical founders" — see company-memory.md
            2026-06-02 pivot entry
```
