# Chatbot-using-Pretrained-Model
# 💬 ChatBuddy - Personal AI Chatbot

ChatBuddy is a friendly AI-powered conversational assistant built with **FastAPI** (backend) and **Streamlit** (frontend).  
It uses the **facebook/blenderbot-400M-distill** model from Hugging Face to generate human-like, engaging, and context-aware conversations — just like ChatGPT but lightweight and CPU-friendly.

---

## 🚀 Features

- 🤖 Conversational AI using **BlenderBot-400M-distill**
- 💡 Context-aware chat history between user and ChatBuddy
- 🧠 Friendly persona for casual, educational, and fun interactions
- 🌐 Backend built with **FastAPI**
- 🎨 Frontend built with **Streamlit**
- ⚡ Works smoothly even on CPU (no GPU required)
- 🧩 Easy to deploy on Railway, Render, or Hugging Face Spaces

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/chatbuddy.git
cd chatbot

2️⃣ Backend Setup
cd backend
pip install -r requirements.txt
uvicorn server:app --reload

Your backend API will start at:
http://127.0.0.1:8000

3️⃣ Frontend Setup
open a terminal window
cd frontend
pip install -r requirements.txt
streamlit run app.py

Your frontend will start at:
http://localhost:8501

💻 Example Prompts

Try these messages with ChatBuddy 👇
Category
Example Prompts
💬 Casual
“Hi ChatBuddy! How’s your day going?”
🎓 Learning
“Explain black holes in simple words.”
🧘 Productivity
“Give me some tips to stay focused.”
🎭 Fun
“Tell me a joke.” or “Write a short story about a dragon.”
💡 Advice
“How can I manage stress better?”

💡 Tip: To get more detailed answers, include “Explain in detail and give examples” at the start of your question.

🧠 Model Information

Model: facebook/blenderbot-400M-distill
Type: Seq2Seq conversational model
Size: 400M parameters
Framework: Hugging Face Transformers
Use Case: Lightweight chatbot / virtual assistant

✨ Acknowledgments
	•	Hugging Face Transformers
	•	FastAPI
	•	Streamlit
	•	Model: facebook/blenderbot-400M-distill

💬 About ChatBuddy

ChatBuddy was designed as a personal AI companion capable of engaging conversations, friendly advice, and lightweight assistance — all running locally on your machine.
Whether you’re studying, working, or just want to chat, ChatBuddy is here to talk!