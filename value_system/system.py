from .schema import ValueProfile

class ValueSystem:
    name = "value_system"

    def default_profile(self) -> ValueProfile:
        return ValueProfile(weights={})
