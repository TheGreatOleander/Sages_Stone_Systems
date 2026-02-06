"""
art_system.schema
=================

Defines the structural schema for the art_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ArtSystemSchema:
    """
    Immutable art system schema definition.
    """

    name: str
    version: str = "1.0"
    medium: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("ArtSystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("ArtSystemSchema.version must be a non-empty string.")

        if not isinstance(self.medium, str) or not self.medium:
            raise ValueError("ArtSystemSchema.medium must be a non-empty string.")
