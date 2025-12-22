# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns

# Set theme for greyscale-friendly plots
sns.set_theme(context="notebook", style="whitegrid", font_scale=1.1)
plt.rcParams["figure.dpi"] = 120

# ==========================
# Data
# ==========================
data = [
    {"Tag": "truth/facts", "Justification": "Combine – Applies to ensuring that data analysis reflects reality.", "Frequency": 71},
    {"Tag": "privacy", "Justification": "Compile – Relevant to data collection.", "Frequency": 54},
    {"Tag": "distortion/manipulation", "Justification": "Combine – Addresses risks of bias.", "Frequency": 53},
    {"Tag": "accuracy", "Justification": "Communicate – Critical in final reporting.", "Frequency": 49},
    {"Tag": "access/use", "Justification": "Compile – Ethical access to data.", "Frequency": 43},
    {"Tag": "verification", "Justification": "Compile – Data validation.", "Frequency": 34},
    {"Tag": "source/disclosure", "Justification": "Compile – Transparency of sources.", "Frequency": 31},
    {"Tag": "fairness", "Justification": "Communicate – Balance in presentation.", "Frequency": 28},
    {"Tag": "transparency", "Justification": "Communicate – Disclosure of methods.", "Frequency": 26},
    {"Tag": "source/reliability", "Justification": "Compile – Credibility of sources.", "Frequency": 21},
    {"Tag": "graphics/visualisation", "Justification": "Communicate – Ethical visual design.", "Frequency": 17},
    {"Tag": "responsibility", "Justification": "Communicate – Accountability.", "Frequency": 13},
    {"Tag": "discrimination/stereotypes", "Justification": "Communicate – Avoiding bias.", "Frequency": 12},
    {"Tag": "objectivity", "Justification": "Combine – Interpretation and analysis.", "Frequency": 12},
    {"Tag": "ugc", "Justification": "Compile – User-generated content.", "Frequency": 6},
    {"Tag": "surveys/polls", "Justification": "Combine – Methodological issues.", "Frequency": 3},
    {"Tag": "analysis/statistics", "Justification": "Combine – Statistical reasoning.", "Frequency": 2},
]

df = pd.DataFrame(data)

# Extract Bradshaw stage from justification
df["Stage"] = df["Justification"].str.split("–", n=1).str[0].str.strip()
df = df.sort_values("Frequency", ascending=False)

# Greyscale colors by stage
stage_colors = {
    "Compile": "#4d4d4d",
    "Combine": "#7f7f7f",
    "Communicate": "#b3b3b3",
}
bar_colors = df["Stage"].map(stage_colors).fillna("#999999")

# ==========================
# Plot: Frequency by category
# ==========================
plt.figure(figsize=(14, 7))
ax = plt.gca()

ax.bar(df["Tag"], df["Frequency"], color=bar_colors, edgecolor="black")

ax.set_title("Frequency of Ethical Categories by Bradshaw Stage", fontsize=14)
ax.set_xlabel("Ethical Category")
ax.set_ylabel("Frequency (Number of Mentions)")
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(rotation=45, ha="right")

# Create greyscale legend
handles = [plt.Line2D([0], [0], color=color, lw=10) for color in stage_colors.values()]
ax.legend(handles, stage_colors.keys(), title="Bradshaw Stage")

plt.tight_layout()
plt.savefig("frequency_by_stage_greyscale.png", dpi=300)
plt.savefig("frequency_by_stage_greyscale.svg")
plt.show()
