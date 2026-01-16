# Results Plots Documentation (Pilot Study v1)

This document explains what each results plot represents, how it connects to the study objectives and research questions, and how to interpret the patterns.

## Study objective (reminder)
Test how different inequality message types affect:
1) Structural understanding (systems/policy vs individual choices),
2) Support for solutions (policy/action support),
3) Accuracy about inequality levels (distance from benchmark; pilot v1 humans = PRE only).

Message conditions:
- control
- narrative_story
- structural_data
- hybrid
- ai_explanation

Key outcomes:
- Structural understanding: mean of structural items (with reverse-coded items handled)
- Policy support: mean of policy support items (with reverse-coded items handled)
- Accuracy error: `abs(Q1_estimate - benchmark)` where benchmark = 16

---

# Plot 1 — Humans: Structural understanding shift by message condition
**File:** `outputs/humans_structural_shift_by_condition.png`

## What it measures
Change in participants’ structural understanding after reading one message.

**Y-axis:** Mean structural shift = (post structural mean − pre structural mean)  
**X-axis:** Message condition

## How to interpret
- Values near **0** = little/no change in structural beliefs.
- Values **> 0** = participants became more likely to explain inequality as caused by systems/policy.
- Values **< 0** = participants shifted away from structural explanations (toward individual-effort explanations).

## What this plot can tell us
- Whether message types differ in their ability to increase structural explanations of inequality.
- This plot supports the “mechanism” part of the project (messages → structural understanding), and is directly relevant to RQ3’s premise.

## Pilot-level takeaway (typical)
In the pilot, inequality-framed messages tended to increase structural understanding relative to control, with some conditions showing larger average shifts than others.

## Caveats
- This is descriptive evidence. Statistical significance depends on sample size and variability.
- Error bars reflect uncertainty around the mean (standard error).

---

# Plot 2 — Humans: Policy support shift by message condition
**File:** `outputs/humans_policy_shift_by_condition.png`

## What it measures
Change in participants’ support for policy/action solutions after reading one message.

**Y-axis:** Mean policy shift = (post policy mean − pre policy mean)  
**X-axis:** Message condition

## How to interpret
- Values near **0** = no change in support for solutions.
- Values **> 0** = increased support for equity-oriented policies/actions.
- Values **< 0** = decreased support (not typically expected in this design, but possible in other data).

## What this plot can tell us
- This plot addresses **RQ2**: which message type most increases support for solutions?
- Comparing conditions to control indicates whether messages tend to move support beyond baseline.

## Pilot-level takeaway (typical)
Control is usually near zero; inequality messages tend to show positive shifts. The highest bar suggests which message type produced the largest average increase in policy support in this pilot dataset.

## Caveats
- Descriptive: do not over-claim causality beyond the design without statistical tests.
- Error bars reflect uncertainty around the mean.

---

# Plot 3 — Humans: Pre-survey accuracy error by condition (benchmark = 16)
**File:** `outputs/humans_pre_accuracy_error_by_condition.png`

## What it measures
How far participants’ **PRE** inequality estimate was from the benchmark *before* exposure to any stimulus.

**Y-axis:** Mean absolute error = `abs(pre_Q1_estimate − 16)`  
**X-axis:** Message condition

## How to interpret
- **Lower** bars = closer to the benchmark (more accurate).
- **Higher** bars = farther from the benchmark (less accurate).

## What this plot can tell us
- This is a **baseline check**: it shows how accurate participants were before they read anything.
- It does **NOT** show message effects on accuracy (because it is PRE only).

## Why this matters
- In an ideal random assignment, pre accuracy should be broadly similar across conditions.
- If pre accuracy differs across conditions, it indicates baseline imbalance due to small samples or randomness.

## Key limitation (Pilot v1 humans)
Humans in v1 did not answer a **post** estimate question, so we cannot compute human accuracy improvement (pre error − post error). Therefore:
- RQ1 cannot be fully answered for humans in v1.
- The correct human interpretation is baseline accuracy distribution by condition.

---

# Plot 4 — AI: Structural understanding (pre vs post) by platform
**File:** `outputs/ai_pre_post_structural_by_platform.png`

## What it measures
For each AI platform, the structural understanding score before and after reading the stimulus.

**Y-axis:** Structural mean (1–7)  
**X-axis:** Platform label (platform + assigned condition)  
Lines:
- **pre** = responses before stimulus
- **post** = responses after stimulus

## How to interpret
- If post > pre, the AI’s responses became more structural after the stimulus.
- If post < pre, the AI’s responses became less structural after the stimulus.
- If post ≈ pre, little change.

## What this plot can tell us
- A model-behavior audit: AI responses can shift after exposure to a message.
- Illustrates sensitivity to framing and content.

## Critical caveat
This is **not** a clean platform comparison because:
- each platform saw a different condition
- only one run per platform was collected

Therefore, treat as illustrative/pilot evidence, not definitive conclusions about platform differences.

---

# Plot 5 — AI: Manipulation checks (post)
**File:** `outputs/ai_manipulation_checks_by_platform.png`

## What it measures
Whether the AI recognized what type of message it read (manipulation check).

Two checks (1–7):
- **M1_framing:** “How structural/system-focused was the message?”
- **M2_stats:** “How much did the message use numbers/data/statistics?”

**Y-axis:** Score (1–7)  
**X-axis:** Platform label (platform + assigned condition)

## How to interpret (intended patterns)
- structural_data: high M1 and high M2
- narrative_story: high M1, low M2
- control: low M1, low M2
- hybrid: moderate/high M1 and moderate/high M2 (depends on how the hybrid message was written)
- ai_explanation: typically high M1; M2 depends on whether numbers were included

## What this plot can tell us
- Validates that the stimuli generally behave as intended (at least as perceived by the AI).
- Helps diagnose whether two conditions are too similar (e.g., hybrid being interpreted as fully “stats-heavy”).

## Caveat
As with the AI structural plot:
- one run per platform
- different conditions across platforms
Treat as stimulus validation evidence, not definitive platform comparisons.

---

# How these plots map to the research questions

## RQ1: Which message type most improves accuracy about inequality levels?
- Humans (Pilot v1): cannot test improvement due to lack of post estimate.
  - Plot 3 provides baseline pre accuracy error by condition only.
- AI: improvement can be computed (pre vs post estimate), but current dataset has one run per platform and different conditions → illustrative only.

## RQ2: Which message type most increases support for solutions?
- Plot 2 directly addresses RQ2 using human policy shifts by condition.

## RQ3: Do changes in structural understanding explain (mediate) changes in support?
- Plot 1 shows message effects on structural understanding (possible mediator).
- Plot 2 shows message effects on policy support (outcome).
- Recommended next plot for RQ3 (not included in the five default plots):
  - Scatter: `structural_shift` vs `policy_shift` (humans), plus a trend line.
  This assesses whether participants who become more structural also become more supportive of solutions.

---

# Future Recommended “next plots” 
1) Humans: Scatter `structural_shift` vs `policy_shift` (tests RQ3 relationship).
2) Humans: Pre vs Post means by condition (two-bar or two-point plots for structural and policy).
3) If v2 adds post accuracy estimate for humans:
   - Accuracy improvement = (pre error − post error) by condition (answers RQ1 properly for humans).

