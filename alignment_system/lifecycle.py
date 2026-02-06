"""
alignment_system.lifecycle
==========================

Defines lifecycle contract for alignment_system.
"""

from typing import Protocol


class AlignmentLifecycle(Protocol):
    """
    Lifecycle contract for alignment systems.

    Implementations must enforce deterministic, auditable transitions.
    """

    def initialize(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def shutdown(self) -> None:
        ...
