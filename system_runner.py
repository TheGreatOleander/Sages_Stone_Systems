"""
System Runner

Coordinates initialization and execution of runtime systems
using dependency-aware ordering.
"""

from system_registry import registry
from system_loader import load_all_systems
from system_dependency_graph import SystemDependencyGraph


class SystemRunner:
    def __init__(self):
        self.registry = registry
        self.graph = SystemDependencyGraph()

    def initialize(self):
        load_all_systems()

        for name in self.registry.list_systems():
            system = self.registry.get(name)
            self.graph.add_system(system)

        ordered_systems = self.graph.resolve_execution_order()

        for system in ordered_systems:
            if hasattr(system, "initialize"):
                system.initialize()

    def execute(self, context):
        ordered_systems = self.graph.resolve_execution_order()

        for system in ordered_systems:
            system.execute(context)

    def shutdown(self):
        ordered_systems = reversed(self.graph.resolve_execution_order())

        for system in ordered_systems:
            if hasattr(system, "shutdown"):
                system.shutdown()


runner = SystemRunner()
