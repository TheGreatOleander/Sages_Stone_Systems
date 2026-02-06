"""
agent_system.system
===================

Canonical system definition for agent_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import SystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "System") -> None:
        ...


class System:
    """
    Canonical base System definition.
    """

    schema: SystemSchema = SystemSchema(name="agent_system")

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
