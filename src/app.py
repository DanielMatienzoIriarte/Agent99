from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client

app = FastAPI()
client = Client(host='http://localhost:11434')

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.chat(
        model='mistral',
        messages=[
        {
            'role': 'user',
            'content': request.prompt,
        },
    ])

    return {"assistant": response['messages']['content']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)