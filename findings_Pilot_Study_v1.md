# Results Plots Documentation — Pilot Study v1 (Benchmark = 16)

## Objective (what this project is testing)
The main objective set at the start of this project is:

**To test how different types of messages about economic inequality change (1) what people believe about inequality and (2) how accurately they estimate the racial wealth gap — and to compare those effects between humans and AI systems.**

**Important emphasis:** Objective (2) is the key focus here:  
**Do messages change how accurately people (and AI systems) estimate the racial wealth gap?**  
In this pilot, “accuracy” is measured using the **absolute distance from a benchmark value (16)**, using a pre vs post design.

---

## Research Questions

### Big question
How do different explanations of inequality affect:
1) **how accurately** people understand inequality, and  
2) **how much** they support solutions (policies/actions)?

### Specific research questions
- **RQ1:** Which message type most improves **accuracy** about inequality levels?
- **RQ2:** Which message type most increases **support for solutions**?
- **RQ3:** Do changes in **structural understanding** explain (mediate) changes in **support**?

---

## Key Outcomes (what we measure)

### 1) Accuracy (primary focus)
Participants answer the estimate question:
> “If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?”

We use benchmark = **16**.

Computed fields:
- `pre_accuracy_error = |pre_Q1_estimate - 16|`
- `post_accuracy_error = |post_Q1_estimate - 16|`
- `accuracy_improvement = pre_accuracy_error - post_accuracy_error`

Interpretation:
- **accuracy_improvement > 0** → improved accuracy (moved closer to benchmark)
- **accuracy_improvement = 0** → no change
- **accuracy_improvement < 0** → got less accurate

### 2) Structural understanding
Measures agreement with statements attributing inequality to structures/policy vs individual choices.

Computed fields:
- `pre_structural_mean`
- `post_structural_mean`
- `structural_shift = post_structural_mean - pre_structural_mean`

Interpretation:
- **positive structural_shift** → participants became more structural in their explanation of inequality.

### 3) Support for solutions (policy support)
Measures support for equity-oriented policies/actions.

Computed fields:
- `pre_policy_mean`
- `post_policy_mean`
- `policy_shift = post_policy_mean - pre_policy_mean`

Interpretation:
- **positive policy_shift** → increased support for solutions/policies.

---

## Study Conditions (message types)
These are the five message conditions participants were randomly assigned:
- `structural_data`
- `narrative_story`
- `hybrid`
- `ai_explanation`
- `control`

Humans: assigned by randomizer.  
AI: you ran **one platform per condition** in this pilot:
- ChatGPT → structural_data
- Gemini → narrative_story
- Perplexity → hybrid
- Claude → ai_explanation
- Meta AI → control

**Important design note:** In the AI pilot, *platform and condition are confounded* (each platform saw a different condition), so AI results cannot cleanly separate “platform effect” from “condition effect.” This is fine for a pilot but must be fixed for a stronger comparison later (run every platform on every condition).

---

# Plots and What They Mean

## Plot 1 — Humans: Structural understanding shift by message condition
**File:** `outputs/humans_structural_shift_by_condition.png`  
**Y-axis:** mean `structural_shift` (post − pre)

### What it describes
This plot shows whether each message type makes people more likely to explain inequality using structural causes (systems/policy) rather than individual effort.

### How to read it
- Higher bars = stronger movement toward structural explanations.
- Bars near 0 = little or no change.
- Error bars = uncertainty (standard error); larger bars suggest more variability and/or small sample sizes.

### What it suggests (pilot interpretation)
- Non-control conditions generally show positive structural shifts, meaning the messages can move people toward structural explanations.
- The conditions differ in how strongly they shift structural understanding.

### Research question linkage
- Helps address **RQ3** by providing the “structural change” variable used to see whether structural change is associated with policy change.

---

## Plot 2 — Humans: Policy support shift by message condition
**File:** `outputs/humans_policy_shift_by_condition.png`  
**Y-axis:** mean `policy_shift` (post − pre)

### What it describes
This plot shows which message types increase support for solutions (policies/actions).

### How to read it
- Higher bars = larger increase in policy support after reading the message.
- Control near 0 is expected (minimal change).
- Error bars show uncertainty.

### What it suggests (pilot interpretation)
- In your pilot, **structural_data** appears to create the largest average increase in policy support.
- Other message types (hybrid, ai_explanation, narrative_story) appear positive but smaller.

### Research question linkage
- Primary evidence for **RQ2** (which message most increases support).

---

## Plot 3 — Humans: Pre-survey accuracy error by condition
**File:** `outputs/humans_pre_accuracy_error_by_condition.png`  
**Y-axis:** mean `pre_accuracy_error = |pre_estimate - 16|`

### What it describes
This plot shows the *baseline* accuracy before any message exposure, split by condition.

### Why it matters
Because participants are randomly assigned, we hope baseline accuracy is similar across conditions. If one condition starts much higher/lower, it can complicate interpretation of “improvement.”

### How to interpret it
- Lower = more accurate before reading a message.
- Higher = less accurate before reading a message.

### What it suggests (pilot interpretation)
- There is variation across conditions at baseline (which can happen with small pilot samples).
- This is one reason why the **post-change metric** (accuracy improvement) is more important than pre-only values.

### Research question linkage
- Not a direct RQ answer, but it supports interpreting RQ1 by showing whether conditions started similar or not.

---

## Plot 4 — Humans: Accuracy improvement by message condition (benchmark=16)
**File:** `outputs/humans_accuracy_improvement_by_condition.png`  
**Y-axis:** mean `accuracy_improvement = |pre-16| - |post-16|`

### What it describes (THIS IS THE KEY PLOT for the core objective)
This plot shows which message type makes humans **more accurate** about the racial wealth gap estimate after reading the message.

### How to read it
- **Above 0** = improved accuracy (moved closer to benchmark after message)
- **At 0** = no change
- **Below 0** = worse accuracy

### What it suggests (pilot interpretation)
- **structural_data** shows the strongest improvement in accuracy.
- Hybrid and AI explanation show moderate improvements.
- Narrative story shows smaller improvement.
- Control shows little change.

### Research question linkage
- This plot provides the clearest direct evidence for **RQ1** (which message improves accuracy most).

### Why it aligns with the project objective
Objective (2) is about **accuracy of estimating the racial wealth gap.**  
This plot is the most direct “pre vs post accuracy” outcome for humans.

---

## Plot 5 — AI: Structural understanding (pre vs post) by platform (one run each)
**File:** `outputs/ai_pre_post_structural_by_platform.png`

### What it describes
This plot shows AI systems’ structural understanding before and after reading the message, but **each platform is paired with a different condition** in this pilot.

### What it can and cannot conclude
- It can show that each platform’s responses changed (or didn’t change) after stimulus exposure.
- It cannot isolate whether differences are due to the **platform** or the **message condition**, because those are linked in this pilot.

### Research question linkage
- Supports the “compare humans vs AI systems” objective, but this plot focuses on structural understanding, not accuracy.

---

## Plot 6 — AI: Manipulation checks (post)
**File:** `outputs/ai_manipulation_checks_by_platform.png`  
**Measures:** `M1_framing`, `M2_stats` (post only)

### What it describes
These checks test whether the AI “noticed” the message properties:
- `M1_framing`: did the message frame inequality structurally?
- `M2_stats`: did the message include explicit statistics?

### How to interpret
- Higher values mean the AI judged that feature as present.
- This helps confirm your stimulus design is actually distinguishable.

### Research question linkage
- Not a direct RQ answer, but it validates that the “treatment” (message type differences) is being perceived.

---

# Answering the Research Questions (Pilot Conclusions)

## RQ1: Which message type most improves accuracy about inequality levels?
**Humans (strongest evidence):**  
Use **Humans: Accuracy improvement by condition** as the main evidence.  
Pilot pattern suggests **structural_data** yields the largest average accuracy improvement.

**AI (pilot-only / limited evidence):**  
AI accuracy comparison is limited because:
1) You ran **one condition per platform** (confounded design)
2) You ran **one run per platform** (no replication)
So AI results should be treated as **illustrative**, not definitive.

**What you can still say (carefully):**
- You successfully measured pre vs post accuracy for AI platforms.
- AI accuracy shifts can be computed and compared directionally, but stronger inference requires more runs (and all platforms across all conditions).

---

## RQ2: Which message type most increases support for solutions?
Use **Humans: Policy support shift by condition** as the main evidence.  
Pilot pattern suggests **structural_data** yields the largest increase in policy support, with hybrid/ai_explanation/narrative showing smaller positive increases.

---

## RQ3: Do changes in structural understanding explain (mediate) changes in support?
From the plots alone:
- You can **describe** that many conditions that increase structural understanding also increase policy support (directionally consistent with mediation).
- But you cannot claim mediation definitively from bar charts.

### What you can do next (recommended for RQ3)
Run a simple association check using your combined file:
- Does `structural_shift` predict `policy_shift` (within humans)?
- Does the relationship hold when controlling for condition?

A pilot-appropriate analysis:
- Scatterplot: structural_shift vs policy_shift (humans)
- Correlation + simple regression:
  - `policy_shift ~ structural_shift + condition`

A stronger next step (if sample size supports it later):
- Mediation model (e.g., bootstrapped mediation)

---

# The Key Objective: Comparing Humans vs AI on Accuracy (what you can say now)

### What you CAN say now (pilot-appropriate)
- Humans show measurable changes in accuracy after stimulus exposure.
- Message type appears to matter for human accuracy (notably structural_data).
- AI platforms also produce measurable pre vs post estimates and can be scored using the same benchmark-based accuracy method.

### What you should NOT claim yet (because of pilot constraints)
- That one AI platform is “better” than another, because platform and condition are confounded.
- Strong platform comparisons require:
  1) Every platform runs every condition
  2) Multiple runs per platform × condition (replication)

### The clean design for the next iteration (recommended)
To truly compare humans vs AI systems and isolate message effects:
- Run a 5 (conditions) × 5 (platforms) grid = **25 AI runs**
- Ideally repeat each cell (e.g., 3 runs each) = **75 AI runs**
Then you can:
- Compare average accuracy improvement by condition across humans and AI
- Compare AI platforms while holding condition constant

---

# Summary (one-paragraph takeaway)
This pilot supports the project’s core objective by showing that message exposure can shift human beliefs (structural understanding, policy support) and—most importantly—human accuracy on a racial wealth-gap estimate relative to a benchmark. The strongest pilot evidence for accuracy improvement appears in the structural+data condition. AI platforms can be scored with the same benchmark method, but the current AI pilot design confounds platform and condition, so AI comparisons are directional and mainly demonstrate feasibility. The next iteration should run all platforms across all conditions with replication to enable a clean human vs AI comparison of accuracy change.
