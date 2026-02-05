"""
Schema for evaluation outputs.

Evaluations are descriptive, not prescriptive.
"""

from dataclasses import dataclass
from typing import Any, Dict

@dataclass(frozen=True)
class EvaluationResult:
    subject: str
    metrics: Dict[str, float]
    notes: str | None = None
