from dataclasses import dataclass
from typing import Any, Dict

@dataclass(frozen=True)
class Contract:
    id: str
    authority: str
    intent: str
    terms: Dict[str, Any]

    def is_well_formed(self) -> bool:
        return bool(self.id and self.authority and self.intent and self.terms)
