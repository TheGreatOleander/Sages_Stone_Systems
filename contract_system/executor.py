from .schema import Contract
from .rules import validate_contract

def execute(contract: Contract) -> dict:
    validate_contract(contract)
    return {
        "status": "executed",
        "contract_id": contract.id,
        "action": contract.terms.get("action")
    }
