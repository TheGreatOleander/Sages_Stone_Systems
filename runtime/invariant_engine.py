
class InvariantEngine:
    def run(self, systems):
        for name, system in systems.items():
            if hasattr(system, "invariants"):
                for invariant in system.invariants():
                    invariant()
