from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class ExecutionContextSchema:
    allowed_contexts: FrozenSet[str]
