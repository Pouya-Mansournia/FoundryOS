# Brand Graph

## Purpose
Zooms into the one domain that deliberately reaches across every other layer instead of staying inside its own Agent — how CBO-Agent's 17 Skills, the 6 brand Memory files, the 10 Workflows' brand touchpoints, and the brand-specific Artifacts interconnect, and where Brand attaches to Community, Identity, Narrative, and Design System concerns that other companion graphs only mention in passing.

## Nodes
- **CBO-Agent** — the one Agent node, owner of all 17 brand Skills
- **17 Brand Skills** — `42-brand-strategy-skill`, `43-brand-book-skill`, `44-design-system-skill`, `45-content-system-skill`, `46-logo-system-skill`, `47-naming-skill`, `48-positioning-skill`, `49-community-skill`, `50-social-assets-skill`, `51-storytelling-skill`, `52-copywriting-skill`, `53-voice-tone-skill`, `54-color-psychology-skill`, `55-typography-skill`, `56-ui-system-skill`, `57-brand-assets-management-skill`, `58-brand-roadmap-skill`
- **6 Brand Memory files** — `brand-memory.md`, `identity-memory.md`, `design-memory.md`, `content-memory.md`, `voice-memory.md`, `community-memory.md`
- **Brand Artifacts** — Positioning Statement, Naming Shortlist, Brand Strategy Brief, Logo System & Brand Book, Design System & CMF Spec, Voice & Tone Guide, Campaign Copy & Social Assets, Narrative Arc, Brand Roadmap, Employer Brand & Internal Voice Guide
- **10 Workflows** — every one of them, since CBO-Agent runs inside all 10 (default in 9, conditional in `09-hiring-workflow`)
- **13 Brand Commands** — `/brand /logo /naming /tagline /story /design-system /identity /community /website /copy /voice /colors /social-assets`

## Relationships
- **Strategy is the root** — `42-brand-strategy-skill` is the only brand Skill with no brand-side dependency; every other Skill, every brand Memory file, and every brand Artifact traces back to it eventually
- **Skills → Memory is bidirectional, not write-once** — `47-naming-skill`/`48-positioning-skill` write into `brand-memory.md`, but the next invocation of those same Skills reads `brand-memory.md` first so a new product line doesn't get re-litigated archetype decisions already made
- **Identity vs. Design is a governance split, not a duplication** — `identity-memory.md` owns *what the logo/brand book are and who may alter them* (version, deprecated marks, misuse log); `design-memory.md` owns *what the system's tokens and rationale are* (color/type/CMF). `46-logo-system-skill` writes to the former, `44-design-system-skill` and `54-color-psychology-skill`/`55-typography-skill` write to the latter
- **Content vs. Voice is also a split** — `content-memory.md` holds the narrative arc, headline frameworks, and content calendar (the *what*); `voice-memory.md` holds tone-by-channel rules and banned phrases (the *how*). `51-storytelling-skill`/`52-copywriting-skill` lean on the first, `53-voice-tone-skill` owns the second, and both feed `45-content-system-skill` when an actual content artifact ships
- **Community is downstream of Voice, not parallel to it** — `49-community-skill` and `50-social-assets-skill` both read `voice-memory.md` before `community-memory.md` is updated, so a community post never establishes a tone the brand hasn't already sanctioned
- **CBO-Agent's per-workflow role is domain-specific, not a fixed template** — naming/positioning in `01-new-product-workflow`, in-product voice in `02-saas-product-workflow`, CMF/packaging in `03-hardware-product-workflow`, AI persona in `04-ai-product-workflow`, naming/CMF/HRI cues in `05-robotics-product-workflow`, narrative arc in `06-fundraising-workflow`, positioning-first in `07-go-to-market-workflow`, employer brand in `08-company-building-workflow`, brand implications in `10-strategic-planning-workflow`. `09-hiring-workflow` is the deliberate exception — see `WORKFLOW_GRAPH.md`
- **Brand Roadmap is the only Artifact that depends on the full Skill set**, not a subset — `58-brand-roadmap-skill` sequences naming, identity, design, voice, content, and community decisions into one dated plan, which is why it is drafted last in the within-Agent chain (see `SKILL_GRAPH.md`)
- **Commands are thin wrappers over this graph, not a parallel surface** — `/brand` invokes the full chain starting at `42-brand-strategy-skill`; `/logo`, `/naming`, `/tagline`, `/voice`, `/colors` each invoke one Skill directly and read whichever Memory file that Skill owns; `/identity`, `/community`, `/website`, `/design-system` span 2-3 Skills; `/story` and `/copy` map to `51-storytelling-skill`/`52-copywriting-skill`

## Dependencies
```
42-brand-strategy-skill → brand-memory.md
                        → 47-naming-skill / 48-positioning-skill → brand-memory.md
                        → 43-brand-book-skill → identity-memory.md
                                              → 46-logo-system-skill → identity-memory.md
                                                                     → 44-design-system-skill → design-memory.md
                                                                                              → 54-color-psychology-skill / 55-typography-skill / 56-ui-system-skill → design-memory.md
                        → 53-voice-tone-skill → voice-memory.md
                                              → 51-storytelling-skill / 52-copywriting-skill → content-memory.md
                                              → 45-content-system-skill → content-memory.md
                                              → 49-community-skill / 50-social-assets-skill → community-memory.md
                        → 57-brand-assets-management-skill → identity-memory.md + design-memory.md (packages 46+44 output)
                        → 58-brand-roadmap-skill → brand-memory.md (reads all 6 brand Memory files, writes the dated plan back)
```

## Graph Structure
```
                              CBO-Agent
                                  ↓
                    42-brand-strategy-skill  (root; writes brand-memory.md)
                       ↓                ↓
              47-naming-skill   48-positioning-skill
                       ↓                ↓
                 43-brand-book-skill  (writes identity-memory.md)
                       ↓
              46-logo-system-skill  (identity-memory.md)
                       ↓
           44-design-system-skill  (design-memory.md)
              ↓        ↓        ↓
   54-color-psych  55-typography  56-ui-system   (all → design-memory.md)
                       ↓
           53-voice-tone-skill  (voice-memory.md)
              ↓                  ↓
  51-storytelling /        45-content-system-skill
  52-copywriting-skill            ↓
       (content-memory.md)  content-memory.md
              ↓
  49-community-skill / 50-social-assets-skill  (community-memory.md)

  57-brand-assets-management-skill ── packages 46 + 44 output, versions the library
  58-brand-roadmap-skill ── reads all 6 Memory files, sequences the rollout, writes Brand Roadmap

  Touches every Workflow (default in 9 of 10; conditional in 09-hiring-workflow)
  Exposed via 13 Commands: /brand /logo /naming /tagline /story /design-system
                           /identity /community /website /copy /voice /colors /social-assets
```

## Examples
A robotics startup's brand chain runs `42-brand-strategy-skill (archetype: "the calm expert") → 47-naming-skill (product name) → 43-brand-book-skill → 46-logo-system-skill → 44-design-system-skill + 54-color-psychology-skill (CMF: matte charcoal, warm accent, signals trust not toy) → 53-voice-tone-skill (HRI cues: terse, confirmatory, never cute)`. This feeds `05-robotics-product-workflow` directly (CBO-Agent's naming/CMF/HRI step) and writes to `brand-memory.md`, `identity-memory.md`, `design-memory.md`, and `voice-memory.md` simultaneously. Six months later, a `06-fundraising-workflow` run pulls the same `brand-memory.md` archetype and `content-memory.md` narrative arc to brief `51-storytelling-skill` on the pitch deck — no re-derivation, exactly the "Brand is not a separate branch" principle stated in `KNOWLEDGE_GRAPH.md`.
