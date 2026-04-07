#
"""
Main entry point for the FastAPI Q&A Chatbot backend.
Sets up the FastAPI app, middleware, logging, routes, and global exception handling.
"""
# app/main.py

import logging
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.logging_config import setup_logging
from app.core.config import settings

setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger("main")

app = FastAPI(
    title="Q&A Chatbot API",
    description="A simple, production-ready FastAPI backend for a Q&A chatbot.",
    version="1.0.0"
)

# Enable CORS for all origins (React-friendly)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log incoming HTTP requests and their responses.
    Args:
        request (Request): The incoming HTTP request.
        call_next: The next middleware or route handler.
    Returns:
        Response: The HTTP response.
    """
    logger.info("Request: %s %s", request.method, request.url)
    response = await call_next(request)
    logger.info("Response status: %s", response.status_code)
    return response

@app.exception_handler(Exception)
async def global_exception_handler(_: Request, exc: Exception):
    """
    Global exception handler for unhandled errors.
    Logs the error and returns a generic 500 response.
    Args:
        _ (Request): The incoming HTTP request (unused).
        exc (Exception): The exception that was raised.
    Returns:
        JSONResponse: A 500 Internal Server Error response.
    """
    logger.error("Unhandled error: %s", exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
