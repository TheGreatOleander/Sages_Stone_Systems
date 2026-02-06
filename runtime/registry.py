from sages_stone_runtime.runtime.errors import UnboundSystemError
from sages_stone_runtime.runtime.system_base import BaseSystem


class SystemRegistry:
    """
    Single source of truth for all bound runtime systems.
    """

    def __init__(self):
        self.systems: dict[str, BaseSystem] = {}

    def register(self, system: BaseSystem) -> None:
        if not system.name:
            raise UnboundSystemError(
                "System registration failed: system.name is required"
            )

        self.systems[system.name] = system

    def require(self, name: str) -> BaseSystem:
        if name not in self.systems:
            raise UnboundSystemError(f"Required system '{name}' not registered")

        return self.systems[name]
