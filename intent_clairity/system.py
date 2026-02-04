from dataclasses import dataclass
from typing import Dict, Any, List


SYSTEM_ID = "intent_clarity"


@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None


class IntentClaritySystem:
    """
    Canonical Stone system.

    Enforces that an action declares a clear, singular intent.
    This system does not interpret, validate, or repair intent.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "ACTION_MUST_DECLARE_INTENT",
            "INTENT_MUST_BE_SINGULAR",
            "INTENT_MUST_BE_ATOMIC",
        ]

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        # Constraint 1: intent must exist
        if "intent" not in action:
            return self._fail(
                "ACTION_MUST_DECLARE_INTENT",
                "No intent declared for action."
            )

        intent = action["intent"]

        # Constraint 2: intent must be singular
        if isinstance(intent, (list, tuple, set)):
            return self._fail(
                "INTENT_MUST_BE_SINGULAR",
                f"Multiple intents declared: {intent}"
            )

        # Constraint 3: intent must be atomic
        if not isinstance(intent, str):
            return self._fail(
                "INTENT_MUST_BE_ATOMIC",
                f"Intent must be a string, got {type(intent).__name__}."
            )

        if not intent.strip():
            return self._fail(
                "INTENT_MUST_BE_ATOMIC",
                "Intent string is empty."
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
