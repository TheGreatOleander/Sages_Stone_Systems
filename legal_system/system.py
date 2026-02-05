
from .schema import LegalSchema

class LegalSystem:
    def __init__(self):
        self.schema = LegalSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "legal", "status": "placeholder", "intent": intent}
