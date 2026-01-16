# Study Design

## 1) Study objective
This study tests how different explanations of inequality change:
1) accuracy of inequality beliefs, and
2) support for solutions (policies/actions).

Design summary: Pre-survey → randomly assigned message → post-survey.

---

## 2) Design type
- Randomized controlled experiment (between-subjects conditions)
- Pre/post measurement for key outcomes
- Online survey (can be piloted with friends; later run on a participant platform)

---

## 3) Conditions (messages)
Each participant is randomly assigned to **one** condition:

1) Structural + data (human-written)
2) Narrative story (human-written)
3) Hybrid (story + structural/data)
4) AI-written explanation (generated with constraints)
5) Neutral control (unrelated topic)

Message constraints to reduce confounds:
- Similar word count (target: ~140–170 words)
- Similar reading difficulty (target: roughly Grade 8–10)
- Calm, respectful tone (avoid inflammatory wording)
- Similar formatting (no charts unless explicitly tested as a condition)

---

## 4) Survey flow (participant experience)
### Section A — Consent + intro
- Short consent statement
- “You will answer questions about society and social issues. You may skip any question.”

### Section B — Pre-survey
Measures collected before message exposure:
- Inequality estimate(s) (accuracy baseline)
- Structural understanding / causal attribution baseline
- Support for solutions baseline
- Covariates: age range, education, income bracket, political ideology (optional), subjective SES ladder (optional)

### Section C — Message exposure
- Participant reads their assigned message
- Include a minimum reading time (e.g., 12–20 seconds) or “continue” button enabled after time

### Section D — Manipulation checks (recommended)
- Comprehension check (1–2 questions)
- Attention check (1 item)
- Perceived framing check (optional): “This message emphasized: (systems/policy vs individual effort)”

### Section E — Post-survey
Repeat key outcomes:
- Inequality estimate(s)
- Structural understanding / causal attribution
- Support for solutions

### Section F — Debrief
- Brief debrief: purpose is to study how different explanations affect beliefs.
- Provide resources/neutral language.

---

## 5) Measures (high-level; exact wording lives in survey/survey_v1.md)
### 5.1 Inequality accuracy (primary)
Participants estimate one inequality quantity (or a small set).
Examples (choose one for v1):
- Wealth gap estimate
- Income gap estimate
- Homeownership gap estimate

Accuracy will be scored against a benchmark value (defined in docs/measures.md later).

### 5.2 Structural understanding (mechanism)
Short scale measuring agreement that inequality is caused by:
- structural/systemic factors (policy, discrimination, access)
versus
- individual factors (effort, talent)

### 5.3 Support for solutions (primary/secondary)
Short scale measuring support for equity-oriented policies/actions.
Keep items general and non-partisan.

### 5.4 Covariates (optional but useful)
- Education
- Income bracket
- Political ideology (1–7)
- Subjective SES ladder (1–10)
- Prior familiarity with inequality topics (1 item)

---

## 6) Sampling plan (initial + target)
### Pilot (recommended)
- Goal: N = 30–80 (to test clarity, attention checks, timing)
- Outcome: revise stimuli and survey wording

### Main study (target)
- Goal: N = 300–600 total (60–120 per condition)
- Rationale: enough power to detect small-to-medium differences across conditions

Note: You can start smaller and scale up.

---

## 7) Exclusion criteria (pre-specified)
Participants may be excluded if they:
- fail attention check, OR
- fail comprehension check, OR
- complete survey unrealistically fast (e.g., below a minimum threshold)

All exclusions will be reported transparently.

---

## 8) Randomization
- Random assignment to conditions using survey platform randomizer
- Ensure roughly equal allocation across conditions (at least during initial phase)

---

## 9) Data handling
- No personally identifying information collected
- Raw data stored privately (not pushed to public GitHub)
- Public repo includes synthetic data and aggregated results only

---

## 10) Outputs
- Clean stimuli set (stimuli/v1 → v2 finalized)
- Final survey items (survey_v1 → final)
- Python analysis notebook(s) with reproducible tables/figures
- Short report summarizing methods and results
