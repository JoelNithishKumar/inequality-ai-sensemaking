# Scoring Guide (scoring.md)

This document defines exactly how outcomes are scored for the project, so scoring is transparent, consistent, and reproducible.

---

## 1) Overview of what gets scored

The study collects responses **before** and **after** participants read one message.

We score three main things:

1) **Accuracy (primary)**  
   How close someone’s inequality estimate is to a benchmark value.

2) **Support for solutions (primary/secondary)**  
   How much someone supports policies/actions intended to reduce inequality.

3) **Structural understanding (mechanism)**  
   How much someone thinks inequality is caused by systems/policy vs individual choices.

We also score **data quality checks** (attention/comprehension/time) to decide whether a participant is included.

---

## 2) Notation (variables used in scoring)

For each participant:

- `estimate_pre` = inequality estimate before the message  
- `estimate_post` = inequality estimate after the message  
- `benchmark` = reference value used as the “best available” number for the inequality metric

- `support_pre_items[]` = list of Likert items (e.g., 1–7) measuring support (pre)  
- `support_post_items[]` = same items measured post-message  

- `struct_pre_items[]` = list of Likert items measuring structural understanding (pre)  
- `struct_post_items[]` = same items measured post-message  

---

## 3) Scoring Inequality Accuracy (Primary Outcome)

### 3.1 Absolute error (main method)
We measure how far the participant’s estimate is from the benchmark:

- `error_pre  = abs(estimate_pre  - benchmark)`
- `error_post = abs(estimate_post - benchmark)`

### 3.2 Accuracy improvement (primary accuracy score)
We want a single number that says: “Did the person get closer to the benchmark after reading the message?”

- `accuracy_improvement = error_pre - error_post`

**Interpretation:**
- `accuracy_improvement > 0` → improvement (closer to benchmark)
- `accuracy_improvement = 0` → no change
- `accuracy_improvement < 0` → got worse (farther from benchmark)

### 3.3 Optional: Percent error (robustness check)
If estimates can be on a large scale, percent error can help:

- `pct_error_pre  = abs(estimate_pre  - benchmark) / benchmark`
- `pct_error_post = abs(estimate_post - benchmark) / benchmark`
- `pct_accuracy_improvement = pct_error_pre - pct_error_post`

Only use this if it makes sense for the metric and benchmark (benchmark must be > 0).

### 3.4 Optional: Direction of misperception (extra insight)
Sometimes it helps to know if people are over- or under-estimating:

- `signed_error_pre  = estimate_pre  - benchmark`
- `signed_error_post = estimate_post - benchmark`

**Interpretation:**
- positive = overestimate
- negative = underestimate

---

## 4) Scoring Support for Solutions

Support is typically measured with multiple Likert items (for example, 1 = strongly disagree to 7 = strongly agree).

### 4.1 Reverse coding (if needed)
If any items are worded in the opposite direction, reverse-code them before averaging.

For a 1–7 scale:
- `reverse(x) = 8 - x`

(Example: a “Policies are unnecessary” item would be reverse-coded.)

### 4.2 Scale score (mean)
Compute pre and post averages:

- `support_pre  = mean(support_pre_items)`
- `support_post = mean(support_post_items)`

### 4.3 Support change score (primary support score)
- `support_change = support_post - support_pre`

**Interpretation:**
- `support_change > 0` → increased support
- `support_change = 0` → no change
- `support_change < 0` → decreased support

### 4.4 Optional: Standardized scale (z-score)
If you want comparability across different versions, standardize using the **pre** distribution:

- `support_pre_z  = (support_pre  - mean_pre) / sd_pre`
- `support_post_z = (support_post - mean_pre) / sd_pre`
- `support_change_z = support_post_z - support_pre_z`

---

## 5) Scoring Structural Understanding (Mechanism)

Structural understanding is measured with several Likert items about causes of inequality.

### 5.1 Reverse coding (if needed)
If any items represent “individual blame” (opposite direction), reverse-code them so **higher always means more structural**.

For a 1–7 scale:
- `reverse(x) = 8 - x`

### 5.2 Scale score (mean)
- `struct_pre  = mean(struct_pre_items)`
- `struct_post = mean(struct_post_items)`

### 5.3 Structural change
- `struct_change = struct_post - struct_pre`

**Interpretation:**
- Positive values: participant shifted toward structural explanations.

---

## 6) Data Quality Scoring (Inclusion/Exclusion)

These scores decide whether a participant’s data should be included.

### 6.1 Attention check
- `attention_pass = 1` if correct, else `0`

### 6.2 Comprehension check
- `comprehension_pass = 1` if correct, else `0`

### 6.3 Duration / speed check
- `duration_seconds = survey_end_time - survey_start_time`

Define a minimum time threshold (example):
- Exclude if `duration_seconds < 120` (2 minutes)

*(Final threshold should be chosen after pilot timing.)*

### 6.4 Inclusion rule (default)
Include only if:
- `attention_pass == 1`
- `comprehension_pass == 1`
- `duration_seconds >= min_time_threshold`

All exclusions must be reported transparently.

---

## 7) Handling missing or invalid responses

### 7.1 Missing scale items
If a participant misses too many items, don’t compute the scale.

Default rule (simple):
- If fewer than 70% of items are answered, set the scale score to missing.

If most items are answered, compute mean over available items.

### 7.2 Out-of-range values
If an estimate is impossible (negative when it shouldn’t be, >100 when using percent scale, etc.):
- mark it as invalid and treat as missing
- do not “fix” values silently

---

## 8) What gets saved to the final analysis dataset

For each participant, the processed dataset should include:

- `condition`
- `estimate_pre`, `estimate_post`, `benchmark`
- `error_pre`, `error_post`, `accuracy_improvement`
- (optional) `pct_error_pre`, `pct_error_post`, `pct_accuracy_improvement`
- `support_pre`, `support_post`, `support_change`
- `struct_pre`, `struct_post`, `struct_change`
- `attention_pass`, `comprehension_pass`, `duration_seconds`, `included`

---

## 9) Example (simple numeric example)

If benchmark = 70

Participant:
- estimate_pre = 40 → error_pre = |40 - 70| = 30
- estimate_post = 60 → error_post = |60 - 70| = 10

Accuracy improvement:
- 30 - 10 = **+20** (improved)

Support:
- support_pre = 4.0
- support_post = 5.0
- support_change = **+1.0**

Structural understanding:
- struct_pre = 3.5
- struct_post = 4.5
- struct_change = **+1.0**
