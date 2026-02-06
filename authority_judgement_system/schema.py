"""
authority_judgment_system.schema
================================

Defines the structural schema for the authority_judgment_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityJudgmentSystemSchema:
    """
    Immutable authority judgment system schema definition.
    """

    name: str
    version: str = "1.0"
    authority_domain: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("AuthorityJudgmentSystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("AuthorityJudgmentSystemSchema.version must be a non-empty string.")

        if not isinstance(self.authority_domain, str) or not self.authority_domain:
            raise ValueError(
                "AuthorityJudgmentSystemSchema.authority_domain must be a non-empty string."
            )
