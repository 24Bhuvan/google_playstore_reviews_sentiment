# Play Store Sentiment Analysis Dashboard

An end-to-end NLP analytics solution that transforms raw Google Play Store user
reviews into actionable sentiment insights through automated text cleaning,
sentiment classification, visual analytics, and decision-ready reporting.

## Overview

This project implements a complete sentiment analysis pipeline designed for
product teams, startups, and businesses to quickly understand user perception,
app performance, and customer satisfaction.

The system ingests raw app reviews, processes unstructured text data, and
produces clear sentiment insights through charts, KPIs, and summary reports.

## Key Capabilities

Automated text cleaning and preprocessing
Sentiment classification (Positive, Neutral, Negative)
Review-level and aggregate sentiment analysis
Rating vs sentiment correlation analysis
Professional visualizations (bar, pie, word cloud)
Exportable insights for reporting and presentations

## Project Structure

playstore_sentiment_analysis/
│
├── data/
│ ├── raw_reviews.csv
│ └── cleaned_reviews.csv
│
├── notebooks/
│ └── sentiment_analysis.ipynb
│
├── outputs/
│ ├── charts/
│ │ ├── sentiment_distribution.png
│ │ ├── rating_vs_sentiment.png
│ │ └── wordcloud.png
│ └── sentiment_summary.xlsx
│
├── reports/
│ └── sentiment_insights.pdf
│
├── requirements.txt
├── pipeline.txt
├── structure.txt
└── README.md

## Analytics Workflow

Review data ingestion and validation
Text cleaning and normalization
Sentiment scoring and labeling
Aggregation by sentiment and rating
Visualization generation
Insight extraction and reporting

## Deliverables

Charts: Sentiment distribution, rating comparison, keyword insights (PNG)
KPIs: Sentiment percentages and review counts (Excel)
Insights Report: Executive-ready PDF with key findings
Clean Dataset: Preprocessed review data for reuse (CSV)

## Technology Stack

Python
pandas
nltk / textblob
matplotlib / seaborn
wordcloud

## Business Value

Identifies customer pain points and satisfaction drivers
Tracks user sentiment trends over time
Supports product improvement and feature prioritization
Enhances decision-making using real user feedback

## Use Cases

App review analysis
Customer feedback monitoring
Product quality assessment
Entry-level NLP analytics solution

## Status

Production-ready NLP analytics workflow
Designed for clarity, scalability, and real-world usability


