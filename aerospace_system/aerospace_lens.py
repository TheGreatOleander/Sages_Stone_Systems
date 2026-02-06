# path: Sages_Stone_Systems/aerospace_system/aerospace_lens.py

"""
Aerospace Lens
--------------
Projection from generic intent into aerospace domain.
Pure transformation, no decisions.
"""

from typing import Dict, Any

from .aerospace_schema import AerospaceState


class AerospaceLens:
    """
    Converts unstructured input into AerospaceState
    when possible.
    """

    @staticmethod
    def project(intent: Dict[str, Any]) -> AerospaceState:
        return AerospaceState(
            altitude=float(intent.get("altitude", 0.0)),
            velocity=float(intent.get("velocity", 0.0)),
            mass=float(intent.get("mass", 0.0)),
            fuel=(
                float(intent["fuel"])
                if "fuel" in intent else None
            ),
            metadata={
                k: v for k, v in intent.items()
                if k not in {"altitude", "velocity", "mass", "fuel"}
            } or None,
        )
