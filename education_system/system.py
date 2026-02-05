
from .schema import EducationSchema

class EducationSystem:
    def __init__(self):
        self.schema = EducationSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "education", "status": "placeholder", "intent": intent}
