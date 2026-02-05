
from .schema import HealthSchema

class HealthSystem:
    def __init__(self):
        self.schema = HealthSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "health", "status": "placeholder", "intent": intent}
