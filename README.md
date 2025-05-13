
# AI Review Feedback API
![CI](https://github.com/amielsinue/poc-product-review-ai/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/amielsinue/poc-product-review-ai/branch/main/graph/badge.svg?token=ME7JKAPWIU)](https://codecov.io/gh/amielsinue/poc-product-review-ai)

This service accepts user-submitted product reviews and returns structured AI-like feedback including sentiment, readability score, and improvement suggestions.

## Features
- Written in **FastAPI** using **async architecture**
- Simulated AI feedback (sentiment, readability, suggestions)
- Fully Dockerized with `docker-compose`
- CI pipeline using GitHub Actions
- Includes async unit and integration tests

## Setup
👉 [Setup process](./LOCAL_SETUP.md)


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

## 🛠 Available Makefile Commands

This project includes a `Makefile` with common development and DevOps commands:

```bash
make <command>
```

| Command             | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `make install`      | Install project dependencies from `requirements.txt`         |
| `make run`          | Run the FastAPI development server (`localhost:8000`)        |
| `make test`         | Run all unit and integration tests using pytest              |
| `make lint`         | Check code style using flake8                                |
| `make format`       | Format code using black                                      |
| `make clean`        | Remove Python cache files (`__pycache__`, `.pyc`, etc.)      |
| `make coverage`     | Run tests and display code coverage summary in terminal      |
| `make docker-build` | Build the Docker container using docker-compose              |
| `make docker-up`    | Start services with docker-compose (`localhost:8000`)        |
| `make docker-down`  | Stop all services started with docker-compose                |

## 📖 Learn More

👉 [Development Process](./DEVELOPMENT.md)
