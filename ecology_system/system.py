
from .schema import EcologySchema

class EcologySystem:
    def __init__(self):
        self.schema = EcologySchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "ecology", "status": "placeholder", "intent": intent}
