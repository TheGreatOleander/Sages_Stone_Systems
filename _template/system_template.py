"""
Sages_Stone — Canonical System Template

Purpose:
    This file defines the minimum shape required for a valid Sages_Stone System.
    Copy this template when creating a new system.

Rules:
    - Do not mutate global state
    - Do not import other systems directly
    - Interact ONLY through the provided context
    - Internal state is allowed, but must remain private
"""

from typing import Any


class BaseSystem:
    """
    BaseSystem is a conceptual contract.
    The runtime relies on the presence of these attributes and methods.
    """

    # REQUIRED: Human-readable domain identifier
    domain: str = "example_domain"

    def __init__(self) -> None:
        """
        Initialize private, internal system state here.

        This state:
        - Is owned entirely by this system
        - Must not be accessed by other systems
        - May evolve over time via tick()
        """
        self._initialized: bool = False
        self._internal_state: dict[str, Any] = {}

    def initialize(self, context: dict[str, Any]) -> None:
        """
        Called once by the runtime before execution begins.

        Use this to:
        - Validate required context keys
        - Seed internal state
        - Register intent or capabilities with context (if applicable)

        Do NOT:
        - Perform long-running work
        - Assume other systems have already run
        """
        self._initialized = True

    def tick(self, context: dict[str, Any]) -> None:
        """
        Called repeatedly by the runtime during execution.

        Use this to:
        - Read from context
        - Update internal state
        - Write results back into context

        This method should be:
        - Deterministic where possible
        - Side-effect free outside of context
        """
        if not self._initialized:
            raise RuntimeError(
                f"System '{self.domain}' ticked before initialization."
            )

        # --- Example behavior (replace freely) ---
        # value = context.get("input_value")
        # self._internal_state["last_seen"] = value
        # context["output_value"] = value
        pass
