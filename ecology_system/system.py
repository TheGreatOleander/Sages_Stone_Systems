from typing import FrozenSet

from .schema import EcologySchema
from .invariants import invariant_factors_subset
from .lifecycle import EcologyLifecycle


class EcologySystem:
    def __init__(self, schema: EcologySchema) -> None:
        self._schema = schema
        self._active_factors: FrozenSet[str] = frozenset()
        self._lifecycle = EcologyLifecycle()

    @property
    def active_factors(self) -> FrozenSet[str]:
        return self._active_factors

    def set_factors(self, factors: FrozenSet[str]) -> None:
        if not invariant_factors_subset(
            factors,
            self._schema.allowed_factors,
        ):
            return
        self._active_factors = factors

    def has_factor(self, factor: str) -> bool:
        return factor in self._active_factors
