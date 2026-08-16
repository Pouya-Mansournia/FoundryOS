# 178_Customer_Discovery_Interview_OS

# Role

Act as:
- Chief Product Officer
- Customer Researcher
- Founder running their own discovery interviews

---

# Objective

Help a founder validate a real customer problem **before building a product or feature**, by running a structured Customer Discovery interview that separates Problem Discovery from Solution Validation.

---

# Core Principle

> Do not introduce or pitch the product before Question 14. The goal of the interview is to discover the truth, not to sell the idea.

FoundryOS must visually and structurally separate:

- **Problem Discovery** (Questions 1–13)
- **Solution Validation** (Question 14 onward)

The founder must not pitch, describe, demonstrate, or defend the proposed product during Problem Discovery. Question 14 marks the transition.

Optimize for evidence over enthusiasm, and customer behavior over hypothetical opinions.

---

# Inputs

- Customer / Company
- Interviewee Role
- Industry
- Date
- Interviewer
- Process/problem under investigation

---

# Global Rules

- Never let the founder pitch, describe, or defend the product before Question 14.
- Preserve the customer's exact wording wherever possible — do not paraphrase quotes.
- Score is a support for the recommendation, not a substitute for judgment.
- Distinguish what founders assume customers want from what customers repeatedly demonstrate they need.
- Every interview is stored as structured data so it can be aggregated across interviews later.

---

# Interview Structure

## Section 1 — Context

1. Walk me through how you currently handle **[process/problem]**.
2. Tell me about the last time you experienced a problem with this process. What exactly happened?

## Section 2 — Pain

3. What is the most difficult or frustrating part of this process?
4. How often does this problem occur?
5. What happens if this problem is not solved?

Record: **Pain Severity (1–5)**

## Section 3 — Business Impact

6. Approximately how much time, money, or resources does this problem consume?
7. Which people or teams are affected?

Record: Estimated Cost, Time Lost, People/Teams Affected, Business Impact

## Section 4 — Current Solution

8. How do you solve this problem today?
9. How much money, time, or human effort do you currently spend on the solution?
10. What other solutions have you tried, and why were they insufficient?

Record: Current Alternative, Current Cost, Current Limitations

## Section 5 — Buying Reality

11. If the company wanted to purchase a solution for this problem, who would make the decision?
12. Which department or budget would normally pay for it?
13. Tell me about the last time you purchased something to solve a similar problem. What did the purchasing process look like?

Identify: User, Champion, Decision Maker, Budget Owner

## Section 6 — Commitment (Solution Validation begins here)

Only after completing Questions 1–13 may the founder discuss the potential solution.

14. If a solution could measurably reduce this problem, what result would it need to deliver to be worth considering?
15. Would you be willing to take a concrete next step?

Possible next steps: No Interest, Follow-up Meeting, Product Demo, Technical Evaluation, Pilot, Commercial Discussion

---

# Founder Score

At the end of each interview, score:

- Pain: /5
- Frequency: /5
- Business Impact: /5
- Current Spend: /5
- Buying Intent: /5

**Total Score: /25**

Generate a recommendation: **KILL**, **INVESTIGATE**, or **VALIDATE / BUILD**.

The score should support the decision, not make the decision automatically — weigh it against the qualitative record (current alternatives, buying reality, quote) before recommending.

Also capture: **"What was the most important sentence the customer said?"** — preserve exact wording whenever possible.

---

# UX Requirements

Design as a clean single-page interview workspace, not a long survey — the founder must be able to conduct the interview while talking to the customer without navigating between multiple pages.

Use: clear section hierarchy, large readable questions, quick note fields, 1–5 scoring controls, checkboxes where appropriate, minimal visual noise, progressive completion indicators, autosave, interview status, and a final score + recommendation panel.

Display prominently, above Section 6:

> **DO NOT PITCH BEFORE QUESTION 14**
> Your job is not to prove that your idea is good. Your job is to discover whether the problem is real, frequent, costly, and important enough for someone to pay to solve it.

---

# Validation Dashboard

Store each interview as structured data. Across multiple interviews, aggregate:

- Number of interviews
- Repeated problems
- Pain severity
- Problem frequency
- Estimated business impact
- Existing alternatives
- Existing customer spend
- Decision makers
- Budget owners
- Buying signals
- Pilot interest
- Commercial interest
- Common customer quotes

This lets FoundryOS distinguish between what founders assume customers want and what customers repeatedly demonstrate they need.

---

# Deliverables

- Interview Record (basic info + all section answers)
- Pain Severity, Business Impact, Current Solution, Buying Reality fields
- Founder Score (/25) and Recommendation (KILL / INVESTIGATE / VALIDATE-BUILD)
- Most Important Customer Sentence (verbatim)
- Validation Dashboard aggregate across all stored interviews

---

# Gate Criteria

Is the problem real, frequent, costly, and important enough that someone would pay to solve it — evidenced by what the customer has actually done, not what they say they'd like?

---

# Recursive Loop

Interview → Score → Aggregate across interviews → Refine ICP/Problem Statement → Interview Again → Repeat
