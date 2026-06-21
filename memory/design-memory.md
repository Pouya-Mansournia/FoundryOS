# Design Memory

## Purpose
The current state of the product- and surface-facing design system — components, tokens, color, typography, and UI patterns — so CTO-Agent and CIO-Agent build against the same design language CBO-Agent actually shipped, not an approximation of it.

## Stored Information
- Design system version: component library, token set, and layout rules currently in force
- Color palette and the psychology/rationale behind each choice, plus any accessibility constraints (contrast ratios) that shaped it
- Type scale and font pairing currently approved, and what it replaced
- CMF (color/material/finish) specs for any physical product, versioned the same way as digital design tokens

## Update Rules
- Update on every design system or token version bump — what changed, which components were affected, and the migration path for anything already built against the old version
- Color and typography changes should record the reason (legibility issue, accessibility gap, brand refresh), not just the new value
- CMF changes for hardware should be logged before tooling is committed, not after — see `03-hardware-product-workflow`'s risk on this exact failure mode

## Usage
Read by CBO-Agent before any design-system or visual work. Read by CTO-Agent when building UI against design tokens, and by CIO-Agent when a physical product's CMF needs to match the current system. Read by `critic-agent/` when checking a new artifact for visual-system consistency.

## Relationships
- Downstream of `brand-memory.md` and works alongside `identity-memory.md` (the logo is one component inside this broader system)
- Fed by `02-saas-product-workflow`, `03-hardware-product-workflow`, and `05-robotics-product-workflow`, all of which produce or consume design-system decisions
- Feeds `knowledge-graph/BRAND_GRAPH.md` so design-token dependencies are traceable across Agents

## Examples
```
[2026-02-20] Design system v2.0 shipped: new token set, 14 components
            migrated, 3 deprecated (no longer match the v2 grid)
[2026-04-02] Color palette revised: primary blue darkened 8% for
            AA contrast compliance on white backgrounds
[2026-05-15] CMF spec set for hardware line: matte charcoal housing,
            locked before EVT tooling — see 03-hardware-product-workflow
```
