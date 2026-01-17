Sentiment Analysis Web Application
1. Project Overview

This repository implements an end-to-end Sentiment Analysis web application that classifies text as Positive or Negative using a supervised machine learning model.

The project demonstrates model training, API-based inference, and frontend integration in a clean, modular architecture suitable for real-world ML systems.

2. Key Capabilities

Binary sentiment classification

TF-IDF based text feature extraction

REST API for model inference

Browser-based frontend interface

Modular and maintainable codebase

3. Technology Stack
3.1 Backend

Python 3

FastAPI

scikit-learn

Uvicorn

joblib

3.2 Machine Learning

TF-IDF Vectorizer

Supervised classification model

3.3 Frontend

HTML

CSS

JavaScript (Fetch API)

3.4 Tooling

Git

GitHub

4. Repository Structure
sentiment-analysis/
├── backend/
│   ├── app.py
│   ├── train.py
│   └── model/
│       └── sentiment_model.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── notebooks/
│   └── exploration.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md

5. Dataset
5.1 Description

Name: Sentiment140

Size: ~1.6M tweets

Labels: Positive / Negative

5.2 Source

Dataset is intentionally excluded from version control.

Download from:

Kaggle: Sentiment140 Dataset

Expected path:

backend/data/training.1600000.processed.noemoticon.csv

6. Model Training

Run the training pipeline:

python backend/train.py


Generated artifact:

backend/model/sentiment_model.pkl


Observed accuracy during experimentation: ~0.79

7. Backend Setup and Execution
7.1 Environment Setup
python -m venv venv


Activate:

venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

7.2 Dependency Installation
pip install -r requirements.txt

7.3 Start API Server
uvicorn backend.app:app --reload


Swagger UI:

http://127.0.0.1:8000/docs

8. API Specification
8.1 Endpoint

POST /predict

8.2 Request
{
  "text": "I love this product"
}

8.3 Response
{
  "sentiment": "Positive"
}

9. Frontend Usage

Open frontend/index.html using Live Server

Enter text input

Click Analyze

View sentiment output

Frontend communicates with the backend via HTTP.

10. CORS Configuration

CORS middleware is enabled in FastAPI to allow browser-origin requests during development and deployment.

11. Version Control Practices

Virtual environments excluded

Dataset excluded

Model artifact tracked

Clean, readable commit history

12. Project Status

Model trained

API operational

Frontend integrated

Ready for deployment

13. Author

Jesmitha K
BTech Computer Science 

Focus areas:

Machine Learning systems

Backend API development

Full-stack integration
