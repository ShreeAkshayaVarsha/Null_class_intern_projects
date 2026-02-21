# Computer Science Research Chatbot  
### NLP / AI Research Assistant using arXiv Papers


##  Project Overview

This project implements an AI-powered research chatbot that acts as an expert in the Computer Science domain.  
It retrieves relevant research papers from the arXiv dataset, summarizes them, and explains complex concepts in simple language.

The chatbot is built using Streamlit, Natural Language Processing (NLP) techniques, and an open-source Large Language Model (LLM).


##  Objectives

- Build a domain-specific chatbot for Computer Science
- Retrieve relevant arXiv research papers
- Explain complex research concepts clearly
- Support follow-up questions
- Provide concept visualization

##Dataset

- Dataset Name: arXiv Metadata Dataset
- Source: https://www.kaggle.com/datasets/Cornell-University/arxiv
- Format: JSON (one paper per line)
- Subset Used:
  - cs.AI (Artificial Intelligence)
  - cs.CL (Computational Linguistics)
  - cs.LG (Machine Learning)

##  System Architecture

1. Data Loading  
   - Stream-based loading of large JSON dataset  
   - Filters only Computer Science papers  

2. Information Retrieval  
   - TF-IDF vectorization  
   - Cosine similarity for matching papers  

3. Summarization & Explanation  
   - Extractive summarization using NLTK  
   - Open-source LLM (FLAN-T5) for explanations  

4. User Interface  
   - Built with Streamlit  
   - Search, paper display, explanations, follow-ups  

5. Visualization  
   - WordCloud for concept visualization  


##  Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-learn
- Hugging Face Transformers
- FLAN-T5 (Open-source LLM)
- Matplotlib
- WordCloud


##  Installation & Setup

### Step 1: Install Dependencies

```bash
pip install streamlit pandas nltk scikit-learn transformers torch wordcloud matplotlib
