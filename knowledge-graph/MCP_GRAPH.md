# MCP Graph

## Purpose

Maps how an MCP Tool Request declared inside a Skill's output connects back to the Command that triggered it and forward to the Artifact it improves — so a request with no clear origin or no clear destination is a structural warning sign, not a style choice. Companion to `mcp-layer/MCP_LAYER.md`, which defines the declaration format this graph traces.

## Nodes

Command, Meta-Agent, Skill (any Skill capable of emitting a request), MCP Tool Request (Need / Category / If-unavailable), Category (`web-search`, `code-repo`, `project-tracker`, `communications`, `calendar`, `file-storage`, `database`, `other`), Host Assistant's MCP Client, Fallback Assumption, Missing Inputs/Assumptions section (of the Combined Executive Answer), Artifact.

## Relationships

- **A Command always precedes an MCP Tool Request**, never the reverse — the request only becomes concrete once the Meta-Agent has classified the ask and a specific Skill is mid-output on it (see `mcp-layer/MCP_LAYER.md`'s Pipeline Placement), not something declared speculatively ahead of time.
- **Every MCP Tool Request resolves exactly one of two ways**, never both and never neither: the Host Assistant's MCP Client fulfills it and the result folds into the Skill's output, or the request's own If-unavailable clause becomes a Fallback Assumption that surfaces in the Combined Executive Answer's Missing Inputs/Assumptions section.
- **An MCP Tool Request never blocks an Artifact.** Unlike the PRD → Architecture dependency in `ARTIFACT_GRAPH.md`, where a downstream artifact genuinely cannot be built correctly before its upstream one is stable, an Artifact here is produced either way — flagged if the lookup didn't happen, not withheld.
- **Category determines which real connector could fulfill a request**, but FoundryOS itself owns no mapping from Category to a specific server — that binding lives entirely in whichever assistant is running the session (Claude Code's configured MCP servers, Cowork's connected connectors, or another host's equivalent), which is why this graph stops at "Host Assistant's MCP Client" as a black box rather than naming real servers.
- **Most Skills emit zero MCP Tool Requests.** The absence of this node in a given run's output is the expected case, not a gap — see `mcp-layer/MCP_LAYER.md`'s "Which Skills This Applies To."

## Dependencies

```
Command → Meta-Agent → selected Skill(s)
Skill step needing live/external truth → MCP Tool Request (Need + Category + If-unavailable declared inline)
MCP Tool Request → Host Assistant's MCP Client (Category match found) → data folds into Skill output → Artifact
MCP Tool Request → (no Category match found) → Fallback Assumption → Missing Inputs/Assumptions
    section of the Combined Executive Answer → Artifact (produced anyway, flagged not blocked)
```

## Graph Structure

```
        Command
           ↓
       Meta-Agent
           ↓
          Skill
           ↓
   (does this step need live/external truth?)
      ↓                        ↓
     no                       yes
      ↓                        ↓
  (no request              MCP Tool Request
   emitted)              (Need / Category / If-unavailable)
      │                        ↓
      │              ┌─────────┴─────────┐
      │        connector match      no connector match
      │              ↓                    ↓
      │      Host Assistant's       Fallback Assumption
      │        MCP Client                 ↓
      │              ↓            Missing Inputs/Assumptions
      │        data folded in        (Combined Executive Answer)
      │              │                    │
      └──────────────┴─────────┬──────────┘
                                ↓
                            Artifact
```

## Examples

CFO-Agent's financial-modeling Skill declares a `web-search` request for 3 named competitors' current pricing while building a Financial Model; if Claude Code's session has a search-capable MCP server connected, the returned pricing folds directly into the model, and the Financial Model Artifact in `ARTIFACT_GRAPH.md`'s chain is produced with live figures. If no such server is connected, the request's If-unavailable clause pulls the last-known figures from `memory/market-memory.md` instead, the Combined Executive Answer's Missing Inputs/Assumptions section states the figures' as-of date, and the same Financial Model Artifact still gets produced — just flagged rather than blocked. Either path reaches the same downstream node in `ARTIFACT_GRAPH.md`; this graph only describes how the number inside it got sourced.
