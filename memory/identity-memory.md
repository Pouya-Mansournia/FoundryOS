# Identity Memory

## Purpose
The current state of the company's official brand identity system — logo, brand book governance, and usage rules — so every surface that carries the mark stays consistent with what was actually approved, not someone's local copy of an old version.

## Stored Information
- Logo system version: mark, lockups, construction grid, and clear-space rules currently in force
- Brand book version and what changed in the most recent revision
- Approved vs. deprecated identity assets, with the deprecation date and replacement
- Known misuses caught and corrected (wrong lockup, wrong clear space, off-brand color on the mark) — useful pattern data, not just a one-off fix

## Update Rules
- Update whenever the logo system or brand book ships a new version — version number, what changed, and why
- Deprecate old assets explicitly rather than deleting the record; anyone still holding an old export should be traceable back to "yes, that was valid as of version X"
- Log recurring misuse patterns so `57-brand-assets-management-skill` can fix the root cause (a confusing usage rule) instead of the symptom

## Usage
Read by CBO-Agent before any logo, brand book, or asset-library work. Read by CIO-Agent and COO-Agent when the mark appears on physical packaging, to confirm the version being used is current. Referenced by any Agent producing a customer-facing artifact that carries the logo.

## Relationships
- Downstream of `brand-memory.md` — the logo system expresses the strategy decided there, it doesn't redefine it
- Read alongside `design-memory.md` when the logo needs to sit inside a broader design system update
- Feeds `lessons-learned.md` when a recurring misuse pattern reveals a usage-rule gap rather than a one-off mistake

## Examples
```
[2026-03-05] Logo system v1.2 shipped: added dark-mode lockup, fixed
            clear-space rule that was being misread as half the actual
            minimum
[2026-04-18] Deprecated: v1.0 horizontal lockup (replaced by v1.1) —
            still valid on assets shipped before 2026-02-01
[2026-05-30] Misuse pattern: logo repeatedly placed on brand-red
            backgrounds despite contrast rule — usage doc reworded,
            not just the one asset fixed
```
