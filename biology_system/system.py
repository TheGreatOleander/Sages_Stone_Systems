
from .schema import BiologySchema

class BiologySystem:
    def __init__(self):
        self.schema = BiologySchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "biology", "status": "placeholder", "intent": intent}
