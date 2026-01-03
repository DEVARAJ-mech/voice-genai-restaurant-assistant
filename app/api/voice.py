from fastapi import APIRouter, UploadFile, File
from app.services.stt import speech_to_text
from app.services.dialogue import handle_dialogue
from app.services.tts import text_to_speech

router = APIRouter()


@router.post("/interact")
async def interact(audio: UploadFile = File(...)):
    user_text = speech_to_text(audio)
    response_text = handle_dialogue(user_text)
    audio_response = text_to_speech(response_text)

    return {
        "transcription": user_text,
        "response": response_text,
        "audio_bytes": len(audio_response)
    }
