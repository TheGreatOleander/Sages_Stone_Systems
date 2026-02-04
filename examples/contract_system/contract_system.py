
from dataclasses import dataclass
from typing import Dict, Any, List

SYSTEM_ID = "contract_system"

@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str

@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None

class ContractSystem:
    """
    Non-physics example enforcing contractual constraints.
    Demonstrates the same pattern as QuantumSystem.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "CONTRACT_MUST_DECLARE_PARTIES",
            "CONTRACT_MUST_DECLARE_TERMS",
            "SIGNATURES_REQUIRED_FOR_VALIDITY",
            "EXECUTION_REQUIRES_VALID_CONTRACT",
            "NO_RETROACTIVE_MODIFICATION",
        ]

    def evaluate(self, state: Dict[str, Any]) -> SystemResult:
        # Constraint 1: parties
        if not state.get("parties"):
            return self._fail(
                "CONTRACT_MUST_DECLARE_PARTIES",
                "No parties declared in contract."
            )

        # Constraint 2: terms
        if not state.get("terms"):
            return self._fail(
                "CONTRACT_MUST_DECLARE_TERMS",
                "No contractual terms declared."
            )

        # Constraint 3: signatures
        if state.get("executed", False):
            if not state.get("signatures"):
                return self._fail(
                    "SIGNATURES_REQUIRED_FOR_VALIDITY",
                    "Contract executed without signatures."
                )

        # Constraint 4: execution validity
        if state.get("executed", False) and not state.get("valid", True):
            return self._fail(
                "EXECUTION_REQUIRES_VALID_CONTRACT",
                "Invalid contract cannot be executed."
            )

        # Constraint 5: retroactive modification
        if state.get("modified_after_execution", False):
            return self._fail(
                "NO_RETROACTIVE_MODIFICATION",
                "Contract modified after execution."
            )

        return SystemResult(ok=True)

    def _fail(self, rule: str, message: str) -> SystemResult:
        return SystemResult(
            ok=False,
            violation=ConstraintViolation(SYSTEM_ID, rule, message)
        )
