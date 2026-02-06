from sages_stone_runtime.provenance.metadata import SystemMetadata
from sages_stone_runtime.contracts.contract_manager import ContractManager
from sages_stone_runtime.contracts.system_version_contract import SystemVersionContract
from sages_stone_runtime.runtime.errors import ContractViolation

# Setup
meta = SystemMetadata(name="demo_system", version="1.0.0", author="Builder")
manager = ContractManager()
manager.add_contract(SystemVersionContract(meta, required_version="2.0.0"))

try:
    manager.validate_all()
except ContractViolation as e:
    print(f"Contract validation caught: {e}")
