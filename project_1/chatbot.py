from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("faiss_index/index.faiss")

with open("faiss_index/texts.txt", "r", encoding="utf-8") as f:
    docs = f.read().split("\n---\n")

def ask(question):
    q_embedding = model.encode([question])
    D, I = index.search(np.array(q_embedding), k=1)
    return docs[I[0][0]]

while True:
    q = input("Ask: ")
    print("\nAnswer from knowledge:\n", ask(q))
