from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class CapabilityBoundarySchema:
    allowed_capabilities: FrozenSet[str]
