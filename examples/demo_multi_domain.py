"""
demo_multi_domain.py

Demonstrates multi-domain execution under the constitutional runtime:

- contract_system
- identity_system

Shows:
- Governance enforcement
- ExecutionTrace generation
- Guarded runtime enforcement
- Audit logging
"""

from dataclasses import dataclass
from typing import Any

from runtime_entrypoint import RuntimeEntrypoint

# Import real systems
from contract_system.system import system as contract_system_instance
from identity_system.system import system as identity_system_instance

# -----------------------------------------------------------------------
# Demo actors, intents, and context
# -----------------------------------------------------------------------

@dataclass
class Actor:
    id: str
    is_admin: bool = False
    has_capability: bool = True
    verified_identity: bool = True


@dataclass
class Intent:
    name: str
    contract = None  # Optional contract
    action_requires_verification: bool = False


@dataclass
class Context:
    async_required: bool = False
    simulation: bool = False

# -----------------------------------------------------------------------
# Mock systems for governance
# -----------------------------------------------------------------------

class MockAuthorityBoundarySystem:
    def check(self, actor, intent):
        if getattr(intent.contract, "requires_admin", False) and not getattr(actor, "is_admin", False):
            raise PermissionError("Authority denied")


class MockCapabilityBoundarySystem:
    def check(self, actor, intent):
        if getattr(intent, "requires_capability", False) and not getattr(actor, "has_capability", False):
            raise PermissionError("Capability denied")


class MockIrreversibilityGuard:
    def check(self, intent):
        pass  # For demo


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

def run_multi_domain_demo():
    print("=== Multi-Domain Constitutional Runtime Demo ===")

    # Instantiate the constitutional runtime entrypoint
    entrypoint = RuntimeEntrypoint(
        identity_system=identity_system_instance,
        authority_boundary_system=MockAuthorityBoundarySystem(),
        capability_boundary_system=MockCapabilityBoundarySystem(),
        contract_system=contract_system_instance,
        irreversibility_guard=MockIrreversibilityGuard(),
        execution_context_system=MockExecutionContextSystem(),
        audit_log_system=MockAuditLogSystem(),
    )

    # --- Actor with verified identity and capability ---
    actor = Actor(id="user_1", is_admin=True, has_capability=True, verified_identity=True)

    # --- Valid contract ---
    from contract_system.schema import Contract
    valid_contract = Contract(id="contract_001", terms="Demo valid contract", requires_admin=False)

    # Intent requiring both identity verification and contract execution
    intent = Intent(name="multi_domain_task", action_requires_verification=True)
    intent.contract = valid_contract
    context = Context()

    print("\n[TEST] Executing multi-domain task (allowed)")
    result = entrypoint.execute(intent, actor, context)
    print("Result:", "Allowed" if getattr(result, "allowed", False) else "Denied")

    # --- Actor with unverified identity (should be denied by identity_system) ---
    actor_unverified = Actor(id="user_2", is_admin=True, has_capability=True, verified_identity=False)
    print("\n[TEST] Executing multi-domain task (denied by identity)")
    result_denied = entrypoint.execute(intent, actor_unverified, context)
    print("Result:", "Allowed" if getattr(result_denied, "allowed", False) else "Denied")

    print("\n=== Multi-Domain Demo Complete ===")


if __name__ == "__main__":
    run_multi_domain_demo()
