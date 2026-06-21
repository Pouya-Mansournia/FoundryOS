# Command
/hardware

## Purpose
Runs the hardware product workflow end to end — requirements through mechanical/electronics design, BOM, NPI, and the cost model behind it.

## Activated Agents
- CPO-Agent
- CIO-Agent
- COO-Agent
- CFO-Agent

## Activated Skills
- `01-discovery-skill`, `04-prd-skill` (CPO)
- `22-hardware-product-skill`, `33-mechanical-skill`, `34-electronics-skill`, `41-mechatronics-skill`, `35-npi-manufacturing-skill` (CIO)
- `35-npi-manufacturing-skill`, `09-operations-skill`, `18-stage-gate-skill`, `28-risk-management-skill` (COO)
- `07-finance-skill` (CFO)

## Workflows
- `03-hardware-product-workflow`

## Output
- BOM
- Manufacturing / NPI Plan
- Cost Analysis
- Roadmap

## Example
`/hardware Take this hardware concept from requirements through a BOM and manufacturing plan.`
