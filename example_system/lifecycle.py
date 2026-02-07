"""
Example System Lifecycle

Demonstrates a canonical lifecycle implementation.
"""

from .invariants import example_invariants


class ExampleSystemLifecycle:
    """
    Lifecycle for the Example System.

    This lifecycle is intentionally simple.
    """

    def initialize(self) -> bool:
        return True

    def validate(self) -> bool:
        for invariant in example_invariants():
            invariant()
        return True

    def shutdown(self) -> bool:
        return True
