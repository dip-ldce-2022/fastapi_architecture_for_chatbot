# FastAPI Q&A Chatbot Backend

A production-ready FastAPI backend for a simple Q&A chatbot.

## Features

- Modular, scalable structure
- POST `/chat` endpoint (static or OpenAI-powered)
- Health check endpoint `/health`
- CORS enabled (React-friendly)
- Pydantic validation, error handling, logging

## Setup & Run

1. **Clone the repo & enter folder:**
    ```bash
    git clone <your-repo-url>
    cd fastapi_chatbot
    ```

2. **Create `.env` (optional for OpenAI):**
    ```
    OPENAI_API_KEY=sk-...
    LOG_LEVEL=INFO
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server:**
    ```bash
    uvicorn app.main:app --reload
    ```

## Test API

- **Health check:**
    ```bash
    curl http://localhost:8000/health
    ```

- **Chat endpoint:**
    ```bash
    curl -X POST http://localhost:8000/chat \
      -H "Content-Type: application/json" \
      -d '{"question": "What is FastAPI?"}'
    ```

## Example Request & Response

**Request:**
```json
POST /chat
{
  "question": "What is FastAPI?"
}
```

**Response:**
```json
{
  "answer": "This is a sample response. OpenAI integration coming soon."
}
```
*(If OPENAI_API_KEY is set, the answer will come from OpenAI)*

## React Example (fetch)

```js
fetch("http://localhost:8000/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ question: "What is FastAPI?" })
})
  .then(res => res.json())
  .then(data => console.log(data.answer));
```

## Notes

- Extend `app/services/chat_service.py` for more advanced logic.
- Add more endpoints or authentication as needed.
