"""
System Runner

Orchestrates evaluation across multiple Canonical Stone systems.

Responsibilities:
- Maintain ordered list of systems
- Evaluate an action against each system
- Short-circuit on first violation
- Return unified result

This file does NOT:
- Interpret meaning
- Execute actions
- Modify systems
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional


# ---------------------------------------------------------------------
# Canonical Result Types (mirrors existing systems)
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: Optional[ConstraintViolation] = None


# ---------------------------------------------------------------------
# System Interface (implicit, not enforced)
# ---------------------------------------------------------------------
# A system is expected to expose:
#   - get_identity() -> str
#   - evaluate(action: Dict[str, Any]) -> SystemResult
#
# This runner deliberately does NOT require inheritance.
# Duck typing keeps stones independent.
# ---------------------------------------------------------------------


class SystemRunner:
    """
    Runs an action through an ordered chain of systems.
    """

    def __init__(self, systems: List[Any]):
        self._systems = systems

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        """
        Evaluate an action against all systems.

        Stops on first failure.
        """

        for system in self._systems:
            result = system.evaluate(action)

            if not result.ok:
                return result

        return SystemResult(ok=True)


# ---------------------------------------------------------------------
# Example Usage (non-executing reference)
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Example only — safe to delete

    from authority_boundary.system import AuthorityBoundarySystem

    runner = SystemRunner(
        systems=[
            AuthorityBoundarySystem(),
            # Other systems plug in here
        ]
    )

    action = {
        "authority": "read:user_data",
        "allowed_authority": "read"
    }

    result = runner.evaluate(action)

    if result.ok:
        print("Action passed all constraints.")
    else:
        print(
            f"Violation in {result.violation.system}: "
            f"{result.violation.rule} — {result.violation.message}"
        )
