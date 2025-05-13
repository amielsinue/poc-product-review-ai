from fastapi import APIRouter, HTTPException, Query, Depends
from app.schemas.review import ReviewRequest
from app.dependencies.auth import verify_api_key
from app.services.ai.mock import MockAIEngine
from app.services.ai.openai import OpenAIAIEngine
from app.services.ai.engine import ai_engine

router = APIRouter()


@router.post("/analyze")
async def analyze(
    review: ReviewRequest, engine: str = Query("env"), _: str = Depends(verify_api_key)
):
    if not review.content.strip():
        raise HTTPException(status_code=400, detail="Review content cannot be empty")

    if engine == "openai":
        selected = OpenAIAIEngine()
    elif engine == "mock":
        selected = MockAIEngine()
    else:
        selected = ai_engine

    return await selected.get_feedback(review.content)
