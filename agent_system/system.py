
from .schema import AgentSchema

class AgentSystem:
    def __init__(self):
        self.schema = AgentSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "agent", "status": "placeholder", "intent": intent}
