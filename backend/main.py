from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Call Ollama (make sure ollama is running in background: `ollama run llama3`)
        ollama_url = "http://127.0.0.1:11434/api/generate"
        payload = {
            "model": "llama3",   # change if you have another model
            "prompt": req.message
        }

        response = requests.post(ollama_url, json=payload, stream=True)

        # Collect Ollama's streamed response
        full_reply = ""
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8")
                if '"response":' in data:
                    # Extract text piece
                    part = data.split('"response":"')[1].split('"')[0]
                    full_reply += part

        return {"response": full_reply.strip()}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}
