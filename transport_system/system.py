
from .schema import TransportSchema

class TransportSystem:
    def __init__(self):
        self.schema = TransportSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "transport", "status": "placeholder", "intent": intent}
