from google import genai
from app.llm.base import BaseLLM
from app.core.config import GEMINI_API_KEY


class GeminiLLM(BaseLLM):
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )
        return response.text
