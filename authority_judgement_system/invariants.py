"""
authority_judgment_system.invariants
====================================

Invariant enforcement for authority_judgment_system.
"""

from .schema import AuthorityJudgmentSystemSchema


def validate_schema(schema: AuthorityJudgmentSystemSchema) -> None:
    """
    Enforces schema-level invariants.
    """

    if not isinstance(schema, AuthorityJudgmentSystemSchema):
        raise TypeError("Invalid schema type.")

    schema.validate()
