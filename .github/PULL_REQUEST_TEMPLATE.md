## What changed

One logical change — a new Skill, a new Command, a doc fix. Don't bundle unrelated structural changes (see [`CONTRIBUTING.md`](../CONTRIBUTING.md)).

## Why

## Files touched

List every file you touched, including registries and knowledge-graph files — these are the easiest to forget and the most common source of drift.

- [ ] `registry/SKILL_REGISTRY.md` / `registry/AGENT_REGISTRY.md` updated, if applicable
- [ ] `knowledge-graph/*.md` updated, if applicable
- [ ] `README.md` updated, if this changes the Architecture diagram or folder structure
- [ ] Relevant `tests/*.md` checked against this change
- [ ] `.claude/commands/` regenerated via `python3 scripts/generate_claude_commands.py`, if you touched `commands/`

## Checklist

- [ ] Follows the existing format/template for this file type (see `CONTRIBUTING.md`'s Style Guide)
- [ ] No hardcoded company/product/brand names — stays generic
- [ ] Relative links checked and resolve to real files
