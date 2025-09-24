# backend/routers/commit.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.llm import generate_response
from ..utils.prompts import COMMIT_PROMPT



router = APIRouter(prefix="/api/v1", tags=["commit"])
print("✅ COMMIT ROUTER CREATED:", router)

class CommitRequest(BaseModel):
    description: str

class CommitResponse(BaseModel):
    message: str

@router.post("/commit", response_model=CommitResponse)
async def generate_commit_message(request: CommitRequest):
    prompt = COMMIT_PROMPT.format(description=request.description)
    try:
        message = generate_response(prompt, model="llama3")
        return CommitResponse(message=message.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))