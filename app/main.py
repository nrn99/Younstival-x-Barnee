from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
#Infra built

ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",") if o.strip()]


app = FastAPI(title="Youngstival Chat API")


app.add_middleware(
CORSMiddleware,
allow_origins=ALLOWED_ORIGINS if ALLOWED_ORIGINS else ["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


class QARequest(BaseModel):
    question: str
    k: int | None = 6


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/qa")
async def qa(req: QARequest):
    # TODO: wire to your retriever + LLM using the JSONL dataset
    # Placeholder echo response for infra validation
    return {
    "answer": f"You asked: {req.question}",
    "k": req.k,
    "source": "youngstival-jsonl"
    }