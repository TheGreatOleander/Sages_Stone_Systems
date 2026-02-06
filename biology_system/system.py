"""
biology_system.system
=====================

Canonical system definition for biology_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import BiologySystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "BiologySystem") -> None:
        ...


class BiologySystem:
    """
    Canonical base Biology system definition.
    """

    schema: BiologySystemSchema = BiologySystemSchema(
        name="biology_system",
        version="1.0",
        biological_domain="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
