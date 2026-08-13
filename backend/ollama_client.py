import requests
from rag import retrieve_context

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


def generate_response(prompt):
    context = retrieve_context(prompt)

    rag_prompt = f"""
You are a DevOps AI assistant.

Use the following knowledge base context to answer the question.

Context:
{context}

Question:
{prompt}

Answer clearly and concisely.
"""

    payload = {
        "model": "tinyllama",
        "prompt": rag_prompt,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]
