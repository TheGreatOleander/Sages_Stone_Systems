"""
Evaluation System

Charter:
- No side effects
- No authority
- No execution
"""

from .schema import EvaluationResult

class EvaluationSystem:
    name = "evaluation_system"

    def evaluate(self, subject: str, data: dict) -> EvaluationResult:
        """
        Perform a neutral evaluation.

        This default implementation is intentionally minimal.
        """
        metrics = {
            "completeness": float(bool(data)),
            "consistency": 1.0
        }
        return EvaluationResult(
            subject=subject,
            metrics=metrics,
            notes="Baseline neutral evaluation"
        )
