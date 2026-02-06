"""
alignment_system.system
=======================

Canonical system definition for alignment_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import AlignmentSystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "AlignmentSystem") -> None:
        ...


class AlignmentSystem:
    """
    Canonical base Alignment system definition.
    """

    schema: AlignmentSystemSchema = AlignmentSystemSchema(
        name="alignment_system",
        version="1.0",
        alignment_domain="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
