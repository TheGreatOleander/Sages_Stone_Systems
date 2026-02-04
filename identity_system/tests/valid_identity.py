from identity_system.schema import Identity
from identity_system.executor import register

identity = Identity(
    id="id1",
    issuer="root",
    subject="agent_001"
)

result = register(identity)
assert result["status"] == "registered"\n