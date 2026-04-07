#
"""
Logging configuration utility for the Q&A Chatbot backend.
"""
# app/core/logging_config.py

import logging

def setup_logging(level: str = "INFO"):
    """
    Configure global logging settings for the application.
    Args:
        level (str): Logging level (e.g., 'INFO', 'DEBUG').
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
