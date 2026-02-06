from sages_stone_runtime.runtime.errors import ContractViolation

class ContractManager:
    """
    Orchestrates contracts across multiple systems.
    """

    def __init__(self):
        self.contracts = []

    def add_contract(self, contract):
        self.contracts.append(contract)

    def validate_all(self):
        for contract in self.contracts:
            if not hasattr(contract, "validate"):
                raise ContractViolation(f"Contract '{type(contract).__name__}' missing validate()")
            result = contract.validate()
            if result is False:
                raise ContractViolation(f"Contract '{type(contract).__name__}' failed validation")
