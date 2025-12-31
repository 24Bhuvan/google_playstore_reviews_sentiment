# src/wordcloud_generator.py
# =====================================================
# PURPOSE:
# This script creates a word cloud visualization from
# customer review text to highlight the most frequently
# discussed topics and themes.
#
# BUSINESS VALUE:
# - Quickly reveals what customers talk about most
# - Helps product and support teams spot trends
# - Complements sentiment charts with qualitative insight
# - Easy-to-understand visual for non-technical audiences
# =====================================================

import pandas as pd
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Input: sentiment-labeled review dataset
IN_PATH = Path("data/processed/sentiment_labeled.csv")

# Output directory and word cloud image
OUT_DIR = Path("outputs/charts")
OUT_FILE = OUT_DIR / "wordcloud.png"


def main():
    # -------------------------------------------------
    # STEP 1: Load review data
    # -------------------------------------------------
    df = pd.read_csv(IN_PATH)

    # -------------------------------------------------
    # STEP 2: Combine all review text
    # -------------------------------------------------
    # Merges all review content into a single text corpus
    # to analyze overall discussion themes
    text = " ".join(df["content"].dropna().astype(str))

    # -------------------------------------------------
    # STEP 3: Generate word cloud
    # -------------------------------------------------
    # Creates a visual representation of word frequency
    # Larger words indicate more frequent mentions
    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        collocations=False  # avoids repeated word pairs
    ).generate(text)

    # -------------------------------------------------
    # STEP 4: Save visualization
    # -------------------------------------------------
    # Ensures output directory exists and saves the image
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc)
    plt.axis("off")        # removes axes for cleaner visuals
    plt.tight_layout()
    plt.savefig(OUT_FILE)
    plt.close()


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Enables standalone execution and integration into
# automated analytics or reporting pipelines
if __name__ == "__main__":
    main()
