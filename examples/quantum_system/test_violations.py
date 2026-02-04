
from quantum_system import QuantumSystem

qs = QuantumSystem()
bad_state = {"wavefunction": [0.5, 0.5], "measured": True}
print(qs.evaluate(bad_state))
