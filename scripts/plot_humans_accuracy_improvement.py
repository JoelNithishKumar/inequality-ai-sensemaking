# scripts/plot_humans_accuracy_improvement.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Input (combined scored file)
df = pd.read_csv("data/processed/updated_scored_combined_benchmark16.csv")

# Filter humans only
hum = df[df["source"] == "human"].copy()

# Output folder
out_dir = Path("outputs")
out_dir.mkdir(parents=True, exist_ok=True)

# Order of conditions (same as your earlier plots)
order = ["control", "narrative_story", "structural_data", "hybrid", "ai_explanation"]

def mean_se(series):
    s = pd.to_numeric(series, errors="coerce").dropna()
    if len(s) == 0:
        return np.nan, np.nan
    se = s.std(ddof=1) / np.sqrt(len(s)) if len(s) > 1 else 0.0
    return s.mean(), se

# Compute mean + SE per condition
means, ses = [], []
for c in order:
    m, se = mean_se(hum.loc[hum["condition"] == c, "accuracy_improvement"])
    means.append(m)
    ses.append(se)

# Plot
plt.figure()
plt.bar(order, means, yerr=ses, capsize=5)
plt.xticks(rotation=25, ha="right")
plt.axhline(0, linewidth=1)  # zero line
plt.ylabel("Mean accuracy improvement (|pre-16| - |post-16|)")
plt.title("Humans: Accuracy improvement by message condition (benchmark=16)")
plt.tight_layout()

out_path = out_dir / "humans_accuracy_improvement_by_condition.png"
plt.savefig(out_path, dpi=200)
plt.close()

print("Saved plot to:", out_path.resolve())
