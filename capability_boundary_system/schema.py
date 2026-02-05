from dataclasses import dataclass
from typing import Set

@dataclass(frozen=True)
class CapabilityBoundary:
    prohibited_capabilities: Set[str]
