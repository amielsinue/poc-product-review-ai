
# AI Review Feedback API
![CI](https://github.com/amielsinue/poc-product-review-ai/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/amielsinue/poc-product-review-ai/graph/badge.svg?token=ME7JKAPWIU)](https://codecov.io/gh/amielsinue/poc-product-review-ai)

This service accepts user-submitted product reviews and returns structured AI-like feedback including sentiment, readability score, and improvement suggestions.

## Features
- Written in **FastAPI** using **async architecture**
- Simulated AI feedback (sentiment, readability, suggestions)
- Fully Dockerized with `docker-compose`
- CI pipeline using GitHub Actions
- Includes async unit and integration tests

## Setup
```bash
docker-compose up --build
```

## API Usage
`POST /analyze`
```text
X-API-Key: secret123
```

```json
{
  "content": "Great product, I loved it!"
}
```

## Response
```json
{
  "sentiment": "positive",
  "readability_score": 85.23,
  "suggestions": []
}
```

## Tests
```bash
pytest
```

## AI Tools Used
Used **GitHub Copilot** to assist in generating function templates, async migration, test structures, and Docker setup. Copilot accelerated development and ensured consistency.
