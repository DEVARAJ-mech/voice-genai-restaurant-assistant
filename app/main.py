from fastapi import FastAPI
from api.chat import router

app = FastAPI(title="Hybrid Voice AI")
app.include_router(router)


@app.get("/")
def health():
    return {"status": "ok"}
