from dataclasses import dataclass
from typing import Dict, Any, List


SYSTEM_ID = "authority_boundary"


@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None


class AuthorityBoundarySystem:
    """
    Canonical Stone system.

    Enforces that an action's declared authority
    is within the system's allowed authority scope.

    This system does not interpret meaning.
    It only enforces boundary containment.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "ACTION_MUST_DECLARE_AUTHORITY",
            "SYSTEM_MUST_DECLARE_ALLOWED_AUTHORITY",
            "DECLARED_AUTHORITY_MUST_BE_WITHIN_SCOPE",
        ]

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        # Constraint 1: action must declare authority
        if "authority" not in action:
            return self._fail(
                "ACTION_MUST_DECLARE_AUTHORITY",
                "No authority declared for action."
            )

        declared = action["authority"]

        if not isinstance(declared, str) or not declared.strip():
            return self._fail(
                "ACTION_MUST_DECLARE_AUTHORITY",
                "Declared authority must be a non-empty string."
            )

        # Constraint 2: system context must declare allowed authority
        allowed = action.get("allowed_authority")

        if allowed is None:
            return self._fail(
                "SYSTEM_MUST_DECLARE_ALLOWED_AUTHORITY",
                "No allowed authority declared for system context."
            )

        if not isinstance(allowed, str) or not allowed.strip():
            return self._fail(
                "SYSTEM_MUST_DECLARE_ALLOWED_AUTHORITY",
                "Allowed authority must be a non-empty string."
            )

        # Constraint 3: declared authority must be within allowed scope
        if not self._within_scope(declared, allowed):
            return self._fail(
                "DECLARED_AUTHORITY_MUST_BE_WITHIN_SCOPE",
                f"Declared authority '{declared}' exceeds allowed scope '{allowed}'."
            )

        return SystemResult(ok=True)

    def _within_scope(self, declared: str, allowed: str) -> bool:
        """
        Symbolic containment check.
        Example:
            allowed  = "read"
            declared = "read:user_data"  -> OK
            declared = "write:user_data" -> FAIL
        """
        return declared.startswith(allowed)

    def _fail(self, rule: str, message: str) -> SystemResult:
        return SystemResult(
            ok=False,
            violation=ConstraintViolation(
                system=SYSTEM_ID,
                rule=rule,
                message=message
            )
        )
