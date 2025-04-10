import re
import streamlit as st
def check_password_strength(password):
    score = 0
    remarks = ""

    # Criteria for scoring
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Check each criteria
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

    # Remarks based on score
    if score == 5:
        remarks = "Very Strong"
    elif score == 4:
        remarks = "Strong"
    elif score == 3:
        remarks = "Moderate"
    elif score == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    return score, remarks

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    score, strength = check_password_strength(pwd)
    print(f"Password Strength: {strength} (Score: {score}/5)")
