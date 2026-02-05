"""
Runtime System Interface

Defines the base contract all systems must implement.
This ensures consistent lifecycle behavior across the runtime.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class RuntimeSystem(ABC):
    """
    Base class for all runtime systems.
    """

    name: str = "unnamed_system"
    version: str = "0.1"

    def initialize(self) -> None:
        """
        Optional setup logic.
        Override if needed.
        """
        pass

    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> None:
        """
        Main execution entrypoint.
        Must be implemented by all systems.
        """
        raise NotImplementedError()

    def shutdown(self) -> None:
        """
        Optional cleanup logic.
        """
        pass
