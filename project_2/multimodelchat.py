import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
import time

#  Configuration

GOOGLE_API_KEY = "AIzaSyC-bte6qRLnF0hSZuFYLlKTld5dx6ZvWeA"  # Replace with your valid API key
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)


#  Streamlit Setup

st.set_page_config(page_title="🤖 Multimodel Chatbot", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "start"

#  Gemini Helper Functions

def chat_with_gemini(user_input):
    model = genai.GenerativeModel("gemini-2.5-flash")
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    return response.text

def analyze_image(prompt, image):
    model = genai.GenerativeModel("gemini-2.5-flash")
    if prompt:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Page 1: Start Screen

if st.session_state.page == "start":
    st.title("🤖 Welcome to Multimodel Chatbot")
    st.markdown("This app can **generate text** and **understand images**")
    st.markdown("---")
    st.markdown("Click below to get started!")

    if st.button("🚀 Start Chatting"):
        st.session_state.page = "main"
        st.rerun()

#  Page 2: Choose Mode

elif st.session_state.page == "main":
    st.title("Select a Mode")
    st.markdown("Choose what you want to do:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Text Generation"):
            st.session_state.page = "text"
            st.rerun()

    with col2:
        if st.button("🕶️ Recognize from Image"):
            st.session_state.page = "vision"
            st.rerun()
#  Page 3: Text Generation

elif st.session_state.page == "text":
    st.title("💬 Text Chat Mode")
    st.markdown("Talk with me and get instant smart responses! 🤖")

    user_input = st.text_input("Enter your chat here:")

    if st.button("Send"):
        if user_input.strip():
            with st.spinner("Coming up with an answer..."):
                reply = chat_with_gemini(user_input)
                time.sleep(1)
            st.success("Yeah your response is ready !!!")
            st.write(reply)
            
                       
        else:
            st.warning("Please enter a question or message.")

    if st.button("⬅ Back to Main Menu"):
        st.session_state.page = "main"
        st.rerun()

#  Page 4: Image Recognition

elif st.session_state.page == "vision":
    st.title("🕶️ Turning ON the Vision Mode")
    st.markdown("Upload an image and ask me about it! 🖼️")

    user_prompt = st.text_input("Enter your question or prompt about the image:")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    else:
        image = None

    if st.button("🔍 Analyze Image"):
        if image:
            with st.spinner("Analyzing your image..."):
                response = analyze_image(user_prompt, image)
                time.sleep(1)
            st.success("Here's what I found:")
            st.write(response)
            
        else:
            st.warning("Please upload an image first.")
    if st.button("Back to Main Menu"):
        st.session_state.page = "main"
        st.rerun()
