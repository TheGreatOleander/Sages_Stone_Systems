
from config import SYSTEM_NAME, VERSION

def describe():
    return {
        "name": SYSTEM_NAME,
        "version": VERSION,
        "capabilities": [
            "lifecycle",
            "logging",
            "config",
            "state",
            "metrics",
            "health",
            "cli",
        ]
    }
