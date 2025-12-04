from fastapi import APIRouter, Body
from services.chat_service import get_chat_response

router = APIRouter()

@router.post("/chat", tags=["Chat"])
async def chat(query: str = Body(..., embed=True)):
    response = get_chat_response(query)
    return {"answer": response}
