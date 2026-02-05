
from .schema import ClimateSchema

class ClimateSystem:
    def __init__(self):
        self.schema = ClimateSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "climate", "status": "placeholder", "intent": intent}
