import streamlit as st
import requests

# API Endpoint
API_URL = "http://127.0.0.1:8000/random_joke"

# Static Image for UI
STATIC_IMAGE = "https://protoinfrastack-myfirstbucketb8884501-fnnzvxt2ee5v.s3.amazonaws.com/DutxHhiyYbUXjQaVi54Xs6NzF5bzLIrZvD2d.png"

sidebar_image_path = "images/sidebar-img.png" 
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
            st.session_state.joke_history.append(joke_text)  # Store in history
            return joke_text
        else:
            return "Failed to fetch a joke. Please try again later!"
    except:
        return "Something went wrong. Check your internet or server!"

# Streamlit UI
def main():
    st.set_page_config(
        page_title="Dev Jokes Generator", 
        page_icon="😂", 
        layout="wide"
    )
    
    # 🚀 **Advanced Sidebar**
    with st.sidebar:
        st.image(sidebar_image_path, use_container_width=True)
        st.markdown("<h2 style='text-align: center;'>🎭 Fun Options</h2>", unsafe_allow_html=True)
        
        st.markdown("### 📌 Features:")
        st.markdown("- ✅ **Generate Dev Jokes Generator**")
        st.markdown("- ⚡ **FastAPI + Streamlit Powered**")
        st.markdown("- 🔥 **Super Fun & Engaging UI**")
        
        st.markdown("---")
        
        st.markdown("<h3 style='text-align: center;'>📜 Joke History</h3>", unsafe_allow_html=True)
        if st.session_state.joke_history:
            for joke in reversed(st.session_state.joke_history[-5:]):  # Show last 5 jokes
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
        st.markdown("<h3 style='text-align: center;'>Click below to get a **hilarious** Dev Jokes Generator!</h3>", unsafe_allow_html=True)

        if st.button("🎭 Generate Joke", use_container_width=True):
            joke = get_random_joke()
            st.success(joke)

    st.markdown("---")
    st.markdown("""
        <p style='text-align: center; font-size: 1.2rem;'>🔥 Built with ❤️ using FastAPI & Streamlit</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
