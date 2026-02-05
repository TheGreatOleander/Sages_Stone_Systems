
from .schema import SecuritySchema

class SecuritySystem:
    def __init__(self):
        self.schema = SecuritySchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "security", "status": "placeholder", "intent": intent}
