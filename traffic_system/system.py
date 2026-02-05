
from .schema import TrafficSchema

class TrafficSystem:
    def __init__(self):
        self.schema = TrafficSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "traffic", "status": "placeholder", "intent": intent}
