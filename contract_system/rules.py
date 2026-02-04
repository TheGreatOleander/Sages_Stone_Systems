from .schema import Contract

def validate_contract(contract: Contract) -> None:
    if not contract.is_well_formed():
        raise ValueError("Contract is not well formed.")

    if "action" not in contract.terms:
        raise ValueError("Contract terms must specify an action.")
