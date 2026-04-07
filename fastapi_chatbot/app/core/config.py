#
"""
Configuration module for loading environment variables and settings.
"""
# app/core/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Application settings loaded from environment variables.
    Attributes:
        OPENAI_API_KEY (str): OpenAI API key for integration.
        LOG_LEVEL (str): Logging level for the application.
    """
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
