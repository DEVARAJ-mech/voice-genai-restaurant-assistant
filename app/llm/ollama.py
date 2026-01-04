import requests
from llm.base import LLMProvider
from core.config import settings


class OllamaProvider(LLMProvider):
    """Offline LLM provider using Ollama."""

    def generate(self, prompt: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": settings.OLLAMA_MODEL,
                "prompt": prompt,
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["response"]
