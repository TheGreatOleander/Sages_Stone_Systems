class BaseSystem:
    """
    Minimal, enforceable base class for all runtime systems.
    """

    name: str | None = None

    def initialize(self) -> None:
        pass

    def validate(self) -> bool:
        return True

    def run(self) -> None:
        pass

    def shutdown(self) -> None:
        pass
