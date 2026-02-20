from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import matplotlib.pyplot as plt


INDEX_DIR = "faiss_index"
index_path = os.path.join(INDEX_DIR, "index.faiss")
texts_path = os.path.join(INDEX_DIR, "texts.txt")
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(index_path)
with open(texts_path, "r", encoding="utf-8") as f:
    docs = [d.strip() for d in f.read().split("\n---\n") if d.strip()]
query = "What is FAISS?"


query_embedding = model.encode([query])


D, I = index.search(np.array(query_embedding), k=3)


labels = [f"Doc {i+1}" for i in range(len(D[0]))]
distances = D[0]

plt.figure()
plt.bar(labels, distances)
plt.xlabel("Retrieved Documents")
plt.ylabel("Distance (Lower = More Similar)")
plt.title("FAISS Similarity Scores for Query")
plt.show()

print("Query:", query)
print("\nRetrieved Documents:\n")
for idx in I[0]:
    print("-", docs[idx], "\n")
