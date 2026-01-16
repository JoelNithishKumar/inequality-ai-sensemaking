import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Update this path to where your file is

ROOT = Path(__file__).resolve().parents[1]  # project root
DATA = ROOT / "processed" / "scored_combined_benchmark16.csv"
df = pd.read_csv(DATA)


hum = df[df["source"] == "human"].copy()
ai  = df[df["source"] == "ai"].copy()

out_dir = ROOT / "outputs"
out_dir.mkdir(exist_ok=True)


order = ["control", "narrative_story", "structural_data", "hybrid", "ai_explanation"]

def mean_se(series):
    s = pd.to_numeric(series, errors="coerce").dropna()
    if len(s) == 0:
        return np.nan, np.nan
    se = s.std(ddof=1) / np.sqrt(len(s)) if len(s) > 1 else 0.0
    return s.mean(), se

# 1) Humans: Structural shift by condition
means, ses = [], []
for c in order:
    m, se = mean_se(hum.loc[hum["condition"] == c, "structural_shift"])
    means.append(m); ses.append(se)

plt.figure()
plt.bar(order, means, yerr=ses, capsize=5)
plt.xticks(rotation=25, ha="right")
plt.ylabel("Mean structural shift (post - pre)")
plt.title("Humans: Structural understanding shift by message condition")
plt.tight_layout()
plt.savefig(out_dir / "humans_structural_shift_by_condition.png", dpi=200)
plt.close()

# 2) Humans: Policy shift by condition
means, ses = [], []
for c in order:
    m, se = mean_se(hum.loc[hum["condition"] == c, "policy_shift"])
    means.append(m); ses.append(se)

plt.figure()
plt.bar(order, means, yerr=ses, capsize=5)
plt.xticks(rotation=25, ha="right")
plt.ylabel("Mean policy shift (post - pre)")
plt.title("Humans: Policy support shift by message condition")
plt.tight_layout()
plt.savefig(out_dir / "humans_policy_shift_by_condition.png", dpi=200)
plt.close()

# 3) Humans: Pre accuracy error by condition (benchmark already baked into file)
means, ses = [], []
for c in order:
    m, se = mean_se(hum.loc[hum["condition"] == c, "pre_accuracy_error"])
    means.append(m); ses.append(se)

plt.figure()
plt.bar(order, means, yerr=ses, capsize=5)
plt.xticks(rotation=25, ha="right")
plt.ylabel("Mean |estimate - 16|")
plt.title("Humans: Pre-survey accuracy error by condition")
plt.tight_layout()
plt.savefig(out_dir / "humans_pre_accuracy_error_by_condition.png", dpi=200)
plt.close()

# 4) AI: Pre vs post structural mean by platform (one run each)
ai_plot = ai.sort_values("platform").copy()
x = np.arange(len(ai_plot))

plt.figure()
plt.plot(x, ai_plot["pre_structural_mean"], marker="o", label="pre")
plt.plot(x, ai_plot["post_structural_mean"], marker="o", label="post")
plt.xticks(x, ai_plot["platform"], rotation=25, ha="right")
plt.ylabel("Structural mean (1–7)")
plt.title("AI: Structural understanding (pre vs post) by platform\n(one run per platform; different conditions)")
plt.legend()
plt.tight_layout()
plt.savefig(out_dir / "ai_pre_post_structural_by_platform.png", dpi=200)
plt.close()

# 5) AI: Manipulation checks (post)
plt.figure()
plt.plot(x, ai_plot["post_M1_framing"], marker="o", label="M1_framing")
plt.plot(x, ai_plot["post_M2_stats"], marker="o", label="M2_stats")
plt.xticks(x, ai_plot["platform"], rotation=25, ha="right")
plt.ylim(0, 7.2)
plt.ylabel("Score (1–7)")
plt.title("AI: Manipulation checks (post)\n(one run per platform; different conditions)")
plt.legend()
plt.tight_layout()
plt.savefig(out_dir / "ai_manipulation_checks_by_platform.png", dpi=200)
plt.close()

print("Saved plots to:", out_dir.resolve())
