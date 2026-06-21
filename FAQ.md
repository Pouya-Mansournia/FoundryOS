# FAQ

### What is FoundryOS?
A folder of structured markdown files — Modules, Skills, Agents, a Meta-Agent, Workflows, and an Advanced Layer (Memory, Reflection, Critic, Planner, Knowledge Graph) — that turns an AI assistant into a standing operating system for building and running a company. You give it a request; it routes that request to the right specialist "Agent," which uses the right "Skills," and hands back one coherent answer instead of ten disconnected ones. That includes brand: a CBO-Agent and 17 brand Skills are built into the same system, not bolted on separately — see "What is the Brand Operating System?" below.

### Do I need to know how to code?
No. Nothing in this system runs as software — it's all markdown that an AI assistant reads. If you can copy a folder and type a sentence to Claude or ChatGPT, you can use it.

### Can I use ChatGPT?
Yes. See [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md). The main thing to know: ChatGPT doesn't have native slash commands, so you set it up through a Project or Custom GPT with instructions that tell it to read `commands/{name}.md` when it sees a `/command`.

### Can I use Claude?
Yes, two ways. Claude Projects works like ChatGPT Projects (upload the files, set the instruction). Claude Code goes further — it supports real slash commands backed by files in `.claude/commands/`, so `/cpo` actually appears as a command in the UI. See [`docs/CLAUDE_SETUP.md`](docs/CLAUDE_SETUP.md).

### How do slash commands work?
Each file in `commands/` (like `commands/prd.md`) specifies which Agents, Skills, and Workflow a command activates, plus the expected output. Typing `/prd <your request>` tells the assistant to read that file and follow it. In Claude Code, this is literal — Claude Code loads the file as the command definition. In other environments, it works because you've instructed the assistant up front to treat `/command` messages this way.

### Can I contribute?
Yes — see [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions that add Modules, propose new Skills, refine an Agent's mandate, or add a new command are welcome.

### Can I add my own Skills?
Yes. A Skill is just a folder under `skills/` with a `SKILL.md` describing what it does, its source Modules, and its output — see any existing `skills/{NN}-{name}-skill/SKILL.md` as a template, then add the new Skill to whichever Agent should own it (`agents/{Role}-Agent/AGENT.md` and `registry/SKILL_REGISTRY.md`).

### Can I create new Agents?
Yes, though think carefully first — the system deliberately keeps the C-suite-shaped Agent structure stable (now 10 Agents), and ownership of Skills has moved across Agents before without needing a new Agent. CBO-Agent is the precedent for when a new Agent is actually warranted: brand/identity work didn't fit cleanly inside CPO-Agent or CMO-Agent's existing mandates, so it got its own Agent rather than being squeezed into either. If you do add one, give it that same kind of clear, non-overlapping mandate and update `registry/AGENT_REGISTRY.md` and `meta-agent/META_AGENT.md`'s routing logic.

### What is the Brand Operating System?
The brand layer of FoundryOS: CBO-Agent (Chief Brand Officer) plus 17 Skills (`42-brand-strategy-skill` through `58-brand-roadmap-skill`) covering strategy, naming, positioning, brand book, logo system, design system, voice/tone, community, and more. It's wired into the rest of the system the same way every other domain is — CBO-Agent runs by default in 9 of the 10 Workflows, has its own Memory files (`brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`), and is reachable through plain English or dedicated commands (`/brand`, `/logo`, `/naming`, `/voice`, and others — see `COMMANDS.md`). The point of building it this way instead of as a standalone "branding GPT": a name, logo, and voice decided in isolation drift from the product and the financial model decided alongside them. See [`brand/BRAND_OS.md`](brand/BRAND_OS.md) for the full charter.

### Can I use this commercially?
Yes — see [`LICENSE`](LICENSE) (MIT). You can use, modify, and redistribute it, including commercially, with attribution.

### Is there a sensitive-topics caveat?
This system gives structured frameworks and a starting point for product, technical, and business decisions — it is not a substitute for legal, financial, or regulatory advice specific to your situation. Treat its financial models, compliance checklists, and contracts-adjacent outputs (e.g. cap tables, investor terms) as a draft to review with a qualified professional, not a final answer.
