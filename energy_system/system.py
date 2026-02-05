
from .schema import EnergySchema

class EnergySystem:
    def __init__(self):
        self.schema = EnergySchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "energy", "status": "placeholder", "intent": intent}
