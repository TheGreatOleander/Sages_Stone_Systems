from dataclasses import dataclass
from typing import Optional, Dict

@dataclass(frozen=True)
class ExecutionContext:
    context_id: str
    actor_id: str
    authority_level: str
    parent_context: Optional[str]
    metadata: Dict[str, str]
