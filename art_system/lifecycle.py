"""
art_system.lifecycle
====================

Defines lifecycle contract for art_system.
"""

from typing import Protocol


class ArtLifecycle(Protocol):
    """
    Lifecycle contract for art systems.

    Implementations must ensure deterministic transitions.
    """

    def initialize(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def shutdown(self) -> None:
        ...
