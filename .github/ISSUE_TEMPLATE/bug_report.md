---
name: Inconsistency / Broken Reference
about: Report a broken link, wrong file reference, naming drift, or other structural inconsistency
title: "[Inconsistency] "
labels: bug
assignees: ''
---

## What's inconsistent

A clear description of what's broken or wrong — a broken relative link, a Skill referenced that doesn't exist, an Agent's documented Skills list that doesn't match its `AGENT.md`, a Workflow pointing at a Command that was renamed, etc.

## Where

File path(s), and line number(s) if you have them.

## Expected

What it should say, or what it should point to instead.

## Additional context

How you found it (reading a specific file, following a command end-to-end, running `scripts/generate_claude_commands.py`, etc.), and whether it affects routing — Meta-Agent classification, a Workflow's Agent Execution Order, or a Command's Activated Agents/Skills.
