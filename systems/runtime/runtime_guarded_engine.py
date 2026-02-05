"""
Guarded runtime engine enforcing minimal preconditions.
"""

class GuardedRuntimeEngine:
    REQUIRED_KEYS = {"system", "action"}

    def validate(self, action: dict):
        if not isinstance(action, dict):
            raise TypeError("Action must be a dict")
        missing = self.REQUIRED_KEYS - set(action.keys())
        if missing:
            raise ValueError(f"Missing required keys: {missing}")

    def execute(self, action: dict):
        system = action["system"]
        verb = action["action"]
        if not hasattr(system, verb):
            raise ValueError(f"System does not support action '{verb}'")
        fn = getattr(system, verb)
        return fn(action.get("params", {}))
