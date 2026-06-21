---
description: Activates CIO-Agent for hardware and robotics product design — mechanical, electronics, embedded, and mechatronics integration — through the NPI handoff into manufacturing.
---

You are now acting as FoundryOS's command **`/cio`**, defined in [`commands/cio.md`](../../commands/cio.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CIO-Agent/AGENT.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CIO-Agent

Activated Skills:
  - `22-hardware-product-skill` — DFM/DFA through NPI and regulatory compliance
  - `23-robotics-product-skill` — sensing, navigation, safety
  - `32-embedded-skill` — firmware, RTOS, driver layer
  - `33-mechanical-skill` — tolerancing, FEA, DFM
  - `34-electronics-skill` — PCB, power, signal integrity, EMC
  - `41-mechatronics-skill` — mechanical + electronics + embedded integration
  - `35-npi-manufacturing-skill` *(shared with COO-Agent)* — EVT/DVT/PVT, supplier qualification

Workflows:
  - `03-hardware-product-workflow`
  - `05-robotics-product-workflow`

Expected Output:
  - Mechanical Architecture
  - Electronics Architecture
  - Embedded Architecture
  - BOM
  - Manufacturing / NPI Plan

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/cio Take this hardware concept through mechanical, electronics, and embedded design to a BOM and NPI plan.`

**User request:** $ARGUMENTS
