
from contract_system import ContractSystem

system = ContractSystem()

state = {
    "parties": ["Alice", "Bob"],
    "terms": ["Alice pays Bob", "Bob delivers goods"],
    "signatures": ["Alice", "Bob"],
    "executed": True,
    "valid": True
}

print(system.evaluate(state))
