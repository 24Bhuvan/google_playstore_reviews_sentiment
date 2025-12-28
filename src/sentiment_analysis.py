# src/sentiment_analysis.py
import pandas as pd
from pathlib import Path

IN_PATH = Path("data/processed/cleaned_reviews.csv")
OUT_PATH = Path("data/processed/sentiment_labeled.csv")

def label_sentiment(score: int) -> str:
    if score >= 4:
        return "Positive"
    elif score == 3:
        return "Neutral"
    else:
        return "Negative"

def main():
    df = pd.read_csv(IN_PATH)

    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df = df.dropna(subset=["score"])

    df["sentiment"] = df["score"].astype(int).apply(label_sentiment)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
