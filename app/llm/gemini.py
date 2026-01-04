import os
import google.generativeai as genai

from llm.base import LLMProvider
from core.config import settings


from google import genai as new_genai
from google.genai import types


class GeminiProviderNew(LLMProvider):
    """Uses the NEW google-genai library (recommended)."""

    def __init__(self):
        if not settings.GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY is not set. Please check your .env file."
            )

        # Create client with API key
        self.client = new_genai.Client(api_key=settings.GOOGLE_API_KEY)
        self.model_name = "gemini-1.5-flash"  # or gemini-1.5-pro

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text or ""
