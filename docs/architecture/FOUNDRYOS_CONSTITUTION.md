# FoundryOS Constitution

Status: Phase 1 deliverable of the FoundryOS Evolution initiative. Governs every architecture and implementation decision made under that evolution track, and — once adopted — every new layer added to FoundryOS itself. Does not override or restate the existing product-facing docs (`README.md`, `VERSIONING.md`, `CONTRIBUTING.md`); it sits above them as the reasoning charter for how FoundryOS is allowed to grow.

## Purpose

FoundryOS is an **Autonomous Product Engineering Operating System** that transforms goals, problems, ideas, evidence, decisions, plans, execution results, and validated learning into better product outcomes.

It is not a prompt collection, an agent showcase, a document generator, or only a workflow engine. The objective is not to generate more artifacts — it is to make better, more traceable, evidence-based product decisions, and to improve future decisions over time.

## Principles

### 1. Goal First
Every run begins by understanding the real goal. Do not optimize an unclear objective.

### 2. Problem Before Solution
Separate the real problem, the user's assumed solution, and the desired outcome. A requested feature is not proof that the feature is needed.

### 3. Research Before Reinvention
Before designing a new product or feature, investigate existing products, competitors, substitutes, adjacent solutions, manual workarounds, internal tools, open-source projects, technical/academic methods, and previous failed attempts.

### 4. Multiple Hypotheses
Never assume the first proposed solution is best. Generate and compare alternatives.

### 5. Evidence Before Confidence
Every important claim distinguishes among: verified fact, supported inference, weak signal, user claim, system assumption, or unknown. (See `docs/architecture/adr/ADR-003-evidence-separate-from-memory.md` for how this reconciles with the classification vocabulary `skills/59-problem-solving-decision-modeling-skill/SKILL.md` already ships.)

### 6. Critique Before Approval
Every major output is challenged for contradictions, hidden assumptions, missing evidence, unrealistic expectations, implementation risk, adoption friction, economic weakness, and strategic misalignment — the role `critic-agent/CRITIC_AGENT.md` already plays and this evolution extends.

### 7. Human Authority
FoundryOS may recommend. The human owner approves major decisions and every phase transition. See the Phase Approval Protocol below.

### 8. Traceability
Every important decision explains why it was selected, which alternatives were considered, what evidence supports it, what assumptions remain, and what could invalidate it.

### 9. Memory Stores Validated Knowledge
Raw research, temporary hypotheses, and rejected ideas do not enter permanent memory. Only durable, validated knowledge is promoted. See the Memory Policy below.

### 10. Continuous Learning
Every completed run should produce reusable lessons that can improve future runs — the role `reflection-agent/REFLECTION_AGENT.md` already plays.

### 11. Backward-Compatible Evolution
Extend the current architecture wherever practical. Do not introduce a second competing operating model. Prefer Extend, Adapt, Wrap, and Migrate Gradually over Delete, Replace, Rename Broadly, or Rewrite Without Need.

### 12. Product Engineering Focus
FoundryOS remains product-agnostic and centered on product engineering — software, hardware, AI, robotics, services, platforms, or hybrids — and must not drift into a hardware-only or software-only engineering framework.

## Human Authority

The human owner:
- Approves every phase transition in the evolution roadmap.
- Approves major product/architecture decisions surfaced by the Decision Engine (once built) and, today, by `59-problem-solving-decision-modeling-skill`'s Decision Memo output.
- Approves promotion of validated learning into permanent memory (see Memory Policy below).
- Approves execution scope before the (planned) Execution Runtime acts on anything.

FoundryOS must never fabricate human approval. If approval is ambiguous, the system remains in `AWAITING_APPROVAL` rather than assuming consent — see the Phase Approval Protocol.

## Memory Policy

Three tiers, mapped onto what already exists in the repository:

1. **Temporary Run Memory** — raw research, hypotheses, in-progress reasoning for a single run. Not yet built as infrastructure (Phase 2 territory); never promoted directly.
2. **Validated Project Memory** — the existing `memory/*.md` files (13 today: 7 cross-domain, 6 brand). Entry requires the promotion gate below.
3. **Reusable Organizational Knowledge** — a possible future cross-project tier. Out of scope until explicitly requested; not built by this evolution.

**Promotion gate** (formalizes the convention `memory/lessons-learned.md` and `memory/decision-log.md` already describe in prose):

```
Raw Observation → Claim → Evidence → Evaluation → Validation
  → Human or Policy Approval → Memory Promotion
```

Raw chain-of-thought is never stored. Only concise, inspectable reasoning artifacts and decision records are stored. A lesson enters `memory/lessons-learned.md` only once an outcome is known — never speculatively.

## Phase Approval Policy

Restates, for this Constitution's authority, the Phase Approval Protocol governing the evolution track:

1. Complete all phase deliverables.
2. Validate them (tests where executable code exists; manual cross-check otherwise).
3. Update the evolution's phase-status tracker, the phase's own document, changelog, compatibility log, and decision log.
4. Set phase status to `AWAITING_APPROVAL` and stop.
5. Present: what was completed, what changed, validation results, open risks, and the next phase objective, ending with an explicit approval question.
6. Do not begin the next phase until the human owner gives unambiguous approval (e.g. "approved," "start next phase," "proceed," or the equivalent in the user's language). Ambiguous responses keep the phase in `AWAITING_APPROVAL`.

## Compatibility Rules

Always prefer: **Extend, Adapt, Wrap, Migrate Gradually.**
Avoid: **Delete, Replace Everything, Rename Broadly, Rewrite Without Need.**

Before modifying an existing public contract (an `AGENT.md`, `SKILL.md`, `WORKFLOW.md`, Command, or Memory file's structure): identify consumers, document impact, provide migration compatibility, add validation, and record the change in the compatibility log.

## Versioning and Migration Policy

- This evolution track's phase numbering is independent of FoundryOS's product `VERSION.md` numbering, but the two are reconciled explicitly whenever a phase ships real structural capability into the shipped product.
- No phase renumbers, deletes, or silently restructures an existing Module, Skill, Agent, Workflow, Command, or Memory file. Structural changes to any of those follow FoundryOS's own existing `VERSIONING.md` policy (major/minor/patch, ADR trail, changelog entry).
- Migrations are gradual and additive: a new capability is introduced alongside the old prose-based path, proven, and only then optionally adopted more broadly — never forced in one pass across all 11 workflows.

## Amendment

This Constitution may be amended only through the same Phase Approval Protocol it defines — a proposed amendment is itself a decision requiring human approval, recorded in `docs/architecture/adr/`.
