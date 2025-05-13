## 🧠 Development Process

This project was built following clean architecture principles, a modular service-oriented design, and strict TDD discipline. I leveraged AI-assisted tools (ChatGPT, Cursor Copilot) to accelerate reasoning, catch blind spots, and streamline code refactoring.

The main steps:
- Architecture planning (modular breakdown)
- Scaffolding using FastAPI, Pydantic
- Test-first development (pytest)
- AI-assisted implementation of logic layers
- Dockerization and CI setup
- Proposal for CI/CD to ECS with GitHub Actions

## ✅ Test-Driven Development (TDD)

Each functionality (such as the review analysis endpoint, or engine selection logic) was implemented only after writing failing tests first. This ensured:
- Full test coverage (~88%)
- Refactor-safe code
- Early detection of misalignments

Tools used:
- pytest
- pytest-asyncio
- Makefile with `make test` and `make coverage`

## ⚙️ DevOps & Delivery

- Docker-based local setup (`docker-compose up`)
- Makefile commands for lint, test, format
- CI via GitHub Actions for lint, tests, formatting, coverage
- Codecov integration
- CD proposal for ECS-based deployment via GitHub Actions