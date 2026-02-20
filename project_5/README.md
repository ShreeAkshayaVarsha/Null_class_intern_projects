SENTIMENT AWARE CHATBOT USING STREAMLIT

PROJECT OVERVIEW
This project implements a sentiment-aware chatbot that detects the emotional tone of user messages and responds appropriately. The chatbot classifies user input into Positive, Negative, or Neutral sentiment and adapts its responses to improve customer satisfaction.

PROBLEM STATEMENT
Integrate sentiment analysis into the chatbot to detect and respond appropriately to customer emotions during interactions.

EXPECTED OUTCOME
• The chatbot recognizes positive, negative, and neutral sentiments
• The chatbot responds appropriately based on detected emotion
• Improved customer interaction and satisfaction

TECHNOLOGIES USED
• Python
• Streamlit
• Rule-Based Sentiment Analysis
• Regular Expressions (re)

SYSTEM DESCRIPTION

Sentiment Detection:
The chatbot uses predefined lists of positive and negative words. A sentiment score is calculated based on the occurrence of these words in user input.

Response Generation:
• Positive sentiment → Friendly and encouraging response
• Negative sentiment → Apologetic and supportive response
• Neutral sentiment → Professional and helpful response

SAMPLE TEST CASES

Input: I am very happy today  
Sentiment: Positive  
Response: Friendly and encouraging message  

Input: This service is bad  
Sentiment: Negative  
Response: Apologetic and supportive message  

Input: I want to check my order status  
Sentiment: Neutral  
Response: Professional and helpful message  

EVALUATION CRITERIA

Accuracy of Sentiment Detection:
Uses keyword-based sentiment scoring to classify user emotions effectively.

Appropriateness of Responses:
Responses are tailored based on detected sentiment to match user emotions.

Impact on Customer Satisfaction:
Empathetic responses reduce frustration and improve user engagement.

ALGORITHM
1. Accept user input
2. Convert input text to lowercase
3. Remove punctuation
4. Match words with sentiment keyword lists
5. Calculate sentiment score
6. Classify sentiment as Positive, Negative, or Neutral
7. Display appropriate chatbot response

HOW TO RUN THE PROJECT

Step 1: Install Streamlit
pip install streamlit

Step 2: Run the application
python -m streamlit run exp4.py

Step 3: Open browser
http://localhost:8501

FUTURE ENHANCEMENTS
• Implement machine learning based sentiment analysis
• Support multilingual sentiment detection
• Improve accuracy using trained datasets

CONCLUSION
This project demonstrates the integration of sentiment analysis into a chatbot to create emotionally intelligent interactions. The rule-based approach ensures simplicity while fulfilling all project requirements.
