
from runtime.registry import SystemRegistry

class RuntimeEngine:
    def __init__(self):
        self.registry = SystemRegistry()

    def boot(self):
        print("[Runtime] Booting systems...")
        for name, system in self.registry.systems.items():
            if hasattr(system, "initialize"):
                system.initialize()

    def validate(self):
        print("[Runtime] Validating systems...")
        for name, system in self.registry.systems.items():
            if hasattr(system, "validate"):
                system.validate()

    def shutdown(self):
        print("[Runtime] Shutting down systems...")
        for name, system in self.registry.systems.items():
            if hasattr(system, "shutdown"):
                system.shutdown()
