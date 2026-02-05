"""
Runtime Context

Provides a shared, controlled state for all runtime systems.
Tracks execution metadata, system outputs, and audit logs.
"""

from typing import Any, Dict, List
import time


class RuntimeContext:
    """
    Shared execution context for all systems.
    """

    def __init__(self):
        # State dictionary available to all systems
        self.state: Dict[str, Any] = {}

        # Optional per-system storage
        self.system_data: Dict[str, Dict[str, Any]] = {}

        # Execution metadata (timestamps, order)
        self.execution_trace: List[Dict[str, Any]] = []

        # Audit logs (append-only)
        self.audit_log: List[str] = []

        # Runtime start time
        self.start_time: float = time.time()

    def set_state(self, key: str, value: Any):
        self.state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)

    def set_system_data(self, system_name: str, key: str, value: Any):
        if system_name not in self.system_data:
            self.system_data[system_name] = {}
        self.system_data[system_name][key] = value

    def get_system_data(self, system_name: str, key: str, default: Any = None) -> Any:
        return self.system_data.get(system_name, {}).get(key, default)

    def log_event(self, system_name: str, message: str):
        timestamp = time.time()
        entry = f"{timestamp:.6f} | {system_name} | {message}"
        self.execution_trace.append({"system": system_name, "timestamp": timestamp, "message": message})
        self.audit_log.append(entry)

    def snapshot(self) -> Dict[str, Any]:
        """
        Returns a full snapshot of the context for inspection or persistence.
        """
        return {
            "state": dict(self.state),
            "system_data": {k: dict(v) for k, v in self.system_data.items()},
            "execution_trace": list(self.execution_trace),
            "audit_log": list(self.audit_log),
            "start_time": self.start_time,
            "current_time": time.time(),
        }
