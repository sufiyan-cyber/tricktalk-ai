import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Setup OpenAI client for OpenRouter
openai_client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Page setup
st.set_page_config(
    page_title="Social Engineering Chatbot",
    page_icon="🎭",
    layout="centered"
)

# Title and description
st.markdown("<h1 style='color:#004AAD;'>🎭 Social Engineering Simulator</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:16px;'>An educational demo showcasing how scammers manipulate conversations. Built for awareness only.</p>", unsafe_allow_html=True)
st.warning("⚠️ Do not enter real personal information. This is for educational purposes only.")

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a social engineer trying to trick the user into sharing personal information. Be sneaky but keep it short and don’t include links."}
    ]
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Display chat history
# Display chat history
for msg in st.session_state.messages[1:]:  # Skip system prompt
    if msg["role"] == "user":
        st.markdown(
            f"<div style='background-color:#d0ebff;color:#003366;padding:10px;border-radius:10px;margin-bottom:10px'><b>You:</b> {msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#ffe0e9;color:#4a0f27;padding:10px;border-radius:10px;margin-bottom:10px'><b>Bot:</b> {msg['content']}</div>",
            unsafe_allow_html=True
        )


# Define callback to handle submission
def submit():
    user_message = st.session_state.user_input.strip()
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        with st.spinner("Thinking..."):
            response = openai_client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=st.session_state.messages
            )
        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.session_state.user_input = ""  # Clear input AFTER processing

# Centered input box
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.text_input("You:", key="user_input", on_change=submit, label_visibility="collapsed")

# Footer credit
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:14px;'>What seems real, isn’t always right. Stay informed.</p>", unsafe_allow_html=True)
