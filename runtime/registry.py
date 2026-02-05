
import os
import importlib

class SystemRegistry:
    def __init__(self):
        self.systems = {}
        self.discover_systems()

    def discover_systems(self, root="."):
        for entry in os.listdir(root):
            if entry.endswith("_system") and os.path.isdir(entry):
                try:
                    module_path = f"{entry}.lifecycle"
                    module = importlib.import_module(module_path)
                    for attr in dir(module):
                        if attr.endswith("System"):
                            cls = getattr(module, attr)
                            instance = cls()
                            self.systems[entry] = instance
                            print(f"[Registry] Loaded {entry}")
                except Exception as e:
                    print(f"[Registry] Failed to load {entry}: {e}")
