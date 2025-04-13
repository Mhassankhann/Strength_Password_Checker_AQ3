import streamlit as st
import re
import random
import string
import time

# Set page config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Add background color and animation using custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0b1e3f;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }
    .stApp {
        background-color: #0b1e3f;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p, div {
        color: #ffffff;
    }
    .stButton>button {
        background-color: #01b4e4;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        box-shadow: 0 0 15px rgba(1, 180, 228, 0.6);
    }
    .stButton>button:hover {
        background-color: #00a3c6;
        transition: background-color 0.3s ease;
        box-shadow: 0 0 20px rgba(1, 180, 228, 0.9);
    }
    .stTextInput>div>input {
        background-color: #3c4d6b;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(1, 180, 228, 0.6);
    }
    .hacking {
        font-size: 22px;
        color: #00FF00;
        font-weight: bold;
        text-shadow: 0 0 10px #00FF00, 0 0 20px #00FF00, 0 0 30px #00FF00;
        animation: hackingAnimation 1.5s infinite;
    }
    @keyframes hackingAnimation {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("🔐 Password Strength Checker")
st.markdown("""
##  Welcome to the Password Strength Checker!
This tool will help you determine the **strength** of your **password**.  
Simply type in your password and hit the button below to check its strength! 💪
""")

# Password generator function
def generate_strong_pass(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%&*?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Inputs
password = st.text_input("🔒 Enter your password:", type='password')
col1, col2 = st.columns(2)
with col1:
    checkbtn = st.button("✅ Check Password")
with col2:
    generatebtn = st.button("✨ Generate Strong Password")

# Function to check password strength
def check_password_strength(password):
    feedback = []
    score = 0
    strength_meter = ""

    if len(password) < 8:
        st.error("❌ Password must be at least 8 characters long.")
        strength_meter = "Weak"
    else:
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            score += 1
        else:
            feedback.append("🔠 Add both **uppercase** and **lowercase** letters to strengthen your password.")

        if re.search("[0-9]", password):
            score += 1
        else:
            feedback.append("🔢 Include at least one **number** (0-9) in your password.")

        if re.search("[!@#$%^&*?]", password):
            score += 1
        else:
            feedback.append("✨ Use a **special character** like !@#$%^&* to make your password more secure.")

        if score == 3:
            st.success("🎉 Your password is **strong**! Great job! 🔥")
            strength_meter = "Strong"
        elif score == 2:
            st.warning("⚠️ Your password is **moderate**. Consider adding more variety to make it stronger.")
            strength_meter = "Moderate"
        else:
            st.error("❌ Your password is **weak**. Follow the suggestions below! 🚨")
            strength_meter = "Weak"

    return strength_meter, feedback

# Real-time password check (Dynamic feedback)
if password:
    st.markdown("<p class='hacking'>*Hacking password...*</p>", unsafe_allow_html=True)
    time.sleep(1)  # Small delay to create the hacking effect

    strength_meter, feedback = check_password_strength(password)
    st.progress(50 if strength_meter == "Weak" else (75 if strength_meter == "Moderate" else 100))

    # Show suggestions
    if feedback:
        st.markdown("## 🛠️ Suggestions:")
        for tip in feedback:
            st.markdown(f"- {tip}")

# Generate password
if generatebtn:
    strong_password = generate_strong_pass()
    st.text_input("🛡️ Your Strong Password:", value=strong_password, type='default')

# Footer
st.markdown("---")
st.markdown("**👨‍💻 Created by: Muhammad Hassan Khan**")
