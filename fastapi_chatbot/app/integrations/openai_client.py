#
"""
Integration client for OpenAI chat completion API.
"""
# app/integrations/openai_client.py

import openai

class OpenAIClient:
    """
    Client for interacting with the OpenAI chat completion API.
    """
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI client with the provided API key.
        Args:
            api_key (str): OpenAI API key.
        """
        openai.api_key = api_key

    async def get_answer(self, question: str) -> str:
        """
        Get an answer from OpenAI's chat completion API for the given question.
        Args:
            question (str): The user's question.
        Returns:
            str: The generated answer from OpenAI.
        """
        response = await openai.AsyncOpenAI().chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
