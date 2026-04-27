from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import generate_mongo_query
from query_executor import run_query
from formatter import format_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(data: ChatRequest):

    query = generate_mongo_query(data.question)

    result = run_query(query)

    answer = format_answer(data.question, result)

    return {
        "question": data.question,
        "answer": answer,
        "generated_query": query,
        "raw_result": result
    }
