import streamlit as st
import pandas as pd
import csv
import datetime
import os
import plotly.express as px
import random

st.set_page_config(page_title="Mood Tracker", page_icon="🌈", layout="wide")


st.markdown("""
    <style>
        /* Styling for Mood Log Button */
        .stButton>button {
            background-color: #4CAF50; 
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 30px;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

        /* Sidebar adjustments */
        .stSidebar .sidebar-content {
            padding: 20px;
            background-color: #f1f1f1;
        }

        /* Success message styling */
        .stSuccess>div {
            padding: 12px;
            background-color: #d4edda;
            color: #155724;
            border-radius: 8px;
            font-size: 16px;
            border: 1px solid #c3e6cb;
            margin-top: 20px;
        }

        /* Main page title */
        h1 {
            font-size: 40px;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 20px;
        }

        /* Insights Section */
        .insight-header {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-top: 40px;
            text-align: center;
        }

        /* Chart and gif animation */
        .stImage {
            margin-top: 20px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        .stWrite {
            font-size: 18px;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# File to store mood data
MOOD_FILE = "mood_data.csv"
JOURNAL_FILE = "journal_entries.txt"

# Function to load mood data safely
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])

    df = pd.read_csv(MOOD_FILE)
    df.columns = [col.strip() for col in df.columns]
    
    if "Date" not in df.columns or "Mood" not in df.columns:
        st.error("❌ CSV file format is incorrect! Deleting and recreating...")
        os.remove(MOOD_FILE)
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return df

# Function to save mood data safely
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])
        writer.writerow([date, mood])

# Function to calculate mood insights
def get_mood_insights(data):
    mood_counts = data["Mood"].value_counts()
    most_frequent_mood = mood_counts.idxmax()
    most_frequent_count = mood_counts.max()
    total_entries = len(data)
    return most_frequent_mood, most_frequent_count, total_entries

# Function to get a random motivational quote or joke
def get_fun_insight(mood):
    quotes = {
        "😊 Happy": ["You are a Super Star today! Keep smiling and spread positivity! 😄", 
                     "The best way to predict the future is to create it! 💪"],
        "😢 Sad": ["It's okay to feel low sometimes. Take a deep breath, you got this! 💖", 
                   "Remember, every storm passes, and there's always a rainbow after it! 🌈"],
        "😡 Angry": ["Anger is temporary. Calm down and remember peace starts from within! 🧘", 
                     "Take a moment to breathe, you'll feel much better! 💭"],
        "😰 Stressed": ["Take a break, do some deep breathing. You deserve peace of mind! 🧘", 
                        "Stress is like a rocking chair: it gives you something to do but gets you nowhere! 😌"],
        "😟 Anxious": ["It's normal to feel anxious. Try some relaxation techniques to calm down. 🧘", 
                       "Breathe in, breathe out. You got this! 💪"],
        "😐 Neutral": ["Sometimes neutrality is the best approach! Keep the balance and move forward! ⚖️"]
    }
    
    return random.choice(quotes.get(mood, ["Stay strong! 💪"]))

# Function to show mood-based animations
def show_mood_animation(mood):
    animations = {
        "😊 Happy": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3liYmt6c29xM24xdDJ6eXlnZGVrajJlc3pmMDZ3c2tuNXN6andiMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KD1vZ7drv5wmsIQMos/giphy.gif",
        "😢 Sad": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczd6aHF1cGtiZ2t4dmRnYmhyNnI5bXQycTVld21nbnVpOXdtbjhhaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XFwDrV9NEtl6st47Ah/giphy.gif",
        "😡 Angry": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExenluajZmZjlvNmZ6czd1bXhyMmxxYWE1c216dmV5dDQ4MHE1OGJudSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/yJexcB8wvjqftCOMao/giphy.gif",
        "😰 Stressed": "https://media.giphy.com/media/UcNcCQmPdkNYDkU6Vd/giphy.gif?cid=ecf05e47bbd6x9wcm014nvcpgaq6wnitcwht8k1z5wdoti08&ep=v1_gifs_search&rid=giphy.gif&ct=g",
        "😟 Anxious": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2RyZGhtMjNnZTBrOG13Zmtjbnoya3NscGczZDlvNDZmam8wc2xwZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hWGZVAGqUwpmxIzB2y/giphy.gif",
        "😐 Neutral": "https://media.giphy.com/media/iJCoL6TCSgVaePaZ2M/giphy.gif?cid=ecf05e47ws5lxqedsc1afbqlasotrijfd7ytv9bmkvi1gajp&ep=v1_gifs_search&rid=giphy.gif&ct=g"
    }
    
    st.image(animations.get(mood, ""), width=800) 

# App Title
st.title("🌈 Mood Tracker - Your Emotional Journal")

# Get Today's Date
today = datetime.datetime.today().strftime("%Y-%m-%d")

# Sidebar for Mood Selection
st.sidebar.header("📅 Log Your Mood")
mood = st.sidebar.selectbox("How are you feeling today?", ["😊 Happy", "😢 Sad", "😡 Angry", "😰 Stressed", "😟 Anxious", "😐 Neutral"])

# Log Mood Button
if st.sidebar.button("Log Mood"):
    save_mood_data(today, mood)
    st.sidebar.success("✅ Mood Logged Successfully! 🎉")

# Load mood data
data = load_mood_data()

# Ensure DataFrame is not empty
if not data.empty:
    # Get mood insights
    most_frequent_mood, most_frequent_count, total_entries = get_mood_insights(data)
    
    # Display insights
    st.subheader("🌟 Mood Insights")
    st.write(f"Your most frequent mood is: **{most_frequent_mood}** with **{most_frequent_count}** occurrences. 🌟")
    st.write(f"You've logged a total of **{total_entries}** mood entries so far. 📊")

    # Visualization for mood trends
    st.subheader("📊 Mood Frequency")
    mood_counts = data["Mood"].value_counts()
    fig = px.bar(mood_counts, x=mood_counts.index, y=mood_counts.values, 
                 title="Mood Frequency", labels={'x':'Mood', 'y':'Count'}, 
                 color=mood_counts.index, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

    # Fun Message Based on Mood
    st.subheader("💬 Fun Insight: ")
    st.write(get_fun_insight(mood))

    # Show mood animation based on selected mood
    show_mood_animation(mood)

else:
    st.write("No mood data available yet. Please log your first mood entry. 📝")
