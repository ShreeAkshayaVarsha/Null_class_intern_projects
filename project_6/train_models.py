import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -------- Sentiment Model --------
sent_df = pd.read_csv("sentiment_data.csv")
sent_vectorizer = TfidfVectorizer()
X_sent = sent_vectorizer.fit_transform(sent_df["text"])
y_sent = sent_df["sentiment"]

sent_model = LogisticRegression()
sent_model.fit(X_sent, y_sent)

joblib.dump(sent_model, "sentiment_model.pkl")
joblib.dump(sent_vectorizer, "sentiment_vectorizer.pkl")

# -------- Intent Model --------
intent_df = pd.read_csv("intent_data.csv")
intent_vectorizer = TfidfVectorizer()
X_intent = intent_vectorizer.fit_transform(intent_df["text"])
y_intent = intent_df["intent"]

intent_model = LogisticRegression()
intent_model.fit(X_intent, y_intent)

joblib.dump(intent_model, "intent_model.pkl")
joblib.dump(intent_vectorizer, "intent_vectorizer.pkl")

print("Models trained successfully")
