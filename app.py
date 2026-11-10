import streamlit as st
import random
import string

# Page Configuration
st.set_page_config(page_title="CyberPulse Security Hub", page_icon="⚡", layout="centered")

# Custom styling for dark aesthetic
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #2ea043; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ CyberPulse Security Hub")
st.markdown("### Lightweight Python Security & Utility Dashboard")
st.write("A clean and interactive frontend tool built purely using Python and Streamlit.")

# Tabs for navigation
tab1, tab2 = st.tabs(["🔒 Password Strength Checker", "🔑 Secure Password Generator"])

with tab1:
    st.subheader("Check Password Security")
    password = st.text_input("Enter your password to analyze:", type="password")
    
    if password:
        score = 0
        if len(password) >= 8: score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1

        if score == 5:
            st.success("🟢 Strong Password! Excellent security level.")
        elif score >= 3:
            st.warning("🟡 Moderate Password. Consider adding numbers and special symbols.")
        else:
            st.error("🔴 Weak Password! Highly vulnerable to attacks.")

with tab2:
    st.subheader("Generate Random Secure Password")
    length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
    
    if st.button("Generate Password"):
        chars = string.ascii_letters + string.digits + string.punctuation
        gen_pass = "".join(random.choice(chars) for _ in range(length))
        st.code(gen_pass, language="")

st.markdown("---")
st.caption("Developed with Python & Streamlit | Ready for GitHub Deployment 🚀")