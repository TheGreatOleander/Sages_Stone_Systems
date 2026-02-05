"""
runtime_demo.py

Minimal end-to-end demo of the constitutional runtime:

- Demonstrates intent approval
- Demonstrates denial
- Shows audit trace generation
"""

from dataclasses import dataclass, field
from typing import Any, List

# Import the entrypoint
from runtime_entrypoint import RuntimeEntrypoint

# -----------------------------------------------------------------------
# Mock systems for demo purposes
# -----------------------------------------------------------------------

class MockIdentitySystem:
    def validate(self, actor):
        if getattr(actor, "id", None) is None:
            raise ValueError("Actor missing ID")


class MockAuthorityBoundarySystem:
    def check(self, actor, intent):
        if getattr(intent, "requires_admin", False) and not getattr(actor, "is_admin", False):
            raise PermissionError("Authority denied")


class MockCapabilityBoundarySystem:
    def check(self, actor, intent):
        if getattr(intent, "requires_capability", False) and not getattr(actor, "has_capability", False):
            raise PermissionError("Capability denied")


class MockContractSystem:
    def resolve(self, intent, actor):
        if getattr(intent, "broken_contract", False):
            raise RuntimeError("Contract violation")


class MockIrreversibilityGuard:
    def check(self, intent):
        if getattr(intent, "irreversible_forbidden", False):
            raise RuntimeError("Irreversibility violation")


class MockExecutionContextSystem:
    def validate(self, context):
        if getattr(context, "invalid_context", False):
            raise RuntimeError("Invalid execution context")


class MockAuditLogSystem:
    def __init__(self):
        self.records: List[Any] = []

    def record(self, record):
        print(f"[AUDIT] Recording trace {record['trace_id']} | Allowed: {record['allowed']}")
        self.records.append(record)


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
    requires_admin: bool = False
    requires_capability: bool = False
    broken_contract: bool = False
    irreversible_forbidden: bool = False


@dataclass
class Context:
    async_required: bool = False
    simulation: bool = False
    invalid_context: bool = False


# -----------------------------------------------------------------------
# Run demo
# -----------------------------------------------------------------------

def run_demo():
    print("=== Constitutional Runtime Demo ===")

    # Instantiate entrypoint with mock systems
    entrypoint = RuntimeEntrypoint(
        identity_system=MockIdentitySystem(),
        authority_boundary_system=MockAuthorityBoundarySystem(),
        capability_boundary_system=MockCapabilityBoundarySystem(),
        contract_system=MockContractSystem(),
        irreversibility_guard=MockIrreversibilityGuard(),
        execution_context_system=MockExecutionContextSystem(),
        audit_log_system=MockAuditLogSystem(),
    )

    # --- Approved intent ---
    actor1 = Actor(id="user_1", is_admin=True)
    intent1 = Intent(name="approved_task", requires_admin=True)
    context1 = Context()

    print("\n[TEST] Approved execution")
    result1 = entrypoint.execute(intent1, actor1, context1)
    print("Result:", "Allowed" if getattr(result1, "allowed", True) else "Denied")

    # --- Denied intent ---
    actor2 = Actor(id="user_2", is_admin=False)
    intent2 = Intent(name="denied_task", requires_admin=True)
    context2 = Context()

    print("\n[TEST] Denied execution")
    result2 = entrypoint.execute(intent2, actor2, context2)
    print("Result:", "Allowed" if getattr(result2, "allowed", True) else "Denied")

    print("\n=== Demo complete ===")


if __name__ == "__main__":
    run_demo()
