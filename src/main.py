from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests
import json

app = FastAPI(title="MistralAI")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: PromptRequest):
    ollama_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": request.prompt,
        "stream": False #Set false to get the complete response
    }

    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status() #raise an exception

        #ollama returns a json response, parse nd extract content
        result = response.json()
        return {"response": result.get("response", "No response")}
    except requests.exceptions.RequestException as exception:
        raise HTTPException(status_code=500, detail=f"Request failed connectin to ollama service: {exception}")