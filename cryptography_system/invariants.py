from typing import FrozenSet


def invariant_primitives_subset(
    active: FrozenSet[str],
    allowed: FrozenSet[str],
) -> bool:
    return active.issubset(allowed)
