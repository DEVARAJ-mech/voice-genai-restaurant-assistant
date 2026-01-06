import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = "mistral"
DB_PATH = "reservations.db"
USE_GEMINI = False

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
