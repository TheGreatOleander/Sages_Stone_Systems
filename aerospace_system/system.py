# path: Sages_Stone_Systems/aerospace_system/aerospace_system.py

"""
Aerospace System – Canonical Location
------------------------------------
Placed in its own system directory to match
the pattern used by all peer systems.

This module represents a judgment-only domain
with strict non-execution guarantees.
"""

from dataclasses import dataclass
from typing import Dict, Any, Literal


@dataclass(frozen=True)
class AerospaceJudgement:
    status: Literal["VALID", "INVALID"]
    reason: str
    data: Dict[str, Any]


class AerospaceSystem:
    """
    System Invariants
    -----------------
    - READ ONLY domain
    - No side effects
    - No external calls
    - Deterministic evaluation
    """

    @staticmethod
    def evaluate(payload: Dict[str, Any]) -> AerospaceJudgement:
        if not isinstance(payload, dict):
            return AerospaceJudgement(
                status="INVALID",
                reason="SchemaViolation: payload must be dict",
                data={},
            )

        required = {"altitude", "velocity", "mass"}
        missing = required - payload.keys()

        if missing:
            return AerospaceJudgement(
                status="INVALID",
                reason=f"SchemaViolation: missing {sorted(missing)}",
                data=payload,
            )

        if payload.get("altitude", 0) < 0:
            return AerospaceJudgement(
                status="INVALID",
                reason="InvariantBreach: altitude < 0",
                data=payload,
            )

        if payload.get("mass", 0) <= 0:
            return AerospaceJudgement(
                status="INVALID",
                reason="InvariantBreach: mass <= 0",
                data=payload,
            )

        return AerospaceJudgement(
            status="VALID",
            reason="Accepted within aerospace domain constraints",
            data=payload,
        )
