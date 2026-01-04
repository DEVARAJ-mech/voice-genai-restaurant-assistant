from fastapi import APIRouter
from pydantic import BaseModel
from services.dialogue import DialogueService

router = APIRouter()
dialogue = DialogueService()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = dialogue.handle(req.message)
    return {"response": reply}
