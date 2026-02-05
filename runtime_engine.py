"""
Runtime Engine

Coordinates system discovery, initialization, dependency-ordered execution,
event-driven updates, and context auditing.
"""

import time
from system_loader import load_all_systems
from system_registry import registry
from system_dependency_graph import SystemDependencyGraph
from runtime_context import RuntimeContext
from runtime_event_bus import EventBus
from runtime_system import RuntimeSystem


class RuntimeEngine:
    def __init__(self, strict_loader: bool = False):
        self.context = RuntimeContext()
        self.context.event_bus = EventBus()
        self.graph = SystemDependencyGraph()
        self.strict_loader = strict_loader
        self.ordered_systems = []

    def initialize(self):
        # Discover and load all systems
        loaded_systems = load_all_systems(strict=self.strict_loader)

        # Register systems into dependency graph
        for name in loaded_systems:
            system = registry.get(name)
            self.graph.add_system(system)

        # Resolve dependency order
        self.ordered_systems = self.graph.resolve_execution_order()

        # Initialize systems in dependency order
        for system in self.ordered_systems:
            if hasattr(system, "initialize"):
                system.initialize()
                self.context.log_event(system.name, "Initialized")

    def run_cycle(self):
        """
        Execute one runtime cycle: all systems in dependency order
        """
        for system in self.ordered_systems:
            system.execute(self.context)
            self.context.log_event(system.name, "Executed")

    def run(self, cycles: int = 1, delay: float = 0.0):
        """
        Run multiple cycles with optional delay (seconds) between cycles
        """
        for i in range(cycles):
            self.context.log_event("runtime_engine", f"Cycle {i+1} start")
            self.run_cycle()
            self.context.log_event("runtime_engine", f"Cycle {i+1} end")
            if delay > 0:
                time.sleep(delay)

    def shutdown(self):
        """
        Shutdown all systems in reverse dependency order
        """
        for system in reversed(self.ordered_systems):
            if hasattr(system, "shutdown"):
                system.shutdown()
                self.context.log_event(system.name, "Shutdown")

    def snapshot(self):
        """
        Returns the full context snapshot
        """
        return self.context.snapshot()


# Singleton runtime instance
engine = RuntimeEngine()
