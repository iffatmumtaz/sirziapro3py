import streamlit as st
import re

def check_password_strength(password):
    score = 0

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if not length_error:
        score += 1
    if not digit_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not symbol_error:
        score += 1

    if score == 5:
        return "Very Strong", score
    elif score == 4:
        return "Strong", score
    elif score == 3:
        return "Moderate", score
    elif score == 2:
        return "Weak", score
    else:
        return "Very Weak", score

# Streamlit App
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, score = check_password_strength(password)
    st.write(f"**Strength**: {strength}")
    st.progress(score / 5)
