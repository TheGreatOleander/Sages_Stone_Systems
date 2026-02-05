
from .schema import MarketSchema

class MarketSystem:
    def __init__(self):
        self.schema = MarketSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "market", "status": "placeholder", "intent": intent}
