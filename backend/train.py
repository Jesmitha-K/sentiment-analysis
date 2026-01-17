import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training.1600000.processed.noemoticon.csv")

MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")
os.makedirs(MODEL_DIR, exist_ok=True)


# ---------- load data ----------
df = pd.read_csv(DATA_PATH, encoding="latin-1", header=None)
df = df[[0, 5]]
df.columns = ["polarity", "text"]
df = df[df.polarity != 2]
df["polarity"] = df["polarity"].map({0: 0, 4: 1})

# ---------- vectorize ----------
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["text"])
y = df["polarity"]

# ---------- train ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# ---------- save ----------
joblib.dump(
    (model, vectorizer),
    os.path.join(MODEL_DIR, "sentiment_model.pkl")
)
