from .schema import ResolvedIntent

class IntentResolutionSystem:
    name = "intent_resolution_system"

    def resolve(self, intents: list[str]) -> ResolvedIntent:
        if not intents:
            raise ValueError("No intents provided")
        return ResolvedIntent(chosen=intents[0], deferred=intents[1:])
