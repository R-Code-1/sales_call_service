from fastapi import APIRouter, Form
from app.services.coachable_moment import get_coachable_moment, replay_moment
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/replay")
async def replay(call_id: str = Form(...)):
    moment = get_coachable_moment(call_id)
    audio_path = replay_moment(moment)
    return FileResponse(audio_path, media_type="audio/wav", filename="replay.wav")
