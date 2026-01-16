# scripts/build_scored_combined.py
from pathlib import Path
import pandas as pd
import numpy as np

BENCHMARK = 16

HUMANS_PATH = Path("data/processed/humans_scored.csv")
AI_PATH     = Path("data/processed/ai_clean.csv")

OUT_COMBINED = Path("data/processed/updated_scored_combined_benchmark16.csv")
OUT_SUMMARY  = Path("data/processed/updated_pilot_summary_benchmark16.csv")


def reverse_1_to_7(x):
    # reverse-code a 1–7 item: 1<->7, 2<->6, 3<->5, 4 stays 4
    return 8 - x


def coerce_numeric(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def drop_qualtrics_label_row(df):
    """
    Qualtrics exports often include a 2nd row that contains the full question text.
    In your case, it shows values like 'Start Date', 'End Date', 'Response Type', etc.
    We detect and drop that row.
    """
    # Common signals from your export
    for col in ["StartDate", "ResponseId", "Status"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    mask = pd.Series(False, index=df.index)
    if "StartDate" in df.columns:
        mask = mask | df["StartDate"].str.strip().eq("Start Date")
    if "ResponseId" in df.columns:
        mask = mask | df["ResponseId"].str.strip().eq("Response ID")
    if "Status" in df.columns:
        mask = mask | df["Status"].str.strip().eq("Response Type")

    return df.loc[~mask].copy()


def pick_condition(df):
    # Prefer lowercase 'condition' if it has values; otherwise use 'Condition'
    cond = None
    if "condition" in df.columns:
        if df["condition"].notna().any():
            cond = "condition"
    if cond is None and "Condition" in df.columns:
        cond = "Condition"
    if cond is None:
        raise ValueError("Could not find a usable condition/Condition column.")
    df["condition"] = df[cond].astype(str).str.strip().str.lower()
    return df


def build_humans(hum):
    # Clean label row and condition
    hum = drop_qualtrics_label_row(hum)
    hum = pick_condition(hum)

    # Ensure numeric
    hum = coerce_numeric(
        hum,
        [
            "pre_Q1_estimate", "post_Q1_estimate",
            "Q1","Q2","Q3","Q4","Q5","Q6","Q7",
            "Q8","Q9","Q10","Q11","Q12","Q13","Q14","Q15","Q16",
            "pre_accuracy_error","post_accuracy_error","accuracy_improvement"
        ],
    )

    # --- Human scoring assumptions based on your exported question text ---
    # PRE structural: Q1,Q2,Q3, reverse(Q4)
    # PRE policy:     Q5,Q6,Q7   (no reverse policy item in PRE block in this export)
    #
    # POST estimate column exists, then:
    # POST policy reverse item: Q8 (inequality not major problem...)
    # POST structural: Q9,Q10,Q11, reverse(Q12)
    # POST policy: Q13,Q14,Q15, reverse(Q16)

    hum["pre_structural_mean"] = pd.concat(
        [hum["Q1"], hum["Q2"], hum["Q3"], reverse_1_to_7(hum["Q4"])], axis=1
    ).mean(axis=1, skipna=True)

    hum["pre_policy_mean"] = pd.concat(
        [hum["Q5"], hum["Q6"], hum["Q7"]], axis=1
    ).mean(axis=1, skipna=True)

    hum["post_structural_mean"] = pd.concat(
        [hum["Q9"], hum["Q10"], hum["Q11"], reverse_1_to_7(hum["Q12"])], axis=1
    ).mean(axis=1, skipna=True)

    hum["post_policy_mean"] = pd.concat(
        [hum["Q13"], hum["Q14"], hum["Q15"], reverse_1_to_7(hum["Q16"])], axis=1
    ).mean(axis=1, skipna=True)

    hum["structural_shift"] = hum["post_structural_mean"] - hum["pre_structural_mean"]
    hum["policy_shift"]     = hum["post_policy_mean"] - hum["pre_policy_mean"]

    # Accuracy (recompute to be safe, even if already present)
    hum["pre_accuracy_error"]  = (hum["pre_Q1_estimate"]  - BENCHMARK).abs()
    hum["post_accuracy_error"] = (hum["post_Q1_estimate"] - BENCHMARK).abs()
    hum["accuracy_improvement"] = hum["pre_accuracy_error"] - hum["post_accuracy_error"]

    out = pd.DataFrame({
        "source": "human",
        "platform": pd.NA,
        "run_id": pd.NA,
        "condition": hum["condition"],
        "pre_Q1_estimate": hum["pre_Q1_estimate"],
        "post_Q1_estimate": hum["post_Q1_estimate"],
        "pre_accuracy_error": hum["pre_accuracy_error"],
        "post_accuracy_error": hum["post_accuracy_error"],
        "accuracy_improvement": hum["accuracy_improvement"],
        "pre_structural_mean": hum["pre_structural_mean"],
        "post_structural_mean": hum["post_structural_mean"],
        "structural_shift": hum["structural_shift"],
        "pre_policy_mean": hum["pre_policy_mean"],
        "post_policy_mean": hum["post_policy_mean"],
        "policy_shift": hum["policy_shift"],
        "post_M1_framing": pd.NA,
        "post_M2_stats": pd.NA,
    })

    return out


def build_ai(ai):
    # Normalize condition
    ai = ai.copy()
    ai["condition"] = ai["condition"].astype(str).str.strip().str.lower()

    # Ensure numeric
    ai = coerce_numeric(
        ai,
        [
            "pre_Q1_estimate", "post_Q1_estimate",
            "pre_S1","pre_S2","pre_S3","pre_S4",
            "pre_P1","pre_P2","pre_P3","pre_P4",
            "post_S1","post_S2","post_S3","post_S4",
            "post_P1","post_P2","post_P3","post_P4",
            "post_M1_framing","post_M2_stats",
        ],
    )

    ai["pre_structural_mean"] = pd.concat(
        [ai["pre_S1"], ai["pre_S2"], ai["pre_S3"], reverse_1_to_7(ai["pre_S4"])], axis=1
    ).mean(axis=1, skipna=True)

    ai["post_structural_mean"] = pd.concat(
        [ai["post_S1"], ai["post_S2"], ai["post_S3"], reverse_1_to_7(ai["post_S4"])], axis=1
    ).mean(axis=1, skipna=True)

    ai["pre_policy_mean"] = pd.concat(
        [ai["pre_P1"], ai["pre_P2"], ai["pre_P3"], reverse_1_to_7(ai["pre_P4"])], axis=1
    ).mean(axis=1, skipna=True)

    ai["post_policy_mean"] = pd.concat(
        [ai["post_P1"], ai["post_P2"], ai["post_P3"], reverse_1_to_7(ai["post_P4"])], axis=1
    ).mean(axis=1, skipna=True)

    ai["structural_shift"] = ai["post_structural_mean"] - ai["pre_structural_mean"]
    ai["policy_shift"]     = ai["post_policy_mean"] - ai["pre_policy_mean"]

    ai["pre_accuracy_error"]  = (ai["pre_Q1_estimate"]  - BENCHMARK).abs()
    ai["post_accuracy_error"] = (ai["post_Q1_estimate"] - BENCHMARK).abs()
    ai["accuracy_improvement"] = ai["pre_accuracy_error"] - ai["post_accuracy_error"]

    out = pd.DataFrame({
        "source": "ai",
        "platform": ai["platform"].astype(str),
        "run_id": ai.get("run_id", pd.NA),
        "condition": ai["condition"],
        "pre_Q1_estimate": ai["pre_Q1_estimate"],
        "post_Q1_estimate": ai["post_Q1_estimate"],
        "pre_accuracy_error": ai["pre_accuracy_error"],
        "post_accuracy_error": ai["post_accuracy_error"],
        "accuracy_improvement": ai["accuracy_improvement"],
        "pre_structural_mean": ai["pre_structural_mean"],
        "post_structural_mean": ai["post_structural_mean"],
        "structural_shift": ai["structural_shift"],
        "pre_policy_mean": ai["pre_policy_mean"],
        "post_policy_mean": ai["post_policy_mean"],
        "policy_shift": ai["policy_shift"],
        "post_M1_framing": ai.get("post_M1_framing", pd.NA),
        "post_M2_stats": ai.get("post_M2_stats", pd.NA),
    })

    return out


def summarize(combined):
    # Human summary by condition
    human_sum = (
        combined[combined["source"] == "human"]
        .groupby(["source", "condition"], dropna=False)
        .agg(
            n=("accuracy_improvement", lambda s: s.notna().sum()),
            mean_pre_error=("pre_accuracy_error", "mean"),
            mean_post_error=("post_accuracy_error", "mean"),
            mean_accuracy_improvement=("accuracy_improvement", "mean"),
            mean_structural_shift=("structural_shift", "mean"),
            mean_policy_shift=("policy_shift", "mean"),
        )
        .reset_index()
    )

    # AI summary by platform (and condition)
    ai_sum = (
        combined[combined["source"] == "ai"]
        .groupby(["source", "platform", "condition"], dropna=False)
        .agg(
            n=("accuracy_improvement", lambda s: s.notna().sum()),
            mean_pre_error=("pre_accuracy_error", "mean"),
            mean_post_error=("post_accuracy_error", "mean"),
            mean_accuracy_improvement=("accuracy_improvement", "mean"),
            mean_structural_shift=("structural_shift", "mean"),
            mean_policy_shift=("policy_shift", "mean"),
            mean_post_M1_framing=("post_M1_framing", "mean"),
            mean_post_M2_stats=("post_M2_stats", "mean"),
        )
        .reset_index()
    )

    # Stack
    summary = pd.concat([human_sum, ai_sum], ignore_index=True, sort=False)
    return summary


def main():
    if not HUMANS_PATH.exists():
        raise FileNotFoundError(f"Missing humans file: {HUMANS_PATH.resolve()}")
    if not AI_PATH.exists():
        raise FileNotFoundError(f"Missing AI file: {AI_PATH.resolve()}")

    hum = pd.read_csv(HUMANS_PATH)
    ai  = pd.read_csv(AI_PATH)

    hum_out = build_humans(hum)
    ai_out  = build_ai(ai)

    combined = pd.concat([hum_out, ai_out], ignore_index=True)

    OUT_COMBINED.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(OUT_COMBINED, index=False)

    summary = summarize(combined)
    summary.to_csv(OUT_SUMMARY, index=False)

    print("Wrote:", OUT_COMBINED.resolve())
    print("Wrote:", OUT_SUMMARY.resolve())
    print("\nCombined preview:")
    print(combined.head(10))
    print("\nSummary preview:")
    print(summary.head(20))


if __name__ == "__main__":
    main()
