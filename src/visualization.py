# src/visualization.py
# =====================================================
# PURPOSE:
# This script generates a visual summary of customer
# sentiment distribution in the form of a bar chart.
#
# BUSINESS VALUE:
# - Converts raw sentiment data into an easy-to-read visual
# - Helps stakeholders quickly understand customer mood
# - Suitable for reports, presentations, and dashboards
# - Automates chart generation for repeatable analysis
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Input: sentiment-labeled review dataset
IN_PATH = Path("data/processed/sentiment_labeled.csv")

# Output directory and chart file
OUT_DIR = Path("outputs/charts")
OUT_FILE = OUT_DIR / "sentiment_distribution.png"


def main():
    # -------------------------------------------------
    # STEP 1: Load sentiment-labeled data
    # -------------------------------------------------
    df = pd.read_csv(IN_PATH)

    # -------------------------------------------------
    # STEP 2: Aggregate sentiment counts
    # -------------------------------------------------
    # Counts how many reviews fall into each sentiment
    # category (Positive / Neutral / Negative)
    counts = df["sentiment"].value_counts().sort_index()

    # -------------------------------------------------
    # STEP 3: Generate and save visualization
    # -------------------------------------------------
    # Creates output folder if it does not exist
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Builds a clean, presentation-ready bar chart
    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()

    # Saves the chart as an image file
    plt.savefig(OUT_FILE)
    plt.close()


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Allows this script to be executed independently or
# as part of a larger automated analytics pipeline
if __name__ == "__main__":
    main()
