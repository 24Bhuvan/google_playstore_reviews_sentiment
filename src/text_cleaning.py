# src/text_cleaning.py
# =====================================================
# PURPOSE:
# This module standardizes and cleans raw review text
# to make it suitable for analytics and sentiment analysis.
#
# BUSINESS VALUE:
# - Improves data quality and consistency
# - Removes noise that does not add business insight
# - Increases accuracy of sentiment classification
# - Ensures clean, repeatable text preprocessing
# =====================================================

import pandas as pd
import re
from pathlib import Path

# Input & output paths
# This step enriches the existing cleaned dataset
IN_PATH = Path("data/processed/cleaned_reviews.csv")
OUT_PATH = Path("data/processed/cleaned_reviews.csv")

# -----------------------------------------------------
# REGEX PATTERNS
# -----------------------------------------------------

# Matches URLs such as http:// or www links
# These do not contribute to sentiment understanding
URL_RE = re.compile(r"http\S+|www\S+")

# Matches emojis and symbols
# Emojis are removed to maintain consistent text input
# across different languages and platforms
EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "]+",
    flags=re.UNICODE,
)

# Matches punctuation characters
# Keeps only words and spaces for cleaner analysis
PUNCT_RE = re.compile(r"[^\w\s]")


def clean_text(text: str) -> str:
    """
    Applies standardized text cleaning rules.

    Cleaning steps:
    - Convert text to lowercase
    - Remove URLs
    - Remove emojis and symbols
    - Remove punctuation
    - Normalize extra spaces

    Result:
    Produces clean, uniform text suitable for
    sentiment analysis and keyword extraction.
    """
    text = text.lower()
    text = URL_RE.sub("", text)
    text = EMOJI_RE.sub("", text)
    text = PUNCT_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    # -------------------------------------------------
    # STEP 1: Load previously cleaned review data
    # -------------------------------------------------
    df = pd.read_csv(IN_PATH)

    # -------------------------------------------------
    # STEP 2: Apply text cleaning pipeline
    # -------------------------------------------------
    # Converts all review content into a standardized format
    # to ensure consistency across the dataset
    df["content"] = df["content"].astype(str).apply(clean_text)

    # -------------------------------------------------
    # STEP 3: Remove duplicate and empty reviews
    # -------------------------------------------------
    # Prevents repeated content from skewing insights
    # and removes rows with no meaningful text
    df = df.drop_duplicates(subset=["content"])
    df = df[df["content"].str.len() > 0]

    # -------------------------------------------------
    # STEP 4: Save cleaned dataset
    # -------------------------------------------------
    # Overwrites the processed file to keep downstream
    # pipelines simple and consistent
    df.to_csv(OUT_PATH, index=False)


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Enables standalone execution and integration
# into larger automated data pipelines
if __name__ == "__main__":
    main()
