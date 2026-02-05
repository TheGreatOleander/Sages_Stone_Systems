
from .schema import SocialSchema

class SocialSystem:
    def __init__(self):
        self.schema = SocialSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "social", "status": "placeholder", "intent": intent}
