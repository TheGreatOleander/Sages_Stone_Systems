
import numpy as np
from quantum_system import QuantumSystem

qs = QuantumSystem()
state = {"wavefunction": [np.sqrt(0.6), np.sqrt(0.4)]}
print(qs.evaluate(state))
