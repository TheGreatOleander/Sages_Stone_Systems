from typing import FrozenSet

from .schema import IdentitySchema
from .invariants import invariant_identities_subset
from .lifecycle import IdentityLifecycle


class IdentitySystem:
    def __init__(self, schema: IdentitySchema) -> None:
        self._schema = schema
        self._active_identities: FrozenSet[str] = frozenset()
        self._lifecycle = IdentityLifecycle()

    @property
    def active_identities(self) -> FrozenSet[str]:
        return self._active_identities

    def set_identities(self, identities: FrozenSet[str]) -> None:
        if not invariant_identities_subset(
            identities,
            self._schema.allowed_identities,
        ):
            return
        self._active_identities = identities

    def has_identity(self, identity: str) -> bool:
        return identity in self._active_identities
