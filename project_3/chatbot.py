import json
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------
# PART 1 → BUILD VECTOR STORE (RUN ONLY ONE TIME)
# ---------------------------------------------------

def build_vector_store():
    import os

    DATA_PATH = r"D:\downloads\MedQuAD-master\medquad_final.json"

    print("Loading MedQuAD dataset...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    answers = []

    for item in data:
        q = item["question"]
        a = item["answer"]
        focus = item["focus"]

        doc_text = f"{focus}. Question: {q}"
        documents.append(doc_text)
        answers.append(a)

    print("Generating embeddings...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    doc_embeddings = model.encode(documents, convert_to_numpy=True)

    vector_store = {
        "documents": documents,
        "answers": answers,
        "embeddings": doc_embeddings,
    }

    # 🔥 CREATE THE DIRECTORY IF IT DOES NOT EXIST
    os.makedirs("models", exist_ok=True)

    pickle.dump(vector_store, open("models/vector_store.pkl", "wb"))
    print("🎉 Vector store created successfully! Saved as models/vector_store.pkl")

# ---------------------------------------------------
# PART 2 → ANSWERING FUNCTION
# ---------------------------------------------------

def get_answer(query):
    store = pickle.load(open("models/vector_store.pkl", "rb"))

    docs = store["documents"]
    answers = store["answers"]
    embeddings = store["embeddings"]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embed = model.encode([query])

    scores = cosine_similarity(query_embed, embeddings)[0]
    best_idx = np.argmax(scores)

    return answers[best_idx]


# ---------------------------------------------------
# AUTO RUN VECTOR STORE CREATION
# ONLY if vector_store.pkl does NOT exist
# ---------------------------------------------------

import os

if not os.path.exists("models/vector_store.pkl"):
    print("vector_store.pkl not found → creating it now...")
    build_vector_store()
else:
    print("Vector store already exists ✔")
