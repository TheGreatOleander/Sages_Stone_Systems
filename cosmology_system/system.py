from typing import FrozenSet

from .schema import CosmologySchema
from .invariants import invariant_axioms_subset
from .lifecycle import CosmologyLifecycle


class CosmologySystem:
    def __init__(self, schema: CosmologySchema) -> None:
        self._schema = schema
        self._active_axioms: FrozenSet[str] = frozenset()
        self._lifecycle = CosmologyLifecycle()

    @property
    def active_axioms(self) -> FrozenSet[str]:
        return self._active_axioms

    def set_axioms(self, axioms: FrozenSet[str]) -> None:
        if not invariant_axioms_subset(
            axioms,
            self._schema.allowed_axioms,
        ):
            return
        self._active_axioms = axioms

    def has_axiom(self, axiom: str) -> bool:
        return axiom in self._active_axioms
