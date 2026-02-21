import streamlit as st
import joblib
import os
import pandas as pd
from datetime import datetime

# NLP & Translation
from langdetect import detect
from deep_translator import GoogleTranslator

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# PAGE CONFIG

st.set_page_config(page_title="Multilingual Intelligent Chatbot", layout="wide")
st.title("🌍 Multilingual Intelligent Chatbot")


# LOAD MODELS

sent_model = joblib.load("sentiment_model.pkl")
sent_vectorizer = joblib.load("sentiment_vectorizer.pkl")

intent_model = joblib.load("intent_model.pkl")
intent_vectorizer = joblib.load("intent_vectorizer.pkl")

# LOG FILE

DATA_FILE = "chatbot_logs.csv"

# FUNCTIONS

def translate_text(text, target_lang):
    return GoogleTranslator(source="auto", target=target_lang).translate(text)

def get_response(intent, sentiment):
    responses = {
        "greeting": {
            "positive": "Hello! 😊 How can I help you?",
            "neutral": "Hello! How can I assist you?",
            "negative": "Hello. I’m here to help."
        },
        "complaint": {
            "positive": "Thanks for sharing. How can I help?",
            "neutral": "Please tell me your issue.",
            "negative": "I’m really sorry for the inconvenience 🙏"
        },
        "help": {
            "positive": "Sure! Happy to help 😊",
            "neutral": "I’m here to assist you.",
            "negative": "Don’t worry, I’ll help you."
        },
        "feedback": {
            "positive": "Thank you for your feedback! 😊",
            "neutral": "Thanks for sharing.",
            "negative": "Thank you. We’ll improve."
        }
    }
    return responses.get(intent, {}).get(sentiment, "How can I help you?")

def log_interaction(text, lang, sentiment, intent):
    log_data = {
        "timestamp": datetime.now(),
        "language": lang,
        "sentiment": sentiment,
        "intent": intent,
        "text": text
    }
    df = pd.DataFrame([log_data])

    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)

# CHAT INPUT

user_input = st.text_input("💬 Type your message:")

if user_input:
    try:
        lang = detect(user_input)
    except:
        lang = "en"

    # Fix English detection
    if user_input.isascii():
        lang = "en"

    # Translate input only if needed
    if lang == "en":
        input_en = user_input
    else:
        input_en = translate_text(user_input, "en")

    # Sentiment prediction
    sent_vec = sent_vectorizer.transform([input_en])
    sentiment = sent_model.predict(sent_vec)[0]

    # Intent prediction
    intent_vec = intent_vectorizer.transform([input_en])
    intent = intent_model.predict(intent_vec)[0]

    # Bot response
    reply_en = get_response(intent, sentiment)

    if lang == "en":
        final_reply = reply_en
    else:
        final_reply = translate_text(reply_en, lang)

    st.markdown("### 🤖 Bot:")
    st.success(final_reply)

    log_interaction(user_input, lang, sentiment, intent)


# ANALYTICS BUTTON

st.divider()
show_analytics = st.button("📊 Show Analytics Dashboard")

if show_analytics:

    st.header("📊 Chatbot Analytics Dashboard")

    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)

        col1, col2 = st.columns(2)

        
        # Sentiment Distribution
        
        with col1:
            st.subheader("😊 Sentiment Distribution")
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.countplot(x="sentiment", data=data, ax=ax)
            st.pyplot(fig)

        
        # Language Distribution
        
        with col2:
            st.subheader("🌍 Language Usage")
            fig, ax = plt.subplots(figsize=(4, 3))
            data["language"].value_counts().plot(kind="bar", ax=ax)
            ax.set_xlabel("Language")
            ax.set_ylabel("Messages")
            st.pyplot(fig)

        
        # Intent Pie Chart
        
        st.subheader("🎯 Intent Distribution")
        fig = px.pie(
            data,
            names="intent",
            title="User Intent Breakdown"
        )
        st.plotly_chart(fig, use_container_width=False)

        
        # Sentiment vs Intent Heatmap
        
        st.subheader("🔥 Sentiment vs Intent Analysis")
        pivot = pd.crosstab(data["intent"], data["sentiment"])
        fig, ax = plt.subplots(figsize=(5, 3))
        sns.heatmap(pivot, annot=True, fmt="d", ax=ax)
        st.pyplot(fig)

    else:
        st.info("No interaction data available yet. Start chatting to see analytics.")
