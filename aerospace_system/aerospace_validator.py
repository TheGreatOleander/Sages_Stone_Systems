# path: Sages_Stone_Systems/aerospace_system/aerospace_validator.py

"""
Aerospace Validator
-------------------
Domain rule enforcement separate from schema.
"""

from .aerospace_schema import AerospaceState, AerospaceEnvelope


class AerospaceValidator:

    @staticmethod
    def within_envelope(
        state: AerospaceState,
        envelope: AerospaceEnvelope = AerospaceEnvelope(),
    ) -> bool:

        if state.altitude > envelope.max_altitude:
            return False

        if abs(state.velocity) > envelope.max_velocity:
            return False

        if state.mass < envelope.min_mass:
            return False

        return True
