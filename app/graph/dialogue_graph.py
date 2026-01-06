class DialogueGraph:
    def __init__(self):
        self.history = []

    def update(self, role, text):
        self.history.append(f"{role}: {text}")

    def context(self):
        return "\n".join(self.history[-6:])
