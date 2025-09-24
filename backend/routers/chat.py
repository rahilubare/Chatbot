# backend/routers/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import requests
import os

print("✅ LOADED: routers/chat.py")
print("✅ IMPORTED FastAPI, defining router...")

router = APIRouter(prefix="/api/v1", tags=["chat"])
print("✅ ROUTER CREATED:", router)

# 👇 THIS IS THE KEY LINE — you must define 'router'
router = APIRouter(prefix="/api/v1", tags=["chat"])

class ChatRequest(BaseModel):
    prompt: str
    model: Optional[str] = "llama3"
    use_fallback: Optional[bool] = False

class ChatResponse(BaseModel):
    response: str
    model_used: str

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    Chat with local LLM (Ollama) or fallback to OpenAI
    """
    try:
        if not request.use_fallback:
            # Try local Ollama first
            payload = {
                "model": request.model,
                "prompt": request.prompt,
                "stream": False
            }
            response = requests.post(
                os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate"),
                json=payload,
                timeout=60
            )
            if response.status_code == 200:
                result = response.json()
                return ChatResponse(
                    response=result.get("response", "").strip(),
                    model_used=request.model
                )
            else:
                print(f"Local LLM failed: {response.text}. Falling back to OpenAI.")

        # Fallback to OpenAI
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="No fallback API key configured")

        openai_resp = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": request.prompt}],
                "temperature": 0.2
            },
            timeout=30
        )
        if openai_resp.status_code == 200:
            data = openai_resp.json()
            message = data["choices"][0]["message"]["content"]
            return ChatResponse(response=message.strip(), model_used="gpt-3.5-turbo")
        else:
            raise HTTPException(status_code=500, detail="OpenAI API failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")