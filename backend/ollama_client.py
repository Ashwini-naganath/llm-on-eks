import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt):
    payload = {
    "model": "tinyllama",
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0
    }
}

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]