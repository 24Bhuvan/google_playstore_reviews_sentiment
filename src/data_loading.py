# src/data_loading.py
# =====================================================
# PURPOSE:
# This script is responsible for ingesting raw Google
# Play Store review data, cleaning it, and producing a
# standardized dataset ready for analytics, dashboards,
# and machine learning workflows.
#
# BUSINESS VALUE:
# - Ensures consistent, high-quality input data
# - Removes noise and unusable records
# - Creates a reliable foundation for sentiment analysis
# - Fully automated and repeatable data pipeline step
# =====================================================

import pandas as pd
from pathlib import Path

# Location of raw, unprocessed Play Store review data
# This represents the original data source (unchanged)
RAW_PATH = Path("data/raw/playstore_reviews.csv")

# Location where cleaned, analytics-ready data will be stored
# Downstream components (notebooks, models, dashboards)
# depend on this standardized output
OUT_PATH = Path("data/processed/cleaned_reviews.csv")


def main():
    # -------------------------------------------------
    # STEP 1: Load raw data
    # -------------------------------------------------
    # Reads the original review dataset into memory
    # This is equivalent to loading a source table in a data warehouse
    df = pd.read_csv(RAW_PATH)

    # -------------------------------------------------
    # STEP 2: Select business-relevant fields only
    # -------------------------------------------------
    # Keeps only columns required for insights and modeling
    # Reduces storage size, improves performance, and
    # enforces a clean data contract for downstream systems
    df = df[
        ["content", "score", "at", "thumbsUpCount", "replyContent"]
    ]

    # -------------------------------------------------
    # STEP 3: Remove unusable records
    # -------------------------------------------------
    # Reviews without textual content cannot contribute
    # to sentiment analysis or customer insight extraction
    df = df.dropna(subset=["content"])

    # -------------------------------------------------
    # STEP 4: Standardize timestamp format
    # -------------------------------------------------
    # Converts review timestamps into a consistent datetime format
    # Invalid or corrupt values are safely handled instead of
    # breaking the pipeline
    df["at"] = pd.to_datetime(df["at"], errors="coerce")

    # -------------------------------------------------
    # STEP 5: Ensure output directory exists
    # -------------------------------------------------
    # Automatically creates required folders so the pipeline
    # can run in any environment (local, cloud, CI/CD)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------
    # STEP 6: Persist cleaned data
    # -------------------------------------------------
    # Writes a clean, analysis-ready dataset
    # This file becomes the single source of truth for:
    # - Reporting
    # - Dashboards
    # - Machine learning models
    df.to_csv(OUT_PATH, index=False)


# -----------------------------------------------------
# ENTRY POINT
# -----------------------------------------------------
# Guarantees predictable execution behavior and allows
# this script to be safely reused as part of a larger
# automated data pipeline
if __name__ == "__main__":
    main()
