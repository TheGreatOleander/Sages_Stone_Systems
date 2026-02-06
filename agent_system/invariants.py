"""
agent_system.invariants
=======================

Invariant enforcement for agent_system.
"""

from .schema import SystemSchema


def validate_schema(schema: SystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, SystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
