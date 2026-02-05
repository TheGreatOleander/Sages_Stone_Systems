
from .schema import AiSchema

class AiSystem:
    def __init__(self):
        self.schema = AiSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "ai", "status": "placeholder", "intent": intent}
