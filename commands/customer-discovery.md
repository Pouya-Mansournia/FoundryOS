# Command
/customer-discovery

## Purpose
Run a structured Customer Discovery & Problem Validation interview to validate a real customer problem before building a product or feature. Enforces the core rule: no pitching, describing, demonstrating, or defending the product before Question 14 — the interview exists to discover the truth, not to sell the idea. Use this before `/prd` or `04-prd-skill` whenever a problem hasn't yet been validated against real customer evidence, or after `/idea-discovery` once the idea has cleared the existing-solutions check and needs direct customer evidence.

## Activated Agents
- CPO-Agent

## Activated Skills
- `60-customer-discovery-interview-skill` — the structured interview (Context, Pain, Business Impact, Current Solution, Buying Reality, Commitment), Founder Score, recommendation, and validation dashboard
- `01-discovery-skill` — problem framing that the interview questions validate against

## Workflows
- None dedicated — runs standalone per interview, or as evidence input into `01-new-product-workflow`'s discovery phase.

## Output
- Interview Record: Customer/Company, Interviewee Role, Industry, Date, Interviewer
- Context, Pain Severity (1–5), Business Impact (Estimated Cost, Time Lost, People/Teams Affected), Current Solution (Alternative, Cost, Limitations), Buying Reality (User, Champion, Decision Maker, Budget Owner), Commitment & Next Step
- Founder Score (Pain, Frequency, Business Impact, Current Spend, Buying Intent — /25) and Recommendation: **KILL**, **INVESTIGATE**, or **VALIDATE / BUILD**
- Most Important Customer Sentence (verbatim quote)
- Validation Dashboard aggregate across stored interviews: repeated problems, pain severity, frequency, business impact, existing alternatives/spend, decision makers, budget owners, buying signals, pilot/commercial interest, common quotes

## Example
`/customer-discovery Run a discovery interview with the ops lead at Acme Corp about how they currently handle vendor invoice reconciliation.`
`/customer-discovery Score this completed interview and tell me KILL, INVESTIGATE, or VALIDATE/BUILD: [paste interview notes].`
