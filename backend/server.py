from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import uvicorn

app = FastAPI(title="Personal Chatbot API")

print("🤖 Loading BlenderBot-400M-Distill model...")

model_path = "facebook/blenderbot-400M-distill"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
generator = pipeline(
    "text2text-generation",  # Seq2Seq model
    model=model,
    tokenizer=tokenizer
)

print("✅ Model loaded successfully!")

class MessageInput(BaseModel):
    text: str
    history: list  # list of {"user": "...", "bot": "..."}

@app.get("/")
def root():
    return {"message": "Personal Chatbot API is running 🚀"}

@app.post("/chat")
def chat_with_bot(input_data: MessageInput):
    user_message = input_data.text.strip()
    history = input_data.history or []

    if len(user_message) == 0:
        return {"reply": "Please say something!"}

    # Build prompt with persona + history
    prompt = "You are ChatBuddy, a friendly AI assistant. Talk casually, give helpful answers, and keep the conversation engaging.\n\nConversation History:\n"
    for msg in history:
        prompt += f"User: {msg['user']}\nBot: {msg['bot']}\n"
    prompt += f"User: {user_message}\nBot:"

    # Generate response
    outputs = generator(
        prompt,
        max_length=200,  # maximum output tokens
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )

    bot_reply = outputs[0]["generated_text"].strip()
    history.append({"user": user_message, "bot": bot_reply})

    return {"reply": bot_reply, "history": history}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
