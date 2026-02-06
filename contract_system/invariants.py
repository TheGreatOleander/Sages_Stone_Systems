from typing import FrozenSet


def invariant_contracts_subset(
    active: FrozenSet[str],
    allowed: FrozenSet[str],
) -> bool:
    return active.issubset(allowed)
