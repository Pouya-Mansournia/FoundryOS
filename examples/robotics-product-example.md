# Example: Robotics Product Development

**Prompt:** *"Build a PRD for a robotics product — a warehouse-floor inventory-scanning robot for mid-size 3PLs."*

---

## Meta-Agent Result

### 1. Request Classification
Robotics / Hardware product — multi-agent (product, hardware engineering, operations).

### 2. Selected Agents
`CPO-Agent` → `CIO-Agent` → `CTO-Agent` → `COO-Agent`

### 3. Selected Skills
- `01-discovery-skill`, `04-prd-skill` (CPO-Agent) — problem framing and PRD structure
- `23-robotics-product-skill`, `41-mechatronics-skill` (CIO-Agent) — robotics architecture, integrated mechanical/electronics/embedded design
- `05-architecture-skill` (CTO-Agent) — fleet software, navigation stack, cloud backend
- `18-stage-gate-skill` (COO-Agent) — phase gates from prototype to pilot to production

### 4. Agent Execution Order
CPO-Agent → CIO-Agent / CTO-Agent (parallel — hardware and software stacks are designed together) → COO-Agent

### 5. Combined Executive Answer

**Problem & scope (CPO):** Mid-size 3PLs run cycle counts manually, walking aisles with handheld scanners — slow, error-prone, and a recurring labor cost rather than a one-time one. The PRD targets a robot that runs scheduled or on-demand inventory scans autonomously, reconciling against the WMS, and surfacing discrepancies for human follow-up rather than trying to physically correct them (that's a v2+ problem). Success metric: scan-cycle time per 10,000 SKU locations reduced by 70%+ versus manual count, with discrepancy detection accuracy ≥98% against ground truth.

**Robotics architecture (CIO):** Differential-drive base for tight-aisle maneuverability, LiDAR + camera fusion for navigation and barcode/RFID reading, designed for a fully racked warehouse with aisles as narrow as 1.2m. Mechatronics integration (`41-mechatronics-skill`) covers the full stack as one validation pass rather than three separate sign-offs: mechanical (chassis, mast for vertical scan coverage, IP-rated enclosure for dust), electronics (PCB power budget for an 8-hour shift on one charge, sensor signal integrity), and embedded (real-time control loop, RTOS choice for the navigation stack, watchdog/safety-stop firmware). Safety case treated as a first-class deliverable, not an afterthought — this operates around forklifts and people.

**Fleet & navigation software (CTO):** SLAM-based localization rather than relying solely on fixed infrastructure (no warehouse-wide beacon retrofit required, which matters for a mid-size-3PL price point). Fleet management backend handles scheduling, charging-dock routing, and WMS reconciliation via API. Architecture should assume multi-robot fleets from day one even if v1 ships single-unit pilots — retrofitting multi-robot coordination later is materially more expensive than designing for it now.

**Stage-gate plan (COO):** Four gates before general availability — (1) bench prototype: mechatronics validation pass (GD&T, PCB review, firmware test plan) complete; (2) single-aisle pilot in a controlled facility; (3) multi-aisle pilot at a design-partner 3PL with real inventory and real foot traffic; (4) production readiness — DFM sign-off, supplier qualification, EVT/DVT/PVT complete via `35-npi-manufacturing-skill` (co-owned with CIO-Agent). Don't let pilot 3 start before pilot 2's safety case is signed off — that ordering is non-negotiable given the people-proximity risk.

### 6. Contradictions / Conflicts
None identified. CIO's SLAM-based navigation and CTO's fleet-software assumption (no infrastructure retrofit) are mutually reinforcing, not competing.

### 7. Missing Inputs / Assumptions
- Assumed standard pallet racking and aisle widths (1.2–3m). Narrower or non-standard racking would change the chassis design materially.
- Assumed integration target is a generic WMS API, not a specific named system. If the design-partner 3PL runs a particular WMS, the integration spec needs that vendor's API docs before CTO work starts.
- Assumed battery swap is acceptable downtime (charging dock model) rather than requiring hot-swap. Flag if 24/7 operation without any charging window is a hard requirement.

### 8. Risks
- Regulatory/safety risk is the highest-severity item given proximity to forklifts and warehouse staff — budget real time for the safety case, not a checkbox pass.
- Battery and power budget risk: an 8-hour shift target with LiDAR + compute running continuously is tight; validate early with the actual sensor suite, not a spec-sheet estimate.
- Supplier lead time for the mechatronics BOM (motors, LiDAR, embedded compute) can dominate the schedule more than the design work itself — start supplier qualification in parallel with prototype design, not after.

### 9. Next Actions
1. Lock aisle-width and racking assumptions with the design-partner 3PL before chassis design freezes (CPO + CIO, this week).
2. Run the mechatronics validation pass (GD&T, FEA, PCB review, firmware test plan) on the bench prototype (CIO).
3. Stand up the SLAM navigation stack and fleet backend skeleton in parallel (CTO).
4. Open supplier qualification for the long-lead BOM items now, ahead of DVT (COO + CIO, shared via `35-npi-manufacturing-skill`).
