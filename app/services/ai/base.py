from abc import ABC, abstractmethod


class AIEngine(ABC):

    @abstractmethod
    async def get_feedback(self, content: str) -> dict:
        pass
