import streamlit as st
import pandas as pd
import json
import nltk
import torch
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download("punkt")

# ---------------------------------
# CONFIG
# ---------------------------------
DATA_PATH = r"C:\Users\Aa\OneDrive\Desktop\Final project null class\arxiv-cs-chatbot\data\arxiv-metadata-oai-snapshot.json"
MAX_PAPERS = 3000

# ---------------------------------
# LOAD DATA (MEMORY SAFE)
# ---------------------------------
@st.cache_data
def load_data(max_papers):
    records = []
    count = 0

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            paper = json.loads(line)

            # ONLY NLP PAPERS
            if "categories" in paper and "cs.CL" in paper["categories"]:
                records.append({
                    "title": paper.get("title", "").strip(),
                    "abstract": paper.get("abstract", "").strip()[:1200],
                    "categories": paper.get("categories", "")
                })
                count += 1

            if count >= max_papers:
                break

    return pd.DataFrame(records)
# ---------------------------------
# SEARCH ENGINE
# ---------------------------------
@st.cache_data
def build_search_engine(texts):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=2000,
        dtype="float32"
    )
    vectors = vectorizer.fit_transform(texts)
    return vectorizer, vectors

# ---------------------------------
# LOAD OPEN-SOURCE LLM (FLAN-T5)
# ---------------------------------
@st.cache_resource
def load_llm():
    return pipeline(
        "text-generation",
        model="google/flan-t5-small",
        device=0 if torch.cuda.is_available() else -1,
        max_new_tokens=150
    )

# ---------------------------------
# EXTRACTIVE FALLBACK SUMMARY
# ---------------------------------
def extractive_summary(text, max_sentences=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])

# ---------------------------------
# WORD CLOUD VISUALIZATION
# ---------------------------------
def show_wordcloud(text):
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)

# ---------------------------------
# STREAMLIT UI
# ---------------------------------
st.set_page_config(page_title="Computer Science Research Chatbot", layout="wide")
st.title("🤖 Computer Science Research Chatbot")
st.write("NLP / AI Research Assistant using arXiv papers")

# Load resources
df = load_data(MAX_PAPERS)
vectorizer, vectors = build_search_engine(df["abstract"])
llm = load_llm()

# ---------------------------------
# USER QUERY
# ---------------------------------
query = st.text_input("🔍 Ask a research question (e.g., Explain transformers in NLP)")

if query:
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, vectors)[0]
    top_indices = similarities.argsort()[-3:][::-1]

    st.subheader("📄 Relevant Research Papers")

    combined_text = ""

    for idx in top_indices:
        paper = df.iloc[idx]
        combined_text += paper["abstract"] + " "

        st.markdown(f"### {paper['title']}")
        st.write(f"**Category:** {paper['categories']}")

        with st.expander("📘 Abstract"):
            st.write(paper["abstract"])

        with st.expander("🧠 Simplified Explanation (LLM)"):
            prompt = f"Explain this research paper in simple terms:\n{paper['abstract']}"
            try:
                response = llm(prompt)[0]["generated_text"]
                st.write(response)
            except:
                st.write(extractive_summary(paper["abstract"]))

    # ---------------------------------
    # CONCEPT VISUALIZATION
    # ---------------------------------
    st.subheader("📊 Concept Visualization")
    show_wordcloud(combined_text)

# ---------------------------------
# FOLLOW-UP QUESTIONS
# ---------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if query:
    st.subheader("💬 Ask Follow-up Questions")

follow_up = st.text_input("Ask a follow-up question")

if follow_up and query:
    st.session_state.chat_history.append(follow_up)

    context = " ".join(df.iloc[top_indices]["abstract"].tolist())
    prompt = f"Based on the following research context, answer the question:\nContext:{context}\nQuestion:{follow_up}"

    try:
        answer = llm(prompt)[0]["generated_text"]
    except:
        answer = extractive_summary(context, 4)

    st.markdown("### 🤖 Chatbot Answer")
    st.write(answer)

    st.markdown("### 🕘 Conversation History")
    for i, q in enumerate(st.session_state.chat_history, 1):
        st.write(f"{i}. {q}")
