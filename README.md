# AI Candidate Discovery & Ranking System

## Overview

Recruiters often miss strong candidates because traditional ATS systems rely heavily on keyword matching. This project builds an AI-powered candidate ranking system that understands candidate profiles semantically and ranks them based on true job fit rather than exact keyword matches.

The solution was developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

## Features

### Intelligent Job Understanding

* Analyzes job descriptions
* Extracts required skills and experience
* Identifies behavioral and hiring signals
* Understands semantic meaning instead of keyword matching

### Candidate Analysis

* Processes complete candidate profiles
* Evaluates career history
* Reviews education and certifications
* Analyzes skills and proficiency levels
* Incorporates Redrob behavioral signals

### Hybrid Ranking Engine

The ranking score combines:

* Semantic Similarity (35%)
* Skill Match (25%)
* Experience Match (15%)
* Behavioral Signals (15%)
* Leadership/Product Mindset (10%)

### Behavioral Intelligence

Uses Redrob platform signals such as:

* Recruiter response rate
* Interview completion rate
* GitHub activity
* Profile completeness
* Open-to-work status
* Notice period
* Recruiter engagement

### Explainable AI

Generates recruiter-friendly reasoning for every recommendation, helping hiring teams understand why a candidate was ranked highly.

---

## Project Structure

```text
project/
│
├── app.py
├── data_loader.py
├── scoring.py
├── ranker.py
├── requirements.txt
│
├── data/
│   ├── candidates.jsonl
│   ├── sample_candidates.json
│   └── job_description.md
│
├── outputs/
│   └── submission.csv
│
└── README.md
```

---

## Technology Stack

### Backend

* Python
* Pandas
* NumPy

### AI & Machine Learning

* Sentence Transformers
* FAISS
* Semantic Embeddings
* Hybrid Ranking Models

### Frontend

* Streamlit

### Ranking Techniques

* Semantic Search
* Vector Similarity
* Behavioral Scoring
* Rule-Based Ranking
* Hybrid AI Scoring

---

## Workflow

```text
Job Description
        │
        ▼
 JD Understanding
        │
        ▼
 Candidate Processing
        │
        ▼
 Semantic Matching
        │
        ▼
 Behavioral Analysis
        │
        ▼
 Hybrid Scoring
        │
        ▼
 Candidate Ranking
        │
        ▼
 Top 100 Candidates
```

---

## Output

The system generates:

* Ranked Top 100 Candidates
* Candidate Score
* AI-Based Reasoning
* CSV Submission File

Example:

| Rank | Candidate ID | Score |
| ---- | ------------ | ----- |
| 1    | CAND_0042871 | 0.987 |
| 2    | CAND_0019884 | 0.973 |
| 3    | CAND_0091235 | 0.962 |

---

## Future Improvements

* Learning-to-Rank Models
* XGBoost Ranker
* Cross Encoder Re-ranking
* Fine-tuned Embedding Models
* Recruiter Feedback Loop
* Online A/B Testing

---

## Author

Sejal Rani

B.Tech Computer Science Engineering

AI • Data Analytics • Power BI • Azure • Machine Learning
