import re
import streamlit as st
import random as ra
import string
st.title("Password Checker")
if "password" not in st.session_state:
    st.session_state.password=""
if "password_manager" not in st.session_state:
    st.session_state.password_manager=[]
if "password_genrator" not in st.session_state:
    st.session_state.password_genrator=[]


def password_manager(password):
    score=0
    if len(password)>12:
        score+=1

    if re.search(r"^[A-Z]",password) and (r"^[a-z]",password) or\
       re.search(r"$[A-Z]",password) and (r"$[a-z]",password) or\
       re.search(r"[A-Z]+",password) and (r"[a-z]+",password):
        score+=1
    else:
        st.error("Password must include an upper case and a lower case")
    if len(password) > 8:
        score+=1
    else:
        st.error("Password must be contain 8 or more letter")
    if re.search(r"[@#$%^&*]+",password):
        score+=1
    else:
        st.error("Password must contain atleast one special character")
    if re.search(r"\d",password):
        score+=1
    else:
        st.error("Password must contain alteat one number")
    if re.search(r"\s+",password):
        st.error("Password can not have any white spaces")
    st.success(f"Your score is {score}")
    if score == 1 or score==2:
        st.success("Weak Password")
    if score == 4 or score==3:
        st.success("Moderate Password")
    if score == 5:
        st.success("Good")
    # st.success(f"Your score is {score}")

password=st.text_input("Input your password: ")
st.write(f"Inputed Password Is: {password}" )
password_manager(password)


if st.button("password_genrator"): 
    suggestion=""
    sep="@#$%^&*"
    all_ch=string.digits+string.ascii_uppercase+sep.strip()+string.ascii_lowercase+string.ascii_letters
    while len(suggestion) <14:
        suggestion+=ra.choice(all_ch)
    if re.search(r"\d",suggestion):
        suggestion[0:-1]
        suggestion+=ra.choice(string.digits)
    if re.search(sep,password):
        suggestion[0:-1]
        suggestion+=ra.choice(sep)

    # st.write(f"Suggested Password {suggestion}")
