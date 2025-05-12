import re

from app.services.ai.base import AIEngine


class MockAIEngine(AIEngine):
    async def get_feedback(self, content: str) -> dict:
        sentiment = self.analyze_sentiment(content)
        readability = self.calculate_readability_score(content)
        suggestions = self.generate_suggestions(content)

        return {
            "sentiment": sentiment,
            "readability_score": readability,
            "suggestions": suggestions,
        }

    def analyze_sentiment(self, text: str) -> str:
        text = text.lower()
        if any(w in text for w in ["nice", "great", "love"]):
            return "positive"
        elif any(w in text for w in ["bad", "terrible", "hate"]):
            return "negative"
        else:
            return "neutral"

    def calculate_readability_score(self, text: str) -> float:
        sentences = max(1, len(re.findall(r"[^.!?]+", text)))
        words = len(re.findall(r"\w+", text))
        syllables = sum(self.count_syllables(word) for word in text.split())
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        return round(score, 2)

    def count_syllables(self, word: str) -> int:
        word = word.lower()
        return max(1, len(re.findall(r"[aeiouy]+", word)))

    def generate_suggestions(self, text: str) -> list:
        suggestions = []
        if len(text.split()) < 5:
            suggestions.append(
                "Consider adding more details to make your review clearer."
            )
        if not re.search(r"[.!?]$", text.strip()):
            suggestions.append("End your review with proper punctuation.")
        if any(word in text.lower() for word in ["bad", "terrible", "hate"]):
            suggestions.append(
                "Try to offer constructive feedback instead of harsh words."
            )
        return suggestions
