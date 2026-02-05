"""
Dynamic Runtime Engine

Extends the core runtime to support:
- Dynamic system registration/unregistration at runtime
- Event-driven execution triggers
- Dependency validation on-the-fly
- Full audit logging and context snapshots
"""

import time
from typing import List, Optional
from system_registry import registry
from system_dependency_graph import SystemDependencyGraph
from runtime_context import RuntimeContext
from runtime_event_bus import EventBus
from runtime_system import RuntimeSystem
from system_loader import load_all_systems


class DynamicRuntimeEngine:
    def __init__(self, strict_loader: bool = False):
        self.context = RuntimeContext()
        self.context.event_bus = EventBus()
        self.graph = SystemDependencyGraph()
        self.strict_loader = strict_loader
        self.ordered_systems: List[RuntimeSystem] = []

    # ---------------------------
    # System Management
    # ---------------------------
    def add_system(self, system: RuntimeSystem):
        if system.name in registry.list_systems():
            raise ValueError(f"System already registered: {system.name}")

        registry.register(system.name, system)
        self.graph.add_system(system)
        self._resolve_order()
        self.context.log_event(system.name, "Dynamically added")

    def remove_system(self, system_name: str):
        if system_name not in registry.list_systems():
            raise KeyError(f"System not found: {system_name}")

        del registry._systems[system_name]
        if system_name in self.graph._systems:
            del self.graph._systems[system_name]
            del self.graph._dependencies[system_name]
        self._resolve_order()
        self.context.log_event(system_name, "Dynamically removed")

    def _resolve_order(self):
        self.ordered_systems = self.graph.resolve_execution_order()

    # ---------------------------
    # Initialization
    # ---------------------------
    def initialize(self):
        loaded_systems = load_all_systems(strict=self.strict_loader)

        for name in loaded_systems:
            system = registry.get(name)
            self.graph.add_system(system)

        self._resolve_order()

        for system in self.ordered_systems:
            if hasattr(system, "initialize"):
                system.initialize()
                self.context.log_event(system.name, "Initialized")

    # ---------------------------
    # Execution
    # ---------------------------
    def run_cycle(self, trigger_events: Optional[List[str]] = None):
        """
        Execute systems in order. If trigger_events is provided, only
        systems subscribed to those events will execute.
        """
        for system in self.ordered_systems:
            if trigger_events:
                subscribed = [
                    event for event in trigger_events
                    if event in getattr(system, "subscribed_events", [])
                ]
                if not subscribed:
                    continue  # Skip systems not interested in these events

            system.execute(self.context)
            self.context.log_event(system.name, "Executed")

    def run(
        self, cycles: int = 1, delay: float = 0.0, event_triggers: Optional[List[List[str]]] = None
    ):
        """
        Run multiple cycles with optional per-cycle event triggers.
        """
        for i in range(cycles):
            self.context.log_event("runtime_engine", f"Cycle {i+1} start")

            triggers = None
            if event_triggers and i < len(event_triggers):
                triggers = event_triggers[i]

            self.run_cycle(trigger_events=triggers)

            self.context.log_event("runtime_engine", f"Cycle {i+1} end")
            if delay > 0:
                time.sleep(delay)

    # ---------------------------
    # Shutdown
    # ---------------------------
    def shutdown(self):
        for system in reversed(self.ordered_systems):
            if hasattr(system, "shutdown"):
                system.shutdown()
                self.context.log_event(system.name, "Shutdown")

    # ---------------------------
    # Snapshot
    # ---------------------------
    def snapshot(self):
        return self.context.snapshot()


# ---------------------------
# Singleton dynamic engine
# ---------------------------
dynamic_engine = DynamicRuntimeEngine()
