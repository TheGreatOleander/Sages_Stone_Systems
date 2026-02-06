class Contract:
    """
    Minimal contract interface.
    Contracts must fail loudly.
    """

    name: str | None = None

    def validate(self) -> bool:
        raise NotImplementedError("Contract must implement validate()")
