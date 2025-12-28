# src/wordcloud_generator.py
import pandas as pd
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

IN_PATH = Path("data/processed/sentiment_labeled.csv")
OUT_DIR = Path("outputs/charts")
OUT_FILE = OUT_DIR / "wordcloud.png"

def main():
    df = pd.read_csv(IN_PATH)
    text = " ".join(df["content"].dropna().astype(str))

    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        collocations=False
    ).generate(text)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(OUT_FILE)
    plt.close()

if __name__ == "__main__":
    main()
