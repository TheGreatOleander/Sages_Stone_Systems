
from .schema import SupplychainSchema

class SupplychainSystem:
    def __init__(self):
        self.schema = SupplychainSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "supplychain", "status": "placeholder", "intent": intent}
