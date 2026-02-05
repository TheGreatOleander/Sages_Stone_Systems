
from .schema import WeatherSchema

class WeatherSystem:
    def __init__(self):
        self.schema = WeatherSchema()

    def evaluate(self, intent: dict) -> dict:
        return {"domain": "weather", "status": "placeholder", "intent": intent}
