"""
biology_system.schema
=====================

Defines the structural schema for the biology_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BiologySystemSchema:
    """
    Immutable biology system schema definition.
    """

    name: str
    version: str = "1.0"
    biological_domain: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("BiologySystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("BiologySystemSchema.version must be a non-empty string.")

        if not isinstance(self.biological_domain, str) or not self.biological_domain:
            raise ValueError(
                "BiologySystemSchema.biological_domain must be a non-empty string."
            )
