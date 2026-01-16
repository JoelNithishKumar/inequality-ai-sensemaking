from pathlib import Path
import pandas as pd

BENCHMARK = 16

RAW_PATH = Path("data/raw/humans/humans_raw.csv")
OUT_PATH = Path("data/processed/humans_scored.csv")

def main():
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Could not find: {RAW_PATH.resolve()}")

    df = pd.read_csv(RAW_PATH)

    # ✅ You said these are already renamed in the CSV
    required = ["pre_Q1_estimate", "post_Q1_estimate"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing columns: {missing}. "
            f"Make sure humans_raw.csv has pre_Q1_estimate and post_Q1_estimate."
        )

    # Convert to numeric safely
    df["pre_Q1_estimate"] = pd.to_numeric(df["pre_Q1_estimate"], errors="coerce")
    df["post_Q1_estimate"] = pd.to_numeric(df["post_Q1_estimate"], errors="coerce")

    # Compute errors + improvement
    df["pre_accuracy_error"] = (df["pre_Q1_estimate"] - BENCHMARK).abs()
    df["post_accuracy_error"] = (df["post_Q1_estimate"] - BENCHMARK).abs()
    df["accuracy_improvement"] = df["pre_accuracy_error"] - df["post_accuracy_error"]

    # Ensure output directory exists
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save
    df.to_csv(OUT_PATH, index=False)

    # Quick sanity output
    print("Saved:", OUT_PATH.resolve())
    print(df[["pre_Q1_estimate", "post_Q1_estimate",
              "pre_accuracy_error", "post_accuracy_error",
              "accuracy_improvement"]].head(10))

if __name__ == "__main__":
    main()
