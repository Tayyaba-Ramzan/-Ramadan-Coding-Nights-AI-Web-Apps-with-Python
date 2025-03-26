import streamlit as st
import requests
import random
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# 🎭 **FastAPI Setup**
app = FastAPI()

# Jokes categorized         
jokes = {
    "frontend": [
        {"setup": "Why did the React developer break up with Vue?", "punchline": "Because Vue was too reactive!"},
        {"setup": "Why do frontend developers love tea?", "punchline": "Because they hate CoffeeScript!"},
        {"setup": "Why do frontend developers prefer CSS?", "punchline": "Because they like things to be well-styled!"},
    ],
    "backend": [
        {"setup": "Why do backend developers make bad DJs?", "punchline": "Because they always keep things in the background!"},
        {"setup": "Why do backend devs love REST APIs?", "punchline": "Because they always need a break!"},
        {"setup": "Why was the SQL query sad?", "punchline": "It had too many joins but still felt lonely!"},
    ],
    "javascript": [
        {"setup": "Why did the JavaScript developer go broke?", "punchline": "Because he kept using `null` as his value!"},
        {"setup": "Why do JS devs never trust numbers?", "punchline": "Because `0 == false`, but `0 !== false`!"},
        {"setup": "How do JavaScript devs like their burgers?", "punchline": "With extra `this`!"},
    ],
    "python": [
        {"setup": "Why did the Python developer bring a ladder to work?", "punchline": "Because he wanted to reach the high-level syntax!"},
        {"setup": "What’s a Python developer’s favorite type of music?", "punchline": "Loops and Conditions!"},
        {"setup": "Why did the Python developer get promoted?", "punchline": "Because he handled exceptions like a pro!"},
    ],
    "pakistani_dev": [
        {"setup": "Why do Pakistani developers always bring chai to meetings?", "punchline": "Because caffeine is their only debugger! ☕"},
        {"setup": "What happens when a Pakistani developer pushes code on Friday?", "punchline": "Monday becomes a disaster recovery drill!"},
        {"setup": "Why don’t Pakistani devs use Stack Overflow at work?", "punchline": "Because they already overflow with bugs! 🐛"},
    ]
}

@app.get("/random_joke")
def get_joke(category: str = "general"):
    if category in jokes:
        return random.choice(jokes[category])
    else:
        all_jokes = sum(jokes.values(), [])  # Flatten list
        return random.choice(all_jokes)

# 🔥 **Run FastAPI in Background**
def run_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)

threading.Thread(target=run_api, daemon=True).start()

# 🎨 **Streamlit UI Setup**
API_URL = "http://127.0.0.1:8000/random_joke"

# Static Images
STATIC_IMAGE = "https://protoinfrastack-myfirstbucketb8884501-fnnzvxt2ee5v.s3.amazonaws.com/DutxHhiyYbUXjQaVi54Xs6NzF5bzLIrZvD2d.png"


# Store Jokes History
if "joke_history" not in st.session_state:
    st.session_state.joke_history = []

# Function to Get Joke from API
def get_random_joke():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            joke = response.json()
            joke_text = f"**{joke['setup']}**\n\n*{joke['punchline']}*"
            st.session_state.joke_history.append(joke_text)
            return joke_text
        else:
            return "Failed to fetch a joke. Please try again later!"
    except:
        return "Something went wrong. Check your internet or server!"

# 🎭 **Streamlit UI**
def main():
    st.set_page_config(
        page_title="Dev Jokes Generator", 
        page_icon="😂", 
        layout="wide"
    )
    
    # 🚀 **Sidebar**
    with st.sidebar:
        st.image(STATIC_IMAGE, use_container_width=True)
        st.markdown("<h2 style='text-align: center;'>🎭 Fun Options</h2>", unsafe_allow_html=True)
        
        st.markdown("### 📌 Features:")
        st.markdown("- ✅ **Generate Dev Jokes Generator**")
        st.markdown("- ⚡ **FastAPI + Streamlit Powered**")
        st.markdown("- 🔥 **Super Fun & Engaging UI**")
        
        st.markdown("---")
        
        st.markdown("<h3 style='text-align: center;'>📜 Joke History</h3>", unsafe_allow_html=True)
        if st.session_state.joke_history:
            for joke in reversed(st.session_state.joke_history[-5:]):
                st.markdown(f"- {joke}")
        else:
            st.markdown("⚠️ **No jokes generated yet!** Click the button below to get your first joke.")

        st.markdown("---")
        st.markdown("<p style='text-align: center;'>🚀 Built with ❤️ using FastAPI & Streamlit</p>", unsafe_allow_html=True)

    # 🎨 **Main Content**
    st.markdown("""
        <h1 style='text-align: center; color: #FF5733; font-size: 3rem;'>
        😂 Dev Jokes Generator 🎭</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(STATIC_IMAGE, use_container_width=True)
        st.markdown("<h3 style='text-align: center;'>Click below to get a **hilarious** Dev Joke!</h3>", unsafe_allow_html=True)

        if st.button("🎭 Generate Joke", use_container_width=True):
            joke = get_random_joke()
            st.success(joke)

    st.markdown("---")
    st.markdown("""
        <p style='text-align: center; font-size: 1.2rem;'>🔥 Built with ❤️ using FastAPI & Streamlit</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
