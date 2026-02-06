# path: Sages_Stone_Systems/aerospace_system/aerospace_schema.py

"""
Aerospace Schema
----------------
Pure structural definitions for flight-domain messages.
No behavior, only form.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass(frozen=True)
class AerospaceState:
    altitude: float
    velocity: float
    mass: float
    fuel: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class AerospaceEnvelope:
    max_altitude: float = 400_000.0   # meters
    max_velocity: float = 12_000.0    # m/s
    min_mass: float = 1.0             # kg

