"""
art_system
==========

Canonical art system package.
"""

from .schema import ArtSystemSchema
from .system import ArtSystem
from .lifecycle import ArtLifecycle
from .invariants import validate_schema

__all__ = [
    "ArtSystemSchema",
    "ArtSystem",
    "ArtLifecycle",
    "validate_schema",
]
