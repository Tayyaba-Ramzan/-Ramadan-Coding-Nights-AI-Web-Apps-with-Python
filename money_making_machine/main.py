import streamlit as st
import random
import time
import requests
import pandas as pd

# Page Configurations
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")

# Custom CSS for Sidebar Styling
st.markdown("""
    <style>
        /* Main Background */
        .main {
            background-color: #f5f7fa;
        }

        /* Sidebar Button Styling */
        .stButton>button {
            background-color: #007BFF;
            color: black;
            font-size: 20px;
            padding: 14px 32px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }

        /* Radio Button Styling */
        .stRadio div {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .stRadio label {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 8px;
            transition: background 0.3s;
        }
        .stRadio label:hover {
            background-color: #007BFF;
            cursor: pointer;
        }
        .stRadio input[type="radio"]:checked + label {
            background-color: #007BFF;
            color: white;
            font-weight: bold;
        }

        /* Input Field Styling */
        .stNumberInput>div>input {
            font-size: 18px;
            padding: 8px;
        }

        /* Result Box Styling */
        .result-box {
            background-color: #e8f4fd;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #007BFF;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }

        /* Sidebar Styles */
        .css-1d391kg { 
            background-color: #1e1e1e; 
            color: white; 
            border-radius: 10px;
        }
        .css-1d391kg .sidebar-content {
            background-color: #2c2c2c;
        }
        .css-1d391kg .stSidebar {
            font-family: 'Arial', sans-serif;
        }
        .stSidebar .css-1q1h9vd:hover {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            cursor: pointer;
        }
        .stSidebar .css-1q1h9vd {
            margin-bottom: 15px;
        }

        /* Animation for Money Falling */
        .money {
            font-size: 50px;
            font-weight: bold;
            color: green;
            animation: money-fall 3s ease-in-out infinite;
        }

        @keyframes money-fall {
            0% { transform: translateY(-100px); }
            50% { transform: translateY(0px); }
            100% { transform: translateY(-100px); }
        }

        /* Sidebar styling */
        .stSidebar .css-1q1h9vd {
            border-radius: 10px;
            margin-top: 20px;
        }

        /* Hover Effects for Sidebar Buttons */
        .stSidebar .css-1q1h9vd:hover {
            background-color: #0056b3;
            color: white;
        }

        /* Sidebar Header Styling */
        .stSidebar h1 {
            color: #fff;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }

        /* Additional padding for main content */
        .css-1v3fvcr {
            padding-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation with Extra Features
st.sidebar.markdown("### 🏆 Money-Making Journey")
option = st.sidebar.radio("Select Action", ["💵 Instant Cash", "🚀 Side Hustle Ideas", "💡 Money Quotes", "🏆 Leaderboard", "🔄 Currency Converter", "📈 Progress Tracker"])

# Function to Generate Money
def generate_money():
    return random.randint(10, 10000)

# Function to Fetch Side Hustle Idea
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            return response.json().get("side_hustle", "Freelancing")
    except:
        return "Something went wrong"

# Function to Fetch Money Quote
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            return response.json().get("money_quote", "Money is power.")
    except:
        return "Something went wrong"

st.title("🚀 Money Making Machine 💸💰📈")
# Function for Leaderboard
def leaderboard():
    st.subheader("🏆 Money-Making Leaderboard")
    st.write("1. Elon Musk - $230B")
    st.write("2. Jeff Bezos - $180B")
    st.write("3. Bill Gates - $135B")

# Function for Currency Converter
def currency_converter():
    st.subheader("💱 Live Currency Converter")
    amount = st.number_input("Enter Amount in USD:", min_value=1, step=1)
    if st.button("Convert", help="Click to convert USD to PKR"):
        conversion_rate = 220  # Example: 1 USD = 220 PKR
        converted = amount * conversion_rate
        st.success(f"💰 {amount} USD = {converted} PKR")

# Function for Progress Tracker (using a simple Pandas DataFrame)
def progress_tracker():
    st.subheader("📈 Money-Making Progress Tracker")
    data = {
        "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
        "Money Made (USD)": [random.randint(100, 5000) for _ in range(3)]
    }
    df = pd.DataFrame(data)
    st.write(df)
    st.line_chart(df.set_index("Date"))

# Main Logic
if option == "💵 Instant Cash":
    st.subheader("💵 Instant Cash Generator")
    if st.button("Generate Money", help="Click to become rich!"):
        with st.spinner("Counting your money..."):
            time.sleep(1)
            amount = generate_money()
        st.success(f"💸 You made ${amount}!")
        st.balloons()  # Adding a balloon animation effect when money is generated
    
elif option == "🚀 Side Hustle Ideas":
    st.subheader("🚀 Side Hustle Ideas")
    if st.button("Generate Side Hustle", help="Get a new business idea!"):
        idea = fetch_side_hustle()
        st.success(f"💼 Try this: {idea}")
    
elif option == "💡 Money Quotes":
    st.subheader("💡 Money-Making Motivation")
    if st.button("Get Inspired", help="Get a motivational money quote"):
        quote = fetch_money_quote()
        st.info(f"📜 {quote}")
    
elif option == "🏆 Leaderboard":
    leaderboard()

elif option == "🔄 Currency Converter":
    currency_converter()

elif option == "📈 Progress Tracker":
    progress_tracker()

# Footer
st.markdown("---")
st.markdown("### 🌟 Built with ❤️ by Tayyaba Ramzan 🚀")
