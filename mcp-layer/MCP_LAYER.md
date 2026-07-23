# MCP Integration Layer

## Status

**v5.0.0-preview.1 — declaration only.** This file ships the *declaration* half of the planned v5.0.0 major (`docs/ROADMAP.md`, `VERSION.md`) — a contract for how a Skill names a real-world data or action need instead of guessing silently. It does **not** ship a Runtime (state held across Workflow steps) or an Execution Engine (steps that run unattended). Those two remain planned and unshipped; see [Explicitly Out of Scope](#explicitly-out-of-scope-tracked-separately) below. Per `VERSIONING.md` §9/§11, the plain `v5.0.0` tag is reserved for the release where all three land together — this is a pre-release tag toward it, not the release itself.

## Goal

FoundryOS Skills are durable domain knowledge — a PRD structure, a mechatronics design pattern, an org-design framework doesn't go stale week to week. But a handful of Skills produce better answers with a fact that *does* go stale: today's competitor pricing, what's actually in a codebase, what's open in a ticket queue. Until now, a Skill facing that gap had exactly one move: state it as a flagged assumption in the Meta-Agent's existing Missing Inputs/Assumptions section and move on. This layer adds a second move — name the specific external lookup that would close the gap, in a format any MCP-capable assistant can act on — without FoundryOS itself holding state, executing code, or requiring installation. It's the same "zero install, it's markdown" promise the rest of the system makes, extended to cover one more case: a Skill that knows exactly what it doesn't know.

## Pipeline Placement

```
        ...
 Brand Intelligence
        ↓
 41 Commands
        ↓
   MCP Layer   <- this file
        ↓
   Artifacts
```

Sits between Commands and Artifacts because the need for a live lookup only becomes concrete once a Skill is actually mid-output on a specific request — not something the Meta-Agent can pre-determine at classification time (`meta-agent/META_AGENT.md` step 3–4), and not something that changes what gets produced (still a PRD, a Financial Model, a GTM Plan — see `knowledge-graph/ARTIFACT_GRAPH.md`), only how current the numbers or facts inside it are.

## Why a Declaration Layer, Not Tool Code

FoundryOS's whole pitch is zero install, works inside any assistant that can read files (`README.md`'s opening line). Shipping an actual MCP client or server here would quietly break that promise for the 95% of a request that's still pure reasoning. Instead, this layer standardizes *what a request for an external tool looks like*, so it's equally satisfiable by Claude Code's connected MCP servers, Cowork's connectors, any other MCP-capable host, or — if nothing is connected — nothing at all, in which case the Skill's own stated fallback keeps the answer usable rather than blocked.

## Declaration Format

When a Skill's step would produce a materially better or more current answer with a live tool call, it appends an `## MCP Tool Request` block to that step's output instead of guessing silently:

```markdown
## MCP Tool Request
- **Need:** <the specific real-world information or action that would improve this step>
- **Category:** web-search | code-repo | project-tracker | communications | calendar | file-storage | database | other
- **If unavailable:** <the assumption this Skill falls back to, and where it gets flagged>
```

**Worked example** — CFO-Agent's financial-modeling Skill checking live competitor pricing instead of relying only on `memory/market-memory.md`:

```markdown
## MCP Tool Request
- **Need:** Current published pricing tiers for the 3 named competitors in this Financial Model
- **Category:** web-search
- **If unavailable:** Uses the pricing figures already in memory/market-memory.md, flagged
  as "as of [last-updated date]" in the Combined Executive Answer's Missing
  Inputs/Assumptions section
```

**Second example** — CTO-Agent's architecture Skill validating a proposed design against a repo that already exists:

```markdown
## MCP Tool Request
- **Need:** Current folder structure and primary language/framework of the existing repo
  this architecture builds on top of
- **Category:** code-repo
- **If unavailable:** Proceeds on the repo description given in the user's request,
  flagged as unverified against the actual codebase
```

## How the Meta-Agent Handles It

- If the host assistant has an MCP tool matching the declared Category connected, it's invoked mid-run and the returned data folds into that Skill's output as if it had always been known — no separate step, no separate output section.
- If not, the request's own **If unavailable** clause feeds directly into the Meta-Agent's existing Missing Inputs/Assumptions section (`meta-agent/META_AGENT.md`, Output Format §7) — this is a more specific failure mode than "no internet access," not a new one.
- The Meta-Agent never blocks a response waiting on a tool call it can't guarantee, consistent with the Operating Principle already in `meta-agent/META_AGENT.md`: "default to the assumption and state it."
- An MCP Tool Request is never required. Most Skills — PRD structure, mechatronics patterns, org design, brand voice — are durable domain knowledge with nothing to look up, and should emit no request at all.

## End-to-End Example

```
$ You:  /finance Model unit economics for our SaaS product against 3 named competitors.

Meta-Agent Result
──────────────────────────────────────────────────────────────
1. Request Classification    Finance / Competitive Pricing
2. Selected Agents           CFO-Agent
3. Selected Skills           09-financial-modeling-skill

## MCP Tool Request
- Need: current published pricing tiers for the 3 named competitors
- Category: web-search
- If unavailable: falls back to memory/market-memory.md, flagged with its last-updated date

4. Combined Executive Answer
   → Unit economics model, using live competitor pricing (Claude's web search
     connector fulfilled the request above) instead of a stale memory snapshot
──────────────────────────────────────────────────────────────
✓ Same output shape as any other FoundryOS run — one line longer when a live
  lookup mattered, zero lines longer when it didn't.
```

## Which Skills This Applies To

Most relevant to Skills whose output quality depends on real-time or external truth rather than durable domain knowledge: CPO-Agent's market/competitor research, CRO-Agent's pricing-and-sales Skill checking live comps, CTO-Agent's Skills validating against an existing codebase, CFO-Agent's financial modeling pulling live market data, CBO-Agent's community Skill checking existing social activity. It is equally correct — and the common case — for a Skill to never use it.

## Explicitly Out of Scope (Tracked Separately)

- **Runtime** — nothing here holds state between one MCP Tool Request and the next Workflow step; every request is stateless and self-contained, exactly like every other part of today's system.
- **Execution Engine** — nothing here runs a Workflow unattended or chains steps automatically; a human (or the host assistant on the human's behalf) still reviews and re-prompts between Commands.
- **Autonomous / closed-loop workflows** — out of scope for the same reason; depends on both of the above.

Full v5.0.0 target scope and what still needs to ship before the plain `v5.0.0` tag is cut: [`docs/ROADMAP.md`](../docs/ROADMAP.md#v500--runtime--execution-engine-planned), [`VERSION.md`](../VERSION.md), [`VERSIONING.md`](../VERSIONING.md) §9.
