from pydantic import BaseModel
from typing import Optional

class ContentRequest(BaseModel):
    prompt: str
    title: Optional[str] = None

class ContentResponse(BaseModel):
    content: str
    notion_url: str
    id: int 