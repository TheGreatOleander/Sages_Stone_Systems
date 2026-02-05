
from .schema import GameSchema

class GameSystem:
    def __init__(self):
        self.schema = GameSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "game", "status": "placeholder", "intent": intent}
