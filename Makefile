.PHONY: help install run test lint format clean


help:
	@echo "Available commands:"
	@echo "  make install       - Install project dependencies"
	@echo "  make run           - Run the FastAPI development server"
	@echo "  make test          - Run all unit and integration tests"
	@echo "  make lint          - Check code style with flake8"
	@echo "  make format        - Format code with black"
	@echo "  make clean         - Remove Python cache files and folders"
	@echo "  make coverage      - Run tests with coverage report (term output)"
	@echo "  make docker-build  - Build the Docker container"
	@echo "  make docker-up     - Start the application with docker-compose"
	@echo "  make docker-down   - Stop docker-compose containers"

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	PYTHONPATH=. pytest

lint:
	flake8 app tests

format:
	black app tests

clean:
	@find . -type d -name '__pycache__' -exec rm -r {} +
	@find . -type f -name '*.pyc' -delete

coverage:
	PYTHONPATH=. pytest --cov=app --cov-report=term-missing

docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-down:
	docker-compose down