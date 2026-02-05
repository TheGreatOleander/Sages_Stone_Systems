
from .schema import InformationSchema

class InformationSystem:
    def __init__(self):
        self.schema = InformationSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "information", "status": "placeholder", "intent": intent}
