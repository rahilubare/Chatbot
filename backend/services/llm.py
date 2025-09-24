# backend/services/llm.py
import requests
import os

print("✅ LOADING services/llm.py...")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def generate_response(prompt: str, model: str = "llama3", fallback: bool = False) -> str:
    """
    Generate response using Ollama (local) or fallback to OpenAI.
    """
    # Try local Ollama first
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=60)
        if resp.status_code == 200:
            return resp.json().get("response", "").strip()
        elif not fallback:
            raise Exception("Local LLM failed")
    except Exception as e:
        if not fallback:
            raise e

    # Fallback to OpenAI
    if not OPENAI_KEY:
        raise Exception("No OpenAI API key provided for fallback")

    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    try:
        resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=30)
        if resp.status_code != 200:
            raise Exception(f"OpenAI API failed: {resp.text}")
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise Exception(f"OpenAI request failed: {str(e)}")

print("✅ generate_response FUNCTION DEFINED")