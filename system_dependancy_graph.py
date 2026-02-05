"""
System Dependency Graph

Provides dependency ordering and cycle detection
for runtime systems.
"""

from typing import Dict, List, Set
from runtime_system import RuntimeSystem


class DependencyGraphError(Exception):
    pass


class SystemDependencyGraph:
    def __init__(self):
        self._systems: Dict[str, RuntimeSystem] = {}
        self._dependencies: Dict[str, List[str]] = {}

    def add_system(self, system: RuntimeSystem):
        name = system.name
        self._systems[name] = system

        if not hasattr(system, "dependencies"):
            self._dependencies[name] = []
        else:
            self._dependencies[name] = list(system.dependencies)

    def _visit(
        self,
        node: str,
        visited: Set[str],
        temp: Set[str],
        result: List[str],
    ):
        if node in temp:
            raise DependencyGraphError(f"Cycle detected at {node}")

        if node not in visited:
            temp.add(node)

            for dep in self._dependencies.get(node, []):
                if dep not in self._systems:
                    raise DependencyGraphError(
                        f"Missing dependency: {dep} required by {node}"
                    )
                self._visit(dep, visited, temp, result)

            temp.remove(node)
            visited.add(node)
            result.append(node)

    def resolve_execution_order(self) -> List[RuntimeSystem]:
        visited: Set[str] = set()
        temp: Set[str] = set()
        result: List[str] = []

        for system_name in self._systems.keys():
            self._visit(system_name, visited, temp, result)

        return [self._systems[name] for name in result]
