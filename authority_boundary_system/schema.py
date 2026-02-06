"""
authority_boundary_system.schema
================================

Defines the structural schema for the authority_boundary_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityBoundarySystemSchema:
    """
    Immutable authority boundary system schema definition.
    """

    name: str
    version: str = "1.0"
    boundary_type: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("AuthorityBoundarySystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("AuthorityBoundarySystemSchema.version must be a non-empty string.")

        if not isinstance(self.boundary_type, str) or not self.boundary_type:
            raise ValueError(
                "AuthorityBoundarySystemSchema.boundary_type must be a non-empty string."
            )
