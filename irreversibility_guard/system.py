from dataclasses import dataclass
from typing import Dict, Any, List


SYSTEM_ID = "irreversibility_guard"


@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None


class IrreversibilityGuardSystem:
    """
    Canonical Stone system.

    Enforces explicit declaration and acknowledgment
    of irreversible actions.

    This system does not judge consequences.
    It only enforces awareness.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "ACTION_MUST_DECLARE_REVERSIBILITY",
            "IRREVERSIBLE_ACTION_MUST_BE_ACKNOWLEDGED",
        ]

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        # Constraint 1: reversibility must be declared
        if "reversible" not in action:
            return self._fail(
                "ACTION_MUST_DECLARE_REVERSIBILITY",
                "Reversibility not declared for action."
            )

        reversible = action["reversible"]

        if not isinstance(reversible, bool):
            return self._fail(
                "ACTION_MUST_DECLARE_REVERSIBILITY",
                f"Reversible flag must be boolean, got {type(reversible).__name__}."
            )

        # Constraint 2: irreversible actions must be acknowledged
        if reversible is False:
            acknowledged = action.get("acknowledge_irreversibility")

            if acknowledged is not True:
                return self._fail(
                    "IRREVERSIBLE_ACTION_MUST_BE_ACKNOWLEDGED",
                    "Irreversible action not explicitly acknowledged."
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
