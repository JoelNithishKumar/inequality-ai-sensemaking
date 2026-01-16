# AI Survey Script (v1) — Cross-Platform (ChatGPT / Gemini / Perplexity / Others)
**Project:** Human vs AI Inequality Sensemaking  
**Version:** v1  
**Purpose:** Run the same “PRE → STIMULUS → POST” survey on multiple AI platforms and compare outputs.  
**Start date for documentation:** 2025-10-19

---

## 1) How to use this script (important)
You will run this script **separately for each condition** and **separately for each AI platform**.

Example for one platform (e.g., ChatGPT):
- Run 1: structural_data
- Run 2: narrative_story
- Run 3: hybrid
- Run 4: ai_explanation
- Run 5: control

Then repeat the same 5 runs for Gemini, Perplexity, etc.

**Key rules**
- Copy/paste prompts exactly as written (avoid extra context).
- Run each condition in a **fresh chat/session** if possible (reduces “memory” contamination).
- Save both PRE and POST JSON outputs.

---

## 2) Recording template (fill this at the top of each run)
Before starting, write this somewhere (notes or a spreadsheet):

- Platform: (ChatGPT / Gemini / Perplexity / etc.)
- Model name/version (if visible):
- Date:
- Time:
- Condition: (structural_data / narrative_story / hybrid / ai_explanation / control)
- Run ID: (e.g., GPT_structural_001)

---

## 3) AI Instructions Prompt (paste first)
### Prompt A — AI Setup (paste into the AI platform)
```text
You are participating in a research-style survey. Follow these rules strictly:

1) Answer as if you are an average U.S. adult.
2) For numeric questions, return a number (integer or decimal).
3) For 1–7 questions, return an integer from 1 to 7 where:
   1 = Strongly disagree
   4 = Neither agree nor disagree
   7 = Strongly agree
4) Do not include explanations unless asked.
5) Output must be VALID JSON only (no extra text).

If you understand, reply with exactly: {"ready": true}
Expected response:

json
Copy code
{"ready": true}
If the AI adds extra text, re-paste Prompt A and say:

“Return JSON only.”

4) PRE Questions (paste second)
Prompt B — PRE Questions (paste into the AI platform after it replies ready)
text
Copy code
Answer the following PRE questions. Output VALID JSON only.

Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4
Expected output format (example template):

json
Copy code
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
  "P4": 0
}
What you do next: Save this JSON as your PRE response for the run.

5) STIMULUS + POST Questions (paste third)
After you get the PRE JSON, choose ONE of the 5 condition blocks below and paste it into the AI platform.

Important: The stimulus and the post questions must be pasted together in the same message to keep context stable.

5A) Condition: structural_data
Prompt C — Stimulus + POST (structural_data)

text
Copy code
Read the message below. Then answer the POST questions. Output VALID JSON only.

MESSAGE:
Many differences in wealth are not just about personal choices. Wealth grows over time through systems: access to safe neighborhoods, school quality, job networks, mortgages, and the ability to save and invest. If some groups face barriers in lending, housing, and hiring, those barriers can compound across generations. One national survey of U.S. family finances reports that the typical White non-Hispanic household has far more wealth than the typical Black non-Hispanic household—roughly $285,000 versus about $44,900 in median net worth. That gap is shaped by history and by rules and opportunities that affect where people can live, what jobs they can get, and how easily they can build assets. When we talk about inequality, it helps to consider how policies and institutions distribute opportunities, not only individual effort.

POST QUESTIONS:
Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Manipulation checks (POST only):
M1_framing:
The message mainly emphasized:
1 = Personal choices/effort
7 = Systems/policies/structures
(Respond 1–7)

M2_stats:
The message included specific numbers or statistics.
(1–7)

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4, M1_framing, M2_stats
5B) Condition: narrative_story
Prompt C — Stimulus + POST (narrative_story)

text
Copy code
Read the message below. Then answer the POST questions. Output VALID JSON only.

MESSAGE:
Jordan grew up in a neighborhood where the schools had fewer resources and the local jobs paid mostly hourly wages. When Jordan’s mom’s car broke down, she missed work and lost pay. Saving money was hard because unexpected costs kept showing up—rent increases, medical bills, and repairs. Later, Jordan worked two jobs while taking classes at night, but it still felt like getting ahead was slow. Meanwhile, Jordan noticed classmates from wealthier areas had family help: a parent who could co-sign a lease, a relative who knew how to apply for internships, or savings that made a short-term setback less damaging. Jordan’s story isn’t about a lack of effort. It’s about how starting points, support, and opportunities can shape what’s possible. Inequality can feel invisible until you see how different paths can be, even when people work equally hard.

POST QUESTIONS:
Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Manipulation checks (POST only):
M1_framing:
The message mainly emphasized:
1 = Personal choices/effort
7 = Systems/policies/structures
(Respond 1–7)

M2_stats:
The message included specific numbers or statistics.
(1–7)

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4, M1_framing, M2_stats
5C) Condition: hybrid
Prompt C — Stimulus + POST (hybrid)

text
Copy code
Read the message below. Then answer the POST questions. Output VALID JSON only.

MESSAGE:
When Maya graduated, she wanted to save for a home. She worked steadily, but rent rose and a medical bill wiped out her savings. Maya’s parents wanted to help but had little wealth to draw on. A friend from another neighborhood had family support for a down payment and access to better credit terms, so buying a home felt more achievable. These differences are not only personal—they are shaped by systems like housing markets, lending rules, school quality, and job opportunities. In national U.S. finance data, median household wealth differs dramatically by race: the typical White non-Hispanic household has been reported around $285,000 in net worth compared with about $44,900 for the typical Black non-Hispanic household. That kind of gap can influence what risks people can take and what opportunities they can afford. Stories like Maya’s show how structural barriers and resources can compound over time.

POST QUESTIONS:
Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Manipulation checks (POST only):
M1_framing:
The message mainly emphasized:
1 = Personal choices/effort
7 = Systems/policies/structures
(Respond 1–7)

M2_stats:
The message included specific numbers or statistics.
(1–7)

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4, M1_framing, M2_stats
5D) Condition: ai_explanation
Prompt C — Stimulus + POST (ai_explanation)

text
Copy code
Read the message below. Then answer the POST questions. Output VALID JSON only.

MESSAGE:
Inequality can be thought of as differences in resources and opportunities that build up over time. Wealth is not just income; it includes savings, a home, investments, and also debts. Because wealth can be passed from one generation to the next, small advantages or disadvantages can grow into large gaps. For example, if one group is more likely to receive help with tuition, down payments, or emergencies, they may avoid high-interest debt and build assets faster. Systems also matter: school funding, neighborhood safety, job access, and lending practices can influence who has the chance to save and invest. People often explain inequality in different ways—some focus on effort and choices, while others focus on access and barriers. In reality, both personal decisions and broader systems can play roles. Understanding inequality usually requires looking at how opportunities are distributed and how setbacks can affect families differently depending on the resources they start with.

POST QUESTIONS:
Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Manipulation checks (POST only):
M1_framing:
The message mainly emphasized:
1 = Personal choices/effort
7 = Systems/policies/structures
(Respond 1–7)

M2_stats:
The message included specific numbers or statistics.
(1–7)

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4, M1_framing, M2_stats
5E) Condition: control
Prompt C — Stimulus + POST (control)

text
Copy code
Read the message below. Then answer the POST questions. Output VALID JSON only.

MESSAGE:
Sleep is one of the most important parts of staying healthy and focused. During sleep, the brain consolidates memory, the body repairs tissues, and energy levels reset for the next day. Many people find that a consistent routine helps: going to bed and waking up at the same time, limiting bright screens before bed, and keeping the room dark and cool. Small habits can make a difference, such as avoiding large meals right before bedtime and getting some daylight exposure in the morning. If someone has trouble falling asleep, a simple approach is to write down worries or tasks earlier in the evening so the mind does not keep rehearsing them at night. Over time, improving sleep can support mood, attention, and performance in school or work. Even a short nap can help on some days, but regular nighttime sleep tends to be the most restorative.

POST QUESTIONS:
Q1_estimate:
If a typical White non-Hispanic household has $100 in wealth, about how many dollars does a typical Black or African American non-Hispanic household have?

Q1_confidence:
How confident are you in your answer to Q1?
(1–7)

Structural understanding (1–7):
S1: Inequality is largely caused by systems and policies that shape opportunities.
S2: Differences in wealth mostly reflect unequal access to education, housing, and jobs.
S3: Even when people work hard, structural barriers can limit economic outcomes.
S4: Economic inequality is mainly the result of individual choices and effort.

Support for solutions (1–7):
P1: Government should take steps to reduce large gaps in wealth and opportunity.
P2: Policies that expand access to quality education and job opportunities are worth supporting, even if they cost money.
P3: Employers and institutions should review rules and practices to reduce unfair barriers.
P4: Inequality is not a major problem, so major policy changes are unnecessary.

Manipulation checks (POST only):
M1_framing:
The message mainly emphasized:
1 = Personal choices/effort
7 = Systems/policies/structures
(Respond 1–7)

M2_stats:
The message included specific numbers or statistics.
(1–7)

Return JSON with exactly these keys:
Q1_estimate, Q1_confidence, S1, S2, S3, S4, P1, P2, P3, P4, M1_framing, M2_stats
6) How to store results (recommended)
After each run, save:

The PRE JSON output

The POST JSON output

The run metadata (platform, model, condition, run_id, date/time)

Suggested filename pattern

ai_runs/{platform}_{condition}_{runid}_pre.json

ai_runs/{platform}_{condition}_{runid}_post.json

Example

ai_runs/chatgpt_structural_data_001_pre.json

ai_runs/chatgpt_structural_data_001_post.json

Optional (recommended): Reliability check
Because AI outputs can vary, run each condition 3 times per platform and average:

accuracy changes (PRE → POST)

framing checks (M1, M2)

support/structural shifts

This improves reliability when comparing platforms.

makefile
Copy code
::contentReference[oaicite:0]{index=0}












