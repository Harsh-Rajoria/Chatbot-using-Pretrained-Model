import streamlit as st
import requests
import time

# -------------------------------
# Configuration
# -------------------------------
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="ChatBuddy", layout="wide")
st.title("💬 ChatBuddy - Personal AI Chatbot")
st.write("Talk to your friendly AI assistant. ChatBuddy remembers your conversation!")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.text_input("Type your message here:", key="user_input")

if st.button("Send") and user_input.strip() != "":
    st.session_state.history.append({"user": user_input, "bot": ""})  # temporary placeholder
    user_input = user_input.strip()
    
    # Show typing indicator
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("🤖 ChatBuddy is typing...")

    # Send request to backend
    try:
        response = requests.post(API_URL, json={"text": user_input, "history": st.session_state.history[:-1]})
        if response.status_code == 200:
            bot_reply = response.json().get("reply", "")
            st.session_state.history[-1]["bot"] = bot_reply
        else:
            st.session_state.history[-1]["bot"] = "❌ Error: Backend returned a non-200 response."
    except Exception as e:
        st.session_state.history[-1]["bot"] = f"❌ Could not connect to backend: {e}"
    placeholder.empty()  # remove typing indicator

# -------------------------------
# Display chat history in bubbles
# -------------------------------
for msg in st.session_state.history:
    st.markdown(f"<div style='text-align:right; background-color:#DCF8C6; padding:8px; border-radius:10px; margin:5px 0;'>{msg['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:left; background-color:#F1F0F0; padding:8px; border-radius:10px; margin:5px 0;'>{msg['bot']}</div>", unsafe_allow_html=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Frontend powered by Streamlit • Backend powered by BlenderBot-400M-Distill")
