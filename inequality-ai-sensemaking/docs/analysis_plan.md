# Analysis Plan

## 1) Goals of the analysis
Primary goals:
1) Determine which message condition most improves inequality accuracy.
2) Determine which message condition most increases support for solutions.

Secondary goal:
3) Test whether increased “structural understanding” explains (mediates) changes in support.

Exploratory:
- Check whether effects differ by SES, education, or ideology (if measured).

---

## 2) Variables and scoring

### 2.1 Condition variable
Condition is categorical with 5 levels:
- structural_data
- narrative_story
- hybrid
- ai_explanation
- control

### 2.2 Accuracy scoring (primary outcome)
Define:
- `estimate_pre` = participant’s pre-survey estimate
- `estimate_post` = participant’s post-survey estimate
- `benchmark` = reference value for the inequality metric

Compute absolute error:
- `error_pre = abs(estimate_pre - benchmark)`
- `error_post = abs(estimate_post - benchmark)`

Primary accuracy improvement:
- `accuracy_improvement = error_pre - error_post`
Interpretation:
- Positive values = improvement (closer to benchmark)
- Negative values = worse accuracy

Optional robustness:
- Use percent error if the estimate scale is large:
  - `pct_error = abs(estimate - benchmark) / benchmark`

### 2.3 Support for solutions (primary/secondary outcome)
Assume a set of Likert items (1–7). Compute:
- `support_pre = mean(items_pre)`
- `support_post = mean(items_post)`
- `support_change = support_post - support_pre`

### 2.4 Structural understanding (mechanism)
Assume a scale of items (1–7). Compute:
- `struct_pre = mean(items_pre)`
- `struct_post = mean(items_post)`
- `struct_change = struct_post - struct_pre`

### 2.5 Data quality flags
- `attention_pass` (0/1)
- `comprehension_pass` (0/1)
- `duration_seconds`

---

## 3) Data cleaning rules (pre-specified)
Exclude participants if:
- attention_pass == 0 OR
- comprehension_pass == 0 OR
- duration_seconds < minimum_time_threshold

Report:
- total N
- excluded N and reasons
- final N

---

## 4) Statistical tests

### 4.1 Primary test: condition differences in accuracy improvement
Model: OLS regression (or ANOVA equivalently)

Option A (simple):
- Compare mean `accuracy_improvement` across conditions

Option B (recommended): ANCOVA-style model predicting post error controlling for pre error:
- `error_post ~ condition + error_pre + covariates`

Why this is strong:
- Controls for baseline differences
- Usually improves precision

Primary contrasts (planned):
1) structural_data vs narrative_story
2) structural_data vs control
3) ai_explanation vs control
4) hybrid vs narrative_story

Multiple comparisons:
- Use Holm correction or control false discovery rate for planned contrasts.

### 4.2 Primary test: condition differences in support change
Model:
- `support_post ~ condition + support_pre + covariates`
and/or compare `support_change` across groups.

Planned contrasts:
1) structural_data vs control
2) structural_data vs narrative_story
3) ai_explanation vs control
4) hybrid vs narrative_story

### 4.3 Mechanism test: does structural understanding explain support changes?
Two options:

Option A (simple mediation-style steps):
1) `struct_change ~ condition + covariates`
2) `support_change ~ condition + struct_change + covariates`
If struct_change reduces the condition effect on support_change, it supports the mechanism.

Option B (bootstrap mediation):
- Use bootstrap resampling to estimate indirect effect:
  condition → struct_change → support_change

(Implement in Python with custom bootstrap or a mediation library.)

---

## 5) Exploratory analyses (clearly labeled)
### 5.1 Heterogeneity
Test interactions (if you measured these):
- `support_change ~ condition * SES + ...`
- `accuracy_improvement ~ condition * ideology + ...`

### 5.2 Manipulation checks
- Confirm participants perceived the intended framing:
  structural_data should score higher on “systems/policy emphasis” than narrative_story.

### 5.3 Sensitivity checks
- Run models with and without exclusions
- Try alternate scoring (percent error)
- Winsorize extreme estimates if needed (document clearly)

---

## 6) Reporting plan (what figures/tables you will produce)
Tables:
- Table 1: sample characteristics by condition (age, education, etc.)
- Table 2: mean outcomes (pre, post, change) by condition

Figures:
- Fig 1: accuracy_improvement by condition (bar/violin with CI)
- Fig 2: support_change by condition (bar/violin with CI)
- Fig 3: structural_change by condition
- Fig 4 (optional): mediation diagram with coefficients

---

## 7) Implementation (Python)
Planned Python stack:
- pandas, numpy
- scipy, statsmodels
- matplotlib (for plots)

Outputs saved to:
- results/tables/
- results/figures/

All analysis steps will be reproducible via:
- notebooks/02_pilot_analysis.ipynb (pilot)
- notebooks/03_main_analysis.ipynb (main)
and/or a script:
- src/analysis.py

---

## 8) Versioning
Any changes to:
- stimuli
- measures
- exclusions
- analysis choices

…will be logged in:
- CHANGELOG.md
- lab_notebook/YYYY-MM-DD.md
