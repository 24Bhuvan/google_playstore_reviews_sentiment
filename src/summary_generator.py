# src/summary_generator.py
# =====================================================
# PURPOSE:
# This script generates a high-level, human-readable
# sentiment summary from labeled review data.
#
# BUSINESS VALUE:
# - Converts raw analytics into executive-friendly insights
# - Highlights overall customer mood
# - Surfaces most common complaint keywords
# - Produces a simple text report usable by non-technical teams
# =====================================================

import pandas as pd
from pathlib import Path
from collections import Counter

# Input: sentiment-labeled review data
IN_PATH = Path("data/processed/sentiment_labeled.csv")

# Output: plain-text summary report
OUT_FILE = Path("outputs/summary.txt")


def main():
    # -------------------------------------------------
    # STEP 1: Load sentiment-labeled data
    # -------------------------------------------------
    df = pd.read_csv(IN_PATH)

    # -------------------------------------------------
    # STEP 2: Calculate overall sentiment distribution
    # -------------------------------------------------
    # Converts sentiment counts into percentages
    # This helps stakeholders quickly understand customer mood
    total = len(df)
    sentiment_pct = (df["sentiment"].value_counts(normalize=True) * 100).round(2)

    # -------------------------------------------------
    # STEP 3: Extract common complaint keywords
    # -------------------------------------------------
    # Focuses only on negative reviews to identify
    # recurring issues and pain points
    negative_text = " ".join(
        df[df["sentiment"] == "Negative"]["content"].dropna()
    )

    # Counts the most frequently occurring words
    # Used as a lightweight alternative to complex NLP models
    common_words = Counter(negative_text.split()).most_common(10)

    # -------------------------------------------------
    # STEP 4: Determine overall app sentiment
    # -------------------------------------------------
    # Identifies the dominant sentiment category
    # (Positive / Neutral / Negative)
    overall = sentiment_pct.idxmax()

    # -------------------------------------------------
    # STEP 5: Write summary report to file
    # -------------------------------------------------
    # Produces a clean, readable text report that can be:
    # - Shared with product teams
    # - Sent to stakeholders
    # - Used in presentations or audits
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("Sentiment Percentage:\n")
        for k, v in sentiment_pct.items():
            f.write(f"{k}: {v}%\n")

        f.write("\nTop Complaint Keywords:\n")
        for word, count in common_words:
            f.write(f"{word}: {count}\n")

        f.write(f"\nOverall App Sentiment: {overall}\n")


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Ensures predictable execution and allows this script
# to be integrated into automated analytics pipelines
if __name__ == "__main__":
    main()
