# Evidence: idea-discovery-demo-0001

Append-only. Provisional per-run evidence note (`../../runtime/state-machine/workflows/idea-discovery/STATE_REGISTRY.md`'s Minimal Evidence Note) — not the formal Evidence Engine, which is Phase 4 scope. Each entry classified per `skills/59-problem-solving-decision-modeling-skill/SKILL.md`'s vocabulary.

### EV-01 — Release Drafter (existing solution)
- Claim: "Release Drafter (open-source GitHub Action) generates draft release notes automatically from merged PR labels."
- Classification: fact
- Source: Public GitHub repository (release-drafter/release-drafter), well-established, actively maintained.
- Recorded in: EXISTING_SOLUTION_DISCOVERY

### EV-02 — semantic-release (existing solution)
- Claim: "semantic-release automates version numbers and changelog generation from Conventional Commits."
- Classification: fact
- Source: Public GitHub repository (semantic-release/semantic-release).
- Recorded in: EXISTING_SOLUTION_DISCOVERY

### EV-03 — Coverage gap in both tools (inference)
- Claim: "Neither Release Drafter nor semantic-release natively handles per-package changelogs in a monorepo without additional configuration."
- Classification: inference (drawn from tool documentation, not independently verified against this team's exact repo structure)
- Recorded in: EXISTING_SOLUTION_DISCOVERY

### EV-04 — Manual changelog workaround (adjacent solution)
- Claim: "Many teams maintain release notes manually via a CHANGELOG.md updated by convention at PR-merge time — a common adjacent workaround rather than a tool."
- Classification: weak_signal-equivalent, recorded as: hypothesis (general industry pattern, not verified for this specific team)
- Recorded in: ADJACENT_SOLUTION_DISCOVERY

### EV-05 — No prior internal attempt found (historical)
- Claim: "No entry in `memory/lessons-learned.md` or `memory/decision-log.md` references a prior attempt at automated release notes for this team."
- Classification: fact (absence confirmed by direct search of both files)
- Recorded in: HISTORICAL_ATTEMPT_DISCOVERY

### EV-06 — Human-reported evaluation of Release Drafter (user claim)
- Claim: "Team evaluated Release Drafter ~6 months ago; found it didn't handle monorepo multi-package versioning well."
- Classification: user_claim (reported directly by the human during USER_EVIDENCE_REVIEW / WAITING_FOR_USER_EXPERIENCE, not independently re-verified)
- Recorded in: USER_EXPERIENCE_INTEGRATION
