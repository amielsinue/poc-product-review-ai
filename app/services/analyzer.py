from app.services.ai.engine import ai_engine


async def analyze_review(content: str) -> dict:
    return await ai_engine.get_feedback(content)
