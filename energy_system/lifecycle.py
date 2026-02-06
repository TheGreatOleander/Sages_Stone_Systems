"""
Energy System Lifecycle
======================
Optional lifecycle hooks for the Energy system.
"""

from typing import Optional, Dict, Any


class EnergyLifecycle:
    """
    Lifecycle hooks for the Energy system.
    """

    @staticmethod
    def on_initialize(config: Optional[Dict[str, Any]] = None) -> None:
        return None

    @staticmethod
    def on_activate(context: Optional[Dict[str, Any]] = None) -> None:
        return None

    @staticmethod
    def on_deactivate(context: Optional[Dict[str, Any]] = None) -> None:
        return None

    @staticmethod
    def on_shutdown() -> None:
        return None
