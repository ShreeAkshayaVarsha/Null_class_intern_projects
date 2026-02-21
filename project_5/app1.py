import streamlit as st
import re
import matplotlib.pyplot as plt
import pandas as pd


# Page title

st.title("Customer Sentiment Aware Chatbot")


# Sentiment word lists

positive_words = [
    "good", "great", "excellent", "happy", "love",
    "awesome", "nice", "satisfied", "amazing"
]

negative_words = [
    "bad", "poor", "worst", "sad", "hate",
    "angry", "frustrated", "disappointed", "problem", "issue"
]


# Sentiment analysis function

def analyze_sentiment(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  
    words = text.split()
    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    return score


# User input

user_input = st.text_input("Type your message here:")

# Store history for analytics
if "history" not in st.session_state:
    st.session_state.history = []


# Process input

if user_input:
    score = analyze_sentiment(user_input)

    if score > 0:
        sentiment = "Positive"
        response = "😊 I’m glad to hear that! Let me know if you need any help."
    elif score < 0:
        sentiment = "Negative"
        response = "😔 I’m sorry for the inconvenience. I’m here to help you."
    else:
        sentiment = "Neutral"
        response = "🙂 Thank you for your message. How can I assist you?"

    st.write("**Detected Sentiment:**", sentiment)
    st.write("**Chatbot Response:**", response)

    # Save conversation for analytics
    st.session_state.history.append(sentiment)


# Analytics Button

st.markdown("---")
show_analytics = st.button("📊 Show Analytics")

if show_analytics and st.session_state.history:

    st.subheader("📈 Sentiment Analytics")

    # Convert history to DataFrame
    sentiment_counts = pd.Series(st.session_state.history).value_counts()

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Positive", sentiment_counts.get("Positive", 0))
    col2.metric("Negative", sentiment_counts.get("Negative", 0))
    col3.metric("Neutral", sentiment_counts.get("Neutral", 0))

    
    # Small Bar Chart
    
    fig, ax = plt.subplots(figsize=(4, 3))
    sentiment_counts.plot(kind="bar", ax=ax)
    ax.set_title("Sentiment Distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.pyplot(fig)

elif show_analytics:
    st.info("No data yet. Start chatting to generate analytics.")
