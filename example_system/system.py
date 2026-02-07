"""
Example System Definition

Canonical reference system binding lifecycle and schema.
"""

from .lifecycle import ExampleSystemLifecycle
from .schema import EXAMPLE_SCHEMA


class ExampleSystem:
    """
    Example canonical system.

    This system exists for demonstration purposes only.
    """

    def __init__(self):
        self.lifecycle = ExampleSystemLifecycle()
        self.schema = EXAMPLE_SCHEMA

    def initialize(self) -> bool:
        return self.lifecycle.initialize()

    def validate(self) -> bool:
        return self.lifecycle.validate()

    def shutdown(self) -> bool:
        return self.lifecycle.shutdown()
