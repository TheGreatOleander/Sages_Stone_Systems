"""
ai_system.lifecycle
===================

Defines lifecycle contract for ai_system.
"""

from typing import Protocol


class AILifecycle(Protocol):
    """
    Lifecycle contract for AI systems.

    Implementations must ensure deterministic transitions.
    """

    def initialize(self) -> None:
        ...

    def validate(self) -> None:
        ...

    def shutdown(self) -> None:
        ...
