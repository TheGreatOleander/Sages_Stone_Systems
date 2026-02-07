"""
Evaluation System Definition

Binds lifecycle, schema, and invariants into a canonical system shell.
"""

from .lifecycle import EvaluationSystemLifecycle
from .schema import EVALUATION_SCHEMA


class EvaluationSystem:
    """
    Canonical Evaluation System.

    Declares evaluation posture without executing evaluation.
    """

    def __init__(self):
        self.lifecycle = EvaluationSystemLifecycle()
        self.schema = EVALUATION_SCHEMA

    def initialize(self) -> bool:
        return self.lifecycle.initialize()

    def validate(self) -> bool:
        return self.lifecycle.validate()

    def shutdown(self) -> bool:
        return self.lifecycle.shutdown()
