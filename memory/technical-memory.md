# Technical Memory

## Purpose
A running record of architecture decisions and their rationale, so CTO-Agent and CIO-Agent don't re-litigate a settled technical decision every time a related request comes in, and so technical debt is visible rather than rediscovered the hard way.

## Stored Information
- Architecture Decision Records (ADRs): the decision, the alternatives considered, and why this one won
- Current tech stack / hardware platform, and the date it was last materially changed
- Known technical debt items, with a rough severity/cost-to-fix estimate
- Past technical incidents or failures and the root cause (the technical equivalent of `lessons-learned.md`, scoped to engineering/hardware specifically)

## Update Rules
- Every architecture decision that comes out of `05-architecture-skill`, `31-ai-architecture-skill`, or CIO-Agent's hardware design skills gets an ADR entry, even small ones — cheap to log, expensive to reconstruct later
- Technical debt entries are never deleted on resolution, only marked resolved with a date — the history of what debt existed and how long it lived is itself useful signal
- Superseding an ADR requires linking to the new ADR that replaces it; never silently overwrite a past decision

## Usage
Read by CTO-Agent and CIO-Agent before any new architecture pass, to check for a relevant precedent or a known constraint. Read by `critic-agent/CRITIC_AGENT.md` when stress-testing a new architecture proposal against past decisions it might contradict.

## Relationships
- Fed by every workflow with a CTO-Agent or CIO-Agent step
- Feeds `knowledge-graph/AGENT_GRAPH.md` and `ARTIFACT_GRAPH.md` to trace which architecture decision underlies which shipped artifact
- Checked by `reflection-agent/` for recurring technical-debt patterns worth escalating

## Examples
```
[2026-01-20] ADR-014: Chose retrieval-augmented generation over fine-tuning
            for v1 AI feature. Alternatives considered: fine-tune from day 1
            (rejected — no edit-distance dataset yet to train on).
[2026-03-09] Tech debt logged: analytics pipeline still batch, not
            streaming — acceptable at current volume, revisit above 10x scale
[2026-04-30] ADR-019 supersedes ADR-014: moved to a hybrid retrieval +
            light fine-tune once 6 months of edit-distance data existed
```
