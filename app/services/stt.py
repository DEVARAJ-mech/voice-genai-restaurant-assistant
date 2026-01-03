import whisper
import tempfile
import os
from typing import cast

model = whisper.load_model("base")


def speech_to_text(audio_file) -> str:
    """
    Converts uploaded audio file to text using Whisper.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.file.read())
        temp_path = tmp.name

    try:
        result = model.transcribe(temp_path)
        text = cast(str, result["text"])
        return text.strip()
    finally:
        os.remove(temp_path)
