# Example: Hardware Manufacturing Readiness Plan

**Prompt:** *"Create a manufacturing readiness plan — we're moving our hardware product from prototype to production."*

---

## Meta-Agent Result

### 1. Request Classification
Operations / Hardware manufacturing — multi-agent.

### 2. Selected Agents
`CIO-Agent` → `COO-Agent` → `CFO-Agent`

### 3. Selected Skills
- `22-hardware-product-skill`, `35-npi-manufacturing-skill` (CIO-Agent) — DFM/DFA, EVT/DVT/PVT, regulatory compliance
- `09-operations-skill`, `18-stage-gate-skill`, `28-risk-management-skill`, `35-npi-manufacturing-skill` (COO-Agent) — supply chain, process control, stage gates, risk register; `35-npi-manufacturing-skill` is co-owned with CIO-Agent and run once, jointly, not duplicated
- `07-finance-skill` (CFO-Agent) — CAPEX and per-unit cost modeling

### 4. Agent Execution Order
CIO-Agent → COO-Agent → CFO-Agent

### 5. Combined Executive Answer

**Engineering readiness (CIO):** Before committing to tooling, run a full DFM/DFA pass on the current prototype — tolerancing, material substitutions for volume cost, and assembly-step count, since every manual assembly step is a recurring labor cost at volume that a one-time engineering fix can remove. Lock the BOM and confirm second-source availability for any single-sourced part — single-source components are the most common reason production ramps slip 60–90 days. Regulatory compliance plan (CE/FCC/ISO/IEC as applicable) needs to start now, not at PVT — certification lead times routinely run 6–12 weeks and are a frequent critical-path item teams discover too late.

**NPI sequencing (CIO + COO, shared):** Run EVT (engineering validation, confirms the design works) → DVT (design validation, confirms it works at representative volume and tooling) → PVT (production validation, confirms the actual production line and process produce consistent units) as three distinct, gated phases — don't compress them to save calendar time. The build quantities at each stage (typically 10s at EVT, 100s at DVT, 1,000s at PVT) should be enough to catch the failure modes that only show up at that scale; compressing PVT specifically is the most common way a product ships with a defect rate that wasn't visible in smaller builds.

**Operations & supply chain (COO):** Supplier qualification should run in parallel with DVT, not after — qualifying a contract manufacturer and tooling vendor takes real calendar time and shouldn't sit on the critical path after engineering is already done. Process control plan (incoming QC, in-line QC, outgoing QC with defined AQL) needs to exist before PVT starts, not be improvised during it. Risk register should explicitly carry supply chain concentration risk (any single-source supplier or single-region manufacturing) as a named, owned risk — not an assumed one.

**Financial readiness (CFO):** Per-unit cost model needs to be locked at the BOM-plus-labor-plus-overhead level before committing to a production order quantity, with a clear view of how unit cost curves down with volume (and at what volume breakpoints, since tooling amortization changes the curve in steps, not smoothly). CAPEX for tooling should be sized against a realistic first-year volume forecast, not the optimistic case — tooling is a sunk, non-recoverable cost if volume undershoots.

### 6. Contradictions / Conflicts
None identified — CIO's "don't compress PVT" and COO's "process control before PVT" reinforce each other; both push against the same time-pressure failure mode.

### 7. Missing Inputs / Assumptions
- Assumed a single contract manufacturer model (not in-house assembly). In-house production would shift several of the COO recommendations (process control, QC) to be designed for an internal line rather than a vendor relationship.
- Assumed the product has already passed EVT informally (a working prototype exists). If EVT hasn't formally happened yet, that's the actual next gate, not DVT.
- No specific regulatory regions were given — compliance scope (CE for EU, FCC for US, etc.) depends on target markets; assumed multi-region given no constraint stated, which is the more conservative (and more expensive/slower) assumption.

### 8. Risks
- Single-source components are the highest-likelihood schedule risk identified — flagged explicitly because it's the most common and most avoidable cause of production delays.
- Compressed PVT to hit a launch date is the highest-severity quality risk — defects that ship at volume are far more expensive than the calendar time saved by skipping validation.
- Regulatory certification lead time, if not started early, can silently become the actual critical path even when engineering and operations are both on schedule.

### 9. Next Actions
1. Run the DFM/DFA pass and lock the BOM, flagging any single-sourced parts for second-sourcing (CIO, immediate).
2. Start regulatory certification testing in parallel with DVT, not after (CIO).
3. Begin contract manufacturer and tooling vendor qualification now, in parallel with DVT (COO).
4. Lock the per-unit cost model and tooling CAPEX against a realistic (not optimistic) first-year volume forecast before placing a production order (CFO).
