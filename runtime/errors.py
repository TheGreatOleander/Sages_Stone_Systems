class RuntimeViolation(Exception):
    """Base runtime violation. All hard failures derive from this."""
    pass


class ContractViolation(RuntimeViolation):
    """Raised when a system contract is not satisfied."""
    pass


class UnboundSystemError(RuntimeViolation):
    """Raised when a required system is missing or not registered."""
    pass
