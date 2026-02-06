from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class CognitionSchema:
    allowed_modes: FrozenSet[str]
