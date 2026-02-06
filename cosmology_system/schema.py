from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class CosmologySchema:
    allowed_axioms: FrozenSet[str]
