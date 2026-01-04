import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized configuration."""
    LLM_MODE = os.getenv("LLM_MODE", "offline")  # offline | online
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


settings = Settings()
