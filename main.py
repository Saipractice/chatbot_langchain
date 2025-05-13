from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature=0.7
)

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/chat")
async def chat(input: ChatInput):
    response = llm.invoke(input.message)
    return {"response": response}