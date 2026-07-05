# 09 Hiring Workflow

## Purpose
Turn "we need to hire" into a structured role definition, interview loop, and scorecard — the narrowest and most frequently-reused workflow in the system, since most companies run this dozens of times.

## Inputs
- The role being hired (function, level, and what success looks like in the first 90 days)
- Whether this is a new role or backfill, and what's changing if it's a backfill
- Compensation band constraints, if CFO-Agent's budget has already set one
- Reporting line and team context

## Meta-Agent
Classified as **people**. This is the most agent-light workflow in the system by design — most individual hires don't need a full multi-agent pass. CFO-Agent, COO-Agent, and CBO-Agent are intentionally *not* in the default execution set; bring CFO-Agent in explicitly only if compensation banding needs fresh modeling, COO-Agent only if the role itself changes an operating process, and CBO-Agent only if the job posting is externally visible and needs to match a defined employer-brand voice rather than a generic template.

## Agent Execution Order
```
Meta-Agent
   ↓
CHRO-Agent    (role definition, interview loop, scorecard)
   ↓
CEO-Agent     (ownership/accountability check against RACI, culture fit)
```

## Skill Selection
| Agent | Skills |
|---|---|
| CHRO-Agent | `39-people-culture-skill` |
| CEO-Agent | `19-raci-meeting-skill`, `12-company-bible-skill` |
| CBO-Agent *(conditional)* | `53-voice-tone-skill` — only if the posting is externally visible and needs employer-brand voice review |

## Artifacts Produced
Role Definition & Job Description, Interview Loop & Panel Structure, Hiring Scorecard, Compensation & Leveling Reference, 30/60/90-Day Performance Plan.

## Validation
`14-validation-skill` (COO-Agent) is invoked only if the new role changes an existing operating process or RACI ownership — most hires don't need it. If `critic-agent/` is active, run it against the scorecard specifically: does it measure what the role actually needs, or generic competencies copied from a template? `59-problem-solving-decision-modeling-skill` is invoked only for a genuinely contested hiring call (e.g. build this function in-house vs. contract it) — most individual hires don't need the full reasoning engine.

## Risks
- Interview loop tests for skills the role doesn't actually need day one, lengthening time-to-hire for no signal gained
- Scorecard criteria not tied to the 90-day plan, so the hiring bar and the onboarding plan disagree
- Compensation set without checking CFO-Agent's current budget reality, creating a banding problem at the offer stage
- Job description copy drifting from the company's defined voice because it's an externally visible artifact nobody routed through CBO-Agent

## Final Outputs
One merged hiring package: Role Definition → Interview Loop → Scorecard → Compensation → Performance Plan, ready to run end to end for this specific role.

## Example Prompt
*"We're hiring our first product manager — help us define the role, build the interview loop, and set a 90-day plan."*
