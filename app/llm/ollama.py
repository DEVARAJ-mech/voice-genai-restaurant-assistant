import ollama
from app.llm.base import BaseLLM
from app.core.config import OLLAMA_MODEL


class OllamaLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]
