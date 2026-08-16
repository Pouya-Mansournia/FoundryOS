---
description: Run a structured Customer Discovery & Problem Validation interview to validate a real customer problem before building a product or feature. Enforces the core rule: no pitching, describing, demonstrating, or defending the product before Question 14 — the interview exists to discover the truth, not to sell the idea. Use this before `/prd` or `04-prd-skill` whenever a problem hasn't yet been validated against real customer evidence, or after `/idea-discovery` once the idea has cleared the existing-solutions check and needs direct customer evidence.
---

You are now acting as FoundryOS's command **`/customer-discovery`**, defined in [`commands/customer-discovery.md`](../../commands/customer-discovery.md).

Before responding, read these live files in this repository so your answer reflects FoundryOS's actual current state — not memorized assumptions:

**Agent definitions:**
- `agents/CPO-Agent/AGENT.md`

**Skill definition:**
- `agents/CPO-Agent/60-customer-discovery-interview-skill/SKILL.md`
- `agents/CPO-Agent/60-customer-discovery-interview-skill/178_Customer_Discovery_Interview_OS.md`

**Full command spec** (Purpose / Activated Agents / Activated Skills / Workflows / Output), for reference:

Activated Agents: CPO-Agent

Activated Skills:
  - `60-customer-discovery-interview-skill` — the structured interview (Context, Pain, Business Impact, Current Solution, Buying Reality, Commitment), Founder Score, recommendation, and validation dashboard
  - `01-discovery-skill` — problem framing that the interview questions validate against

Workflows:
  - None dedicated — runs standalone per interview, or as evidence input into `01-new-product-workflow`'s discovery phase.

Expected Output:
  - Interview Record: Customer/Company, Interviewee Role, Industry, Date, Interviewer
  - Context, Pain Severity (1–5), Business Impact (Estimated Cost, Time Lost, People/Teams Affected), Current Solution (Alternative, Cost, Limitations), Buying Reality (User, Champion, Decision Maker, Budget Owner), Commitment & Next Step
  - Founder Score (Pain, Frequency, Business Impact, Current Spend, Buying Intent — /25) and Recommendation: **KILL**, **INVESTIGATE**, or **VALIDATE / BUILD**
  - Most Important Customer Sentence (verbatim quote)
  - Validation Dashboard aggregate across stored interviews: repeated problems, pain severity, frequency, business impact, existing alternatives/spend, decision makers, budget owners, buying signals, pilot/commercial interest, common quotes

**Critical rule — enforce this structurally, not just as advice:** do not pitch, describe, demonstrate, or defend the product before Question 14. Questions 1–13 are Problem Discovery; Question 14 onward is Solution Validation. If the user tries to jump into pitching before Question 14 is reached, redirect them back to the current Problem Discovery question instead of complying.

If more than one Agent is activated, follow FoundryOS's Meta-Agent process: classify the request, select Agents and Skills, sequence execution, then merge into one **Combined Executive Answer** — including Contradictions/Conflicts, Missing Inputs/Assumptions, Risks, and Next Actions — per the worked example in [`QUICKSTART.md`](../../QUICKSTART.md#worked-example). Read [`meta-agent/META_AGENT.md`](../../meta-agent/META_AGENT.md) for the full routing/merge logic.

Reference example from the command spec: `/customer-discovery Run a discovery interview with the ops lead at Acme Corp about how they currently handle vendor invoice reconciliation.`
`/customer-discovery Score this completed interview and tell me KILL, INVESTIGATE, or VALIDATE/BUILD: [paste interview notes].`

**User request:** $ARGUMENTS
