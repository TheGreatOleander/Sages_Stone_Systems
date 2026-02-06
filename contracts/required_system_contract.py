from sages_stone_runtime.runtime.errors import ContractViolation


class RequiredSystemContract:
    """
    Ensures required systems exist in the registry.
    """

    def __init__(self, registry, required: list[str]):
        self.registry = registry
        self.required = required

    def validate(self) -> bool:
        for name in self.required:
            if name not in self.registry.systems:
                raise ContractViolation(
                    f"Required system '{name}' not registered"
                )
        return True
