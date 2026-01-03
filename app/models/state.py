from pydantic import BaseModel
from typing import Optional


class ConversationState(BaseModel):
    intent: Optional[str] = None
    name: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    guests: Optional[int] = None
