# src/data_loading.py
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/playstore_reviews.csv")
OUT_PATH = Path("data/processed/cleaned_reviews.csv")

def main():
    df = pd.read_csv(RAW_PATH)

    df = df[
        ["content", "score", "at", "thumbsUpCount", "replyContent"]
    ]

    df = df.dropna(subset=["content"])
    df["at"] = pd.to_datetime(df["at"], errors="coerce")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
