# Dynamic Knowledge Expansion Chatbot

## Project Overview
This project implements a chatbot that can dynamically expand its knowledge base.
New documents are automatically ingested, converted into vector embeddings, and stored
in a vector database. The chatbot retrieves relevant information using semantic search
and answers user queries without retraining the model.

---

## Problem Statement
Implement a system for dynamically expanding a chatbot's knowledge base by periodically
updating a vector database with new information from specified sources.

---

## Expected Outcome
A chatbot that can:
- Automatically ingest new documents
- Update its vector database dynamically
- Retrieve information using semantic similarity
- Answer questions using the latest knowledge

---

## Project Structure

project_7/
│
├── data/
│   └── docs/
│       └── sample.txt
│
├── vector_store/        (auto-generated)
│   ├── index.faiss
│   ├── texts.pkl
│   └── ingested_files.txt
│
├── ingest.py
├── retriever.py
├── chatbot.py
├── scheduler.py
└── README.md

---

## Technologies Used
- Python
- FAISS
- Sentence Transformers
- Hugging Face Models
- Semantic Search

---

## Installation

Install required libraries:

pip install faiss-cpu sentence-transformers

---

## How to Run the Project

### Step 1: Add Knowledge Files
Place text files inside:

data/docs/

Example:
data/docs/sample.txt

---

### Step 2: Build the Vector Database (First Run)

python ingest.py

This will:
- Create the vector_store folder
- Generate embeddings
- Store document tracking information

---

### Step 3: Run the Chatbot

python chatbot.py

Ask questions related to the ingested documents.

---

## Dynamic Knowledge Expansion

To add new knowledge:
1. Add a new .txt file inside data/docs/
2. Run python ingest.py again
3. The chatbot will immediately use the new information

---

## Automatic Updates (Optional)

Run:

python scheduler.py

This script periodically checks for new documents and updates the vector database.

---

## Example Queries
- What is artificial intelligence?
- What is a vector database?
- Explain machine learning
- What is FAISS used for?

---

## Notes
- UNEXPECTED model warnings are normal and can be ignored
- Hugging Face token warning is optional
- No model retraining is required

---

## Limitations
- Retrieval-based responses (no summarization)
- Supports text files only

---

## Future Enhancements
- Add LLM-based response generation (RAG)
- Support PDF and web ingestion
- Add web or GUI interface
- Use cloud-based vector databases

---

## Conclusion
This project demonstrates a dynamic knowledge expansion system where a chatbot
continuously learns from new data using vector embeddings and semantic search.

---

## Author
Varsha  
Final Project – Null Class Internship