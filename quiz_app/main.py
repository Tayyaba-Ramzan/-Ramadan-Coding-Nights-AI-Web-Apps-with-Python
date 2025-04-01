import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Ultimate Quiz App", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main-title { text-align: center; font-size: 36px; font-weight: bold; color: #FF5733; }
    .sidebar-title { font-size: 24px; font-weight: bold; color: #1E88E5; text-align: center; }
    .sidebar-content { font-size: 18px; text-align: center; padding: 10px; }
    .score-box { background: linear-gradient(135deg, #3B82F6, #1E40AF); color: white; padding: 15px; border-radius: 10px; font-size: 20px; text-align: center; margin-bottom: 10px; }
    .streak-box { background: linear-gradient(135deg, #F59E0B, #B45309); color: white; padding: 15px; border-radius: 10px; font-size: 20px; text-align: center; margin-bottom: 10px; }
    .question-box { background: linear-gradient(135deg, #10B981, #047857); color: white; padding: 15px; border-radius: 10px; font-size: 20px; text-align: center; margin-bottom: 10px; }
    .correct-answer-box {
        background-color: #DFF2BF;
        color: #4F8A10;
        padding: 20px;
        border-radius: 12px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
        border: 3px solid #4F8A10;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
        animation: glow 1.5s infinite alternate;
    }
    @keyframes glow {
        0% { border-color: #4F8A10; }
        100% { border-color: #79c879; }
    }
    .incorrect-answer-box { background-color: #FFBABA; color: #D8000C; padding: 15px; border-radius: 10px; font-size: 20px; text-align: center; margin-top: 10px; border: 2px solid #D8000C; }
    </style>
""", unsafe_allow_html=True)

# Questions Bank
questions = {
    "Geography": [
        {"question": "What is the capital of Pakistan?", "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"], "answer": "Islamabad"},
        {"question": "Which is the largest province of Pakistan by area?", "options": ["Punjab", "Sindh", "Balochistan", "KPK"], "answer": "Balochistan"},
        {"question": "Which river is the longest in Pakistan?", "options": ["Jhelum", "Chenab", "Indus", "Ravi"], "answer": "Indus"},
        {"question": "Which is the highest peak in Pakistan?", "options": ["Nanga Parbat", "K2", "Rakaposhi", "Broad Peak"], "answer": "K2"},
        {"question": "Which desert is located in Sindh?", "options": ["Thal", "Thar", "Cholistan", "Dasht"], "answer": "Thar"}
    ],
    "History": [
        {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Quaid-e-Azam", "Benazir Bhutto", "Imran Khan"], "answer": "Quaid-e-Azam"},
        {"question": "In which year did Pakistan gain independence?", "options": ["1940", "1945", "1947", "1950"], "answer": "1947"},
        {"question": "Who was the first Prime Minister of Pakistan?", "options": ["Liaquat Ali Khan", "Zulfiqar Ali Bhutto", "Benazir Bhutto", "Ayub Khan"], "answer": "Liaquat Ali Khan"},
        {"question": "Which movement led to the creation of Pakistan?", "options": ["Khilafat Movement", "Pakistan Movement", "Non-Cooperation Movement", "Quit India Movement"], "answer": "Pakistan Movement"},
        {"question": "Who gave the idea of Pakistan?", "options": ["Quaid-e-Azam", "Liaquat Ali Khan", "Allama Iqbal", "Sir Syed Ahmad Khan"], "answer": "Allama Iqbal"}
    ],
    "Finance": [
        {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Euro", "Pound"], "answer": "Rupee"},
        {"question": "What is the central bank of Pakistan called?", "options": ["State Bank of Pakistan", "Bank of Punjab", "Habib Bank", "National Bank"], "answer": "State Bank of Pakistan"},
        {"question": "Which is the largest stock exchange in Pakistan?", "options": ["Islamabad Stock Exchange", "Lahore Stock Exchange", "Karachi Stock Exchange", "Pakistan Stock Exchange"], "answer": "Pakistan Stock Exchange"},
        {"question": "Who presents the annual budget in Pakistan?", "options": ["Prime Minister", "President", "Finance Minister", "Governor State Bank"], "answer": "Finance Minister"},
        {"question": "Which tax is applied on imported goods?", "options": ["Income Tax", "Sales Tax", "Customs Duty", "Excise Duty"], "answer": "Customs Duty"}
    ]
}

# Session State Initialization
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Geography"
if "selected_question" not in st.session_state:
    st.session_state.selected_question = questions[st.session_state.selected_category][st.session_state.question_index]
if "timer_start" not in st.session_state:
    st.session_state.timer_start = time.time()
if "answers" not in st.session_state:
    st.session_state.answers = []

# UI Components
st.markdown("<h1 class='main-title'>🎯 Ultimate Quiz Challenge</h1>", unsafe_allow_html=True)

# Sidebar for Category Selection and Stats
st.sidebar.markdown("<div class='sidebar-container'>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 class='sidebar-title'>🏆 Quiz Stats</h2>", unsafe_allow_html=True)
st.sidebar.markdown(f"<div class='score-box'>✅ Score: <b>{st.session_state.score}</b></div>", unsafe_allow_html=True)
st.sidebar.markdown(f"<div class='streak-box'>🔥 Streak: <b>{st.session_state.streak}</b></div>", unsafe_allow_html=True)
st.sidebar.markdown(f"<div class='question-box'>🔢 Question: <b>{st.session_state.question_index + 1}</b></div>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Category selection dropdown
category = st.sidebar.selectbox("Select Category 📚", list(questions.keys()), key="category")
if category != st.session_state.selected_category:
    st.session_state.selected_category = category
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.answers = []
    st.session_state.selected_question = questions[st.session_state.selected_category][st.session_state.question_index]
    st.rerun()

# Display Question
question = st.session_state.selected_question
st.subheader(f"📌 {question['question']}")
selected_option = st.radio("Choose your answer 📝", question["options"], key=f"answer_{st.session_state.question_index}")

# Timer
time_remaining = 10 - (time.time() - st.session_state.timer_start)
if time_remaining <= 0:
    st.warning("⏳ Time's up! Moving to the next question.")
    st.session_state.question_index += 1
    if st.session_state.question_index < len(questions[st.session_state.selected_category]):
        st.session_state.selected_question = questions[st.session_state.selected_category][st.session_state.question_index]
    st.session_state.timer_start = time.time()
    st.rerun()
else:
    st.progress(int((time_remaining / 10) * 100))

# Submit Answer
if st.button("Submit Answer ✔️"):
    if selected_option == question["answer"]:
        st.success("🎉 Correct Answer!")
        st.balloons()
        st.session_state.score += 10 + (st.session_state.streak * 2)  # Streak Bonus
        st.session_state.streak += 1
    else:
        st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
        st.session_state.streak = 0
    
    # Store answer history
    st.session_state.answers.append({
        "Question": question["question"],
        "Your Answer": selected_option,
        "Correct Answer": question["answer"],
        "Result": "Correct" if selected_option == question["answer"] else "Incorrect",
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # Move to next question
    if st.session_state.question_index + 1 < len(questions[st.session_state.selected_category]):
        st.session_state.question_index += 1
        st.session_state.selected_question = questions[st.session_state.selected_category][st.session_state.question_index]
        st.session_state.timer_start = time.time()
        st.rerun()
    else:
        st.success("🏆 Quiz Completed!")
        df = pd.DataFrame(st.session_state.answers)
        
        st.markdown("<h2>📊 Final Results</h2>", unsafe_allow_html=True)
        st.markdown("<div class='table-container'>", unsafe_allow_html=True)
        st.dataframe(df.style.set_properties(**{'background-color': '#FFFFFF', 'color': '#333', 'border': '1px solid #ddd'}))
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.sidebar.markdown(f"<p class='sidebar-content'>🎯 Final Score: <b>{st.session_state.score}</b></p>", unsafe_allow_html=True)
