import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No GEMINI_API_KEY found in .env file")

# FastAPI app
app = FastAPI(
    title="NASA Bioscience Chatbot",
    description="A chatbot that answers any user query related to NASA bioscience research using Gemini AI.",
    version="1.0"
)

# Gemini API endpoint
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-pro:generateContent?key={api_key}"

# Request model for dynamic queries
class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "✅ Gemini AI Chatbot is running!"}

@app.post("/ask")
async def ask_gemini(request: QueryRequest):
    """
    Accepts any user query and returns a response from Gemini AI.
    """
    payload = {"contents": [{"parts": [{"text": request.query}]}]}
    
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(GEMINI_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            
            # Extract reply safely
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": reply}

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    
    except httpx.ReadTimeout:
        raise HTTPException(status_code=504, detail="Gemini API timed out. Please try again.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
