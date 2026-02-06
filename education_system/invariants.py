"""
Education System Invariants
===========================
Defines guarantees and constraints for the Education system.

Invariants are intentionally lightweight and declarative.
They may be enforced by higher-level runtime or orchestration layers.
"""


class EducationInvariants:
    """
    Invariants for the Education system.
    """

    # System identity
    NAME = "education"

    # Capability guarantees
    GUARANTEES = [
        "Concept explanations are structured and level-aware",
        "Lesson plans include objectives and instructional phases",
        "Curricula are modular and progressively ordered",
        "Assessments are non-destructive and advisory only",
    ]

    # Explicit non-goals
    NON_GOALS = [
        "Formal accreditation",
        "Authoritative grading",
        "Behavioral enforcement",
    ]

    @classmethod
    def summary(cls) -> dict:
        """
        Return invariant summary for introspection.
        """
        return {
            "name": cls.NAME,
            "guarantees": cls.GUARANTEES,
            "non_goals": cls.NON_GOALS,
        }
