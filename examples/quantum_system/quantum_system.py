
from dataclasses import dataclass
from typing import Dict, Any, List
import numpy as np

SYSTEM_ID = "quantum_system"

@dataclass(frozen=True)
class ConstraintViolation:
    system: str
    rule: str
    message: str

@dataclass(frozen=True)
class SystemResult:
    ok: bool
    violation: ConstraintViolation | None = None

class QuantumSystem:
    """
    Canonical constraint system enforcing quantum-mechanical laws.
    """

    def get_identity(self) -> str:
        return SYSTEM_ID

    def get_constraints(self) -> List[str]:
        return [
            "STATE_MUST_DECLARE_WAVEFUNCTION",
            "WAVEFUNCTION_MUST_BE_NORMALIZED",
            "EVOLUTION_OPERATOR_MUST_BE_UNITARY",
            "UNCERTAINTY_PRINCIPLE_MUST_HOLD",
            "NO_CLONING_THEOREM_MUST_HOLD",
            "MEASUREMENT_MUST_COLLAPSE_SUPERPOSITION",
        ]

    def evaluate(self, state: Dict[str, Any]) -> SystemResult:
        if "wavefunction" not in state:
            return self._fail("STATE_MUST_DECLARE_WAVEFUNCTION",
                              "No wavefunction declared.")

        psi = np.array(state["wavefunction"])
        prob = np.sum(np.abs(psi) ** 2)

        if not np.isclose(prob, 1.0):
            return self._fail("WAVEFUNCTION_MUST_BE_NORMALIZED",
                              f"∑|ψ|² = {prob} ≠ 1")

        if "evolution_operator" in state:
            U = np.array(state["evolution_operator"])
            if not np.allclose(U.conj().T @ U, np.eye(U.shape[0])):
                return self._fail("EVOLUTION_OPERATOR_MUST_BE_UNITARY",
                                  "U†U ≠ I")

        if state.get("cloning_attempted", False):
            return self._fail("NO_CLONING_THEOREM_MUST_HOLD",
                              "Quantum state cloning attempted")

        if state.get("measured", False):
            nonzero = np.sum(np.abs(psi) > 1e-6)
            if nonzero > 1:
                return self._fail("MEASUREMENT_MUST_COLLAPSE_SUPERPOSITION",
                                  "Superposition remains after measurement")

        return SystemResult(ok=True)

    def _fail(self, rule, msg):
        return SystemResult(False, ConstraintViolation(SYSTEM_ID, rule, msg))
