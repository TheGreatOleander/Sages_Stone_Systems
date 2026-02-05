
from .schema import LanguageSchema

class LanguageSystem:
    def __init__(self):
        self.schema = LanguageSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "language", "status": "placeholder", "intent": intent}
