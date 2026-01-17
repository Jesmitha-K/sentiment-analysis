from fastapi import FastAPI
from pydantic import BaseModel
import os
import joblib
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "sentiment_model.pkl")

model, vectorizer = joblib.load(MODEL_PATH)

class Tweet(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(tweet: Tweet):
    X = vectorizer.transform([tweet.text])
    pred = model.predict(X)[0]
    return {"sentiment": "Positive" if pred == 1 else "Negative"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)