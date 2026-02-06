"""
agent_system
============

Canonical agent system package.
"""

from .schema import SystemSchema
from .system import System
from .lifecycle import Lifecycle
from .invariants import validate_schema

__all__ = [
    "SystemSchema",
    "System",
    "Lifecycle",
    "validate_schema",
]
