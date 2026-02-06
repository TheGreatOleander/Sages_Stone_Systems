from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class CryptographySchema:
    allowed_primitives: FrozenSet[str]
