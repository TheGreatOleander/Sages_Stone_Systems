from typing import FrozenSet

from .schema import CapabilityBoundarySchema
from .invariants import invariant_capabilities_subset
from .lifecycle import CapabilityBoundaryLifecycle


class CapabilityBoundarySystem:
    def __init__(self, schema: CapabilityBoundarySchema) -> None:
        self._schema = schema
        self._active: FrozenSet[str] = frozenset()
        self._lifecycle = CapabilityBoundaryLifecycle()

    @property
    def active_capabilities(self) -> FrozenSet[str]:
        return self._active

    def set_active_capabilities(self, capabilities: FrozenSet[str]) -> None:
        if not invariant_capabilities_subset(capabilities, self._schema.allowed_capabilities):
            return
        self._active = capabilities

    def permits(self, capability: str) -> bool:
        return capability in self._active
