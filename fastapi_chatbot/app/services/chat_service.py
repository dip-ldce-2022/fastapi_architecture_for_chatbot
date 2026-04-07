#
"""
Business logic for handling chat requests and integrating with OpenAI.
"""
# app/services/chat_service.py

import logging
from app.core.config import settings
from app.integrations.openai_client import OpenAIClient

logger = logging.getLogger("chat_service")

class ChatService:
    """
    Service class for handling chat logic and OpenAI integration.
    """
    def __init__(self):
        """
        Initialize the ChatService, setting up OpenAI integration if API key is present.
        """
        self.openai_enabled = bool(settings.OPENAI_API_KEY)
        self.openai_client = OpenAIClient(settings.OPENAI_API_KEY) if self.openai_enabled else None

    async def get_answer(self, question: str) -> str:
        """
        Generate an answer for the given question.
        Uses OpenAI if enabled, otherwise returns a static response.
        Handles empty input and OpenAI errors gracefully.
        Args:
            question (str): The user's question.
        Returns:
            str: The chatbot's answer.
        """
        if not question.strip():
            logger.warning("Received empty question.")
            return "Please provide a valid question."
        if self.openai_enabled:
            try:
                return await self.openai_client.get_answer(question)
            except Exception as e:
                logger.error(f"OpenAI error: {e}")
                return "Sorry, there was an error generating the answer."
        return "This is a sample response. OpenAI integration coming soon."
