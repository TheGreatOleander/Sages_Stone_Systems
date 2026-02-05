
from .schema import SpaceflightSchema

class SpaceflightSystem:
    def __init__(self):
        self.schema = SpaceflightSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "spaceflight", "status": "placeholder", "intent": intent}
