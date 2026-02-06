from typing import FrozenSet

from .schema import CryptographySchema
from .invariants import invariant_primitives_subset
from .lifecycle import CryptographyLifecycle


class CryptographySystem:
    def __init__(self, schema: CryptographySchema) -> None:
        self._schema = schema
        self._active_primitives: FrozenSet[str] = frozenset()
        self._lifecycle = CryptographyLifecycle()

    @property
    def active_primitives(self) -> FrozenSet[str]:
        return self._active_primitives

    def set_primitives(self, primitives: FrozenSet[str]) -> None:
        if not invariant_primitives_subset(
            primitives,
            self._schema.allowed_primitives,
        ):
            return
        self._active_primitives = primitives

    def permits(self, primitive: str) -> bool:
        return primitive in self._active_primitives
