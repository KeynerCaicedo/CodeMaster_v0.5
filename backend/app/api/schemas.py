from pydantic import BaseModel, Field
from typing import Optional

class GenerateRequest(BaseModel):
    provider: str = Field(..., example='openai')
    model: str = Field(..., example='gpt-4o-mini')
    prompt: str = Field(..., example='Write a function that reverses a string', max_length=5000)
    meta: Optional[dict] = None

class GenerateResponse(BaseModel):
    success: bool
    text: Optional[str] = None
    meta: Optional[dict] = None
