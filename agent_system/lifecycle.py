"""
agent_system.lifecycle
======================

Defines lifecycle contract for agent_system.
"""

from typing import Protocol


class Lifecycle(Protocol):
    """
    Lifecycle contract.

    Implementations must define deterministic, side-effect
    controlled lifecycle transitions.
    """

    def initialize(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def shutdown(self) -> None:
        ...
