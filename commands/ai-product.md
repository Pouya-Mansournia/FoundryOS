# Command
/ai-product

## Purpose
Runs the AI product workflow — requirements, AI/data architecture, and evaluation strategy. CIO-Agent joins only if on-device or edge inference is in scope.

## Activated Agents
- CPO-Agent
- CTO-Agent
- CIO-Agent *(conditional — on-device/edge inference only)*

## Activated Skills
- `01-discovery-skill`, `04-prd-skill` (CPO)
- `21-ai-product-skill`, `31-ai-architecture-skill`, `30-data-architecture-skill` (CTO)
- `32-embedded-skill` (CIO, conditional)

## Workflows
- `04-ai-product-workflow`

## Output
- AI Architecture
- Data & Evaluation Strategy
- PRD

## Example
`/ai-product Define the data, model, and evaluation strategy for an AI feature that predicts customer churn.`
