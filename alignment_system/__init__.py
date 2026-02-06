"""
alignment_system
================

Canonical alignment system package.
"""

from .schema import AlignmentSystemSchema
from .system import AlignmentSystem
from .lifecycle import AlignmentLifecycle
from .invariants import validate_schema

__all__ = [
    "AlignmentSystemSchema",
    "AlignmentSystem",
    "AlignmentLifecycle",
    "validate_schema",
]
