
from fastapi import FastAPI
from app.api.endpoints import transcribe, speak, replay

app = FastAPI()

app.include_router(transcribe.router)
app.include_router(speak.router)
app.include_router(replay.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
