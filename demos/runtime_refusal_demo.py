from sages_stone_runtime.runtime.engine import RuntimeEngine
from sages_stone_runtime.runtime.system_base import BaseSystem


class DemoSystem(BaseSystem):
    name = "demo_system"

    def validate(self) -> bool:
        return False  # Intentional hard failure


engine = RuntimeEngine()
engine.registry.register(DemoSystem())

engine.boot()
engine.validate()  # MUST raise ContractViolation
