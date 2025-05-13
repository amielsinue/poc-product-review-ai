from enum import Enum

from pydantic_settings import BaseSettings  # Correct import for Pydantic v2


class AIEngineType(str, Enum):
    MOCK = "mock"
    OPENAI = "openai"


class Settings(BaseSettings):
    AI_ENGINE: AIEngineType = AIEngineType.MOCK
    OPENAI_API_KEY: str = ""
    API_KEY: str = "your_api_key_here"  # Replace with your actual API key

    model_config = {"env_file": ".env"}


settings = Settings()
