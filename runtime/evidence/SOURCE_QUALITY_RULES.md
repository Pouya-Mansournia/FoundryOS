# Source Quality Rules

Status: Phase 4 deliverable. Rules for assigning an evidence entry's `Quality Score` (1–5) in `../evidence/EVIDENCE_LEDGER_CONTRACT.md`.

## Quality Tiers

| Score | Tier | Examples |
|---|---|---|
| 5 | Independent, verifiable, primary | Direct inspection of a codebase/repo; a signed contract; a measured metric from the run's own system |
| 4 | Independent, verifiable, secondary | Reputable third-party analysis, academic/technical source, established documentation not authored by the entity being evaluated |
| 3 | Semi-independent or well-corroborated first-party | Vendor documentation for a widely-adopted, actively-maintained open-source tool (verifiable by inspection even though first-party) |
| 2 | First-party, unverified claims | Marketing material, a vendor's own claims about their product's capability, uncorroborated |
| 1 | Anecdotal / single unverified source | A single forum post, an unattributed claim, a `weak_signal`-classified entry by definition |

## First-Party vs. Independent Validation

A source authored by the entity whose claim is being evaluated (a vendor's own pricing page, a competitor's own feature list) is capped at Quality Score 3 regardless of how confident its language is, unless independently corroborated by a second, unrelated source — in which case the corroborating pair may be scored on the higher of the two, with both entries' `Supports` fields cross-referenced. This directly implements the mission's "distinguish first-party marketing from independent validation" requirement.

## Unsupported Uniqueness Claims

A claim of the form "X is the only solution that does Y" sourced from X's own marketing is never assigned Quality Score above 2, and must be flagged in `Limitations` as an unverified uniqueness claim — these are exactly the claims most likely to be marketing framing rather than fact, per the mission's explicit warning against them.

## Relevance Score (separate from Quality)

Quality measures how trustworthy a source is; Relevance measures how directly it bears on *this run's* actual decision. A high-quality source about an adjacent-but-different problem still gets a low Relevance Score. Both scores are recorded independently — a high-quality, low-relevance entry should not be allowed to inflate a decision's apparent confidence.

## Confidence Score (derived)

`Confidence Score` combines Classification, Quality, and Relevance — not a formula (no code, per ADR-0006), but a judgment call the entry's author states a one-line reason for. As a guide: a `fact`-classified, Quality-5, Relevance-5 entry should score near 5; a `weak_signal`-classified entry can never score above 2, regardless of quality/relevance, because the classification itself caps it.

## Applying These Rules

These rules are read and applied by whichever state's Actions produce an evidence entry (see `../state-machine/workflows/idea-discovery/STATE_REGISTRY.md`'s discovery states, and any future workflow's evidence-producing states). They are a discipline, not an automated gate — per the markdown-only decision, a future assistant session must actively apply them each time, the same trade-off already accepted for `../state-machine/TRANSITION_CONTRACT.md`.
