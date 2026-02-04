from identity_system.schema import Identity
from identity_system.executor import register

identity = Identity(
    id="",
    issuer="root",
    subject=""
)

try:
    register(identity)
    assert False
except ValueError:
    assert True\n