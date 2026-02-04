from dataclasses import dataclass

@dataclass(frozen=True)
class IrreversibleAction:
    action_id: str
    description: str
