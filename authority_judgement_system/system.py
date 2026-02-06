"""
authority_judgment_system.system
================================

Canonical system definition for authority_judgment_system.
"""

from __future__ import annotations

from typing import Any, Protocol

from .schema import AuthorityJudgmentSystemSchema
from .invariants import validate_schema


class RegistryProtocol(Protocol):
    def register(self, system: "AuthorityJudgmentSystem") -> None:
        ...


class AuthorityJudgmentSystem:
    """
    Canonical base Authority Judgment system definition.
    """

    schema: AuthorityJudgmentSystemSchema = AuthorityJudgmentSystemSchema(
        name="authority_judgment_system",
        version="1.0",
        authority_domain="generic",
    )

    def __init__(self) -> None:
        validate_schema(self.schema)

    def register(self, registry: RegistryProtocol) -> None:
        registry.register(self)

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute()."
        )
