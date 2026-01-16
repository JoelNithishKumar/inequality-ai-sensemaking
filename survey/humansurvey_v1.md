# Survey v1 (Humans) — Qualtrics-Style Structure
**Project:** Human vs AI Inequality Sensemaking  
**Version:** v1  
**Notes:**  
- Show participants only the stimulus text (not internal notes).  
- In Qualtrics, set **Export Tags** to match the IDs below so your CSV columns are stable.

---

## Survey Flow (Qualtrics Blocks)

### Block 1 — Consent (Required)
**H_CONSENT_1**  
**Question type:** Multiple Choice (Single Answer)  
**Prompt:**  
You are invited to take part in a short research study about how people understand social issues. Participation is voluntary. You may skip any question and stop at any time. The topic includes economic inequality and opportunity, which some people may find sensitive. No personally identifying information is required. Your responses will be used for research purposes.

**Answer choices:**  
1. I agree to participate.  
2. I do not agree to participate.

**Display logic:**  
- If “I do not agree,” end survey.

---

### Block 2 — Pre-Survey (Before Message)

#### A) Accuracy (Pre)
**H_PRE_Q1**  
**Question type:** Text Entry (Numeric)  
**Prompt:**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

**Validation:** numeric, allow 0–200 (or 0–300)

**H_PRE_Q1B** (optional)  
**Question type:** Slider or Multiple Choice (1–7)  
**Prompt:**  
How confident are you in your answer to the previous question?  
1 = Not confident at all … 7 = Very confident

---

#### B) Structural Understanding (Pre)
**Instructions (text):**  
Please indicate how much you agree or disagree with each statement.

**Scale (all S items):**  
1 Strongly disagree  
2 Disagree  
3 Somewhat disagree  
4 Neither agree nor disagree  
5 Somewhat agree  
6 Agree  
7 Strongly agree

**H_PRE_S1**  
Inequality is largely caused by **systems and policies** that shape opportunities.

**H_PRE_S2**  
Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.

**H_PRE_S3**  
Even when people work hard, **structural barriers** can limit economic outcomes.

**H_PRE_S4** *(reverse-coded)*  
Economic inequality is mainly the result of **individual choices and effort**.

---

#### C) Support for Solutions (Pre)
**Instructions (text):**  
Please indicate how much you agree or disagree with each statement.

**Scale (all P items):** (same 1–7 as above)

**H_PRE_P1**  
Government should take steps to reduce large gaps in wealth and opportunity.

**H_PRE_P2**  
Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.

**H_PRE_P3**  
Employers and institutions should review rules and practices to reduce unfair barriers.

**H_PRE_P4** *(reverse-coded)*  
Inequality is not a major problem, so major policy changes are unnecessary.

---

#### D) Optional Covariates (Pre)
**H_PRE_D1 (Education)**  
**Question type:** Multiple Choice (Single Answer)  
What is the highest level of education you have completed?  
- Less than high school  
- High school diploma / GED  
- Some college (no degree)  
- Associate degree  
- Bachelor’s degree  
- Graduate or professional degree  
- Prefer not to say

**H_PRE_D2 (Household income)**  
**Question type:** Multiple Choice (Single Answer)  
What is your approximate annual household income?  
- Less than $25,000  
- $25,000–$49,999  
- $50,000–$74,999  
- $75,000–$99,999  
- $100,000–$149,999  
- $150,000–$199,999  
- $200,000 or more  
- Prefer not to say

**H_PRE_D3 (Subjective SES ladder)** *(optional)*  
**Question type:** Multiple Choice (Single Answer)  
Imagine a ladder where 10 is the highest status in society and 1 is the lowest. Where do you see yourself on this ladder?  
- 1 2 3 4 5 6 7 8 9 10

**H_PRE_D4 (Ideology)** *(optional)*  
**Question type:** Multiple Choice (Single Answer)  
How would you describe your political ideology?  
- 1 Very liberal … 7 Very conservative

**H_PRE_D5 (Familiarity)** *(optional)*  
**Question type:** Multiple Choice (Single Answer)  
Before today, how familiar were you with wealth inequality statistics?  
- 1 Not at all familiar … 7 Very familiar

---

### Block 3 — Random Assignment + Stimulus Display
**Setup:** Create an Embedded Data field: `condition`

**Randomizer:** Randomly present ONE of the following 5 blocks (even allocation):
- Block 3A: structural_data
- Block 3B: narrative_story
- Block 3C: hybrid
- Block 3D: ai_explanation
- Block 3E: control

**Embedded Data values:**  
- If structural_data shown → set `condition = structural_data`  
- If narrative_story shown → set `condition = narrative_story`  
- If hybrid shown → set `condition = hybrid`  
- If ai_explanation shown → set `condition = ai_explanation`  
- If control shown → set `condition = control`

**Stimulus text display:**  
Paste only the participant-facing stimulus text.

---

### Block 4 — Post-Survey (After Message)

#### A) Accuracy (Post)
**H_POST_Q1**  
**Question type:** Text Entry (Numeric)  
**Prompt:**  
If a typical White non-Hispanic household has **$100** in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

**Validation:** numeric, allow 0–200 (or 0–300)

**H_POST_Q1B** (optional)  
**Question type:** Slider or Multiple Choice (1–7)  
**Prompt:**  
How confident are you in your answer to the previous question?  
1 = Not confident at all … 7 = Very confident

---

#### B) Structural Understanding (Post)
**Same scale (1–7) as pre**

**H_POST_S1**  
Inequality is largely caused by **systems and policies** that shape opportunities.

**H_POST_S2**  
Differences in wealth mostly reflect **unequal access to education, housing, and jobs**.

**H_POST_S3**  
Even when people work hard, **structural barriers** can limit economic outcomes.

**H_POST_S4** *(reverse-coded)*  
Economic inequality is mainly the result of **individual choices and effort**.

---

#### C) Support for Solutions (Post)
**Same scale (1–7) as pre**

**H_POST_P1**  
Government should take steps to reduce large gaps in wealth and opportunity.

**H_POST_P2**  
Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.

**H_POST_P3**  
Employers and institutions should review rules and practices to reduce unfair barriers.

**H_POST_P4** *(reverse-coded)*  
Inequality is not a major problem, so major policy changes are unnecessary.

---

#### D) Manipulation Checks (Post Only)
**H_POST_M1**  
**Question type:** Multiple Choice (Single Answer)  
**Prompt:** The message I read mainly emphasized:  
- 1 Personal choices/effort  
- 2  
- 3  
- 4  
- 5  
- 6  
- 7 Systems/policies/structures

**H_POST_M2**  
**Question type:** Multiple Choice (Single Answer)  
**Prompt:** The message included specific numbers or statistics.  
- 1 Strongly disagree … 7 Strongly agree

---

#### E) Data Quality Checks (Post Only; Humans Only)
**H_POST_A1 (Attention check)**  
**Question type:** Multiple Choice (Single Answer)  
**Prompt:** To show you’re paying attention, please select **“Agree”** below.  
- Strongly disagree  
- Disagree  
- Neutral  
- Agree  
- Strongly agree

**H_POST_C1 (Comprehension topic check)**  
**Question type:** Multiple Choice (Single Answer)  
**Prompt:** What was the main topic of the message you read?  
- Sleep and daily habits  
- Economic inequality and opportunity  
- Sports performance  
- Weather patterns

---

### Block 5 — Debrief
**H_DEBRIEF_1**  
**Prompt:**  
Thank you for participating. This study examines how different explanations influence people’s beliefs about inequality and their support for solutions. Your responses are anonymous. You may close the survey now.
