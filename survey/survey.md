# Survey Questions (v1) — Humans vs AI (FULL TEXT)
**Document purpose:** Provide the exact question wording for both (1) human participants and (2) an AI system.  
**Project:** Human vs AI Inequality Sensemaking  
**Version:** v1  
**Start date for documentation:** 2025-10-19

---

## 1) Human Survey (v1)

### 1.1 Consent (Humans only)
**H-CONSENT-1**
**Prompt:**  
You are invited to take part in a short research study about how people understand social issues. Participation is voluntary. You may skip any question and stop at any time. The topic includes economic inequality and opportunity, which some people may find sensitive. No personally identifying information is required. Your responses will be used for research purposes.

**Response options:**  
- ☐ I agree to participate.

---

### 1.2 Pre-survey (Humans)

#### A) Accuracy (Pre)
**H-PRE-Q1 (Accuracy estimate)**  
**Prompt:**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

**Response type:** Numeric entry (allow 0–200)

**H-PRE-Q1b (Confidence; optional)**  
**Prompt:**  
How confident are you in your answer to the previous question?

**Response type:** 1–7 scale  
1 = Not confident at all  
7 = Very confident

---

#### B) Structural understanding (Pre)
**Instructions:** Please indicate how much you agree or disagree with each statement.  
**Response type:** 1–7 Likert scale  
1 = Strongly disagree  
2 = Disagree  
3 = Somewhat disagree  
4 = Neither agree nor disagree  
5 = Somewhat agree  
6 = Agree  
7 = Strongly agree

**H-PRE-S1**  
**Prompt:** Inequality is largely caused by **systems and policies** that shape opportunities.

**H-PRE-S2**  
**Prompt:** Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.

**H-PRE-S3**  
**Prompt:** Even when people work hard, **structural barriers** can limit economic outcomes.

**H-PRE-S4 (reverse-coded)**  
**Prompt:** Economic inequality is mainly the result of **individual choices and effort**.

---

#### C) Support for solutions (Pre)
**Instructions:** Please indicate how much you agree or disagree with each statement.  
**Response type:** same 1–7 Likert scale as above

**H-PRE-P1**  
**Prompt:** Government should take steps to reduce large gaps in wealth and opportunity.

**H-PRE-P2**  
**Prompt:** Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.

**H-PRE-P3**  
**Prompt:** Employers and institutions should review rules and practices to reduce unfair barriers.

**H-PRE-P4 (reverse-coded)**  
**Prompt:** Inequality is not a major problem, so major policy changes are unnecessary.

---

#### D) Optional covariates (Pre; humans only)
**H-PRE-D1 (Education)**  
**Prompt:** What is the highest level of education you have completed?  
**Response options (example):**  
- Less than high school  
- High school diploma / GED  
- Some college (no degree)  
- Associate degree  
- Bachelor’s degree  
- Graduate or professional degree  
- Prefer not to say

**H-PRE-D2 (Household income)**  
**Prompt:** What is your approximate annual household income?  
**Response options (example):**  
- Less than $25,000  
- $25,000–$49,999  
- $50,000–$74,999  
- $75,000–$99,999  
- $100,000–$149,999  
- $150,000–$199,999  
- $200,000 or more  
- Prefer not to say

**H-PRE-D3 (Subjective SES ladder; optional)**  
**Prompt:** Imagine a ladder where 10 is the highest status in society and 1 is the lowest. Where do you see yourself on this ladder?  
**Response type:** 1–10 scale

**H-PRE-D4 (Ideology; optional)**  
**Prompt:** How would you describe your political ideology?  
**Response type:** 1–7 scale  
1 = Very liberal  
7 = Very conservative

**H-PRE-D5 (Prior familiarity; optional)**  
**Prompt:** Before today, how familiar were you with wealth inequality statistics?  
**Response type:** 1–7 scale  
1 = Not at all familiar  
7 = Very familiar

---

### 1.3 Message exposure (Humans)
- Randomly assign one condition: structural_data / narrative_story / hybrid / ai_explanation / control
- Display only the participant-facing stimulus text.
- Optional: minimum reading time 12–20 seconds.

---

### 1.4 Post-survey (Humans)

#### A) Accuracy (Post)
**H-POST-Q1 (Accuracy estimate)**  
**Prompt:**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

**Response type:** Numeric entry (allow 0–200)

**H-POST-Q1b (Confidence; optional)**  
**Prompt:**  
How confident are you in your answer to the previous question?

**Response type:** 1–7 scale  
1 = Not confident at all  
7 = Very confident

---

#### B) Structural understanding (Post)
**Instructions:** Please indicate how much you agree or disagree with each statement.  
**Response type:** 1–7 Likert scale (same as pre)

**H-POST-S1**  
**Prompt:** Inequality is largely caused by **systems and policies** that shape opportunities.

**H-POST-S2**  
**Prompt:** Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.

**H-POST-S3**  
**Prompt:** Even when people work hard, **structural barriers** can limit economic outcomes.

**H-POST-S4 (reverse-coded)**  
**Prompt:** Economic inequality is mainly the result of **individual choices and effort**.

---

#### C) Support for solutions (Post)
**Instructions:** Please indicate how much you agree or disagree with each statement.  
**Response type:** 1–7 Likert scale (same as pre)

**H-POST-P1**  
**Prompt:** Government should take steps to reduce large gaps in wealth and opportunity.

**H-POST-P2**  
**Prompt:** Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.

**H-POST-P3**  
**Prompt:** Employers and institutions should review rules and practices to reduce unfair barriers.

**H-POST-P4 (reverse-coded)**  
**Prompt:** Inequality is not a major problem, so major policy changes are unnecessary.

---

#### D) Manipulation checks (Post only)
**H-POST-M1 (Perceived framing; bipolar scale)**  
**Prompt:** The message I read mainly emphasized:  
**Response type:** 1–7 scale  
1 = Personal choices/effort  
7 = Systems/policies/structures

**H-POST-M2 (Statistics presence)**  
**Prompt:** The message included specific numbers or statistics.  
**Response type:** 1–7 Likert scale  
1 = Strongly disagree  
7 = Strongly agree

---

#### E) Attention + comprehension checks (Humans only; Post)
**H-POST-A1 (Attention check)**  
**Prompt:** To show you’re paying attention, please select **“Agree”** below.  
**Response options:**  
- Strongly disagree  
- Disagree  
- Neutral  
- Agree  
- Strongly agree

**H-POST-C1 (Comprehension topic check)**  
**Prompt:** What was the main topic of the message you read?  
**Response options:**  
- Sleep and daily habits  
- Economic inequality and opportunity  
- Sports performance  
- Weather patterns

---

### 1.5 Debrief (Humans only)
**H-DEBRIEF-1**  
**Prompt:**  
Thank you for participating. This study examines how different explanations influence people’s beliefs about inequality and their support for solutions. Your responses are anonymous. You may close the survey now.

---

## 2) AI Survey (v1)

### 2.1 AI Instructions (wrapper)
**AI-INSTR-1 (shown to AI before questions):**  
You will answer a set of survey questions.  
- Answer as if you are an **average U.S. adult**.  
- Use numbers where asked.  
- For 1–7 questions, respond with an integer from 1 to 7.  
- Return answers in the exact JSON format requested.  
- Do not add extra commentary outside the JSON.

---

### 2.2 AI Pre-questions (before message)
**AI-PRE-Q1 (Accuracy estimate)**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?  
(Respond with a number.)

**AI-PRE-S1**  
Inequality is largely caused by **systems and policies** that shape opportunities.  
(1–7)

**AI-PRE-S2**  
Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.  
(1–7)

**AI-PRE-S3**  
Even when people work hard, **structural barriers** can limit economic outcomes.  
(1–7)

**AI-PRE-S4 (reverse-coded)**  
Economic inequality is mainly the result of **individual choices and effort**.  
(1–7)

**AI-PRE-P1**  
Government should take steps to reduce large gaps in wealth and opportunity.  
(1–7)

**AI-PRE-P2**  
Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.  
(1–7)

**AI-PRE-P3**  
Employers and institutions should review rules and practices to reduce unfair barriers.  
(1–7)

**AI-PRE-P4 (reverse-coded)**  
Inequality is not a major problem, so major policy changes are unnecessary.  
(1–7)

**AI-PRE-Q1b (Confidence; optional)**  
How confident are you in your answer to Q1?  
(1–7)

---

### 2.3 AI Post-questions (after message)
**AI-POST-Q1 (Accuracy estimate)**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?  
(Respond with a number.)

**AI-POST-S1**  
Inequality is largely caused by **systems and policies** that shape opportunities.  
(1–7)

**AI-POST-S2**  
Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.  
(1–7)

**AI-POST-S3**  
Even when people work hard, **structural barriers** can limit economic outcomes.  
(1–7)

**AI-POST-S4 (reverse-coded)**  
Economic inequality is mainly the result of **individual choices and effort**.  
(1–7)

**AI-POST-P1**  
Government should take steps to reduce large gaps in wealth and opportunity.  
(1–7)

**AI-POST-P2**  
Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.  
(1–7)

**AI-POST-P3**  
Employers and institutions should review rules and practices to reduce unfair barriers.  
(1–7)

**AI-POST-P4 (reverse-coded)**  
Inequality is not a major problem, so major policy changes are unnecessary.  
(1–7)

**AI-POST-M1 (Perceived framing; bipolar scale)**  
The message mainly emphasized:  
1 = Personal choices/effort  
7 = Systems/policies/structures  
(Respond 1–7)

**AI-POST-M2 (Statistics presence)**  
The message included specific numbers or statistics.  
(1–7)

**AI-POST-Q1b (Confidence; optional)**  
How confident are you in your answer to Q1?  
(1–7)

---

### 2.4 AI Output format (JSON template)
Return only JSON in this structure:

```json
{
  "Q1_estimate": 0,
  "Q1_confidence": 0,
  "S1": 0,
  "S2": 0,
  "S3": 0,
  "S4": 0,
  "P1": 0,
  "P2": 0,
  "P3": 0,
  "P4": 0,
  "M1_framing": 0,
  "M2_stats": 0
}
