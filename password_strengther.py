import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter By Iffat Mumtaz", page_icon="📄",layout="centered")
st. markdown("""
           <style>
           .main {text-align: center;}
           .stTextInput {width: 60% ! important; margin: auto;}
           .stButton button{width:50% background-color #4CAF50; color:white; font-size:18px;}
           .stButton button:hover {background-color: #45a049;}
           </style>
           """,unsafe_allow_html=True)
#Page Title and Description
st.title("🔒Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

#Function to check password strength
def check_password_strength(password):
    score = 0
feedback = []
if len(password) >= 8:  # type: ignore
    score += 1 # type: ignore #
else:
    feedback.append("❌ Password should be ""atleast 8 charactor long"".")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password): # type: ignore
        score += 1 # type: ignore
    else:
        feedback.append("❌Password should include""both uppercase (A-Z) and lowercase (a-z) letters"",")
        if re.search(r"/d",password):       # type: ignore
            score += 1 # type: ignore
        else:
            feedback.append("❌ Password should be ""atleast one number(0-9)"".")
            
            #Special charactors
            if re.search(r"[!@#$%%^*],password"):
                score += 1 # type: ignore
            else:
                feedback.append("❌ Include "" at least one Special charactor (@#$%^&*)"",")
                #Display password strength result
                
                if score == 4: # type: ignore
                 st.success("✅ ""Strong Password"" Your password is Secure.")
                elif score == 3: # type: ignore
                    st.info("⚠️ ""Moderate Password"". Consider improving secutrity by adding more feature")
                else:
                    st.error(" ""Week password"" . Follow thw suggestion below to strength it.")
                    
                    #Feedback
                    if feedback:
                         with st.expander("🔍""Improve Your Password"):
                             for item in feedback:
                                 st.write(item)
                                 password =st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔒")
                                 
                                 #Button working
                             if st.button("Check Strength"):
                                    check_password_strength(password)
                             else:
                                 st.warning("⚠️ Please enter a password first!") #show warning if pasword empty
                    
    
