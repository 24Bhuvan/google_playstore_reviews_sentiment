# src/text_cleaning.py
import pandas as pd
import re
from pathlib import Path

IN_PATH = Path("data/processed/cleaned_reviews.csv")
OUT_PATH = Path("data/processed/cleaned_reviews.csv")

URL_RE = re.compile(r"http\S+|www\S+")
EMOJI_RE = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "]+",
    flags=re.UNICODE,
)
PUNCT_RE = re.compile(r"[^\w\s]")

def clean_text(text: str) -> str:
    text = text.lower()
    text = URL_RE.sub("", text)
    text = EMOJI_RE.sub("", text)
    text = PUNCT_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def main():
    df = pd.read_csv(IN_PATH)

    df["content"] = df["content"].astype(str).apply(clean_text)
    df = df.drop_duplicates(subset=["content"])
    df = df[df["content"].str.len() > 0]

    df.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
