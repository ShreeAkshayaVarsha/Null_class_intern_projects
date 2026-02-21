import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

DATA_DIR = r"C:\Users\Aa\OneDrive\Desktop\Final project null class\project_1\data\docs"
VECTOR_DIR = "vector_store"
INDEX_PATH = f"{VECTOR_DIR}/index.faiss"
TEXTS_PATH = f"{VECTOR_DIR}/texts.pkl"
TRACK_PATH = f"{VECTOR_DIR}/ingested_files.txt"

os.makedirs(VECTOR_DIR, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load tracking file
ingested = set()
if os.path.exists(TRACK_PATH):
    with open(TRACK_PATH, "r") as f:
        ingested = set(f.read().splitlines())

# Load existing index
if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    texts = pickle.load(open(TEXTS_PATH, "rb"))
else:
    index = faiss.IndexFlatL2(384)
    texts = []

new_files = []

for file in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, file)
    if file not in ingested and file.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
        embeddings = model.encode(chunks)

        index.add(embeddings)
        texts.extend(chunks)

        new_files.append(file)

# Save updates
faiss.write_index(index, INDEX_PATH)
pickle.dump(texts, open(TEXTS_PATH, "wb"))

with open(TRACK_PATH, "a") as f:
    for nf in new_files:
        f.write(nf + "\n")

print(f"✅ Ingested {len(new_files)} new documents")