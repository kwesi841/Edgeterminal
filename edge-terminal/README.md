# Edge Terminal

Professional crypto analytics web app. Backend (FastAPI + APScheduler + SQLite + Alembic). Frontend (React + Vite + TS). All data from free sources (CoinGecko, RSS) with disk cache to minimize API calls. No placeholders.

## Dev

1) Backend

- Create venv and install deps: `pip install -r edge-terminal/requirements.txt`
- Initialize DB: `python -m edge-terminal.backend.app.db.init_db`
- Run API: `uvicorn edge-terminal.backend.app.main:app --reload --port 8000`

2) Frontend

- `cd edge-terminal/frontend`
- `npm i`
- `npm run dev`

Open http://localhost:5173

## Alembic

- `cd edge-terminal/backend`
- `alembic revision --autogenerate -m "init"`
- `alembic upgrade head`

## Notes

- HTTP client implements ETag/If-Modified-Since and TTL disk cache under `.cache/http`.
- Initial seed creates `admin@example.com` (password printed once). Update via auth endpoints.
- Reports Center endpoints stubbed; implement builder and SMTP when wiring UI.
