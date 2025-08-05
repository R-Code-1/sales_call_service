from fastapi import APIRouter, UploadFile, File, Form
from app.services.stt_service import transcribe_audio

router = APIRouter()

@router.post("/transcribe")
async def transcribe(
    audio: UploadFile = File(...),
    call_id: str = Form(...),
    agent_id: str = Form(...),
    customer_id: str = Form(...)
):
    return await transcribe_audio(audio, call_id, agent_id, customer_id)
