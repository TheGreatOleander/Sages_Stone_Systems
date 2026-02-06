"""
alignment_system.schema
=======================

Defines the structural schema for the alignment_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AlignmentSystemSchema:
    """
    Immutable alignment system schema definition.
    """

    name: str
    version: str = "1.0"
    alignment_domain: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("AlignmentSystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("AlignmentSystemSchema.version must be a non-empty string.")

        if not isinstance(self.alignment_domain, str) or not self.alignment_domain:
            raise ValueError(
                "AlignmentSystemSchema.alignment_domain must be a non-empty string."
            )
