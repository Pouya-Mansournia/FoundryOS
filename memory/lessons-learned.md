# Lessons Learned

## Purpose
A curated, distilled set of lessons — not a raw log — capturing what the system and the team got wrong (or right in a non-obvious way) so the same mistake doesn't get made twice across different workflows or agents.

## Stored Information
- The lesson, stated as a general principle, not a one-off complaint
- The specific decision or outcome that produced it, with a link back to `decision-log.md` or the relevant domain memory file
- Which Agent(s) or workflow(s) the lesson applies to
- Status: active (still relevant), superseded (a later lesson refined it), or resolved (the underlying cause was fixed and the lesson is now historical)

## Update Rules
- A lesson only gets added here once an outcome is known — this file is downstream of `decision-log.md` and the domain memory files, not a place to log predictions
- Lessons should be specific enough to act on ("validate evaluation-metric-to-goal alignment before launch, not after") not generic ("be more careful with launches")
- This is the primary output target for `reflection-agent/REFLECTION_AGENT.md` — most entries should originate from a reflection pass, not be added ad hoc

## Usage
Read by the Meta-Agent at the start of any workflow as a quick check against known failure patterns relevant to that workflow's domain. Read by `critic-agent/CRITIC_AGENT.md` when stress-testing a new plan, specifically to check whether it's about to repeat a logged mistake.

## Relationships
- Downstream of `decision-log.md`, `product-memory.md`, and `technical-memory.md` — lessons are extracted from these, not generated independently
- Also downstream of `brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, and `community-memory.md` — an off-voice launch or a misused logo is exactly the kind of pattern this file exists to catch
- Feeds back into every workflow's "Risks" section over time, as recurring lessons become standard risk callouts
- Central input to `reflection-agent/REFLECTION_AGENT.md`'s own operating loop

## Examples
```
[2026-04-10] LESSON (active): When an AI feature's evaluation metric is a
            proxy (e.g., draft quality) rather than the actual business
            goal (e.g., handle time), launch decisions get made on the
            wrong signal. Applies to: 04-ai-product-workflow, CTO-Agent.
[2026-05-25] LESSON (active): Pricing decisions made without checking
            CFO-Agent's gross-margin model first get revisited within one
            quarter. Applies to: 07-go-to-market-workflow, CRO-Agent.
```
