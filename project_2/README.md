# 🤖 Multimodal Chatbot using Gemini API

This project implements a **multimodal AI chatbot** using **Google Gemini API** and **Streamlit**.  
The system supports:
- 💬 Text-based conversation
- 🖼️ Image understanding and analysis
- 📊 Usage analytics with metrics and visualizations

---

## 🚀 Features

### 1. Text Generation
- Interactive chatbot powered by Gemini
- Real-time response generation
- Response-time measurement

### 2. Image Recognition
- Upload images (JPG / PNG)
- Ask questions related to the image
- Gemini-based visual understanding
- Image analysis time measurement

### 3. Analytics & Visual Outputs
The application includes **visual outputs and metrics**, as required:

- ⏱️ Response time metrics (Text & Image)
- 📊 Bar chart: Average response time comparison
- 🥧 Pie chart: Usage distribution (Text vs Image)
- 📋 Interaction log table
- 🔢 Simulated confusion matrix (for academic demonstration)

---

## 📈 Visualizations Used

- **Matplotlib**
- **Seaborn**
- **Streamlit Metrics**

These visualizations provide insights into:
- System latency
- User interaction patterns
- Performance comparison between text and image modes

---

## ⚠️ Note on Confusion Matrix

Since this system is **generative** (not a classifier), traditional accuracy metrics are not directly applicable.  
A **simulated confusion matrix** is included **only for academic demonstration purposes**.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Matplotlib
- Seaborn
- Pandas
- PIL (Image Processing)

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install streamlit google-generativeai matplotlib seaborn pandas pillow scikit-learn
