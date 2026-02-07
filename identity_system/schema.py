from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class IdentitySchema:
    allowed_identities: FrozenSet[str]
