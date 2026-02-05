"""
demo_canonical_suite.py

Canonical test suite demonstrating full constitutional runtime:

- Single-domain execution (contract_system)
- Multi-domain execution (contract + identity)
- Approved and denied intents
- Runtime selection: sync, async, simulation
- Audit logging
- Guarded runtime enforcement
"""

from dataclasses import dataclass
from typing import Any

from runtime_entrypoint import RuntimeEntrypoint

# Domain systems
from contract_system.system import system as contract_system_instance
from identity_system.system import system as identity_system_instance

# -----------------------------------------------------------------------
# Actor, Intent, Context definitions
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
    async_required: bool = False
    simulation_required: bool = False
    contract = None
    action_requires_verification: bool = False


@dataclass
class Context:
    async_required: bool = False
    simulation: bool = False

# -----------------------------------------------------------------------
# Mock governance systems
# -----------------------------------------------------------------------

class MockAuthorityBoundarySystem:
    def check(self, actor, intent):
        if intent.contract and getattr(intent.contract, "requires_admin", False):
            if not getattr(actor, "is_admin", False):
                raise PermissionError("Authority denied")


class MockCapabilityBoundarySystem:
    def check(self, actor, intent):
        if getattr(intent, "requires_capability", False) and not getattr(actor, "has_capability", False):
            raise PermissionError("Capability denied")


class MockIrreversibilityGuard:
    def check(self, intent):
        pass


class MockExecutionContextSystem:
    def validate(self, context):
        if getattr(context, "invalid_context", False):
            raise RuntimeError("Invalid context")


class MockAuditLogSystem:
    def __init__(self):
        self.records = []

    def record(self, record):
        print(f"[AUDIT] Trace {record['trace_id']} | Allowed: {record['allowed']} | Runtime: {record['selected_runtime']}")
        self.records.append(record)


# -----------------------------------------------------------------------
# Canonical demo runner
# -----------------------------------------------------------------------

def run_canonical_demo():
    print("=== Canonical Constitutional Runtime Demo Suite ===")

    entrypoint = RuntimeEntrypoint(
        identity_system=identity_system_instance,
        authority_boundary_system=MockAuthorityBoundarySystem(),
        capability_boundary_system=MockCapabilityBoundarySystem(),
        contract_system=contract_system_instance,
        irreversibility_guard=MockIrreversibilityGuard(),
        execution_context_system=MockExecutionContextSystem(),
        audit_log_system=MockAuditLogSystem(),
    )

    # -------------------------------------------------------------------
    # 1. Single-domain execution (contract_system)
    # -------------------------------------------------------------------
    from contract_system.schema import Contract
    actor1 = Actor(id="user_1", is_admin=True)
    intent1 = Intent(name="single_domain_task")
    intent1.contract = Contract(id="contract_001", terms="Valid Contract")
    context1 = Context()
    print("\n[TEST] Single-domain execution")
    result1 = entrypoint.execute(intent1, actor1, context1)
    print("Result:", "Allowed" if getattr(result1, "allowed", False) else "Denied")

    # -------------------------------------------------------------------
    # 2. Multi-domain execution (contract + identity)
    # -------------------------------------------------------------------
    actor2 = Actor(id="user_2", is_admin=True, verified_identity=True)
    intent2 = Intent(name="multi_domain_task", action_requires_verification=True)
    intent2.contract = Contract(id="contract_002", terms="Valid Contract")
    context2 = Context()
    print("\n[TEST] Multi-domain execution")
    result2 = entrypoint.execute(intent2, actor2, context2)
    print("Result:", "Allowed" if getattr(result2, "allowed", False) else "Denied")

    # -------------------------------------------------------------------
    # 3. Denied intent due to authority (non-admin)
    # -------------------------------------------------------------------
    actor3 = Actor(id="user_3", is_admin=False)
    intent3 = Intent(name="denied_task")
    intent3.contract = Contract(id="contract_003", terms="Admin only contract", requires_admin=True)
    context3 = Context()
    print("\n[TEST] Denied intent (authority)")
    result3 = entrypoint.execute(intent3, actor3, context3)
    print("Result:", "Allowed" if getattr(result3, "allowed", False) else "Denied")

    # -------------------------------------------------------------------
    # 4. Runtime selection: sync (default)
    # -------------------------------------------------------------------
    intent_sync = Intent(name="sync_task")
    context_sync = Context()
    print("\n[TEST] Runtime: Sync")
    result_sync = entrypoint.execute(intent_sync, actor1, context_sync)
    print("Result:", "Allowed" if getattr(result_sync, "allowed", False) else "Denied")

    # -------------------------------------------------------------------
    # 5. Runtime selection: async
    # -------------------------------------------------------------------
    intent_async = Intent(name="async_task", async_required=True)
    context_async = Context(async_required=True)
    print("\n[TEST] Runtime: Async")
    result_async = entrypoint.execute(intent_async, actor1, context_async)
    print("Result:", "Allowed" if getattr(result_async, "allowed", False) else "Denied")

    # -------------------------------------------------------------------
    # 6. Runtime selection: simulation
    # -------------------------------------------------------------------
    intent_sim = Intent(name="simulate_task", simulation_required=True)
    context_sim = Context(simulation=True)
    print("\n[TEST] Runtime: Simulation")
    result_sim = entrypoint.execute(intent_sim, actor1, context_sim)
    print("Result:", "Allowed" if getattr(result_sim, "allowed", False) else "Denied")

    print("\n=== Canonical Demo Suite Complete ===")


if __name__ == "__main__":
    run_canonical_demo()
