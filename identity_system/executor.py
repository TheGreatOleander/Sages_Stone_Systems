from .schema import Identity
from .rules import validate_identity

def register(identity: Identity) -> dict:
    validate_identity(identity)
    return {
        "status": "registered",
        "identity_id": identity.id,
        "subject": identity.subject
    }\n