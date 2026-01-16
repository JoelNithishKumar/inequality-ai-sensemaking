## Mermaid Flowchart 2

flowchart TD
  A["Project Objective
Test how messages about inequality change:
1) beliefs (structural understanding + policy support)
2) accuracy of racial wealth-gap estimates
Compare Humans vs AI systems"] --> B["Design
5 message conditions:
control, narrative_story,
structural_data, hybrid,
ai_explanation"]

  B --> C["Humans (Qualtrics)
Random assignment to 1 of 5 conditions"]
  B --> D["AI Platforms (1 run each)
Each platform got 1 condition
(platform & condition confounded)"]

  %% HUMAN PIPELINE
  C --> C1["Pre measures
pre_Q1_estimate (accuracy)
pre structural items
pre policy items"]
  C1 --> C2["Stimulus exposure
(one condition)"]
  C2 --> C3["Post measures
post_Q1_estimate (accuracy)
post structural items
post policy items"]

  C3 --> H1["Compute Human Outcomes
Accuracy error = |estimate-16|
Accuracy improvement = |pre-16| - |post-16|
Structural shift = post - pre
Policy shift = post - pre"]

  H1 --> RQ1H["RQ1 (Humans): Which message improves accuracy most?"]
  RQ1H --> RHAcc["Result (Pilot):
structural_data shows the largest accuracy improvement
hybrid / ai_explanation moderate
narrative_story smaller
control minimal"]

  H1 --> RQ2H["RQ2 (Humans): Which message increases policy support most?"]
  RQ2H --> RHPol["Result (Pilot):
structural_data shows the largest policy shift
hybrid / ai_explanation positive
narrative_story positive smaller
control minimal"]

  H1 --> RQ3H["RQ3 (Humans): Does structural understanding explain policy change?"]
  RQ3H --> RHMed["Result (Pilot):
Directional pattern consistent:
conditions that raise structural understanding often raise policy support
Not a mediation test yet (needs regression/mediation analysis)"]

  %% AI PIPELINE
  D --> A1["AI Pre JSON
pre_Q1_estimate
pre structural items
pre policy items"]
  A1 --> A2["Stimulus exposure
(one condition per platform)"]
  A2 --> A3["AI Post JSON
post_Q1_estimate
post structural items
post policy items
Manipulation checks: M1_framing, M2_stats"]

  A3 --> AIOut["Compute AI Outcomes
Accuracy error + improvement (same benchmark=16)
Structural mean pre vs post
Manipulation checks"]

  AIOut --> AIInterp["AI Result (Pilot):
Pre/post shifts can be measured per platform
But: only 1 run each AND each platform got different condition
=> cannot separate platform vs condition"]

  %% COMPARISON NODE
  RHAcc --> COMP["Human vs AI Comparison (Pilot v1)"]
  AIInterp --> COMP
  COMP --> Takeaway["Main Takeaway (Pilot v1):
Humans: message type appears to affect accuracy and policy support
AI: measurement pipeline works, but inference is limited
Next step: run all 5 platforms x all 5 conditions (+replicates)"]
