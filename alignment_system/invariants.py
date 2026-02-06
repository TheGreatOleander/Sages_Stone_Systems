"""
alignment_system.invariants
===========================

Invariant enforcement for alignment_system.
"""

from .schema import AlignmentSystemSchema


def validate_schema(schema: AlignmentSystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, AlignmentSystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
