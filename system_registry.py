"""
System Registry

Provides discovery and registration of all runtime systems.
This prevents the runner from hardcoding imports and allows
the architecture to scale safely.
"""

from typing import Dict, Type, Any


class SystemRegistry:
    def __init__(self):
        self._systems: Dict[str, Any] = {}

    def register(self, name: str, system: Any) -> None:
        if name in self._systems:
            raise ValueError(f"System already registered: {name}")
        self._systems[name] = system

    def get(self, name: str) -> Any:
        if name not in self._systems:
            raise KeyError(f"Unknown system: {name}")
        return self._systems[name]

    def list_systems(self):
        return list(self._systems.keys())


registry = SystemRegistry()
