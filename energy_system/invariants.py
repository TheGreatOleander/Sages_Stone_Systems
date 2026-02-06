"""
Energy System Invariants
=======================
Declarative guarantees and constraints for the Energy system.
"""


class EnergyInvariants:
    """
    Invariants for the Energy system.
    """

    NAME = "energy"

    GUARANTEES = [
        "Energy is treated as conserved within defined system boundaries",
        "Energy flow descriptions are directional and contextual",
        "Analysis remains descriptive, not prescriptive",
    ]

    NON_GOALS = [
        "Real-time control of physical systems",
        "Numerical simulation or optimization",
        "Violation of conservation principles",
    ]

    @classmethod
    def summary(cls) -> dict:
        """
        Return invariant summary.
        """
        return {
            "name": cls.NAME,
            "guarantees": cls.GUARANTEES,
            "non_goals": cls.NON_GOALS,
        }
