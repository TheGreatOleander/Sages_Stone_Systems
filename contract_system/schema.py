from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class ContractSchema:
    allowed_contracts: FrozenSet[str]
