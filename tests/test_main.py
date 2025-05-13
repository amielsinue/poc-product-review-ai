import pytest

from tests.config import *  # noqa: F403, F401


@pytest.mark.asyncio
class TestAnalyzeEndpoint:

    async def test_valid_review_returns_sentiment(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "Nice product"}, headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"

    async def test_empty_review_returns_400(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "   "}, headers=headers
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Review content cannot be empty"

    async def test_review_returns_readability_score(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "Nice product"}, headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data["readability_score"], (int, float))

    async def test_review_returns_suggestions_list(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "bad product"}, headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data["suggestions"], list)
        assert len(data["suggestions"]) > 0

    async def test_neutral_review_returns_neutral_sentiment(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "This is a product."}, headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "neutral"
        assert isinstance(data["readability_score"], (int, float))
        assert isinstance(data["suggestions"], list)

    async def test_positive_review_has_no_suggestions(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze",
            json={"content": "I love this product. It works great!"},
            headers=headers,
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"
        assert isinstance(data["suggestions"], list)
        assert len(data["suggestions"]) == 0

    async def test_short_incomplete_review_has_multiple_suggestions(self, async_client):
        headers = {"X-API-Key": "secret123"}
        response = await async_client.post(
            "/analyze", json={"content": "Bad"}, headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert "constructive" in " ".join(data["suggestions"]).lower()
        assert "punctuation" in " ".join(data["suggestions"]).lower()
        assert "more details" in " ".join(data["suggestions"]).lower()

    async def test_missing_api_key_header_returns_422(self, async_client):
        response = await async_client.post("/analyze", json={"content": "Test"})
        assert response.status_code == 422
        data = response.json()
        assert "x-api-key" in str(data["detail"])

    async def test_invalid_api_key_returns_401(self, async_client):
        headers = {"X-API-Key": "wrong-key"}
        response = await async_client.post(
            "/analyze", json={"content": "Test"}, headers=headers
        )
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid API Key"
