# Quickstart

This is the fastest path to a useful answer from FoundryOS. If you haven't yet, follow [`INSTALL.md`](INSTALL.md) and the setup guide for your environment before trying these.

## Two Ways to Ask

**Use a command** when you already know what you want — `/cpo`, `/saas`, `/critic`, `/brand`, and 35 others each name their exact Agents, Skills, and Workflow. See [`COMMANDS.md`](COMMANDS.md) for the full table.

```
/prd Write a PRD for a usage-based billing feature.
/robotics Take this concept from requirements through a manufacturing-ready BOM.
/critic Stress-test this go-to-market plan before we commit budget.
/brand Define our brand archetype, name, and positioning from scratch.
```

In Claude Code, these are real native slash commands — the repo ships a pre-built `.claude/commands/` folder, so typing `/` lists all 39 immediately with no setup. In Claude Projects, ChatGPT, Cursor, and Windsurf, typing the command text is an instruction the assistant reads and follows, not a registered command — same result, different mechanism. See your environment's setup guide via [`INSTALL.md`](INSTALL.md).

**Or just ask in plain language** — no special syntax required. The Meta-Agent classifies the request itself and routes it the same way a command would.

- *"Build a PRD for a robotics product."*
- *"Make the company investor-ready."*
- *"Design SaaS dashboard architecture."*
- *"Create a manufacturing readiness plan."*
- *"Build a GTM strategy."*
- *"Should we charge usage-based or seat-based pricing?"*
- *"We're hiring our first 5 engineers — how should the org be structured?"*
- *"Our embedded firmware is blowing the power budget — what's the path forward?"*
- *"We need a name and a logo system before our first hire starts."*

Each of these routes to a different Agent set automatically. You don't need to know which Agents or Skills exist — that's the Meta-Agent's job. The naming/logo example routes to CBO-Agent even though the word "brand" never appears — see `meta-agent/META_AGENT.md`'s brand-trigger keyword list.

## How Routing Works

When you send a request, the Meta-Agent runs through a fixed sequence before answering:

1. **Reads the request in full** — no keyword-matching on the first word.
2. **Classifies it** into a domain (business, product, technology, robotics, operations, finance, revenue, marketing, brand/identity, people, or multi-agent).
3. **Selects the Agent(s)** that own that domain, using the routing table in `meta-agent/META_AGENT.md`.
4. **Selects the Skill(s)** under each selected Agent by reading that Agent's live `AGENT.md` — only the Skills relevant to your specific request, not the Agent's full list by default.
5. **Runs the Agents in dependency order** — e.g. CPO before CTO/CIO (you need to know *what* before you can design *how*), CFO before CRO/CMO (you need unit economics before you price and sell).
6. **Merges everything into one executive answer.** You get a single, coherent response — never separate per-agent dumps.
7. **Surfaces contradictions and missing inputs** explicitly, asking a clarifying question only when skipping it would make the answer a guess that could send you in the wrong direction. Otherwise it states its assumption and keeps moving.

### Worked example

Prompt: *"Build a GTM strategy."*

```
Meta-Agent Result

1. Request Classification: Revenue / Go-to-Market
2. Selected Agents: CRO-Agent, CPO-Agent, CMO-Agent
3. Selected Skills: 08-gtm-skill, 36-pricing-sales-skill, 03-strategy-skill, 37-marketing-customer-success-skill
4. Agent Execution Order: CPO-Agent → CRO-Agent → CMO-Agent
5. Combined Executive Answer: [the actual GTM strategy]
6. Contradictions / Conflicts: None identified
7. Missing Inputs / Assumptions: Assumed B2B SaaS motion with a sales-assisted funnel since deal size and ICP weren't specified — flag if this is wrong
8. Risks: [specific to the plan given]
9. Next Actions: [specific to the plan given]
```

That's the shape of every response — see [`examples/`](examples) for seven fully worked versions across AI products, robotics, SaaS, fundraising, manufacturing, brand/identity, and launch narrative/community.

## When to Be More Specific

The Meta-Agent will give you a usable answer from a one-line prompt. It'll be a *better* answer if you front-load the inputs it would otherwise have to assume:

- Stage of company (idea / pre-seed / seed / Series A+)
- Hardware vs. software vs. both
- Target customer (B2B vs. B2C, SMB vs. enterprise)
- Budget, team size, or timeline constraints if they're real constraints

If you don't provide these, the Meta-Agent states its assumptions in section 7 of the output rather than silently guessing — correct them and re-run if they're off.
