"""
Epistemology System Invariants
=============================
Declarative epistemic guarantees and constraints.
"""


class EpistemologyInvariants:
    """
    Invariants for the Epistemology system.
    """

    NAME = "epistemology"

    GUARANTEES = [
        "Knowledge claims are treated as provisional by default",
        "Evidence is separated from belief",
        "Confidence is explicit and revisable",
    ]

    NON_GOALS = [
        "Declaring absolute truth",
        "Enforcing belief acceptance",
        "Resolving metaphysical certainty",
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
