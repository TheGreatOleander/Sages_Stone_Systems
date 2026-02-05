
from .schema import MemorySchema

class MemorySystem:
    def __init__(self):
        self.schema = MemorySchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "memory", "status": "placeholder", "intent": intent}
