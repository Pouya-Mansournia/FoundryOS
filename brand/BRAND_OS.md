# Brand Operating System

The Brand Operating System (Brand OS) is the layer that gives FoundryOS a point of view on identity, voice, and visual system — not as a deliverable you request once, but as a dimension every other layer already carries. A PRD produced by CPO-Agent, a pitch deck produced by CEO-Agent, and a landing page produced by CRO-Agent should all sound like they came from the same company. Brand OS is what makes that true by default instead of by coincidence.

It is not a 59th Skill bolted onto the side of the system. It is CBO-Agent plus 17 Skills plus 6 Memory files plus routing rules in Meta-Agent plus a stage in every Workflow plus checks in Reflection, Critic, and Planner plus nodes in the Knowledge Graph plus 14 Commands plus its own asset specs. Removing Brand OS would mean editing all of those files, not deleting one folder — that is the test for whether something is integrated or just attached.

## Why This Layer Exists

Most early-stage builders treat brand as decoration: a logo commissioned after the product works, a tagline written the week before launch. That ordering produces the thing investors and users both notice immediately — a product with real substance and no legible identity, or an identity with no substance behind it. FoundryOS treats brand the way it treats architecture or unit economics: a discipline with its own first-principles, its own failure modes, and its own owner, engaged from the first PRD rather than retrofitted before a launch.

## The Brand Stack

| Component | Where It Lives | What It Does |
|---|---|---|
| CBO-Agent | `agents/CBO-Agent/` | Owns brand strategy, identity systems, voice, and narrative — the brand equivalent of what CTO-Agent is to architecture |
| 17 Brand Skills | `skills/42-*` through `skills/58-*` | Atomic brand capabilities: strategy, identity, design systems, content, voice, community, and roadmap |
| 6 Brand Memory files | `memory/brand-memory.md`, `identity-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`, `design-memory.md` | Persistent brand context so identity stays consistent across sessions instead of being reinvented per request |
| Meta-Agent routing | `meta-agent/META_AGENT.md` | Auto-activates CBO-Agent and relevant Skills whenever a request touches identity, naming, voice, visual system, or community |
| Workflow stage | `workflows/*/WORKFLOW.md` | Every Workflow that produces a customer-facing artifact runs a brand pass — CBO-Agent sits in the execution order, not off to the side |
| Knowledge Graph node | `knowledge-graph/BRAND_GRAPH.md` + updates across the other five graphs | Brand is a connected node, not an isolated tree — it touches Skills, Agents, Memory, Workflows, Artifacts, and Community |
| Brand Commands | `commands/brand.md`, `logo.md`, `naming.md`, `tagline.md`, `story.md`, `design-system.md`, `identity.md`, `community.md`, `website.md`, `copy.md`, `voice.md`, `colors.md`, `social-assets.md`, plus `cbo.md` | Direct triggers for any brand-specific request |
| Brand asset specs | `docs/SHOWCASE.md` | Logo and hero-image prompt specs, alongside the existing architecture/banner/screenshot specs |

## What CBO-Agent Owns That No Other Agent Does

CMO-Agent owns demand generation and the retention loop — getting the right people to notice the product and stay. CBO-Agent owns what they notice: whether the name, voice, visual system, and story are coherent enough to be noticed correctly in the first place. CPO-Agent owns what the product does; CBO-Agent owns what the product means. The two are deliberately adjacent and deliberately distinct — see `agents/CBO-Agent/AGENT.md` for the full mandate and `registry/AGENT_REGISTRY.md` for how this boundary is drawn against CMO-Agent and CPO-Agent.

## How a Brand Request Flows

```
Request mentions brand, identity, logo, naming,
tagline, voice, design system, or community
              ↓
       Meta-Agent routes to
       CBO-Agent (+ supporting Agents
       per request-type — see META_AGENT.md)
              ↓
   CBO-Agent selects from 17 Brand Skills
              ↓
   Brand Memory read (existing identity,
   voice, and design decisions) before
   anything new is proposed
              ↓
   Output checked against Critic-Agent's
   brand-consistency criteria
              ↓
   Planner-Agent sequences rollout
   (roadmap, launch order, asset list)
              ↓
   Reflection-Agent later evaluates whether
   the identity held up post-launch and
   writes findings back into Brand Memory
```

## How It Folds Into the Full Architecture

Brand OS does not sit beside the core stack — it sits inside it, with one explicit checkpoint near the end where identity gets applied to whatever the system just built:

```
Modules → Skills → Agents → Meta-Agent → Workflows → Memory
   → Reflection → Critic → Planner → Knowledge Graph → Commands
   → Brand Intelligence → Artifacts → Assets → GitHub Release
```

"Brand Intelligence" in that chain is not a separate engine — it is CBO-Agent and its Skills, invoked at the point where an Artifact is about to become customer-facing. Everything upstream of it (Modules through Commands) can produce a correct answer with zero brand awareness; everything from that checkpoint onward is where the answer gets a name, a voice, and a visual system attached to it before it ships.

## Versioning Note

Brand OS shipped in v4, in the same release as the Founder-CPO-OS → FoundryOS rebrand — see [`../CHANGELOG.md`](../CHANGELOG.md) for the full file-by-file list and [`../VERSION.md`](../VERSION.md) for updated layer counts. It was built to the same depth as the v1 core system and the v2 Advanced Layer on day one, rather than shipped as a thin spine and filled in later.
