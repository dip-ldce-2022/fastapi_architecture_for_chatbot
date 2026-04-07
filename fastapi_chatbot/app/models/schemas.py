#
"""
Pydantic schemas for request and response validation in the Q&A Chatbot API.
"""
# app/models/schemas.py

from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    """
    Request model for chat endpoint. Contains the user's question.
    """
    question: str = Field(..., example="What is FastAPI?")

class ChatResponse(BaseModel):
    """
    Response model for chat endpoint. Contains the chatbot's answer.
    """
    answer: str = Field(..., example="FastAPI is a modern web framework for Python.")

class HealthResponse(BaseModel):
    """
    Response model for health check endpoint.
    """
    status: str = Field(..., example="ok")
