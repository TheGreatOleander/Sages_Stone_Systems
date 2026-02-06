"""
ai_system.schema
================

Defines the structural schema for the ai_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AISystemSchema:
    """
    Immutable AI system schema definition.
    """

    name: str
    version: str = "1.0"
    capability: str = "generic"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("AISystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("AISystemSchema.version must be a non-empty string.")

        if not isinstance(self.capability, str) or not self.capability:
            raise ValueError("AISystemSchema.capability must be a non-empty string.")
