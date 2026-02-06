"""
biology_system.lifecycle
========================

Defines lifecycle contract for biology_system.
"""

from typing import Protocol


class BiologyLifecycle(Protocol):
    """
    Lifecycle contract for biology systems.

    Implementations must ensure deterministic,
    reproducible transitions.
    """

    def initialize(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def shutdown(self) -> None:
        ...
