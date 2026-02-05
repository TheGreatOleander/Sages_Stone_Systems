"""
Canonical runtime system.
Defines the minimal execution lifecycle: load -> validate -> execute -> report.
"""

from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class ExecutionResult:
    ok: bool
    output: Any = None
    error: str | None = None

class RuntimeSystem:
    def __init__(self, engine):
        self.engine = engine

    def run(self, action: Dict[str, Any]) -> ExecutionResult:
        try:
            self.engine.validate(action)
            result = self.engine.execute(action)
            return ExecutionResult(ok=True, output=result)
        except Exception as e:
            return ExecutionResult(ok=False, error=str(e))
