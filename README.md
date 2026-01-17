Sentiment Analysis Web Application
Overview

This repository contains an end-to-end Sentiment Analysis web application that classifies input text as Positive or Negative using a supervised machine learning model.
The system is designed with clear separation between model training, backend inference API, and frontend UI, following standard ML system design practices.

The project demonstrates practical ML deployment, not just experimentation.

Key Features

Supervised sentiment classification using TF-IDF features

RESTful inference API built with FastAPI

Lightweight frontend for real-time predictions

Modular, maintainable project structure

Ready for local development and extension

Tech Stack
Backend

Python 3

FastAPI

scikit-learn

joblib

Uvicorn

Machine Learning

TF-IDF Vectorizer

Supervised text classification model

Frontend

HTML

CSS

JavaScript (Fetch API)

Tooling

Git

GitHub

Project Structure
sentiment-analysis/
│
├── backend/
│   ├── app.py                # FastAPI inference service
│   ├── train.py              # Model training pipeline
│   └── model/
│       └── sentiment_model.pkl
│
├── frontend/
│   ├── index.html             # UI entry point
│   ├── style.css              # Styling
│   └── script.js              # API integration logic
│
├── notebooks/
│   └── exploration.ipynb      # Data analysis & experiments
│
├── .gitignore
├── requirements.txt
└── README.md

Dataset

Dataset: Sentiment140 (Twitter sentiment dataset)

Size: ~1.6 million labeled tweets

Labels: Positive / Negative

Source

The dataset is not committed to the repository.

Download manually from:

Kaggle: Sentiment140 Dataset

Expected path:

backend/data/training.1600000.processed.noemoticon.csv

Model Training

To train the sentiment classifier locally:

python backend/train.py


This will generate the trained model artifact:

backend/model/sentiment_model.pkl


Observed accuracy during experimentation: ~0.79
(Exact performance may vary depending on preprocessing and split.)

Backend Setup
Create virtual environment
python -m venv venv


Activate:

venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux

Install dependencies
pip install -r requirements.txt

Run API server
uvicorn backend.app:app --reload

API Reference
Endpoint

POST /predict

Request
{
  "text": "I love this product"
}

Response
{
  "sentiment": "Positive"
}

API Documentation

Swagger UI available at:

http://127.0.0.1:8000/docs

Frontend Usage

Open frontend/index.html using Live Server (VS Code recommended)

Enter text in the input field

Click Analyze

Sentiment result is displayed instantly

The frontend communicates with the backend via POST /predict.

CORS

CORS middleware is enabled in FastAPI to support browser-based frontend requests during development.

Repository Practices

Virtual environments excluded

Dataset excluded

Model artifact tracked (small size)

Clear directory boundaries

GitHub-ready structure

Current Status

Model training completed

API functional

Frontend integrated

Local deployment verified

Author

Jesmitha K
BTech Computer Science Graduate

Focus areas:

Machine Learning systems

Backend API development

End-to-end project delivery
