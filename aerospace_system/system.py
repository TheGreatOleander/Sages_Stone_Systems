
from .schema import AerospaceSchema

class AerospaceSystem:
    def __init__(self):
        self.schema = AerospaceSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "aerospace", "status": "placeholder", "intent": intent}
