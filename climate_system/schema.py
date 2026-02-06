from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class ClimateSchema:
    allowed_conditions: FrozenSet[str]
