"""
art_system.system
=================

Canonical system definition for art_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import ArtSystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "ArtSystem") -> None:
        ...


class ArtSystem:
    """
    Canonical base Art system definition.
    """

    schema: ArtSystemSchema = ArtSystemSchema(
        name="art_system",
        version="1.0",
        medium="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
