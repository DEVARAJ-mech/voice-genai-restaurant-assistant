from app.core.llm import query_llm
from app.services.reservation import handle_reservation
from app.services.memory import get_state, update_state


def handle_dialogue(user_text: str) -> str:
    state = get_state()
    text = user_text.lower()

    if "reserve" in text or "book" in text:
        update_state(intent="reservation")
        return handle_reservation(user_text)

    prompt = f"""
    You are a restaurant receptionist.
    Conversation context:
    Intent: {state.intent}

    User: {user_text}
    Respond politely and clearly.
    """

    return query_llm(prompt)
