"""
ai_system.invariants
====================

Invariant enforcement for ai_system.
"""

from .schema import AISystemSchema


def validate_schema(schema: AISystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, AISystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
