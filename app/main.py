from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.analyzer import analyze_review

app = FastAPI()


class ReviewRequest(BaseModel):
    content: str


@app.post("/analyze")
async def analyze(review: ReviewRequest):
    if not review.content.strip():
        raise HTTPException(status_code=400, detail="Review content cannot be empty")
    return await analyze_review(review.content)
