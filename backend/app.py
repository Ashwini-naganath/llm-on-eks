from fastapi import FastAPI
from ollama_client import generate_response


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to DevOps AI Assistant"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/chat")
def chat(prompt: str):
    answer = generate_response(prompt)

    return {
        "question": prompt,
        "answer": answer
    }
