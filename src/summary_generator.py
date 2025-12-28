# src/summary_generator.py
import pandas as pd
from pathlib import Path
from collections import Counter

IN_PATH = Path("data/processed/sentiment_labeled.csv")
OUT_FILE = Path("outputs/summary.txt")

def main():
    df = pd.read_csv(IN_PATH)

    total = len(df)
    sentiment_pct = (df["sentiment"].value_counts(normalize=True) * 100).round(2)

    negative_text = " ".join(df[df["sentiment"] == "Negative"]["content"].dropna())
    common_words = Counter(negative_text.split()).most_common(10)

    overall = sentiment_pct.idxmax()

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("Sentiment Percentage:\n")
        for k, v in sentiment_pct.items():
            f.write(f"{k}: {v}%\n")

        f.write("\nTop Complaint Keywords:\n")
        for word, count in common_words:
            f.write(f"{word}: {count}\n")

        f.write(f"\nOverall App Sentiment: {overall}\n")

if __name__ == "__main__":
    main()
