
from .schema import ValueSchema

class ValueSystem:
    def __init__(self):
        self.schema = ValueSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "value", "status": "placeholder", "intent": intent}
