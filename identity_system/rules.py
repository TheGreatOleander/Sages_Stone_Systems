from .schema import Identity

def validate_identity(identity: Identity) -> None:
    if not identity.is_well_formed():
        raise ValueError("Identity is not well formed.")\n