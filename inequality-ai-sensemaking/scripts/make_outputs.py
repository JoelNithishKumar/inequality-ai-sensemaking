import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

# =========================
# SETTINGS (matches your layout)
# =========================
HUMANS_RAW = Path("data/raw/humans/humans_raw.csv")
AI_ROOT = Path("ai_runs")
OUT_DIR = Path("processed")          # change to Path("data/processed") if you prefer
OUT_DIR.mkdir(parents=True, exist_ok=True)

BENCHMARK = 16.0  # your chosen benchmark

LIKERT_MAP = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Somewhat disagree": 3,
    "Neither agree nor disagree": 4,
    "Somewhat agree": 5,
    "Agree": 6,
    "Strongly agree": 7,
}

AI_FILE_RE = re.compile(
    r"^(?P<platform>[a-z_]+)_(?P<condition>[a-z_]+)_(?P<runid>r\d+)_(?P<phase>pre|post)\.json$"
)

def reverse_1_to_7(x):
    return 8 - x

def map_likert(series: pd.Series) -> pd.Series:
    return series.map(LIKERT_MAP)

def safe_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")

# =========================
# 1) HUMANS -> human_clean.csv
# =========================
def build_human_clean(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Drop Qualtrics extra rows if present
    if "ResponseId" in df.columns:
        df = df[~df["ResponseId"].isin(["Response ID", '{"ImportId":"_recordId"}'])].copy()

    # Drop preview rows if present
    if "DistributionChannel" in df.columns:
        df = df[df["DistributionChannel"].astype(str).str.lower() != "preview"].copy()

    # Keep finished only, if present
    if "Finished" in df.columns:
        df = df[df["Finished"].astype(str).str.upper() == "TRUE"].copy()

    # Required columns based on your export
    required = ["Q", "condition"] + [f"Q{i}" for i in range(1, 17)]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns in human CSV: {missing}")

    out = pd.DataFrame()
    out["run_id"] = df.get("ResponseId", pd.Series(range(len(df)))).astype(str)
    out["source"] = "human"
    out["platform"] = "human"
    out["condition"] = df["condition"].astype(str)

    # Numeric estimate (PRE only in your human survey)
    out["pre_Q1_estimate"] = safe_numeric(df["Q"])

    # PRE Likerts Q1..Q8
    out["pre_S1"] = map_likert(df["Q1"])
    out["pre_S2"] = map_likert(df["Q2"])
    out["pre_S3"] = map_likert(df["Q3"])
    out["pre_S4"] = map_likert(df["Q4"])
    out["pre_P1"] = map_likert(df["Q5"])
    out["pre_P2"] = map_likert(df["Q6"])
    out["pre_P3"] = map_likert(df["Q7"])
    out["pre_P4"] = map_likert(df["Q8"])

    # POST Likerts Q9..Q16
    out["post_S1"] = map_likert(df["Q9"])
    out["post_S2"] = map_likert(df["Q10"])
    out["post_S3"] = map_likert(df["Q11"])
    out["post_S4"] = map_likert(df["Q12"])
    out["post_P1"] = map_likert(df["Q13"])
    out["post_P2"] = map_likert(df["Q14"])
    out["post_P3"] = map_likert(df["Q15"])
    out["post_P4"] = map_likert(df["Q16"])

    return out

# =========================
# 2) AI JSON -> ai_clean.csv
# =========================
def build_ai_clean(ai_root: Path) -> pd.DataFrame:
    rows = []
    for platform_dir in ai_root.iterdir():
        if not platform_dir.is_dir():
            continue
        for f in platform_dir.glob("*.json"):
            m = AI_FILE_RE.match(f.name)
            if not m:
                continue
            meta = m.groupdict()
            payload = json.loads(f.read_text(encoding="utf-8"))

            rows.append({
                "platform": meta["platform"],
                "condition": meta["condition"],
                "runid": meta["runid"],
                "phase": meta["phase"],
                **payload
            })

    df = pd.DataFrame(rows)
    if df.empty:
        raise ValueError("No AI JSON files found. Check AI_ROOT and filenames.")

    pre = df[df["phase"] == "pre"].copy()
    post = df[df["phase"] == "post"].copy()

    def prefix(d: pd.DataFrame, pfx: str) -> pd.DataFrame:
        keep = ["platform", "condition", "runid"]
        value_cols = [c for c in d.columns if c not in keep + ["phase"]]
        d = d[keep + value_cols].copy()
        d.rename(columns={c: f"{pfx}{c}" for c in value_cols}, inplace=True)
        return d

    pre_w = prefix(pre, "pre_")
    post_w = prefix(post, "post_")

    out = pd.merge(pre_w, post_w, on=["platform", "condition", "runid"], how="outer")
    out["run_id"] = out.apply(lambda r: f'{r["platform"]}_{r["condition"]}_{r["runid"]}', axis=1)
    out.drop(columns=["runid"], inplace=True)

    out["source"] = "ai"
    return out

# =========================
# 3) SCORING
# =========================
def add_scores(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()

    for phase in ["pre_", "post_"]:
        if f"{phase}S4" in d.columns:
            d[f"{phase}S4_rc"] = reverse_1_to_7(d[f"{phase}S4"])
        if f"{phase}P4" in d.columns:
            d[f"{phase}P4_rc"] = reverse_1_to_7(d[f"{phase}P4"])

    def mean_cols(cols):
        cols = [c for c in cols if c in d.columns]
        return d[cols].mean(axis=1, skipna=True) if cols else np.nan

    d["pre_structural_mean"]  = mean_cols(["pre_S1","pre_S2","pre_S3","pre_S4_rc"])
    d["post_structural_mean"] = mean_cols(["post_S1","post_S2","post_S3","post_S4_rc"])
    d["pre_policy_mean"]      = mean_cols(["pre_P1","pre_P2","pre_P3","pre_P4_rc"])
    d["post_policy_mean"]     = mean_cols(["post_P1","post_P2","post_P3","post_P4_rc"])

    d["structural_shift"] = d["post_structural_mean"] - d["pre_structural_mean"]
    d["policy_shift"]     = d["post_policy_mean"] - d["pre_policy_mean"]

    if "pre_Q1_estimate" in d.columns:
        d["pre_accuracy_error"] = (d["pre_Q1_estimate"] - BENCHMARK).abs()
    if "post_Q1_estimate" in d.columns:
        d["post_accuracy_error"] = (d["post_Q1_estimate"] - BENCHMARK).abs()

    if "pre_accuracy_error" in d.columns and "post_accuracy_error" in d.columns:
        d["accuracy_improvement"] = d["pre_accuracy_error"] - d["post_accuracy_error"]

    return d

# =========================
# 4) SUMMARY
# =========================
def build_pilot_summary(scored: pd.DataFrame) -> pd.DataFrame:
    return (
        scored.groupby(["source", "platform", "condition"], dropna=False)
        .agg(
            n=("run_id", "count"),
            pre_Q1_mean=("pre_Q1_estimate", "mean"),
            pre_Q1_median=("pre_Q1_estimate", "median"),
            pre_accuracy_error_mean=("pre_accuracy_error", "mean"),
            post_Q1_mean=("post_Q1_estimate", "mean"),
            post_accuracy_error_mean=("post_accuracy_error", "mean"),
            structural_shift_mean=("structural_shift", "mean"),
            policy_shift_mean=("policy_shift", "mean"),
        )
        .reset_index()
    )

# =========================
# RUN PIPELINE
# =========================
if __name__ == "__main__":
    human_clean = build_human_clean(HUMANS_RAW)
    ai_clean = build_ai_clean(AI_ROOT)

    human_clean.to_csv(OUT_DIR / "human_clean.csv", index=False)
    ai_clean.to_csv(OUT_DIR / "ai_clean.csv", index=False)

    combined = pd.concat([human_clean, ai_clean], ignore_index=True, sort=False)
    scored = add_scores(combined)
    scored.to_csv(OUT_DIR / "scored_combined_benchmark16.csv", index=False)

    summary = build_pilot_summary(scored)
    summary.to_csv(OUT_DIR / "pilot_summary_benchmark16.csv", index=False)

    print("Wrote:")
    print(" -", OUT_DIR / "human_clean.csv")
    print(" -", OUT_DIR / "ai_clean.csv")
    print(" -", OUT_DIR / "scored_combined_benchmark16.csv")
    print(" -", OUT_DIR / "pilot_summary_benchmark16.csv")
