"""
demo_contract_system.py

Demonstrates integration of a real domain system (contract_system)
into the constitutional runtime with full governance, trace,
guarded execution, and audit logging.
"""

from dataclasses import dataclass
from typing import Any

from runtime_entrypoint import RuntimeEntrypoint

# Import the actual contract system modules
from contract_system.schema import Contract
from contract_system.rules import ContractRules
from contract_system.executor import ContractExecutor
from contract_system.violations import ContractViolation
from contract_system.system import system as contract_system_instance

# -----------------------------------------------------------------------
# Demo actors, intents, and context
# -----------------------------------------------------------------------

@dataclass
class Actor:
    id: str
    is_admin: bool = False
    has_capability: bool = True


@dataclass
class Intent:
    name: str
    contract: Contract = None  # Optional contract attached


@dataclass
class Context:
    async_required: bool = False
    simulation: bool = False

# -----------------------------------------------------------------------
# Mocked systems for governance
# -----------------------------------------------------------------------

class MockIdentitySystem:
    def validate(self, actor):
        if getattr(actor, "id", None) is None:
            raise ValueError("Actor missing ID")


class MockAuthorityBoundarySystem:
    def check(self, actor, intent):
        # Admin required only for certain contract operations
        if intent.contract and getattr(intent.contract, "requires_admin", False):
            if not getattr(actor, "is_admin", False):
                raise PermissionError("Authority denied")


class MockCapabilityBoundarySystem:
    def check(self, actor, intent):
        if intent.contract and not getattr(actor, "has_capability", False):
            raise PermissionError("Capability denied")


class MockIrreversibilityGuard:
    def check(self, intent):
        # For demo, no irreversible logic
        pass


class MockExecutionContextSystem:
    def validate(self, context):
        if getattr(context, "invalid_context", False):
            raise RuntimeError("Invalid context")


class MockAuditLogSystem:
    def __init__(self):
        self.records = []

    def record(self, record):
        print(f"[AUDIT] Trace {record['trace_id']} | Allowed: {record['allowed']}")
        self.records.append(record)


# -----------------------------------------------------------------------
# Run demo
# -----------------------------------------------------------------------

def run_contract_demo():
    print("=== Contract System Demo ===")

    # Instantiate constitutional entrypoint
    entrypoint = RuntimeEntrypoint(
        identity_system=MockIdentitySystem(),
        authority_boundary_system=MockAuthorityBoundarySystem(),
        capability_boundary_system=MockCapabilityBoundarySystem(),
        contract_system=contract_system_instance,  # Use real contract system
        irreversibility_guard=MockIrreversibilityGuard(),
        execution_context_system=MockExecutionContextSystem(),
        audit_log_system=MockAuditLogSystem(),
    )

    # Actor with capability and admin rights
    actor = Actor(id="user_admin", is_admin=True, has_capability=True)

    # Valid contract
    valid_contract = Contract(
        id="contract_001",
        terms="Demo valid contract",
        requires_admin=False,
    )

    # Intent referencing contract
    intent = Intent(name="execute_contract", contract=valid_contract)
    context = Context()

    print("\n[TEST] Executing valid contract")
    result = entrypoint.execute(intent, actor, context)
    print("Result:", "Allowed" if getattr(result, "allowed", True) else "Denied")

    # Invalid contract (requires admin, actor is not admin)
    invalid_contract = Contract(
        id="contract_002",
        terms="Admin only contract",
        requires_admin=True,
    )
    actor_non_admin = Actor(id="user_2", is_admin=False, has_capability=True)
    intent_invalid = Intent(name="execute_contract", contract=invalid_contract)

    print("\n[TEST] Executing invalid contract")
    result_invalid = entrypoint.execute(intent_invalid, actor_non_admin, context)
    print("Result:", "Allowed" if getattr(result_invalid, "allowed", True) else "Denied")

    print("\n=== Contract System Demo Complete ===")


if __name__ == "__main__":
    run_contract_demo()
