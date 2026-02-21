#  Medical Question Answering Chatbot (MedQuAD Powered)

##  Project Overview
This project implements a **Medical Question Answering Chatbot** using the **MedQuAD dataset**.  
The chatbot retrieves the most relevant medical answer by comparing semantic similarity between user queries and a pre-built medical knowledge base using **Sentence Transformers** and **Vector Search**.

The application provides a **Streamlit-based web interface** for easy interaction.


##  Objectives
- Build a medical question-answering system using real medical data
- Convert medical Q&A pairs into vector embeddings
- Perform semantic search using cosine similarity / FAISS
- Provide an interactive chatbot UI using Streamlit

## Dataset Used
**MedQuAD (Medical Question Answering Dataset)**  
- Contains thousands of medical questions and answers  
- Data originally stored in XML format  
- Converted into structured JSON/CSV for processing



## Technologies Used
- **Python**
- **Streamlit** – Web UI
- **SentenceTransformers** (`all-MiniLM-L6-v2`)
- **Scikit-learn** – Cosine similarity
- **FAISS** – Fast vector search
- **NumPy, Pandas**
- **BeautifulSoup & XML parsing**


##  How It Works

### 1. Dataset Processing
- XML medical files are parsed
- Question–Answer pairs are extracted
- Data is saved as `medquad_final.json`

### 2. Vector Store Creation
- Questions are converted into embeddings
- Stored with answers using Pickle OR FAISS
- Created only once (auto-check implemented)

### 3. Query Handling
- User question is embedded
- Compared with stored embeddings
- Most similar answer is retrieved

### 4. User Interface
- Streamlit UI accepts user input
- Displays best medical answer instantly

## 5. Streamlit Interface
The chatbot runs as a web application: