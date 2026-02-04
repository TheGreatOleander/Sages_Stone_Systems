from dataclasses import dataclass
from typing import Dict, Any, List


SYSTEM_ID = "data_boundary"


@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str


@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None


class DataBoundarySystem:
    """
    Canonical Stone system.

    Enforces that an action explicitly declares
    which data it intends to access.

    This system does not classify, validate, or interpret data.
    It only enforces declaration and boundary shape.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "ACTION_MUST_DECLARE_DATA_ACCESS",
            "DATA_ACCESS_MUST_BE_EXPLICIT",
            "DATA_ACCESS_MUST_BE_FINITE",
        ]

    def evaluate(self, action: Dict[str, Any]) -> SystemResult:
        # Constraint 1: data access must be declared
        if "data_access" not in action:
            return self._fail(
                "ACTION_MUST_DECLARE_DATA_ACCESS",
                "No data access declared for action."
            )

        data_access = action["data_access"]

        # Constraint 2: data access must be explicit
        if data_access is None:
            return self._fail(
                "DATA_ACCESS_MUST_BE_EXPLICIT",
                "Data access declaration is null."
            )

        # Constraint 3: data access must be finite
        if not isinstance(data_access, list):
            return self._fail(
                "DATA_ACCESS_MUST_BE_FINITE",
                f"Data access must be a list, got {type(data_access).__name__}."
            )

        if len(data_access) == 0:
            return self._fail(
                "DATA_ACCESS_MUST_BE_FINITE",
                "Data access list is empty."
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
