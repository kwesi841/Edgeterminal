from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .logging_config import configure_logging
from .routers import auth as auth_router
from .routers import tokens as tokens_router
from .routers import settings as settings_router
from .routers import reports as reports_router
from .routers import signals as signals_router
from .routers import narratives as narratives_router
from .routers import risk as risk_router
from .routers import portfolios as portfolios_router
from .routers import alerts as alerts_router

app = FastAPI(title="Edge Terminal API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
configure_logging()

app.include_router(auth_router.router)
app.include_router(tokens_router.router)
app.include_router(settings_router.router)
app.include_router(reports_router.router)
app.include_router(signals_router.router)
app.include_router(narratives_router.router)
app.include_router(risk_router.router)
app.include_router(portfolios_router.router)
app.include_router(alerts_router.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.websocket("/ws/updates")
async def ws_updates(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"type": "hello", "message": "Edge Terminal WS connected"})
    await websocket.close()
