
from .schema import TimeSchema

class TimeSystem:
    def __init__(self):
        self.schema = TimeSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "time", "status": "placeholder", "intent": intent}
