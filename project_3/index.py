import os
import faiss
import numpy as np
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

DATASET_DIR = "MedQuAD-master/MedicalQuAD"
model = SentenceTransformer('all-MiniLM-L6-v2')

questions = []
answers = []

for folder in os.listdir(DATASET_DIR):
    path = os.path.join(DATASET_DIR, folder)
    if not os.path.isdir(path):
        continue

    for file in os.listdir(path):
        if file.endswith(".xml"):
            xml_path = os.path.join(path, file)
            with open(xml_path, "r", encoding="utf-8") as f:
                xml = f.read()

            soup = BeautifulSoup(xml, "lxml")

            for item in soup.find_all("document"):
                q_text = item.find("question").text if item.find("question") else ""
                a_text = item.find("answer").text if item.find("answer") else ""

                if q_text.strip() and a_text.strip():
                    questions.append(q_text)
                    answers.append(a_text)

print("Total Q/A loaded:", len(questions))

embeddings = model.encode(questions, show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "medical_faiss.index")
np.save("medical_questions.npy", np.array(questions, dtype=object))
np.save("medical_answers.npy", np.array(answers, dtype=object))

print("FAISS index created successfully!")
