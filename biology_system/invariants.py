"""
biology_system.invariants
=========================

Invariant enforcement for biology_system.
"""

from .schema import BiologySystemSchema


def validate_schema(schema: BiologySystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, BiologySystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
