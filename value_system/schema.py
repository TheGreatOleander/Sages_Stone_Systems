from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class ValueProfile:
    weights: Dict[str, float]
