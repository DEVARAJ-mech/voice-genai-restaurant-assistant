import streamlit as st
import requests

st.set_page_config(page_title="AI Receptionist")

st.title("🍽️ AI Restaurant Receptionist")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Speak or type your request:")

if st.button("Send") and user_input:
    res = requests.post(
        "http://localhost:8000/chat",
        json={"message": user_input},
    )
    answer = res.json()["response"]
    st.session_state.history.append((user_input, answer))

for u, a in st.session_state.history:
    st.markdown(f"**You:** {u}")
    st.markdown(f"**Assistant:** {a}")
