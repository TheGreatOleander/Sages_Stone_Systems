from typing import FrozenSet

from .schema import ExecutionContextSchema
from .invariants import invariant_contexts_subset
from .lifecycle import ExecutionContextLifecycle


class ExecutionContextSystem:
    def __init__(self, schema: ExecutionContextSchema) -> None:
        self._schema = schema
        self._active_contexts: FrozenSet[str] = frozenset()
        self._lifecycle = ExecutionContextLifecycle()

    @property
    def active_contexts(self) -> FrozenSet[str]:
        return self._active_contexts

    def set_contexts(self, contexts: FrozenSet[str]) -> None:
        if not invariant_contexts_subset(
            contexts,
            self._schema.allowed_contexts,
        ):
            return
        self._active_contexts = contexts

    def has_context(self, context: str) -> bool:
        return context in self._active_contexts
