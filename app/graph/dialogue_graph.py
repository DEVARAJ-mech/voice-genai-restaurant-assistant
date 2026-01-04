from typing import Dict


# Simple state machine (can be replaced by LangGraph later)


def route_intent(text: str) -> str:
    text = text.lower()
    text = text.lower()
    if "menu" in text:
        return "MENU"
    if "reserve" in text:
        return "RESERVATION"
    if "order" in text:
        return "ORDER"
    return "GENERAL"
