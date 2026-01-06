import streamlit as st
import asyncio
from app.services.dialogue import listen, speak, handle

st.set_page_config(page_title="Voice Restaurant AI")

st.title("🍽️ Voice GenAI Restaurant Assistant")

if st.button("🎤 Speak"):
    user_text = listen()
    st.write("You:", user_text)

    response = handle(user_text)
    st.write("Assistant:", response)

    asyncio.run(speak(response))
