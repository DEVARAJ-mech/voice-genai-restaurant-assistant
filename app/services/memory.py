from app.models.state import ConversationState

conversation_state = ConversationState()


def get_state():
    return conversation_state


def update_state(**kwargs):
    for key, value in kwargs.items():
        setattr(conversation_state, key, value)


def reset_state():
    global conversation_state
    conversation_state = ConversationState()
