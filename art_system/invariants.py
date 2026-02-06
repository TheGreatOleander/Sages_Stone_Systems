"""
art_system.invariants
=====================

Invariant enforcement for art_system.
"""

from .schema import ArtSystemSchema


def validate_schema(schema: ArtSystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, ArtSystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
