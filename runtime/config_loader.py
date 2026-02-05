
import json
import os

class ConfigLoader:
    def load(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, "r") as f:
            return json.load(f)
