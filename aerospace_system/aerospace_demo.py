# path: Sages_Stone_Systems/aerospace_system/aerospace_demo.py

"""
Aerospace Demo
--------------
Example usage without side effects.
"""

from .aerospace_lens import AerospaceLens
from .aerospace_system import AerospaceSystem
from .aerospace_validator import AerospaceValidator


def demo(payload: dict) -> dict:

    state = AerospaceLens.project(payload)

    judgement = AerospaceSystem.evaluate(state.__dict__)

    valid = AerospaceValidator.within_envelope(state)

    return {
        "judgement": judgement.status,
        "reason": judgement.reason,
        "within_envelope": valid,
    }


if __name__ == "__main__":
    sample = {"altitude": 120000, "velocity": 7800, "mass": 2000}
    print(demo(sample))
