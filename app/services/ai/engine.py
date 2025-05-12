from app.core.config import AIEngineType, settings
from app.services.ai.base import AIEngine
from app.services.ai.mock import MockAIEngine
from app.services.ai.openai import OpenAIAIEngine

ENGINE_MAP = {
    AIEngineType.MOCK: MockAIEngine,
    AIEngineType.OPENAI: OpenAIAIEngine,
}

ai_engine: AIEngine = ENGINE_MAP[settings.AI_ENGINE]()
