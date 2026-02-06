from typing import FrozenSet

from .schema import ClimateSchema
from .invariants import invariant_conditions_subset
from .lifecycle import ClimateLifecycle


class ClimateSystem:
    def __init__(self, schema: ClimateSchema) -> None:
        self._schema = schema
        self._active_conditions: FrozenSet[str] = frozenset()
        self._lifecycle = ClimateLifecycle()

    @property
    def active_conditions(self) -> FrozenSet[str]:
        return self._active_conditions

    def set_conditions(self, conditions: FrozenSet[str]) -> None:
        if not invariant_conditions_subset(
            conditions,
            self._schema.allowed_conditions,
        ):
            return
        self._active_conditions = conditions

    def has_condition(self, condition: str) -> bool:
        return condition in self._active_conditions
