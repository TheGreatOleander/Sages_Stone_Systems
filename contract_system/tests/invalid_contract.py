from contract_system.schema import Contract
from contract_system.executor import execute

contract = Contract(
    id="c2",
    authority="",
    intent="bad",
    terms={}
)

try:
    execute(contract)
    assert False
except ValueError:
    assert True
