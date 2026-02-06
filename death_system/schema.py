from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class DeathSchema:
    allowed_states: FrozenSet[str]
