#
"""
API route definitions for the Q&A Chatbot backend.
Includes /chat and /health endpoints.
"""
# app/api/routes.py

from fastapi import APIRouter, status, Depends
from app.models.schemas import ChatRequest, ChatResponse, HealthResponse
from app.services.chat_service import ChatService

router = APIRouter()

def get_chat_service():
    """
    Dependency provider for ChatService instance.
    Returns:
        ChatService: An instance of ChatService.
    """
    return ChatService()

@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    summary="Ask a question to the chatbot"
)
async def chat(
    chat_req: ChatRequest,
    service: ChatService = Depends(get_chat_service)
):
    """
    Chat endpoint to handle user questions and return answers.
    Args:
        chat_req (ChatRequest): The incoming chat request with a question.
        service (ChatService): The chat service dependency.
    Returns:
        ChatResponse: The chatbot's answer.
    """
    answer = await service.get_answer(chat_req.question)
    return ChatResponse(answer=answer)

@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint"
)
async def health():
    """
    Health check endpoint to verify service status.
    Returns:
        HealthResponse: The health status of the service.
    """
    return HealthResponse(status="ok")
