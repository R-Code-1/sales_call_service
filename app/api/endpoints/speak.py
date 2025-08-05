from fastapi import APIRouter
from pydantic import BaseModel
from app.services.tts_service import synthesize_speech
from fastapi.responses import FileResponse
import tempfile

router = APIRouter()

class SpeakRequest(BaseModel):
    text: str

@router.post("/speak")
async def speak(req: SpeakRequest):
    audio_path = synthesize_speech(req.text)
    return FileResponse(audio_path, media_type="audio/wav", filename="speech.wav")
