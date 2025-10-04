PY=python

.PHONY: setup backend frontend up down migrate

setup:
	$(PY) -m pip install -r edge-terminal/requirements.txt

backend:
	uvicorn edge-terminal.backend.app.main:app --reload --port 8000

frontend:
	cd edge-terminal/frontend && npm i && npm run dev

up:
	docker compose -f edge-terminal/docker-compose.yml up --build

down:
	docker compose -f edge-terminal/docker-compose.yml down

migrate:
	cd edge-terminal/backend && alembic revision --autogenerate -m "auto" && alembic upgrade head
