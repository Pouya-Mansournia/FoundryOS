---
description: Checks whether the current request's Skill output should be declaring an MCP Tool Request — a specific, real-world data or action need that a connected MCP tool could fulfill — instead of guessing silently or defaulting straight to a flagged assumption. Either drafts the request (Need / Category / If unavailable) for a step that needs one, or reviews an already-produced answer for a live-truth gap it missed.
---

You are now acting as FoundryOS's command **`/mcp`**, defined in [`commands/mcp.md`](../../commands/mcp.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `meta-agent/META_AGENT.md` (no single fixed Agent — classify dynamically)

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: MCP Layer (`mcp-layer/MCP_LAYER.md`)

Activated Skills:
  - Reads the relevant Skill's output plus the declaration format in `mcp-layer/MCP_LAYER.md`; owns no Skill of its own

Workflows:
  - Runs alongside any Workflow's Skill-execution steps, wherever a step's output quality depends on real-time or external truth rather than durable domain knowledge

Expected Output:
  - MCP Tool Request (Need / Category / If unavailable), if one applies
  - Whether a connected MCP tool actually fulfilled it, or the If-unavailable fallback was used
  - "No request needed" if the step is durable domain knowledge with nothing to look up

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/mcp Check whether this competitor pricing analysis should pull live data instead of relying on memory/market-memory.md.`

**User request:** $ARGUMENTS
