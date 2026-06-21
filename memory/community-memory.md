# Community Memory

## Purpose
The state of the brand's community and social presence — structure, engagement history, and asset calendar — so community work compounds instead of restarting with every new request.

## Stored Information
- Community structure and moderation model currently in force (forum, Discord, GitHub Discussions, etc.) and what changed since the last revision
- Engagement history: what worked (format, cadence, channel) and what didn't, with rough engagement numbers where available
- Social asset calendar: what shipped, on which platform, and the platform-specific template it used
- Known community health signals (response time, sentiment, repeat-contributor rate) tracked over time

## Update Rules
- Update the community structure entry only on a deliberate change (new platform, new moderation policy), not on routine day-to-day activity
- Log engagement results against what was planned, including underperformance, so the record reflects what actually happened
- Social asset entries should reference the template used, so `50-social-assets-skill` can tell which templates are earning their keep

## Usage
Read by CBO-Agent before any community or social-asset work. Read by CMO-Agent when planning campaigns that touch community channels, to stay consistent with what's already been tried.

## Relationships
- Downstream of `brand-memory.md` and `content-memory.md` (community engagement distributes the story and voice decided upstream)
- Feeds `lessons-learned.md` when a community or social format underperforms its stated goal
- Read alongside `customer-memory.md` when community sentiment is being checked against broader customer health signals

## Examples
```
[2026-02-15] Community structure set: GitHub Discussions as primary,
            Discord opened for real-time support 2026-04-01
[2026-04-01] Discord launch: 340 members week 1, response time target
            <2h not met until week 3 — logged, not glossed over
[2026-05-25] Social template "launch announcement v2" outperformed v1
            template 1.6x engagement — v1 retired
```
