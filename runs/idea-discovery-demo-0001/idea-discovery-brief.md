# Idea Discovery Brief — idea-discovery-demo-0001

## Idea (as received)
"We should build a tool that automatically writes our release notes from git commit history."

## Problem Framing
- Problem Statement: Engineering teams spend manual effort writing release notes at each release, which is error-prone and often skipped under time pressure.
- Assumed Solution (as given): Build a new custom tool that auto-generates release notes from commit history.
- Desired Outcome: Release notes exist for every release, accurately reflect what changed, with near-zero manual effort.

## Existing Solutions
- **Release Drafter** — generates draft release notes from merged PR labels (EV-01, fact). Free, open-source, widely adopted.
- **semantic-release** — automates versioning and changelog generation from Conventional Commits (EV-02, fact).
- Neither natively handles per-package changelogs in a monorepo without extra configuration (EV-03, inference).

## Adjacent Solutions and Workarounds
- Manual `CHANGELOG.md` maintained by convention at merge time — common industry pattern (EV-04, hypothesis, not verified for this specific team).

## Historical Attempts
- No prior internal attempt found in `memory/lessons-learned.md` or `memory/decision-log.md` (EV-05, fact — absence confirmed by direct search).

## Critic Findings
- Non-blocking: confirm the team's git/PR history is clean and consistent enough for either tool's parsing to work reliably (an unverified assumption underlying both existing solutions).
- No blocking red flags.

## Human Experience and Constraints
The team already evaluated Release Drafter ~6 months ago (EV-06, user_claim) and found it didn't handle monorepo multi-package versioning well. This is the single most important input in this brief — it directly narrows the real gap from "no solution exists" to "the closest existing solution has one specific, addressable shortfall for this team's repo structure." No contradiction between the human's experience and the research findings — the human's account confirms and sharpens EV-03's inference.

## Decision Gate Outcome
- Outcome: **ADAPT_EXISTING**
- Reasoning: Release Drafter already covers the core need (auto-generated notes from merged work); the one known gap (monorepo multi-package versioning) is a configuration/extension problem, not a reason to build a new tool from scratch. Building new would re-solve problems Release Drafter has already solved (label parsing, GitHub Action integration, draft-release UX) for no added value.
- Alternatives Considered:
  - `CONTINUE_NEW_PRODUCT_DISCOVERY` — rejected: would ignore EV-01/EV-02/EV-06 and duplicate substantial existing, working functionality, directly violating Constitution Principle 3 (Research Before Reinvention).
  - `USE_EXISTING` (adopt Release Drafter as-is, no changes) — rejected: EV-06 shows it doesn't fully meet the team's monorepo need as-is.
  - `COMBINE_SOLUTIONS` — considered (Release Drafter + a monorepo-specific changelog splitter) but deferred as a possible refinement of `ADAPT_EXISTING`'s implementation, not a distinct enough path to warrant its own category here.
- Remaining Assumptions: git/PR history is clean enough for reliable parsing (Critic finding, unverified); the specific monorepo gap is addressable via Release Drafter's extension points rather than requiring a fork.
- Confidence: Standard (per skill 59's Output Modes) — a real, moderately consequential engineering-process decision, not high-stakes/irreversible enough to warrant the Deep mode.
