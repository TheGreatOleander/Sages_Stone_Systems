
from .schema import ManufacturingSchema

class ManufacturingSystem:
    def __init__(self):
        self.schema = ManufacturingSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "manufacturing", "status": "placeholder", "intent": intent}
