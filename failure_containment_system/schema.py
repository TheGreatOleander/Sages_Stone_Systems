from dataclasses import dataclass

@dataclass(frozen=True)
class FailureEvent:
    failure_id: str
    severity: str
    origin_system: str
    contained: bool
