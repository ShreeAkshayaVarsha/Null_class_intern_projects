import streamlit as st
from chatbot import get_answer

st.set_page_config(page_title="Medical QA Chatbot", layout="wide")

st.title("🩺 Medical Question Answering Bot (MedQuAD Powered)")

user_input = st.text_input("Ask any medical question:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = get_answer(user_input)
        st.success(answer)
