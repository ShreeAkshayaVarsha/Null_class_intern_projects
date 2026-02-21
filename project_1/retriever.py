import faiss
import pickle
from sentence_transformers import SentenceTransformer

INDEX_PATH = "vector_store/index.faiss"
TEXTS_PATH = "vector_store/texts.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)
texts = pickle.load(open(TEXTS_PATH, "rb"))

def retrieve(query, k=3):
    q_embedding = model.encode([query])
    distances, indices = index.search(q_embedding, k)
    return [texts[i] for i in indices[0]]