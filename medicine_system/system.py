
from .schema import MedicineSchema

class MedicineSystem:
    def __init__(self):
        self.schema = MedicineSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "medicine", "status": "placeholder", "intent": intent}
