"""
demo_runtime_selection.py

Demonstrates dynamic runtime selection in the constitutional runtime:

- sync runtime
- async runtime
- simulation orchestrator

Shows:
- Governance still applies
- ExecutionTrace enforces correct runtime
- Audit logs reflect the chosen runtime
"""

from dataclasses import dataclass
from typing import Any

from runtime_entrypoint import RuntimeEntrypoint

# Import mock systems for governance
from contract_system.system import system as contract_system_instance
from identity_system.system import system as identity_system_instance

# -----------------------------------------------------------------------
# Demo actors, intents, and context
# -----------------------------------------------------------------------

@dataclass
class Actor:
    id: str
    is_admin: bool = True
    has_capability: bool = True
    verified_identity: bool = True


@dataclass
class Intent:
    name: str
    async_required: bool = False
    simulation_required: bool = False


@dataclass
class Context:
    async_required: bool = False
    simulation: bool = False

# -----------------------------------------------------------------------
# Mock systems
# -----------------------------------------------------------------------

class MockAuthorityBoundarySystem:
    def check(self, actor, intent):
        pass


class MockCapabilityBoundarySystem:
    def check(self, actor, intent):
        pass


class MockIrreversibilityGuard:
    def check(self, intent):
        pass


class MockExecutionContextSystem:
    def validate(self, context):
        pass


class MockAuditLogSystem:
    def __init__(self):
        self.records = []

    def record(self, record):
        print(f"[AUDIT] Trace {record['trace_id']} | Allowed: {record['allowed']} | Runtime: {record['selected_runtime']}")
        self.records.append(record)


# -----------------------------------------------------------------------
# Demo runner
# -----------------------------------------------------------------------

def run_runtime_selection_demo():
    print("=== Runtime Selection Demo ===")

    entrypoint = RuntimeEntrypoint(
        identity_system=identity_system_instance,
        authority_boundary_system=MockAuthorityBoundarySystem(),
        capability_boundary_system=MockCapabilityBoundarySystem(),
        contract_system=contract_system_instance,
        irreversibility_guard=MockIrreversibilityGuard(),
        execution_context_system=MockExecutionContextSystem(),
        audit_log_system=MockAuditLogSystem(),
    )

    actor = Actor(id="user_1")

    # --- Sync runtime (default) ---
    intent_sync = Intent(name="sync_task")
    context_sync = Context()
    print("\n[TEST] Sync runtime")
    result_sync = entrypoint.execute(intent_sync, actor, context_sync)
    print("Result:", "Allowed" if getattr(result_sync, "allowed", False) else "Denied")

    # --- Async runtime ---
    intent_async = Intent(name="async_task", async_required=True)
    context_async = Context(async_required=True)
    print("\n[TEST] Async runtime")
    result_async = entrypoint.execute(intent_async, actor, context_async)
    print("Result:", "Allowed" if getattr(result_async, "allowed", False) else "Denied")

    # --- Simulation runtime ---
    intent_sim = Intent(name="simulate_task", simulation_required=True)
    context_sim = Context(simulation=True)
    print("\n[TEST] Simulation runtime")
    result_sim = entrypoint.execute(intent_sim, actor, context_sim)
    print("Result:", "Allowed" if getattr(result_sim, "allowed", False) else "Denied")

    print("\n=== Runtime Selection Demo Complete ===")


if __name__ == "__main__":
    run_runtime_selection_demo()
