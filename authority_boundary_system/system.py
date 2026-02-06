"""
authority_boundary_system.system
================================

Canonical system definition for authority_boundary_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import AuthorityBoundarySystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "AuthorityBoundarySystem") -> None:
        ...


class AuthorityBoundarySystem:
    """
    Canonical base Authority Boundary system definition.
    """

    schema: AuthorityBoundarySystemSchema = AuthorityBoundarySystemSchema(
        name="authority_boundary_system",
        version="1.0",
        boundary_type="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
