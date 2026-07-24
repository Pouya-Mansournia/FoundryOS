# Evaluation Engine

Status: Phase 4 deliverable. Implements Layer 5 of [`../../docs/architecture/TARGET_ARCHITECTURE.md`](../../docs/architecture/TARGET_ARCHITECTURE.md) — unifies the criteria already used separately by `14-validation-skill` (gap/contradiction audits), `18-stage-gate-skill` (go/no-go), and `27-product-scorecard-skill` (PMF/retention scoring) into one shared contract that any state (e.g. `DECISION_GATE` in the Idea Discovery registry) can invoke.

## Evaluation Criteria

Applied to a hypothesis, product direction, solution option, or implementation path, drawing on the evidence entries that support it (per `../evidence/EVIDENCE_LEDGER_CONTRACT.md`):

| Criterion | What it asks |
|---|---|
| Problem Severity | How bad is the problem for whoever has it? |
| Problem Frequency | How often does it occur? |
| User Value | How much value would solving it create? |
| Existing Solution Coverage | How much of this does something that already exists already solve? |
| Differentiation | What would be genuinely different about a new solution? |
| Evidence Quality | Per `../evidence/SOURCE_QUALITY_RULES.md` — is the evidence behind this option actually good? |
| Adoption Friction | How hard is this to get people to actually use? |
| Technical Feasibility | Can this actually be built with available capability? |
| Operational Complexity | What does running this add to ongoing operations? |
| Economic Plausibility | Do the unit economics plausibly work? |
| Time to Value | How long until this produces real value? |
| Strategic Alignment | Does this fit the stated goal (Constitution Principle 1)? |
| Regulatory Risk | Any legal/compliance exposure? |
| Reversibility | How easily can this be undone if wrong? |
| Uncertainty | How much of this rests on `hypothesis`/`weak_signal`/`assumption`-classified evidence rather than `fact`? |

## Scores Must Not Hide Blockers

A high aggregate score across the criteria above must never mask a hard blocker. The following are always surfaced explicitly, regardless of how well an option scores elsewhere:

- No meaningful user problem (Problem Severity/Frequency both effectively zero)
- Existing solution is already sufficient (directly checked against `EXISTING_SOLUTION_DISCOVERY`/`ADJACENT_SOLUTION_DISCOVERY` evidence — see the Idea Discovery demo run's `ADAPT_EXISTING` outcome for a real example of this blocker firing correctly)
- Critical evidence missing (a criterion cannot be scored at all because no evidence exists — this is itself a blocker, not a default middling score)
- Unacceptable legal or regulatory risk
- Impossible economics
- Unacceptable safety risk
- User rejects the problem frame (surfaced at a state like `WAITING_FOR_USER_EXPERIENCE` in the Idea Discovery registry)
- No strategic fit

A state applying this Evaluation Engine must check the blocker list **before** computing any aggregate score, and if a blocker fires, report it as the primary finding — an aggregate score is not even meaningful once a hard blocker applies.

## Hypothesis / Option Comparison

When comparing multiple hypotheses or solution options (Layer 2's "Multiple Hypotheses" requirement, Constitution Principle 4), use a comparison table with one row per option and one column per Evaluation Criterion, each cell citing the specific evidence entry (`evidence_id`) it's based on — never an unsourced score. An option with more cells sourced from `fact`/`inference` evidence is more trustworthy than one resting mostly on `hypothesis`/`assumption`/`weak_signal`, even at the same numeric score — the Uncertainty criterion exists specifically to make this visible rather than averaged away.

## Relationship to Existing Skills

This Evaluation Engine does not replace `14-validation-skill`, `18-stage-gate-skill`, or `27-product-scorecard-skill` — each remains valid for its existing, narrower purpose (contradiction audits, phase-boundary go/no-go, product-health scoring). This contract is what a state-machine state invokes when it needs the *unified* version of "compare options against criteria and surface blockers," reusing those skills' underlying judgment where applicable rather than re-deriving criteria from scratch each time.
