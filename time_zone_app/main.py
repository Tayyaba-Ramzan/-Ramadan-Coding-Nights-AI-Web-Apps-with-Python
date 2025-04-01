import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

st.set_page_config(page_title="Time Zone Converter", page_icon="🌎")


# Custom CSS for Super Stylish UI
st.markdown("""
    <style>
        body { font-family: 'Poppins', sans-serif; }
        .stTitle { text-align: center; font-size: 2.5rem; color: #2C3E50; font-weight: bold; text-shadow: 2px 2px 8px #1ABC9C; }
        .stSubheader { color: #34495E; font-size: 1.8rem; font-weight: bold; border-bottom: 3px solid #BDC3C7; padding-bottom: 8px; }
        .stButton button { background: linear-gradient(135deg, #1ABC9C, #16A085); color: white; font-size: 1.2rem; border-radius: 12px; padding: 10px; transition: 0.3s ease-in-out; }
        .stButton button:hover { background: linear-gradient(135deg, #16A085, #1ABC9C); transform: scale(1.05); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); }
        .stTextInput, .stSelectbox, .stTimeInput { border-radius: 12px; font-size: 1.1rem; padding: 8px; }
        .result { font-size: 1.5rem; color: #E74C3C; font-weight: bold; text-align: center; text-shadow: 1px 1px 5px #E74C3C; }
        .fade-in { animation: fadeIn 1.2s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .glassmorphism {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# List of Time Zones
TIME_ZONES = [
    "UTC",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Europe/London",
    "Asia/Karachi",
]

# App Title
st.markdown("<h1 class='stTitle'>🌍 Time Zone Converter ⏳</h1>", unsafe_allow_html=True)


# Timezone Selection Section
st.markdown("<h2 class='stSubheader'>📍 Select Timezones to Display</h2>", unsafe_allow_html=True)

selected_timezone = st.multiselect("Select a timezone", TIME_ZONES, default=["UTC", "Asia/Karachi"])
st.markdown("<div class='glassmorphism'>", unsafe_allow_html=True)

for timezone in selected_timezone:
    current_time = datetime.now(ZoneInfo(timezone)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"⏰ **{timezone}**: `{current_time}`")

st.markdown("</div>", unsafe_allow_html=True)  # Close glassmorphism div

st.markdown("<hr>", unsafe_allow_html=True)  # Divider line

# Time Conversion Section
st.markdown("<h2 class='stSubheader'>🔄 Convert Time between Timezones</h2>", unsafe_allow_html=True)

current_time = st.time_input("⏳ Select Time", value=datetime.now().time())

from_timezone = st.selectbox("🔻 Convert From", TIME_ZONES, index=0)
to_timezone = st.selectbox("🔺 Convert To", TIME_ZONES, index=8)

if st.button("🚀 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_timezone))
    converted_time = dt.astimezone(ZoneInfo(to_timezone)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Styled Output with Confetti Animation
    st.markdown(f"<p class='result fade-in'>🎉 Converted Time in **{to_timezone}**: {converted_time}</p>", unsafe_allow_html=True)
    
    # Confetti Effect 🎊
    st.balloons()
    time.sleep(1.5)  # Slight delay for animation effect
    st.snow()  # Double animation effect for WOW feel

st.markdown("<hr>", unsafe_allow_html=True)  # Divider line

# Live Clock in Selected Timezones
st.markdown("<h2 class='stSubheader'>⏰ Live Clocks</h2>", unsafe_allow_html=True)
st.markdown("<div class='glassmorphism'>", unsafe_allow_html=True)

for timezone in selected_timezone:
    live_time = datetime.now(ZoneInfo(timezone)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"🌎 **{timezone}**: `{live_time}`")

st.markdown("</div>", unsafe_allow_html=True)  # Close glassmorphism div

