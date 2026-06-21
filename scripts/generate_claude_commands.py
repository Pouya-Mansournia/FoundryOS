#!/usr/bin/env python3
"""
Generate .claude/commands/ from commands/.

commands/*.md is FoundryOS's documentation-style command spec: Purpose,
Activated Agents, Activated Skills, Workflows, Output, Example. It's written
to be read by a human or any assistant with file access.

.claude/commands/*.md is the executable layer Claude Code actually loads as
native slash commands. This script regenerates that folder from commands/ so
the two never drift: each generated file is a thin wrapper that tells Claude
Code to read the relevant live Agent file(s) (and meta-agent/META_AGENT.md
for multi-Agent commands) off disk before answering, rather than freezing a
snapshot of their content at generation time.

Usage:
    python3 scripts/generate_claude_commands.py

Run this from anywhere — paths are resolved relative to the repo root
(the parent directory of this script), not the current working directory.
Re-run it any time a file under commands/ changes. Files inside
.claude/commands/ are generated output — don't hand-edit them; edits will be
overwritten the next time this script runs.
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(REPO_ROOT, "commands")
DST_DIR = os.path.join(REPO_ROOT, ".claude", "commands")

# Maps the Agent names used in commands/*.md's "## Activated Agents" bullets
# to the AGENT.md file Claude Code should read live before answering.
AGENT_FILE_MAP = {
    "CEO-Agent": "agents/CEO-Agent/AGENT.md",
    "CPO-Agent": "agents/CPO-Agent/AGENT.md",
    "CTO-Agent": "agents/CTO-Agent/AGENT.md",
    "CIO-Agent": "agents/CIO-Agent/AGENT.md",
    "COO-Agent": "agents/COO-Agent/AGENT.md",
    "CFO-Agent": "agents/CFO-Agent/AGENT.md",
    "CRO-Agent": "agents/CRO-Agent/AGENT.md",
    "CMO-Agent": "agents/CMO-Agent/AGENT.md",
    "CHRO-Agent": "agents/CHRO-Agent/AGENT.md",
    "CBO-Agent": "agents/CBO-Agent/AGENT.md",
    "Meta-Agent": "meta-agent/META_AGENT.md",
    "Planner Agent": "planner-agent/PLANNER_AGENT.md",
    "Critic Agent": "critic-agent/CRITIC_AGENT.md",
    "Reflection Agent": "reflection-agent/REFLECTION_AGENT.md",
}


def parse_section(lines, header):
    """Return the raw lines under a '## {header}' section, until the next '## ' or EOF."""
    out = []
    capture = False
    for line in lines:
        if line.startswith("## "):
            if capture:
                break
            if line.strip() == f"## {header}":
                capture = True
                continue
        elif capture:
            out.append(line)
    return out


def extract_agent_names(section_lines):
    names = []
    for l in section_lines:
        l = l.strip()
        if not l.startswith("-"):
            continue
        l = l.lstrip("- ").strip()
        m = re.match(r"^([A-Za-z\-]+(?:-Agent|Agent))", l)
        names.append(m.group(1) if m else l.split(" ")[0])
    return names


def block_or(lines_in, fallback):
    """Render a section's bullet lines indented two spaces, or a fallback if empty."""
    items = [x.strip() for x in lines_in if x.strip()]
    if not items:
        return fallback
    return "\n".join("  " + it for it in items)


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(SRC_DIR, "*.md")))
    if not files:
        raise SystemExit(f"No command files found in {SRC_DIR} — check REPO_ROOT resolution.")

    written = []
    for path in files:
        name = os.path.basename(path)[:-3]
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        lines = content.split("\n")

        slug = f"/{name}"
        for i, l in enumerate(lines):
            if l.strip() == "# Command" and i + 1 < len(lines):
                cand = lines[i + 1].strip()
                if cand.startswith("/"):
                    slug = cand
                break

        purpose_lines = parse_section(lines, "Purpose")
        purpose = " ".join(x.strip() for x in purpose_lines if x.strip())

        agents_lines = parse_section(lines, "Activated Agents")
        skills_lines = parse_section(lines, "Activated Skills")
        workflows_lines = parse_section(lines, "Workflows")
        output_lines = parse_section(lines, "Output")
        example_lines = parse_section(lines, "Example")

        agent_names = extract_agent_names(agents_lines)
        agent_file_lines = []
        seen = set()
        for a in agent_names:
            if a in AGENT_FILE_MAP and a not in seen:
                agent_file_lines.append(f"- `{AGENT_FILE_MAP[a]}`")
                seen.add(a)
        if not agent_file_lines:
            agent_file_lines.append(
                "- `meta-agent/META_AGENT.md` (no single fixed Agent — classify dynamically)"
            )

        skills_block = block_or(
            skills_lines, "  _(see `Activated Agents` above — owns no Skill of its own)_"
        )
        workflows_block = block_or(
            workflows_lines, "  _(none specified — Meta-Agent selects if applicable)_"
        )
        output_block = block_or(output_lines, "  _(see Purpose above)_")
        example_block = "\n".join(x for x in example_lines if x.strip())

        agents_display_items = [x.strip().lstrip("- ").strip() for x in agents_lines if x.strip()]
        agents_display = "; ".join(agents_display_items) if agents_display_items else "see above"

        body = f'''---
description: {purpose}
---

You are now acting as FoundryOS's command **`{slug}`**, defined in [`commands/{name}.md`](../../commands/{name}.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
{chr(10).join(agent_file_lines)}

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: {agents_display}

Activated Skills:
{skills_block}

Workflows:
{workflows_block}

Expected Output:
{output_block}

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: {example_block}

**User request:** $ARGUMENTS
'''

        dst_path = os.path.join(DST_DIR, f"{name}.md")
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(body)
        written.append(name)

    print(f"Generated {len(written)} files in {DST_DIR}:")
    for w in written:
        print(" -", w)


if __name__ == "__main__":
    main()
