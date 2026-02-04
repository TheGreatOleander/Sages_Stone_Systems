"""
Authority Judgement System

Consumes a normalized actor and action and produces a judgement:
    - ALLOW
    - DENY
    - ESCALATE

This system assumes:
- Structural validation has already occurred
- Constraint systems have already passed

This module does NOT execute actions.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Any
import time


# ---------------------------------------------------------------------
# Judgement Outcomes
# ---------------------------------------------------------------------

class Judgement(Enum):
    ALLOW = auto()
    DENY = auto()
    ESCALATE = auto()


# ---------------------------------------------------------------------
# Judgement Result
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class JudgementResult:
    judgement: Judgement
    reason: str
    timestamp: float = time.time()


# ---------------------------------------------------------------------
# Authority Judgement Engine
# ---------------------------------------------------------------------

class AuthorityJudgementSystem:
    """
    Evaluates whether an actor may attempt an action.
    """

    def judge(
        self,
        actor: Dict[str, Any],
        action: Dict[str, Any]
    ) -> JudgementResult:

        actor_auth = actor.get("authority")
        action_auth = action.get("authority")
        allowed_auth = action.get("allowed_authority")

        # Absolute denial: actor has no authority
        if not actor_auth:
            return JudgementResult(
                Judgement.DENY,
                "Actor declares no authority."
            )

        # Actor authority must be within action allowed scope
        if not actor_auth.startswith(allowed_auth):
            return JudgementResult(
                Judgement.DENY,
                f"Actor authority '{actor_auth}' exceeds allowed scope '{allowed_auth}'."
            )

        # Escalation rules
        if action_auth.startswith("override"):
            if actor.get("actor_type") != "human":
                return JudgementResult(
                    Judgement.ESCALATE,
                    "Override actions require human authority."
                )

        # Sandbox restriction example
        if "sandboxed" in actor.get("tags", set()):
            if action.get("domain") == "runtime":
                return JudgementResult(
                    Judgement.DENY,
                    "Sandboxed actors may not affect runtime domain."
                )

        return JudgementResult(
            Judgement.ALLOW,
            "Actor authorized for action."
        )
