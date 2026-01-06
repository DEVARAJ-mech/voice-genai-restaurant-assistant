import speech_recognition as sr
import asyncio
import edge_tts
import os
import io
from faster_whisper import WhisperModel

from app.graph.dialogue_graph import DialogueGraph
from app.llm.ollama import OllamaLLM
from app.db import add_reservation

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="float32"
)
llm = OllamaLLM()
graph = DialogueGraph()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    wav = audio.get_wav_data()
    audio_stream = io.BytesIO(wav)
    segments, _ = model.transcribe(audio_stream)
    return " ".join(s.text for s in segments)


async def speak(text):
    tts = edge_tts.Communicate(text, "en-US-JennyNeural")
    await tts.save("reply.mp3")
    os.system("start reply.mp3")


def handle(text: str) -> str:
    graph.update("User", text)

    prompt = f"""
You are a restaurant AI assistant.
Conversation so far:
{graph.context()}

User: {text}
Assistant:
"""
    reply = llm.generate(prompt)

    if "reserve" in text.lower():
        add_reservation("Guest", "Today", "7 PM", 2)

    graph.update("Assistant", reply)
    return reply
