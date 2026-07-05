# Examples

Full worked runs live in [`examples/`](../examples). This page indexes them by what you're trying to build, and adds two lighter-weight walkthroughs for scenarios not yet covered by a full example file.

## Build a startup

Not yet a dedicated example file — the closest full walkthrough is [`examples/investor-readiness-example.md`](../examples/investor-readiness-example.md), which shows CEO + CFO + CPO + CRO + CTO working together. For the earlier, idea-stage version of this, run `/startup` directly:

```
/startup Help me go from idea to a fundable, buildable plan for a
subscription box service for specialty coffee roasters.
```

The Meta-Agent will typically sequence CEO-Agent (framing) → CPO-Agent (discovery, PRD) → CTO/CIO-Agent (if there's a build component) → CFO-Agent (numbers) → CRO-Agent (go-to-market), matching `workflows/01-new-product-workflow/WORKFLOW.md`.

## Build a SaaS

See [`examples/saas-dashboard-example.md`](../examples/saas-dashboard-example.md) — CTO, CPO, and CMO architecting a SaaS analytics dashboard. Trigger with `/saas` or `workflows/02-saas-product-workflow/WORKFLOW.md`.

## Build a robotics product

See [`examples/robotics-product-example.md`](../examples/robotics-product-example.md) — CIO, CTO, CPO, and COO designing a robotics product from scratch. Trigger with `/robotics` or `workflows/05-robotics-product-workflow/WORKFLOW.md`.

## Build a GTM

Not yet a dedicated example file. Trigger with `/gtm`:

```
/gtm Build a go-to-market plan for launching our product in the
EU market for the first time.
```

CRO-Agent leads on channel strategy and pricing, with CMO-Agent on demand gen and retention — matching `workflows/07-go-to-market-workflow/WORKFLOW.md`.

## Build a PRD

The PRD is the hinge artifact almost every other example builds on — see the opening sections of [`examples/ai-product-example.md`](../examples/ai-product-example.md) and [`examples/saas-dashboard-example.md`](../examples/saas-dashboard-example.md) for CPO-Agent's discovery → PRD pattern in context, or trigger it standalone with `/prd`.

## Build an AI product

See [`examples/ai-product-example.md`](../examples/ai-product-example.md) — shipping an AI product feature with CPO, CTO, and CEO. Trigger with `/ai-product`.

## Get manufacturing-ready

See [`examples/manufacturing-plan-example.md`](../examples/manufacturing-plan-example.md) — CIO, COO, and CFO building a hardware manufacturing readiness plan. Trigger with `/hardware` or `/operations`.

## Scale the team and design the org

See [`examples/team-scaling-example.md`](../examples/team-scaling-example.md) — CEO, COO, CHRO, CBO, and CFO building a hiring system, leveling framework, and operating cadence for a company that just crossed 15 people. Trigger with `/chro` or `/company-builder`, matching `workflows/08-company-building-workflow/WORKFLOW.md` and `workflows/09-hiring-workflow/WORKFLOW.md`.

## Build a brand and identity

See [`examples/brand-identity-example.md`](../examples/brand-identity-example.md) — CEO-Agent framing the strategic bet, then CBO-Agent running the full chain (strategy → naming → positioning → brand book → logo system → design system → asset management → roadmap) for a startup with no identity yet. Trigger with `/brand`, or go skill-specific with `/naming`, `/identity`, `/logo`, or `/design-system`.

## Build a website, narrative, and community

See [`examples/brand-narrative-community-example.md`](../examples/brand-narrative-community-example.md) — CBO-Agent sequencing storytelling and copy into a launch-ready website and community presence, then CRO-Agent slotting that into a launch GTM sequence. Trigger with `/story`, `/website`, `/copy`, `/community`, or `/social-assets`.

## Solve a hard problem or make a quantitative decision

See [`examples/decision-modeling-example.md`](../examples/decision-modeling-example.md) — three worked decisions (an AI inference hosting cost trade-off, a SaaS usage-based pricing tier, and a manufacturing inspection-automation call) using `59-problem-solving-decision-modeling-skill` to frame the problem, build a causal/metric model, and select the right formula from `skills/59-problem-solving-decision-modeling-skill/FORMULA_LIBRARY.md` before recommending. Trigger with `/solve`, or run `workflows/11-problem-solving-decision-workflow/WORKFLOW.md` directly. Not a PRD generator — the output is a decision packet, scaled to stakes.

---

Want a worked example for a scenario not listed here? Open an issue, or contribute one — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
