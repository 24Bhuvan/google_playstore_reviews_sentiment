# src/sentiment_analysis.py
# =====================================================
# PURPOSE:
# This module converts numeric user ratings into
# human-readable sentiment labels (Positive, Neutral,
# Negative) to enable clear customer insight analysis.
#
# BUSINESS VALUE:
# - Translates raw ratings into understandable emotions
# - Enables sentiment dashboards and reporting
# - Provides labeled data for ML and analytics pipelines
# - Simple, explainable logic suitable for stakeholders
# =====================================================

import pandas as pd
from pathlib import Path

# Input: cleaned review data produced by the data loading pipeline
IN_PATH = Path("data/processed/cleaned_reviews.csv")

# Output: sentiment-labeled dataset used by notebooks and reports
OUT_PATH = Path("data/processed/sentiment_labeled.csv")


def label_sentiment(score: int) -> str:
    """
    Maps numeric ratings to sentiment categories.

    Business logic:
    - 4 or 5 stars → Positive experience
    - 3 stars     → Neutral experience
    - 1 or 2 stars→ Negative experience

    This rule-based approach ensures transparency and
    easy explainability to non-technical stakeholders.
    """
    if score >= 4:
        return "Positive"
    elif score == 3:
        return "Neutral"
    else:
        return "Negative"


def main():
    # -------------------------------------------------
    # STEP 1: Load cleaned review data
    # -------------------------------------------------
    df = pd.read_csv(IN_PATH)

    # -------------------------------------------------
    # STEP 2: Validate and standardize rating values
    # -------------------------------------------------
    # Ensures scores are numeric and removes invalid entries
    # to maintain data quality and reliability
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df = df.dropna(subset=["score"])

    # -------------------------------------------------
    # STEP 3: Apply sentiment labeling logic
    # -------------------------------------------------
    # Converts star ratings into clear sentiment categories
    # that can be easily understood by business users
    df["sentiment"] = df["score"].astype(int).apply(label_sentiment)

    # -------------------------------------------------
    # STEP 4: Persist sentiment-labeled dataset
    # -------------------------------------------------
    # Creates output directory if needed and saves the
    # enriched dataset for downstream analytics
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Allows this script to run independently or as part
# of a larger automated data processing pipeline
if __name__ == "__main__":
    main()
