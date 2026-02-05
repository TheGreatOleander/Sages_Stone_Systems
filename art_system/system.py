
from .schema import ArtSchema

class ArtSystem:
    def __init__(self):
        self.schema = ArtSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "art", "status": "placeholder", "intent": intent}
