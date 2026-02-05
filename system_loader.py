"""
System Loader

Discovers, validates, and registers runtime systems.

Conventions:
    <name>_system/system.py
    class <Something>System(RuntimeSystem)

Safety features:
    - RuntimeSystem validation
    - duplicate registration detection
    - metadata validation
    - optional strict mode
"""

import importlib
import os
from typing import List

from system_registry import registry
from runtime_system import RuntimeSystem


class SystemLoaderError(Exception):
    pass


def _discover_system_modules(base_path=".") -> List[str]:
    modules = []

    for entry in os.listdir(base_path):
        if entry.endswith("_system") and os.path.isdir(entry):
            modules.append(f"{entry}.system")

    return modules


def _find_system_class(module):
    for attr_name in dir(module):
        attr = getattr(module, attr_name)

        try:
            if issubclass(attr, RuntimeSystem) and attr is not RuntimeSystem:
                return attr
        except TypeError:
            continue

    return None


def _validate_system(system: RuntimeSystem):
    if not system.name:
        raise SystemLoaderError("System missing name")

    if not isinstance(system.name, str):
        raise SystemLoaderError("System name must be string")

    if not hasattr(system, "execute"):
        raise SystemLoaderError(f"{system.name} missing execute()")

    if hasattr(system, "dependencies"):
        if not isinstance(system.dependencies, (list, tuple)):
            raise SystemLoaderError(
                f"{system.name} dependencies must be list or tuple"
            )


def load_all_systems(strict: bool = False):
    modules = _discover_system_modules()

    loaded = []
    failures = []

    for module_name in modules:
        try:
            module = importlib.import_module(module_name)

            system_class = _find_system_class(module)
            if system_class is None:
                continue

            system_instance = system_class()

            _validate_system(system_instance)

            registry.register(system_instance.name, system_instance)

            loaded.append(system_instance.name)

        except Exception as e:
            failures.append((module_name, str(e)))

    print(f"[SystemLoader] Loaded {len(loaded)} systems")

    if failures:
        print("[SystemLoader] Failures:")
        for mod, err in failures:
            print(f"  {mod} -> {err}")

        if strict:
            raise SystemLoaderError("System loading failed in strict mode")

    return loaded
