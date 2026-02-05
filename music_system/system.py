
from .schema import MusicSchema

class MusicSystem:
    def __init__(self):
        self.schema = MusicSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "music", "status": "placeholder", "intent": intent}
