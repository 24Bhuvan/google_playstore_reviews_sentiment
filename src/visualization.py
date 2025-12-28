# src/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

IN_PATH = Path("data/processed/sentiment_labeled.csv")
OUT_DIR = Path("outputs/charts")
OUT_FILE = OUT_DIR / "sentiment_distribution.png"

def main():
    df = pd.read_csv(IN_PATH)

    counts = df["sentiment"].value_counts().sort_index()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig(OUT_FILE)
    plt.close()

if __name__ == "__main__":
    main()
