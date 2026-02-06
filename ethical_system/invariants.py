"""
Ethical System Invariants
========================
Declarative guarantees and constraints for ethical reasoning.
"""


class EthicalInvariants:
    """
    Invariants for the Ethical system.
    """

    NAME = "ethical"

    GUARANTEES = [
        "Ethical analysis is advisory, not authoritative",
        "Multiple value frameworks may coexist",
        "Trade-offs are made explicit",
    ]

    NON_GOALS = [
        "Issuing moral commands",
        "Enforcing compliance",
        "Claiming universal moral certainty",
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
