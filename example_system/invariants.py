"""
Example System Invariants

Illustrative invariants demonstrating invariant structure.
"""


class InvariantViolation(Exception):
    """Raised when an example invariant is violated."""


def example_invariant():
    """
    Example invariant.

    Always passes by design.
    """
    return True


def example_invariants():
    """
    Return all invariants required for the Example System.
    """
    return [
        example_invariant,
    ]
