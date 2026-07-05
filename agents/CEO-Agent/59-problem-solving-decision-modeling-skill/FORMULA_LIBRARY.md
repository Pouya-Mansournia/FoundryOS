# Formula Library — 59-problem-solving-decision-modeling-skill

Reusable, domain-neutral quantitative formulas selected by `176_Solution_Formula_OS.md`'s Formula Selection Protocol — never dumped wholesale into a response. Every entry states purpose, equation, variables, units, assumptions, valid/invalid use, interpretation, and common mistakes. Examples are generic (software, robotics, manufacturing, SaaS, AI) — substitute the actual domain object (order, mission, inference, unit, session) for whatever this library calls "transaction" or "unit."

---

## 1. Basic Outcome and Delta
```
Absolute Change = New Value - Baseline Value
Relative Change = (New Value - Baseline Value) / Baseline Value
Percentage Change = Relative Change × 100
```
Use relative change only when the baseline is nonzero and meaningful. Common mistake: reporting a percentage change off a near-zero or noisy baseline as if it were stable.

## 2. Weighted Additive Model
```
Total Value = Base Value + Σ(weight_i × quantity_i)
```
Uses: dynamic pricing, resource consumption, workload estimation, risk accumulation, BOM variable cost, compute-cost estimation, complexity scoring. Invalid when interactions, saturation, discontinuities, or multiplicative effects dominate — additive models understate compounding effects.

## 3. Fixed and Variable Cost
```
Total Cost = Fixed Cost + Variable Cost per Unit × Volume
Total Cost = Fixed Cost + Σ(unit_cost_i × quantity_i)
```
Common mistake: burying a fixed cost inside a per-unit rate, which makes unit economics look worse at low volume and better than reality at high volume.

## 4. Unit Economics
```
Unit Contribution = Unit Revenue - Unit Variable Cost
Contribution Margin % = Unit Contribution / Unit Revenue
Total Contribution = Unit Contribution × Units
Break-Even Volume = Fixed Cost / Unit Contribution
```
Invalid: computing break-even when unit contribution is zero or negative, unless explicitly modeling loss minimization (then say so).

## 5. Revenue Model
```
Revenue = Price × Quantity
Expected Revenue = Eligible Population × Conversion Rate × Average Transaction Value
Net Revenue = Gross Revenue - Discounts - Refunds - Credits
MRR = Active Paying Accounts × Average Revenue per Account   (subscription systems)
```
Common mistake: reporting gross revenue as if it were net, overstating the real economics.

## 6. Funnel Model
```
Stage Conversion = Output of Stage / Input to Stage
End-to-End Conversion = Π(Stage Conversion_i)
Expected Outcomes = Eligible Population × End-to-End Conversion
```
Identify denominator changes between stages explicitly. Invalid to mix user-level and event-level funnels in the same chain without reconciling the unit of count.

## 7. Average Value and Items
```
Average Value per Transaction = Total Transaction Value / Number of Transactions
Average Items per Transaction = Total Items / Number of Transactions
```
Map "transaction" to order, job, run, task, session, batch, or mission as the domain requires. Common mistake: an average that hides a bimodal or segment-driven distribution — check the segment split before trusting the average.

## 8. Cost per Unit and Cost per Outcome
```
Cost per Input = Total Relevant Cost / Number of Inputs
Cost per Completed Outcome = Total Relevant Cost / Number of Completed Outcomes
```
Examples: cost per item, cost per order, cost per inference, cost per robot mission, cost per manufactured unit, cost per qualified lead. The denominator must match the actual economic object — cost per "user" and cost per "active user" are not interchangeable.

## 9. Profit and Net Impact
```
Profit = Revenue - Total Cost
Incremental Profit = Incremental Revenue + Avoided Cost - Incremental Operating Cost - Implementation Cost - Expected Risk Cost
Net Present Value = Σ(Cash Flow_t / (1 + discount_rate)^t) - Initial Investment
```
Common mistake: an "incremental profit" claim that omits implementation cost or expected risk cost — this is the single most common source of unsupported ROI claims.

## 10. Return on Investment
```
ROI = (Total Benefit - Total Investment) / Total Investment
Payback Period = Initial Investment / Periodic Net Benefit
```
Do not compare initiatives with materially different risk levels or time horizons using ROI alone — pair it with payback period and a stated risk level.

## 11. Expected Value Under Uncertainty
```
Expected Value = Σ(probability_i × outcome_i)
Expected Loss = Probability of Failure × Impact of Failure
Risk-Adjusted Value = Expected Benefit - Expected Loss - Implementation Cost
```
Requires actual probability estimates, labeled as assumptions if not measured — never present a made-up probability as data.

## 12. Threshold Decision Rule
```
Decision =
    Action A, if x < threshold
    Action B, if threshold ≤ x < upper_threshold
    Action C, if x ≥ upper_threshold
```
Every threshold needs: rationale, source, sensitivity, edge behavior, fallback, review frequency, segment applicability. Never present a threshold as a universal constant — state what would change it.

## 13. Piecewise Function
```
f(x) =
    rule_1(x), condition_1
    rule_2(x), condition_2
    ...
    fallback(x), otherwise
```
Uses: pricing, service levels, control policies, alerting, capacity rules, risk tiers, quality gates. Requires complete boundary coverage and no contradictory branches — check both explicitly before shipping the rule.

## 14. Multiplicative Coefficient Model
```
Adjusted Value = Base Value × Π(coefficient_i)
Adjusted Value = Base Value × (1 + Σ(adjustment_i))
```
The two forms are not interchangeable — the first compounds, the second doesn't. Common mistake: applying both forms to the same base value, double-counting the adjustment.

## 15. Capacity Utilization
```
Utilization = Demand / Available Capacity
Effective Capacity = Nominal Capacity × Availability × Efficiency
Headroom = Effective Capacity - Expected Demand
```
Systems operating near full utilization experience nonlinear delay growth — don't extrapolate queue/delay behavior linearly near capacity.

## 16. Throughput, Cycle Time, and Work in Progress
```
Throughput = Completed Units / Time
Cycle Time = Total Processing Time / Completed Units
Work in Progress ≈ Throughput × Cycle Time
```
Little's Law (the WIP relationship above) only holds when the system is reasonably stable and units/measurement windows are consistent across all three terms.

## 17. Availability and Reliability
```
Availability = Uptime / Total Time
Availability = MTBF / (MTBF + MTTR)
Failure Rate = Failed Units / Exposed Units
Success Rate = Successful Outcomes / Attempted Outcomes
System Reliability = Π(component_reliability_i)   (serial system, independent components)
```
State the independence assumption explicitly — correlated component failures (shared power supply, shared vendor) invalidate the simple product form.

## 18. Quality and Yield
```
First Pass Yield = Units Passing Without Rework / Total Units
Defect Rate = Defective Units / Total Units
Scrap Rate = Scrapped Units / Total Units
Rolled Throughput Yield = Π(process_step_yield_i)
```

## 19. Experiment Lift
```
Absolute Lift = Treatment Metric - Control Metric
Relative Lift = (Treatment Metric - Control Metric) / Control Metric
Conversion Rate = Successful Users / Eligible Users   (binary outcomes)
```
Requires sample size, confidence interval, test duration, randomization unit, exposure integrity, novelty-effect check, guardrails, and both practical and statistical significance. Never claim success from a positive point estimate alone.

## 20. Weighted Decision Score
```
Option Score = Σ(weight_i × normalized_score_i)
```
Weights must sum to 1 (or 100%), scoring scales must be defined, normalization method must be visible, and a sensitivity analysis is required. Keep veto constraints (hard no's) separate from weighted preferences — don't let a high score overrule a disqualifying constraint.

## 21. RICE
```
RICE Score = Reach × Impact × Confidence / Effort
```
A prioritization aid, not an automatic decision — use it to rank, not to auto-select.

## 22. ICE
```
ICE Score = Impact × Confidence × Ease
```
Faster than RICE, less rigorous — appropriate for low-stakes triage, not for a decision with real blast radius.

## 23. Cost of Delay
```
Cost of Delay per Period = Lost Revenue + Avoidable Cost + Risk Exposure + Strategic Opportunity Loss
WSJF = Cost of Delay / Job Size
```

## 24. Sensitivity
```
Sensitivity to x ≈ ΔY / Δx     (for Y = f(x))
Elasticity = (% Change in Y) / (% Change in X)
```
Use a sensitivity table across the uncertain parameters rather than presenting one deterministic point estimate as if it were certain.

## 25. Scenario Model
Minimum: downside, base case, upside. Per scenario:
```
Net Outcome = Expected Benefit - Expected Cost - Expected Risk Loss
```
Use ranges where evidence is weak — don't manufacture false precision to make the model look more rigorous than the inputs support.

## 26. Confidence-Adjusted Impact
```
Confidence-Adjusted Impact = Estimated Impact × Confidence
```
Confidence must be grounded in evidence class, not intuition: direct experiment > historical internal data > comparable internal case > external benchmark > expert judgment > assumption.

## 27. Total Cost of Ownership
```
TCO = Acquisition + Integration + Infrastructure + Operations + Maintenance + Support + Training + Compliance + Downtime + Decommissioning
```
The most commonly omitted terms are Maintenance, Support, and Decommissioning — check these are present before trusting a TCO comparison.

## 28. Technical Performance Improvement
```
Performance Improvement % = (Baseline Time - New Time) / Baseline Time × 100        (lower is better)
Improvement % = (New Performance - Baseline Performance) / Baseline Performance × 100  (higher is better)
```
Always declare the desired direction before computing — the same formula shape silently flips meaning depending on which way "better" points.

## 29. Composite Objective
```
Objective = w1×Business Value + w2×User Value + w3×Operational Value - w4×Cost - w5×Risk
```
Use normalized dimensions — never combine incompatible raw units (dollars, days, a 1-5 score) without normalizing first.

---

## Common Misuse Patterns Across This Library
- Mixing stock metrics (a snapshot, e.g. WIP) with flow metrics (a rate, e.g. throughput) as if they were the same kind of number
- Comparing two time windows of different lengths or seasonality as if they were equivalent
- Selection bias (only measuring the population that survived to be measured) and survivorship bias (a special case of it) silently skewing an average
- Simpson's paradox — a trend that holds in every segment reversing when the segments are combined
- Double-counting a benefit across two different formulas in the same decision packet
