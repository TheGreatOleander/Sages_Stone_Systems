from dataclasses import dataclass
from typing import Dict, Any, List


SYSTEM_ID = "null_constraint"


@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None


class NullConstraintSystem:
    """
    Builder demo system.

    This system exists solely to demonstrate:
    - identity
    - constraint declaration
    - deterministic evaluation
    - fail-fast behavior
    - immutable results

    It enforces exactly one rule:
    The action must not be empty.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "ACTION_MUST_NOT_BE_EMPTY",
        ]

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        if not action:
            return self._fail(
                "ACTION_MUST_NOT_BE_EMPTY",
                "Action payload is empty."
            )

        return SystemResult(ok=True)

    def _fail(self, rule: str, message: str) -> SystemResult:
        return SystemResult(
            ok=False,
            violation=ConstraintViolation(
                system=SYSTEM_ID,
                rule=rule,
                message=message
            )
        )
