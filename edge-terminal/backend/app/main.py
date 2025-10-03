from fastapi import FastAPI, WebSocket
from .config import settings
from .logging_config import configure_logging
from .routers import auth as auth_router
from .routers import tokens as tokens_router
from .routers import settings as settings_router
from .routers import reports as reports_router

app = FastAPI(title="Edge Terminal API", version="0.1.0")
configure_logging()

app.include_router(auth_router.router)
app.include_router(tokens_router.router)
app.include_router(settings_router.router)
app.include_router(reports_router.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.websocket("/ws/updates")
async def ws_updates(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"type": "hello", "message": "Edge Terminal WS connected"})
    await websocket.close()
