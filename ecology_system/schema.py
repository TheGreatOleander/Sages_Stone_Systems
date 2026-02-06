from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class EcologySchema:
    allowed_factors: FrozenSet[str]
