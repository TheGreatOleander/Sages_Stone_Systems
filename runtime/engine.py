from sages_stone_runtime.runtime.registry import SystemRegistry
from sages_stone_runtime.runtime.errors import (
    RuntimeViolation,
    ContractViolation,
    UnboundSystemError,
)


class RuntimeEngine:
    """
    Deterministic runtime executor.
    No silent failure. No implicit execution.
    """

    def __init__(self):
        self.registry = SystemRegistry()
        self._booted = False
        self._validated = False

    def boot(self) -> None:
        if not self.registry.systems:
            raise UnboundSystemError(
                "Runtime boot aborted: no systems registered"
            )

        for name, system in self.registry.systems.items():
            if not hasattr(system, "initialize"):
                raise RuntimeViolation(
                    f"System '{name}' missing initialize()"
                )
            system.initialize()

        self._booted = True

    def validate(self) -> None:
        if not self._booted:
            raise RuntimeViolation("validate() called before boot()")

        for name, system in self.registry.systems.items():
            if not hasattr(system, "validate"):
                raise ContractViolation(
                    f"System '{name}' missing validate()"
                )

            ok = system.validate()
            if ok is False:
                raise ContractViolation(
                    f"System '{name}' failed contract validation"
                )

        self._validated = True

    def run(self) -> None:
        if not self._validated:
            raise RuntimeViolation(
                "run() called before successful validate()"
            )

        for system in self.registry.systems.values():
            if hasattr(system, "run"):
                system.run()

    def shutdown(self) -> None:
        for system in self.registry.systems.values():
            if hasattr(system, "shutdown"):
                system.shutdown()

        self._booted = False
        self._validated = False
