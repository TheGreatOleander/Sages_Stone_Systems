from sages_stone_runtime.runtime.errors import ContractViolation

class SystemVersionContract:
    """
    Ensures system metadata matches required version constraints.
    """

    def __init__(self, system_metadata, required_version: str):
        self.system_metadata = system_metadata
        self.required_version = required_version

    def validate(self) -> bool:
        if self.system_metadata.version != self.required_version:
            raise ContractViolation(
                f"System '{self.system_metadata.name}' version mismatch: "
                f"{self.system_metadata.version} != {self.required_version}"
            )
        return True
