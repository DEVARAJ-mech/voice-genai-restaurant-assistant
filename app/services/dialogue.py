from llm.ollama import OllamaProvider
from core.config import settings
from graph.dialogue_graph import route_intent


class DialogueService:
    """Handles conversation logic and LLM routing."""

    def __init__(self):
        self.llm = OllamaProvider()

    def handle(self, user_text: str) -> str:
        intent = route_intent(user_text)

        system_prompt = (
            "You are a polite restaurant receptionist. "
            "Keep answers short and helpful."
        )

        prompt = f"""
        SYSTEM: {system_prompt}
        INTENT: {intent}
        USER: {user_text}
        ASSISTANT:
        """

        return self.llm.generate(prompt)
