# app/services/ai/openai.py
import os
from openai import OpenAI
from app.services.ai.base import AIEngine
from app.core.config import settings

class OpenAIAIEngine(AIEngine):
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def get_feedback(self, content: str) -> dict:
        prompt = self._build_prompt(content)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI writing assistant that reviews product feedback."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )

            result = response.choices[0].message.content

            # Try parsing result as JSON
            import json
            return json.loads(result)

        except Exception as e:
            return {
                "sentiment": "unknown",
                "readability_score": None,
                "suggestions": [f"AI error: {str(e)}"]
            }

    def _build_prompt(self, text: str) -> str:
        return (
            "You will receive a product review from a customer. "
            "Analyze it and return a JSON object with the following keys:\n"
            "- sentiment: one of 'positive', 'neutral', or 'negative'\n"
            "- readability_score: a number from 0 to 100\n"
            "- suggestions: a list of tips to improve the review\n\n"
            "Respond only with a valid JSON object.\n"
            f"Here's the review:\n\"\"\"\n{text}\n\"\"\""
        )