"""
authority_boundary_system.invariants
====================================

Invariant enforcement for authority_boundary_system.
"""

from .schema import AuthorityBoundarySystemSchema


def validate_schema(schema: AuthorityBoundarySystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, AuthorityBoundarySystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
