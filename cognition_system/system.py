from typing import FrozenSet

from .schema import CognitionSchema
from .invariants import invariant_modes_subset
from .lifecycle import CognitionLifecycle


class CognitionSystem:
    def __init__(self, schema: CognitionSchema) -> None:
        self._schema = schema
        self._active_modes: FrozenSet[str] = frozenset()
        self._lifecycle = CognitionLifecycle()

    @property
    def active_modes(self) -> FrozenSet[str]:
        return self._active_modes

    def set_modes(self, modes: FrozenSet[str]) -> None:
        if not invariant_modes_subset(modes, self._schema.allowed_modes):
            return
        self._active_modes = modes

    def has_mode(self, mode: str) -> bool:
        return mode in self._active_modes
