from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ResolvedIntent:
    chosen: str
    deferred: List[str]
