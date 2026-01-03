from fastapi import FastAPI
from app.api.voice import router as voice_router
from app.db.database import init_db

app = FastAPI(
    title="Voice-Enabled GenAI Restaurant Assistant",
    version="1.0"
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(voice_router, prefix="/voice")


@app.get("/health")
def health():
    return {"status": "running"}
