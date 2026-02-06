"""
ai_system
=========

Canonical AI system package.
"""

from .schema import AISystemSchema
from .system import AISystem
from .lifecycle import AILifecycle
from .invariants import validate_schema

__all__ = [
    "AISystemSchema",
    "AISystem",
    "AILifecycle",
    "validate_schema",
]
