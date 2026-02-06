"""
ai_system.system
================

Canonical system definition for ai_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import AISystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "AISystem") -> None:
        ...


class AISystem:
    """
    Canonical base AI system definition.
    """

    schema: AISystemSchema = AISystemSchema(
        name="ai_system",
        version="1.0",
        capability="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
