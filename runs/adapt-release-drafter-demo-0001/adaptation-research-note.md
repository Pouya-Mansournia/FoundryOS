# Adaptation Research Note: Release Drafter Monorepo Gap

Produced by task T1 of `plan.md`, executed per `execution-log.md`'s T1 entry. This is the actual artifact — not a spec of what an artifact should look like, but the real output of one authorized execution step.

## Context

`runs/idea-discovery-demo-0001/decision-record.md` decided `ADAPT_EXISTING`: adapt Release Drafter rather than build a new release-notes tool, based on evidence that Release Drafter covers the core need but has a monorepo multi-package versioning gap (EV-03, corroborated by EV-06).

## Candidate Extension Points

1. **Config-per-package via `.github/release-drafter-<package>.yml`** — Release Drafter supports multiple config files invoked per-workflow-run; a monorepo could run one drafter pass per package directory, each scoped to that package's own PR labels/paths, producing separate draft releases instead of one merged one.
2. **Path-filtered PR categorization** — Release Drafter's `categories` config supports path-based filters; combined with a CI step that determines which package(s) a PR touched, this could route a single PR's changelog entry to the correct per-package draft without needing a second tool.

## Remaining Assumptions (Restated, Not Resolved)

Per the Decision Record's Remaining Assumptions — this note does not resolve either:
- (a) Git/PR history is clean enough for reliable parsing — still unverified, still flagged by the Critic Agent during `EVIDENCE_SYNTHESIS`.
- (b) The monorepo gap is addressable via extension points rather than requiring a fork — this note identifies *candidate* extension points (above), which is progress toward testing hypothesis (b), but does not itself confirm they work for this specific team's repo structure. That confirmation is future work, out of this run's scope.

## Scope Boundary

This note is self-contained within `runs/adapt-release-drafter-demo-0001/`. No file outside this run's directory was created, modified, or read for anything other than citation (the Decision Record and Idea Discovery Brief, both read-only references).
