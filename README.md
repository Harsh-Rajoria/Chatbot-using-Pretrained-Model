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

## 🧩 Project Structue

chatbot/
│
├── frontend/
│   ├── app.py              # Streamlit user interface
│   ├── requirements.txt    # Frontend dependencies
│   └── README.md           # Documentation file (this one)
│
└── backend/
├── server.py           # FastAPI backend with Hugging Face model
├── requirements.txt    # Backend dependencies
└── Procfile            # Deployment configuration (optional)

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

