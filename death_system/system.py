from typing import FrozenSet

from .schema import DeathSchema
from .invariants import invariant_states_subset
from .lifecycle import DeathLifecycle


class DeathSystem:
    def __init__(self, schema: DeathSchema) -> None:
        self._schema = schema
        self._active_states: FrozenSet[str] = frozenset()
        self._lifecycle = DeathLifecycle()

    @property
    def active_states(self) -> FrozenSet[str]:
        return self._active_states

    def set_states(self, states: FrozenSet[str]) -> None:
        if not invariant_states_subset(
            states,
            self._schema.allowed_states,
        ):
            return
        self._active_states = states

    def is_state(self, state: str) -> bool:
        return state in self._active_states
