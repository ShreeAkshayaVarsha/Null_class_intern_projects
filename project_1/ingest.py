from sentence_transformers import SentenceTransformer
import faiss
import os
import numpy as np

DATA_DIR = "data"
INDEX_DIR = "faiss_index"

os.makedirs(INDEX_DIR, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(DATA_DIR, file), "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                texts.append(content)

if not texts:
    raise ValueError("No valid text found in data folder")

embeddings = model.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, os.path.join(INDEX_DIR, "index.faiss"))

with open(os.path.join(INDEX_DIR, "texts.txt"), "w", encoding="utf-8") as f:
    for t in texts:
        f.write(t + "\n---\n")

print(" Knowledge base created with", len(texts), "documents")
