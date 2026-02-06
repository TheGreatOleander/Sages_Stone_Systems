"""
agent_system.schema
===================

Defines the structural schema for the agent_system.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SystemSchema:
    """
    Immutable system schema definition.
    """

    name: str
    version: str = "1.0"

    def validate(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("SystemSchema.name must be a non-empty string.")

        if not isinstance(self.version, str) or not self.version:
            raise ValueError("SystemSchema.version must be a non-empty string.")
