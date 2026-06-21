# Versioning

This document is the canonical policy for how FoundryOS is versioned — what a version number means, when it changes, and why the public release is **v4.0.0**, not v1.0.0. If you only read one section, read [§3](#3-public-release-policy) and [§9](#9-roadmap-version); together they answer "why does a brand-new public repo already say v4?"

---

## 1. Versioning Philosophy

FoundryOS isn't a compiled package — it's a markdown knowledge system: Modules, Skills, Agents, a Meta-Agent, Workflows, and now a Brand Operating System, all expressed as files and folder structure. There's no build step to break, but there's something just as real to protect: the **shape** of the system, and the contract that shape implies for anyone who clones it, automates against it, or builds on top of it.

So the philosophy is simple: **version numbers track structural milestones, not file edits.** A new top-level layer, a new capability class, or a change that alters how the existing layers compose — that's worth a version number. A new Module, a typo fix, a renamed file, an audit correction — that's not. This is already how `CONTRIBUTING.md` describes versioning ("structural milestones... get a version bump... routine additions within an existing layer... don't"); this document formalizes that rule and extends it to cover release naming, tagging, deprecation, and compatibility now that FoundryOS is going public.

The second principle: **internal iteration and public release are different things, numbered differently in spirit even though they share the same numbering scheme.** Section 2 and 3 explain why that distinction matters enough to write down.

---

## 2. Internal Milestone Policy

**Version history at a glance:**

| Version | Milestone | Status |
|---|---|---|
| v0.1 | Raw module foundation | Internal |
| v0.5 | Skill layer | Internal |
| v0.8 | Distributed module architecture inside `skills/*/` | Internal |
| v1.0 | Meta-Agent milestone | Internal |
| v2.0 | Workflow, memory, critic, reflection, planner, and knowledge-graph expansion | Internal |
| v3.0 | Command layer, documentation, Claude setup, and GitHub usability | Internal |
| **v4.0.0** | **First public-ready FoundryOS release** (rebrand + Brand Operating System + full consistency/hygiene pass) | **Public — current** |
| v5.0.0 | Runtime, MCP, tool integration, execution engine, and autonomous workflows | Planned |

*A footnote for anyone cross-referencing `CHANGELOG.md` directly: that file additionally records `v0.9` ("Hardware Consolidation" — merging Mechanical/Electronics/Embedded into Mechatronics, adding CIO-Agent) as a named sub-milestone between `v0.8` and `v1.0`, and titles `v0.8` "Agents" rather than "Distributed module architecture." Both are accurate descriptions of the same internal era from different angles — `CHANGELOG.md` is the detailed, file-by-file record; the table above is this policy's simplified version of the same history. Neither supersedes the other; see §2's closing rule on why internal-era history is never rewritten to force a clean match.*

Everything from **v0.1 through v3.0** — and the rebrand/Brand-OS work that became v4.0 — happened while FoundryOS had no public repository, no external clone, and no one outside this project depending on its shape. These are **internal architecture milestones**: real, sequential, and fully documented in [`CHANGELOG.md`](CHANGELOG.md), but never "released" in the sense of a git tag, a GitHub Release, or a promise that the structure wouldn't change underneath someone.

That distinction matters because internal milestones were allowed to be wrong and get corrected. Skill-to-Agent ownership was reshuffled twice before v1.0 ever shipped (see `VERSION.md`'s Versioning Note). A module got renamed mid-stream. A skill slug collided with another and was renamed before anyone outside the project could have referenced the old one. None of that is a compatibility break, because nothing external existed yet to break. Internal milestones can be renumbered, reinterpreted, or corrected retroactively — and were — without owing anyone a deprecation cycle.

**Rule:** anything before the first public tag stays in `CHANGELOG.md` for lineage (history isn't deleted just because it predates public release — see §12), but it is never treated as a compatibility boundary. Only public releases are.

---

## 3. Public Release Policy

A **public release** is a version that is tagged, pushed to a real GitHub repository, and intended for someone outside this project to clone and use without first talking to the maintainer. By that definition, FoundryOS has exactly one public release so far: **v4.0.0**.

**v4.0.0 is not "v1.0.0" relabeled, and it never will be.** Two reasons:

1. **It would misrepresent how mature the architecture already is.** By the time FoundryOS is publishable, it already has 175 Modules, 58 Skills, 10 Agents, a Meta-Agent, Workflows, a full Advanced Layer (Memory, Reflection, Critic, Planner, Knowledge Graph), a Command Layer, and a Brand Operating System. Calling that "v1.0.0" tells a newcomer this is a first attempt, when it's actually the fourth major internal architectural generation, audited and hardened.
2. **It would collide with real, already-written history.** `CHANGELOG.md` has a `v1.0` entry — the Meta-Agent milestone — that predates the rebrand by a long way. Renumbering the public launch to v1.0.0 would force either rewriting that history or running two incompatible "v1.0" stories side by side. Keeping the public release at v4.0.0 lets `CHANGELOG.md` stay a single, honest, linear record from `v0.1` to today.

**Rule going forward:** public releases get a git tag (§11), a `RELEASE_NOTES.md` entry (§12), and are the only versions this policy's compatibility commitments (§14) apply to. Internal work between public releases — audits, hygiene passes, doc-drift fixes — does not get its own public release unless it changes structure (§5–§7 decide which bucket it falls into).

---

## 4. Semantic Versioning Rules

FoundryOS uses `MAJOR.MINOR.PATCH`, adapted from [SemVer](https://semver.org/) for a markdown/knowledge-system repo instead of a compiled one. The mapping:

| Segment | Changes when... |
|---|---|
| **MAJOR** | A new structural layer or capability class is added, or an existing layer's shape changes in a way that isn't backward-compatible (§5) |
| **MINOR** | An existing layer gains content without changing its shape — new Modules, Skills, Commands, Workflows, Memory files, or a new Agent that fits the existing pattern (§6) |
| **PATCH** | Hygiene, correctness, or documentation fixes that add or remove nothing structural, applied **after** a version has already been publicly tagged (§7) |

Pre-tag internal corrections (anything fixed before a version's public tag is pushed) don't consume a patch number — see §7 and the worked example in §19.

---

## 5. What Counts as a Major Version

A MAJOR bump (`X.0.0`) means a new top-level layer was added, or the relationship between existing layers changed in a way other layers now depend on. Precedent, from this repo's own history:

- **v1.0** — the Meta-Agent itself: the first version where the four core layers (Modules → Skills → Agents → Meta-Agent) were all present and the system could route any request without a human picking specialists.
- **v2.0** — the Workflows layer and the entire Advanced Layer (Memory, Reflection, Critic, Planner, Knowledge Graph) added at once.
- **v3.0** — the Command Layer (`commands/`, later `.claude/commands/`) plus the full onboarding doc set.
- **v4.0.0** — the rebrand to FoundryOS and the Brand Operating System (CBO-Agent, 17 brand Skills, 6 brand Memory files, a 6th Knowledge Graph, 13 Commands) woven into every existing layer — also the version chosen for first public release (§3).
- **v5.0.0 (planned)** — see §9: a Runtime/MCP/execution-engine layer, which changes what FoundryOS *is* (a knowledge system you read from, to one that can also act).

**Test:** if removing the new thing would leave a dangling reference in another layer (a Workflow that expects an Agent that no longer exists, a Command pointing at a layer that's gone), it was structural enough to be a MAJOR.

---

## 6. What Counts as a Minor Version

A MINOR bump (`x.Y.0`) means an existing layer grew without changing shape. Examples that would be MINOR if they happened today, post-v4.0.0:

- Adding new Modules and the Skill(s) built from them.
- Adding a new Command under `commands/` (and regenerating `.claude/commands/` — see §17).
- Adding a new Workflow, Memory file, or Knowledge Graph cross-reference.
- Adding an 11th domain Agent that fits the existing C-suite pattern (per `CONTRIBUTING.md`'s "How to add an Agent" — a real, non-overlapping mandate, not a reorganization).
- Closing a self-flagged completeness gap, like the CHRO-Agent worked-example gap closed during the v4.0.0 audit — additive, no shape change.

**Test:** does every existing file's reference to every other file still resolve unchanged? If yes, and something genuinely new was added, it's MINOR.

---

## 7. What Counts as a Patch Version

A PATCH bump (`x.y.Z`) means a fix that adds or removes no capability — and, critically, it only applies **after** the version it's patching has a public tag. Examples:

- Broken internal link fixes.
- Doc-drift corrections (a file describing a folder as empty after that folder was later populated — exactly what happened to `AUDIT_REPORT.md` during this release; see `FINAL_RELEASE_AUDIT.md` §11).
- Typo, formatting, or cross-reference fixes.
- GitHub hygiene additions (`.gitignore`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue/PR templates) when added to an *already-tagged* release.

**Why v4.0.0's own GitHub-readiness pass did not bump to v4.0.1:** every hygiene fix described above happened *before* v4.0.0 was ever tagged and pushed. Per `CONTRIBUTING.md`'s existing rule and this policy's §3, nothing external could have depended on the unpatched state, so there's nothing to patch — it's still pre-release internal correction, folded into the same v4.0.0 tag. The first real PATCH this project issues will be the first fix that lands **after** v4.0.0 is live on GitHub.

---

## 8. Current Version

**v4.0.0 — first public release.**

Ships: the FoundryOS rebrand, the full Brand Operating System (CBO-Agent, 17 brand Skills, 6 brand Memory files, `BRAND_GRAPH.md`, 13 brand Commands), a complete repo-wide consistency pass (zero broken links, zero phantom references, zero Source-Module/disk mismatches), and a full open-source hygiene pass (`LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.gitignore`, `.github/` templates, badges).

Full detail: [`CHANGELOG.md`](CHANGELOG.md) (`## v4.0`), [`RELEASE_NOTES.md`](RELEASE_NOTES.md), [`AUDIT_REPORT.md`](AUDIT_REPORT.md), and [`FINAL_RELEASE_AUDIT.md`](FINAL_RELEASE_AUDIT.md). Current counts: [`VERSION.md`](VERSION.md).

---

## 9. Roadmap Version

**v5.0.0 (planned) — Runtime, MCP, Tool Integration & Execution Engine.**

This is the next MAJOR, not a MINOR, because it changes what FoundryOS *is*: today it's a knowledge system a human or an assistant reads from and reasons with; v5.0.0 adds an actual execution layer — a Runtime that can hold state across steps, MCP/tool integration so Agents can call real tools instead of only producing text, an execution engine that can run a Workflow's steps without a human re-prompting between each one, and the closed-loop/autonomous-workflow behavior already sketched in `VERSION.md`'s and `docs/ROADMAP.md`'s Roadmap sections. None of that exists yet — v5.0.0 is a target, not a count.

Full detail and current bullet list: [`VERSION.md`](VERSION.md) (Roadmap → v5.0.0) and [`docs/ROADMAP.md`](docs/ROADMAP.md) (v5).

---

## 10. Release Naming Rules

- Every public release gets a version number; a **name** is optional and only added if the release has one coherent theme (it usually will, given §5's bar for what makes a MAJOR).
- Format: `vX.Y.Z — Theme in a Few Words`. Example: `v4.0.0 — FoundryOS Rebrand & Brand Operating System`.
- No internal-only codenames in public-facing docs (`README.md`, `RELEASE_NOTES.md`) — a name should mean something to a reader who has never seen this repo before.
- No third-party trademarked names, no inside jokes that won't survive a maintainer handoff.

---

## 11. Tag Naming Rules

- Git tags are always the **fully-qualified, 3-segment form**: `v4.0.0`, never `v4.0` or `4.0.0`. Prose in `VERSION.md` and `CHANGELOG.md` may refer to a milestone as "v4.0" for readability — the tag itself is always `v4.0.0`.
- One tag per public release. Tags are never moved or force-pushed to point at a different commit after creation — if a release needs correcting post-tag, that's a PATCH and a new tag (§7).
- No floating `latest` tag that gets silently overwritten. If a "latest stable" pointer is ever needed, it's a GitHub Release marked "Latest," not a moving git tag.
- Internal milestones (anything pre-v4.0.0) are never tagged, retroactively or otherwise — see §2.

---

## 12. Changelog Rules

- `CHANGELOG.md` format loosely follows [Keep a Changelog](https://keepachangelog.com/): one heading per version, most recent first.
- Entries describe **what changed and which files were touched**, not just a feature-name bullet — this repo's existing `CHANGELOG.md` entries are the model to match (see `## v4.0` for the level of detail expected).
- Internal milestones (`v0.1` through `v3.0`, and the pre-tag work that became `v4.0.0`) stay in `CHANGELOG.md` permanently. They're not deleted or hidden just because they predate the first public release (§2) — they're FoundryOS's real lineage, and deleting them would make the jump from "nothing" to "v4.0.0" look unexplained.
- PATCH entries (once they start, post-v4.0.0) get their own heading like any other version — `## v4.0.1` — even though they're small, so the tag-to-changelog mapping in §11 stays exact.

---

## 13. Deprecation Policy

FoundryOS doesn't have compiled dependents, but it does have something just as real: clones, forks, bookmarks, and anyone's own notes referencing a Module, Skill, Agent, Command, or Workflow **by name**. Deleting or renaming one outright, post-public-release, silently breaks that reference. So:

1. **Mark, don't delete.** A deprecated file gets a visible note at the top pointing to its replacement (name and path), and stays in place.
2. **Minimum one MAJOR version of overlap.** A Module/Skill/Agent/Command/Workflow deprecated in `v4.x` is not removed before `v5.0.0` at the earliest.
3. **Removal is itself a MAJOR-eligible change** (§5) if removing it breaks a cross-reference elsewhere — update the referencing Workflow, Agent, Knowledge Graph file, and registry in the same change.
4. **Document the deprecation and the eventual removal separately in `CHANGELOG.md`** — two entries, two versions, so the history shows the full window rather than the thing just vanishing.

No FoundryOS file has been deprecated under this policy yet — every rename caught during the v4.0.0 audit (the `122_` module, `57-logo-system-skill`, drafting-stage slug typos) happened **before** the public tag, so it was internal correction (§2), not deprecation. This will be the actual policy the first time something needs replacing after v4.0.0 ships.

---

## 14. Compatibility Policy

For FoundryOS, the "API" anyone outside this project depends on is **filenames, slugs, and folder paths** — not a function signature. Compatibility commitment, effective from v4.0.0 forward:

- **Within a MAJOR version**, an existing Module/Skill/Agent/Command/Workflow filename or folder slug will not be renamed or moved without going through the deprecation policy (§13) first.
- **`commands/` and `.claude/commands/` filenames** are treated with the same care — a renamed command breaks a memorized slash command, exactly as a renamed CLI flag would.
- **MAJOR versions may break this deliberately** — that's what distinguishes a MAJOR from a MINOR (§5) — but the break must be called out explicitly in that version's `CHANGELOG.md` entry and `RELEASE_NOTES.md`, not buried in a file-count diff.
- **Internal structure** (which Agent owns which Skill) is explicitly **not** covered by this commitment — `VERSION.md`'s existing Versioning Note already establishes that ownership reassignment isn't a version-worthy event, and it isn't a compatibility break either, since nothing references ownership directly; everything references the Skill by its own slug.

---

## 15. Architecture Decision Protection

A small set of foundational decisions are protected from casual change even across MAJOR versions, because too much of the rest of the system structurally depends on them:

- **The ownership chain** Modules → Skills → Agents → Meta-Agent, with the Meta-Agent reading live `agents/*/AGENT.md` files rather than a hardcoded map.
- **No top-level `modules/` folder.** Modules live inside `skills/{NN}-{name}-skill/` — re-litigated and confirmed during this release; see `README.md`'s Architecture section and `CONTRIBUTING.md`'s folder-structure block.
- **`commands/` is the documentation source of truth; `.claude/commands/` is always generated**, never hand-edited (§17).
- **The C-suite Agent shape is intentionally stable.** A new Agent requires a genuinely new, non-overlapping mandate — `CONTRIBUTING.md`'s "How to add an Agent" already states this, with CBO-Agent as the precedent for what actually justifies one.
- **`registry/AGENT_REGISTRY.md` and `registry/SKILL_REGISTRY.md` are canonical** — any layer that disagrees with the registry is the one that's wrong, not the registry.

Changing any of these is a MAJOR-version decision by definition (§5), needs an explicit rationale in that version's `CHANGELOG.md` entry, and should be raised as an issue first per `CONTRIBUTING.md` rather than landed directly in a PR.

---

## 16. Brand OS Versioning

The Brand Operating System (`brand/BRAND_OS.md`, CBO-Agent, the 17 brand Skills, the 6 brand Memory files, `BRAND_GRAPH.md`, and the 13 brand Commands) does **not** get its own independent version number. It versions in lockstep with the rest of FoundryOS, for the same reason it was integrated into every existing layer rather than appended as an isolated add-on at v4.0.0: a brand layer that drifts out of sync with the product/technical layers it's supposed to describe is worse than no brand layer at all.

**Rule:** any future change to brand assets, voice, or identity that's significant enough to need its own changelog entry gets documented under whatever FoundryOS version it ships in — never as a separate "Brand vX.Y." If brand-specific work is ever large enough to feel like it deserves independent versioning, that's a signal to re-examine whether it should be its own repo, not a reason to start dual-versioning this one.

---

## 17. Command Versioning

- **`commands/*.md` is the source of truth.** Every command's Purpose, Activated Agents/Skills, Workflow, Output, and Example live here first.
- **`.claude/commands/` is always generated**, via `scripts/generate_claude_commands.py`, and is never hand-versioned or hand-edited — it has no version of its own; it simply reflects whatever state `commands/` is in. Per `CONTRIBUTING.md`, regenerate it after every `commands/` edit so the two never drift, independent of whether the edit was version-worthy.
- **Adding a command** = MINOR (§6) — it extends the existing Command Layer without changing its shape.
- **Renaming or removing a command** = goes through the deprecation policy (§13) once a version is public; doing either pre-tag is internal correction (§2), as happened with the `57` slug fix this release.
- **Total command count is tracked in `VERSION.md` and `COMMANDS.md`**, not in this file — this file states the rule, those files state the current number.

---

## 18. Skill and Agent Versioning

- **Skills and Agents are not individually versioned.** There's no `46-logo-system-skill v2` — every Skill and Agent file versions with the whole repo.
- **Adding a Module or a Skill** = MINOR (§6).
- **Adding a new Agent** is usually MINOR if it fits the existing C-suite pattern cleanly (§5's test: does anything break if you imagine it not existing yet?) — but can be folded into a MAJOR if it ships alongside other structural change, as CBO-Agent did with the v4.0.0 rebrand.
- **Reassigning which Agent owns a Skill is explicitly not a version event**, per `VERSION.md`'s existing Versioning Note — it already happened twice before v1.0.0 and is expected to keep happening as the system is used. This policy doesn't change that; it just writes it down in one more place so it doesn't get rediscovered as a "missing rule" later.
- **Renaming a Skill or Agent slug** post-public-release goes through deprecation (§13); pre-public-release renames (the `122_` module, the `57` collision fix) are internal correction (§2).

---

## 19. Examples

Concrete, worked scenarios using this policy, assuming each happens **after** v4.0.0 is tagged and live on GitHub:

| Scenario | Version change | Why |
|---|---|---|
| Add 3 new Modules and the Skill built from them | `v4.0.0` → `v4.1.0` | Existing layer (Skills) grows; shape unchanged — MINOR (§6) |
| Fix 5 broken internal links and a doc-drift error | `v4.0.0` → `v4.0.1` | No capability added or removed, applied post-tag — PATCH (§7) |
| Add the Runtime / MCP / execution-engine layer | `v4.x.x` → `v5.0.0` | New structural layer; other layers will come to depend on it — MAJOR (§5, §9) |
| Rename `46-logo-system-skill` to something clearer | Deprecation notice in `v4.x`, removal no earlier than `v5.0.0` | Slug rename breaks external references — must go through §13, not done in place |
| Remove CBO-Agent entirely (hypothetical) | MAJOR, earliest `v5.0.0`, after a deprecation cycle | Structural layer removal — protected under §15, gated by §13 |
| Fix a typo in `AGENT.md` | No version change | Doesn't meet the bar for PATCH (§7) — not tracked as a release, just a normal commit |
| The GitHub-readiness pass actually done for this release (`.gitignore`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, templates) | Stayed at `v4.0.0`, no bump | Happened pre-tag — internal correction (§2, §7), exactly as it occurred |

---

See also: [`VERSION.md`](VERSION.md) for current counts and the live roadmap, [`CHANGELOG.md`](CHANGELOG.md) for the file-by-file history this policy is grounded in, [`docs/ROADMAP.md`](docs/ROADMAP.md) for the big-picture narrative, and [`CONTRIBUTING.md`](CONTRIBUTING.md) for how day-to-day changes are made within this policy.
