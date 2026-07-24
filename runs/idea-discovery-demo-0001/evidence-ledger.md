# Evidence Ledger: idea-discovery-demo-0001

Status: Phase 4 formalization of `evidence.md` (Phase 3's provisional per-run notes), conforming to `../../runtime/evidence/EVIDENCE_LEDGER_CONTRACT.md`'s full schema. `evidence.md` is kept as the historical record of what Phase 3 actually produced at the time; this file is the canonical, scored version used by `decision-record.md`. Append-only.

### EV-01 — Release Drafter exists and does core-competitor work
- Claim: Release Drafter (open-source GitHub Action) generates draft release notes automatically from merged PR labels.
- Classification: fact
- Source Type: Public, actively-maintained open-source repository
- Source Reference: github.com/release-drafter/release-drafter (as cited during EXISTING_SOLUTION_DISCOVERY)
- Source Date: ongoing/actively maintained
- Accessed At: 2026-07-24T11:03:00Z
- Summary: A mature, widely-adopted tool doing the core of what was asked.
- Supports: []
- Contradicts: []
- Quality Score: 4 (independent, verifiable, well-established documentation)
- Relevance Score: 5 (directly on-point)
- Confidence Score: 5 — reason: fact classification + high quality + high relevance, no offsetting limitation
- Limitations: Capability claims not independently load-tested by this run; taken from documentation.
- Created In State: EXISTING_SOLUTION_DISCOVERY
- Created By: `02-market-research-skill`

### EV-02 — semantic-release exists and does adjacent work
- Claim: semantic-release automates version numbers and changelog generation from Conventional Commits.
- Classification: fact
- Source Type: Public, actively-maintained open-source repository
- Source Reference: github.com/semantic-release/semantic-release
- Source Date: ongoing/actively maintained
- Accessed At: 2026-07-24T11:03:00Z
- Summary: A second mature tool, commit-convention-driven rather than PR-label-driven.
- Supports: []
- Contradicts: []
- Quality Score: 4
- Relevance Score: 4 (relevant but requires a workflow change — Conventional Commits — the idea's original framing didn't assume)
- Confidence Score: 4
- Limitations: Requires adopting Conventional Commits discipline; not evaluated for this team's current commit style.
- Created In State: EXISTING_SOLUTION_DISCOVERY
- Created By: `02-market-research-skill`

### EV-03 — Both tools have a monorepo gap
- Claim: Neither Release Drafter nor semantic-release natively handles per-package changelogs in a monorepo without additional configuration.
- Classification: inference
- Source Type: Derived from EV-01/EV-02's documentation, not independently tested against this team's repo
- Source Reference: (derived — see EV-01, EV-02)
- Source Date: n/a (derived claim)
- Accessed At: 2026-07-24T11:03:00Z
- Summary: The one identified gap in both leading existing solutions.
- Supports: []
- Contradicts: []
- Quality Score: 3 (reasoned from primary sources, not independently verified against the specific case)
- Relevance Score: 5 (this is the crux of the whole decision)
- Confidence Score: 3 — reason: inference, not fact; later corroborated independently by EV-06
- Limitations: Not verified against this team's actual monorepo structure until EV-06.
- Created In State: EXISTING_SOLUTION_DISCOVERY
- Created By: `02-market-research-skill`

### EV-04 — Manual changelog is a common workaround
- Claim: Many teams maintain release notes manually via a CHANGELOG.md updated by convention at PR-merge time.
- Classification: weak_signal
- Source Type: General industry pattern, not a specific citable source
- Source Reference: general practitioner knowledge, no single citable source
- Source Date: n/a
- Accessed At: 2026-07-24T11:03:45Z
- Summary: A workaround, not a tool — establishes there's an accepted fallback, not that it's a good long-term answer.
- Supports: []
- Contradicts: []
- Quality Score: 1 (anecdotal, unattributed)
- Relevance Score: 2 (low — doesn't change the EV-01/EV-02/EV-03 picture, just confirms the problem is real enough that workarounds exist)
- Confidence Score: 1
- Limitations: Not specific to this team; included only as context, not as a comparison option.
- Created In State: ADJACENT_SOLUTION_DISCOVERY
- Created By: `02-market-research-skill`

### EV-05 — No prior internal attempt
- Claim: No entry in `memory/lessons-learned.md` or `memory/decision-log.md` references a prior attempt at automated release notes for this team.
- Classification: fact
- Source Type: Direct search of internal memory files
- Source Reference: `memory/lessons-learned.md`, `memory/decision-log.md` (searched, no match)
- Source Date: 2026-07-24
- Accessed At: 2026-07-24T11:04:15Z
- Summary: Absence of a prior attempt confirmed by direct search, not assumed.
- Supports: []
- Contradicts: []
- Quality Score: 5 (direct, verifiable inspection of the actual source)
- Relevance Score: 3 (confirms no historical baggage, doesn't drive the decision by itself)
- Confidence Score: 5
- Limitations: Confirms no *recorded* attempt — does not rule out an unrecorded informal attempt.
- Created In State: HISTORICAL_ATTEMPT_DISCOVERY
- Created By: state's own Actions (direct memory search)

### EV-06 — Human confirms and sharpens the monorepo gap
- Claim: Team evaluated Release Drafter ~6 months ago; found it didn't handle monorepo multi-package versioning well.
- Classification: user_claim
- Source Type: Human-reported, first-hand, during this run
- Source Reference: `approvals.md` entry approval-idea-discovery-demo-0001-01, Source Message
- Source Date: ~2026-01 (as reported — "about six months ago")
- Accessed At: 2026-07-24T11:12:00Z
- Summary: Independently corroborates EV-03's inference with a first-hand account, and sharpens it into a specific, real experience rather than a documentation-derived guess.
- Supports: [EV-03]
- Contradicts: []
- Quality Score: 4 (first-hand account from the actual decision-maker, though not independently re-verified by this run)
- Relevance Score: 5 (this is the single most decision-relevant entry in the ledger)
- Confidence Score: 4 — reason: user_claim capped slightly below fact/inference-with-verification, but high quality and maximum relevance
- Limitations: Not independently re-tested by this run — taken as reported.
- Created In State: USER_EXPERIENCE_INTEGRATION
- Created By: human, via `WAITING_FOR_USER_EXPERIENCE`

## Duplicate-Source Check

EV-01 and EV-02 are independent sources (different projects, different maintainers) — no duplicate-source flag. EV-03 and EV-06 are explicitly cross-referenced (EV-06 `Supports` EV-03) rather than treated as two independent confirmations of unrelated strength — EV-06 is what actually upgrades EV-03 from a documentation-derived inference to a corroborated one.

## No Contradictions Found

No entry in this ledger contradicts another — recorded explicitly per `../../runtime/evidence/EVIDENCE_LEDGER_CONTRACT.md`'s Contradiction Handling section (absence of a contradiction is stated, not left ambiguous).
