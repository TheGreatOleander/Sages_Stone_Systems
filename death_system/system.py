
from .schema import DeathSchema

class DeathSystem:
    def __init__(self):
        self.schema = DeathSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "death", "status": "placeholder", "intent": intent}
