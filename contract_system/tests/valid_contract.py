from contract_system.schema import Contract
from contract_system.executor import execute

contract = Contract(
    id="c1",
    authority="root",
    intent="demonstration",
    terms={"action": "test"}
)

result = execute(contract)
assert result["status"] == "executed"
