
from contract_system import ContractSystem

system = ContractSystem()

illegal_state = {
    "parties": ["Alice", "Bob"],
    "terms": ["Alice pays Bob"],
    "executed": True,  # executed
    "signatures": [],  # but unsigned
}

print(system.evaluate(illegal_state))
