import streamlit as st
from math import pow

def main():
    st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")
    
    st.markdown(
        """
        <style>
            .main {
                background-color: #f5f7fa;
            }
            .stButton>button {
                background-color: #007BFF;
                color: white;
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
                background-color: #e8f4fd;
                cursor: pointer;
            }
            .stRadio input[type="radio"]:checked + label {
                background-color: #007BFF;
                color: white;
                font-weight: bold;
            }
            .stNumberInput>div>input {
                font-size: 18px;
                padding: 8px;
            }
            .result-box {
                background-color: #e8f4fd;
                padding: 15px;
                border-radius: 10px;
                border-left: 5px solid #007BFF;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🧮 CALCULATOR")
    st.subheader("Perform complex calculations with ease and accuracy!")

    st.markdown("### 🔢 Enter Numbers")
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First Number", value=0.0, step=0.1, format="%.2f")
    with col2:
        num2 = st.number_input("Second Number", value=0.0, step=0.1, format="%.2f")
    
    st.markdown("### ⚙️ Select an Operation")
    operation = st.radio("Choose an operation", [
        "Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)",
        "Exponentiation (^)", "Modulo (%)"
    ])
    
    if st.button("🚀 Compute Result"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            elif operation == "Division (÷)":
                if num2 == 0:
                    st.error("❌ Division by zero is not allowed.")
                    return
                result = num1 / num2
                symbol = "÷"
            elif operation == "Exponentiation (^)":
                result = pow(num1, num2)
                symbol = "^"
            else:
                if num2 == 0:
                    st.error("❌ Modulo operation with zero is undefined.")
                    return
                result = num1 % num2
                symbol = "%"
            
            st.markdown(f'<div class="result-box">✅ Computed Result: {num1} {symbol} {num2} = {result}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
